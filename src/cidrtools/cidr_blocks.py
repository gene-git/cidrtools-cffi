# SPDX-License-Identifier: GPL-2.0-or-later
# SPDX-FileCopyrightText: © 2026-present Gene C <arch@sapience.com>
"""
Classes :
    - CidrBlock - one cidr block
    - CidrBlocks - a list of cidr blocks.
See also CidrTools class
"""
from __future__ import annotations
from typing import Iterator, Any

from ._core import ffi, lib

#
# C-library wrapper functions
# - cidr block.
#
from .ct_str_to_cidr_block import ct_str_to_cidr_block
from .ct_cidr_to_str import ct_cidr_to_str
from .ct_is_ipv4 import ct_is_ipv4
from .ct_is_ipv6 import ct_is_ipv6
from .ct_num_ips import ct_num_ips
from .ct_format_host_bits import ct_format_host_bits
from .ct_cidr_contains_cidr import ct_cidr_contains_cidr
from .ct_cidr_contains_ip import ct_cidr_contains_ip
from .ct_ip_address_to_str import ct_ip_address_to_str
from .ct_str_to_cidr_parts import ct_str_to_cidr_parts
from .ct_clean_cidr import ct_clean_cidr

#
# C-library wrapper functions
# cidr blocks
#
from .ct_allocate_cidrs import ct_allocate_cidrs
from .ct_add_cidr_to_cidrs import ct_add_cidr_to_cidrs
from .ct_free_cidrs import ct_free_cidrs
from .ct_compact import ct_compact
from .ct_clean_cidrs import ct_clean_cidrs
from .ct_exclude_cidrs import ct_exclude_cidrs


