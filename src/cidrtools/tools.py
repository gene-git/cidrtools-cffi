# SPDX-License-Identifier: GPL-2.0-or-later
# SPDX-FileCopyrightText: © 2026-present Gene C <arch@sapience.com>
"""
CidrTools:
    src/cidrtools/tools.py
"""
# pylint: disable=duplicate-code
from ._core import ffi, lib
from .ct_version import ct_version
from .ct_hostname_to_address import ct_hostname_to_address
from .cidr_blocks import CidrBlocks


class CidrTools:
    """
    Class with some additional member functions of the *cidrtools* library.

    Underlying cidrtools version and some DNS convenience functions.
    """

    @staticmethod
    def ct_version() -> str:
        """
        Returns the native C library version target compilation string.

        :return: The loaded library system release semantic tag value.
        :rtype: str
        """
        return ct_version()

    @staticmethod
    def hostname_to_addresses(hostname: str) -> CidrBlocks:
        """
        Resolves a hostname string into a structured collection of CIDR blocks.

        :param hostname: The explicit domain URL path target string to resolve.
        :type hostname: str
        :return: A fresh collection array tracking resolved system addresses blocks.
        :rtype: CidrBlocks
        :raises RuntimeError: If standard resolution paths fail or return unexpected status flags.
        """
        cidr_blocks = CidrBlocks()
        # pylint: disable=protected-access
        rc = ct_hostname_to_address(hostname, cidr_blocks._c_data)
        if rc != 0:
            raise RuntimeError(f"Failed resolving hostname: {hostname}")
        return cidr_blocks

    @staticmethod
    def ip_str_to_hostname(ip_str: str) -> str:
        """
        Performs a reverse DNS lookup mapping an active IP address string back to a hostname.

        :param ip_str: The textual raw representation layout of the target lookup address.
        :type ip_str: str
        :return: The fully qualified resolved host identifier name string.
        :rtype: str
        :raises RuntimeError: If reverse lookup actions time out or tracking channels fail.
        """
        buf = ffi.new("char[]", 1025)
        rc = lib.ct_ip_str_to_hostname(ip_str.encode('utf-8'), buf)
        if rc != 0:
            raise RuntimeError(f"Reverse DNS failed for IP: {ip_str}")
        return ffi.string(buf).decode('utf-8')

    @staticmethod
    def range_to_cidrs(first_ip: str, last_ip: str) -> CidrBlocks:
        """
        Converts an IP range to a minimal collection of CIDR blocks.

        Should this be moved to CidrBlocks.range_to_cidrs() ?

        :param first_ip: The fist network IP of the rangw
        :param last_ip: The last IP of the range
        :return: A minimal representation tracking collection of matched network blocks.
        :raises ValueError: If input strings map incorrectly to standard protocol types.
        :raises RuntimeError: If underlying C matrix calculations encounter configuration faults.
        """
        c_first = ffi.new("CtAddress *")
        c_last = ffi.new("CtAddress *")

        if lib.ct_str_to_ip_address(first_ip.encode('utf-8'), c_first) != 0:
            raise ValueError(f"Invalid starting IP boundary: {first_ip}")

        if lib.ct_str_to_ip_address(last_ip.encode('utf-8'), c_last) != 0:
            raise ValueError(f"Invalid ending IP boundary: {last_ip}")

        cidr_blocks = CidrBlocks()
        # pylint: disable=protected-access
        rc = lib.ct_range_to_cidrs(c_first, c_last, cidr_blocks._c_data)
        if rc != 0:
            raise RuntimeError("C engine failed calculation parsing range boundaries.")
        return cidr_blocks