class CidrBlock():
    """
    Class to manage one cidr block.
    Uses cidrtools C-library CtCidrBlock structure.

    Handles memory allocation, type inspections, range mapping,
    and contains (is-subnet).

    Built on the cidrtools library.
    """

    def __init__(self, cidr_str: str) -> None:
        """
        Creates a managed C structure from a CIDR string.

        :param cidr_str: The network string (e.g., '192.168.1.0/24').
        :raises ValueError: If the string is not a valis cidr.
        """
        self._raw_input_str: str = cidr_str
        self._c_data: Any = ffi.new("CtCidr *")
        rc = ct_str_to_cidr_block(cidr_str, self._c_data)
        if rc != 0:
            raise ValueError(f"Invalid CIDR block string : '{cidr_str}'")

    @property
    def is_ipv4(self) -> bool:
        """
        Returns True if the cidr block is an IPv4 network family

        :return: True if the network family is IPv4, False otherwise.
        """
        return bool(ct_is_ipv4(self._c_data))

    @property
    def is_ipv6(self) -> bool:
        """
        Returns True if the cidr block is an IPv6 network family.

        :return: True if the network family is IPv6, False otherwise.
        """
        return bool(ct_is_ipv6(self._c_data))

    @property
    def num_ips(self) -> int:
        """
        Returns the total number of IPs inside this cidr block.

        Note that for IPv6 this is capped at 64 bit interger max.
        """
        return int(ct_num_ips(self._c_data))

    def fix_host_bits(self) -> int:
        """
        Cleans up cidr with host bits set, by setting all host bits to zero.
        """
        return int(lib.ct_cidr_fix_host_bits(self._c_data))

    def set_prefix(self, prefix: int) -> int:
        """
        Modifies the network prefix to be the new value.
        """
        if not 0 <= prefix <= (32 if self.is_ipv4 else 128):
            raise ValueError("Prefix size limits bound by protocol rules.")
        return int(lib.ct_cidr_set_prefix(self._c_data, prefix))

    def is_subnet_of(self, cidrs: CidrBlocks) -> bool:
        """
        Checks if this block is a subnet of any of the collection of cidrs.
        """
        # pylint: disable=protected-access
        return bool(lib.ct_cidr_is_subnet(self._c_data, cidrs._c_data))

    def to_range(self) -> tuple[str, str]:
        """
        Computes the first and last IP addresses of this cidr block.
        See allso to_range_mid()
        """
        c_first = ffi.new("CtAddress *")
        c_last = ffi.new("CtAddress *")
        rc = lib.ct_cidr_to_range(self._c_data, c_first, c_last)
        if rc != 0:
            raise RuntimeError("C engine failed range calculations.")
        return ct_ip_address_to_str(c_first), ct_ip_address_to_str(c_last)

    def to_range_mid(self) -> tuple[str, str, str]:
        """
        Compute the first, middle and last IP addresses of this cidr block.
        """
        c_first = ffi.new("CtAddress *")
        c_mid = ffi.new("CtAddress *")
        c_last = ffi.new("CtAddress *")
        rc = lib.ct_cidr_to_range_mid(self._c_data, c_first, c_mid, c_last)
        if rc != 0:
            raise RuntimeError("C engine failed range calculations.")
        return ct_ip_address_to_str(c_first), ct_ip_address_to_str(c_mid), ct_ip_address_to_str(c_last)

    def split(self, prefix: int) -> CidrBlocks:
        """
        Splits the cidr block into a collection of smaller subnets using the provided prefix.
        """
        res_ptr = lib.ct_subnets_split(self._c_data, prefix)
        if res_ptr == ffi.NULL:
            raise RuntimeError("Invalid partition request boundaries.")

        collection = CidrBlocks()
        # pylint: disable=protected-access
        collection._c_data = res_ptr
        return collection

    def get_host_bits(self) -> str:
        """
        Extracts the underlying address portion - these are thr bits past the
        network bits defined by the prefix length.

        <prefix length of network-bits ... ><host-bits>

        E.g. 10.2.2.3/24 => 0.0.0.3
        Note that the host bits are tracked internally but the cidr is always "fixed"
        Example:
            cidr = CidrBlock("192.168.1.22/24")
            str(cidr) --> "192.168.1.0/24"
            cidr.get_host_bits() --> "0.0.0.22"
        """
        return self.format_host_bits()

    def format_host_bits(self) -> str:
        """
        Returns a formatted "address" string of the host bits
        Identical to get_host_bits() -
        """
        input_str = getattr(self, '_raw_input_str', str(self))
        if not input_str:
            return ""

        temp_cidr = ffi.new("CtCidr *")
        max_ip_len = 128
        c_ip_buf = ffi.new("char[]", max_ip_len)
        c_prefix = ffi.new("uint8_t *")
        c_str = ffi.new("char[]", input_str.encode('utf-8'))

        if lib.ct_str_to_cidr_parts(c_str, c_ip_buf, max_ip_len, c_prefix) != 0:
            return ""

        if lib.ct_str_to_ip_address(c_ip_buf, ffi.addressof(temp_cidr.addr)) != 0:
            return ""

        temp_cidr.prefix = self._c_data.prefix
        temp_cidr.addr.family = self._c_data.addr.family
        return ct_format_host_bits(temp_cidr)

    def cidr_parts(self) -> tuple[str, int]:
        """
        Returns the IP address and prefix as a tuple.
         - (ip_address: str, prefix: int)
        """
        cidr_str = getattr(self, '_raw_input_str', str(self))
        if not cidr_str:
            return ("", 0)

        # Ignore the return code - keep the ip and prefix
        _, ip_str, prefix = ct_str_to_cidr_parts(cidr_str)
        return (ip_str, prefix)

    def increment_by(self, steps: int) -> str:
        """
        Find a new network address advanced by 'steps' IP addresses.
        """
        c_dest = ffi.new("CtAddress *")
        rc = lib.ct_ip_address_increment(ffi.addressof(self._c_data.addr), steps, c_dest)
        if rc != 0:
            raise IndexError("Increment vector bounds slipped out of scope.")
        return ct_ip_address_to_str(c_dest)

    def __contains__(self, other: CidrBlock | str) -> bool:
        """
        Checks if this cidr block is a subnet of another.
        """
        if isinstance(other, CidrBlock):
            return bool(ct_cidr_contains_cidr(self._c_data, other._c_data))

        if isinstance(other, str):
            c_addr = ffi.new("CtAddress *")
            if lib.ct_str_to_ip_address(other.encode('utf-8'), c_addr) == 0:
                return bool(ct_cidr_contains_ip(self._c_data, c_addr))
        return False

    def to_string(self) -> str:
        """
        Return the cidr string. Same as str(self)
        """
        return ct_cidr_to_str(self._c_data)

    def __str__(self) -> str:
        return ct_cidr_to_str(self._c_data)

    def __repr__(self) -> str:
        return f"<CidrBlock: {self.__str__()}>"

    def clean(self) -> bool:
        """
        Clean up invalid cidr blocks (prefix, host bits being set)

        :return: Treu on success oterhwise False
        """
        status = bool(ct_clean_cidr(self._c_data) == 0)
        return status


class CidrBlocks():
    """
    An ordered list of CtCidrs

    A list of cidr blocks.  Supports a variety of operations
    via the member functions such as:
    - compacting
    - filtering (excluding),
    - slicing,
    - cleaning.

    Built on the cidrtools library.  Manages memory allocations.
    """

    def __init__(self, initial_cidrs: list[str] | None = None) -> None:
        """
        Initializes an empty or populated collection of cidr blocks.

        :param initial_cidrs: Optional list of network CIDR block strings
        """
        # print(f"DEBUG PYTHON CONSTRUCTOR: Struct size is {ffi.sizeof('CtCidr')} bytes.")
        self._c_data: Any = ffi.new("CtCidrs *")
        self._c_data.blocks = ffi.NULL
        self._c_data.count = 0

        if initial_cidrs:
            total_count = len(initial_cidrs)

            # for idx, cidr in enumerate(initial_cidrs):
            #    # Look for the literal exact match or structural match
            #    if cidr.strip() == "128.0.0.0/2":
            #        print(f"💥 Debug Check : Found literal '128.0.0.0/2' at list index {idx}!")
            #        # Print the surrounding elements to see what generated it
            #        start_p = max(0, idx - 2)
            #        end_p = min(len(initial_cidrs), idx + 3)
            #        print(f"Surrounding context: {initial_cidrs[start_p:end_p]}")

            #
            # This is reasonably fast way to join cidrs into a single flat bytes string
            # - fast way to communicate to-from the C-library
            #
            flat_bytes = ",".join(initial_cidrs).encode('utf-8')

            rc = lib.ct_flat_buffer_to_cidrs(flat_bytes, total_count, self._c_data)
            if rc != 0:
                raise ValueError(f"ct_flat_buffer_to_cidrs() failed with error: {rc}")

    def add(self, cidr: CidrBlock | str) -> bool:
        """
        Appends a CIDR block to the collection.

        :param cidr: The cidr block (object or raw string) to add.
        :return: True if the append succeeded else false.
        """
        if isinstance(cidr, str):
            block: CidrBlock = CidrBlock(cidr)
        else:
            block = cidr

        # pylint: disable=protected-access
        return bool(ct_add_cidr_to_cidrs(self._c_data, block._c_data))

    def clean(self) -> bool:
        """
        Clean any invalid cidr blocks (prefix, host bits being set)

        :return: True if success else False
        """
        return bool(ct_clean_cidrs(self._c_data) == 0)

    def compact(self) -> int:
        """
        Compress the list of cidrs to the mimimal number of subnets.

        This combines adjacent or overlapping subnets to make the
        smallest number of subnets. This is done in place.

        :return: Return status code from the underlying C function.
        """
        return int(ct_compact(self._c_data))

    def sort(self) -> int:
        """
        In-place sort of the cidr blocks.

        :return: Return status code from the underlying C library
        """
        return int(lib.ct_sort(self._c_data))

    def exclude(self, excluded_cidrs: CidrBlocks) -> int:
        """
        Exclude a set of cidr blocks. This is done place.

        new cidrs =>  cidrs - excluded_cidrs.

        :param excluded_cidrs: The cidrs to be excluded.
        :return: Return status code of the underlying C library.
        """
        # pylint: disable=protected-access
        return int(ct_exclude_cidrs(self._c_data, excluded_cidrs._c_data))

    def split_by_family(self) -> tuple[CidrBlocks, CidrBlocks]:
        """
        Splits the cidr blocks into separate IPv4 and IPv6 lists.

        :return: tuple of cidr lists - (IPv4_Pool, IPv6_Pool).
        :raises RuntimeError: If errors found by C-library
        """
        v4_pool = CidrBlocks()
        v6_pool = CidrBlocks()
        # pylint: disable=protected-access
        rc = lib.ct_split_by_family(self._c_data, v4_pool._c_data, v6_pool._c_data)
        if rc != 0:
            raise RuntimeError("Error from ct_split_by_family.")
        return v4_pool, v6_pool

    def to_strings(self) -> list[str]:
        """
        Returns a list of cidr strings.
        Optimized for speed.
        """
        count = self._c_data.count
        if count == 0:
            return []

        #
        # Fetch a single flat buffer pointer from C library
        # - this is a comma separated string: "cidr1,cidr2, ..., cidrN"
        #
        c_ptr = lib.ct_cidrs_to_flat_buffer(self._c_data)
        if c_ptr == ffi.NULL:
            return []

        #
        # Copy to python memory and free the C memory
        #
        flat_string = ffi.string(c_ptr).decode('utf-8')
        lib.free(c_ptr)

        #
        # Split back into a list of cidr strings.
        #
        return flat_string.split(',')

    def __len__(self) -> int:
        return int(self._c_data.count)

    def __iter__(self) -> Iterator[str]:
        """
        Iterates over each cidr block in the using the flat buffer.
        Yields raw string directly without the extra overhead of
        looping on indivudual cidr.
        See to_strings()
        """
        yield from self.to_strings()

    def __getitem__(self, index: int | slice) -> str | list[str]:
        """
        Allows standard list indexing syntax

        :param index: index or list slice sequence object.
        :return: One or more cidr strings. String for one or list of strings if more than one.
        :raises IndexError: If index/slice is bad.
        """
        if isinstance(index, slice):
            start, stop, step = index.indices(self._c_data.count)
            return [self._get_item_at(i) for i in range(start, stop, step)]

        target_idx: int = index
        if target_idx < 0:
            target_idx += int(self._c_data.count)

        if target_idx < 0 or target_idx >= self._c_data.count:
            raise IndexError("CidrBlocks bad index.")
        return self._get_item_at(target_idx)

    def _get_item_at(self, i: int) -> str:
        """Internal helper pulling string from the internal pointer"""
        block_ptr = ffi.addressof(self._c_data.blocks, i)
        return ct_cidr_to_str(block_ptr)

    def __del__(self) -> None:
        """Delete methos: garbage collector hook deals with memory mamagement."""
        if hasattr(self, '_c_data') and self._c_data.blocks != ffi.NULL:
            ct_free_cidrs(self._c_data)

    def __repr__(self) -> str:
        return f"<CidrBlocks count={len(self)} items={self.to_strings()}>"
