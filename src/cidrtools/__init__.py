# SPDX-License-Identifier: GPL-2.0-or-later
# SPDX-FileCopyrightText: © 2026-present Gene C <arch@sapience.com>
"""
cidrtoolls-cffi package provides:
  cidrtools module:
  - public class/member functions
  - wrapper function for each cidrtool ct_xx function.
"""
#
# FFI bindings and library
#
from ._core import ffi, lib

#
# low-level wrapper functions for cidrtools shared library
#
from .ct_add_cidr_to_cidrs import ct_add_cidr_to_cidrs
from .ct_allocate_cidrs import ct_allocate_cidrs
from .ct_cidr_contains_cidr import ct_cidr_contains_cidr
from .ct_cidr_contains_ip import ct_cidr_contains_ip
from .ct_cidr_fix_host_bits import ct_cidr_fix_host_bits
from .ct_cidr_is_subnet import ct_cidr_is_subnet
from .ct_cidr_set_prefix import ct_cidr_set_prefix
from .ct_cidr_to_range import ct_cidr_to_range
from .ct_cidr_to_range import ct_cidr_to_range_mid
from .ct_cidr_to_str import ct_cidr_to_str
from .ct_cidr_to_str_r import ct_cidr_to_str_r
from .ct_clean_cidr import ct_clean_cidr
from .ct_clean_cidrs import ct_clean_cidrs
from .ct_compact import ct_compact
from .ct_exclude_cidrs import ct_exclude_cidrs
from .ct_format_host_bits import ct_format_host_bits
from .ct_free_cidrs import ct_free_cidrs
from .ct_get_host_bits import ct_get_host_bits
from .ct_hostname_to_address import ct_hostname_to_address
from .ct_ip_address_increment import ct_ip_address_increment
from .ct_ip_address_range import ct_ip_address_range
from .ct_ip_address_to_str import ct_ip_address_to_str
from .ct_ip_address_to_str_r import ct_ip_address_to_str_r
from .ct_ip_str_to_hostname import ct_ip_str_to_hostname
from .ct_is_ipv4 import ct_is_ipv4
from .ct_is_ipv6 import ct_is_ipv6
from .ct_num_ips import ct_num_ips
from .ct_range_to_cidrs import ct_range_to_cidrs
from .ct_sort import ct_sort
from .ct_split_by_family import ct_split_by_family
from .ct_str_to_cidr_block import ct_str_to_cidr_block
from .ct_str_to_cidr_parts import ct_str_to_cidr_parts
from .ct_str_to_ip_address import ct_str_to_ip_address
from .ct_subnets_split import ct_subnets_split
from .ct_version import ct_version

#
# high-level public class objects
#
from .cidr_blocks import CidrBlock
from .cidr_blocks import CidrBlocks
from .tools import CidrTools

#
# For lazy importers
# - should we drop this?
#
__all__ = [
    "ffi",
    "lib",
    "CidrBlock",
    "CidrBlocks",
    "CidrTools",
    "ct_add_cidr_to_cidrs",
    "ct_allocate_cidrs",
    "ct_cidr_contains_cidr",
    "ct_cidr_contains_ip",
    "ct_cidr_fix_host_bits",
    "ct_cidr_is_subnet",
    "ct_cidr_set_prefix",
    "ct_cidr_to_range",
    "ct_cidr_to_str",
    "ct_cidr_to_str_r",
    "ct_clean_cidr",
    "ct_clean_cidrs",
    "ct_compact",
    "ct_exclude_cidrs",
    "ct_format_host_bits",
    "ct_free_cidrs",
    "ct_get_host_bits",
    "ct_hostname_to_address",
    "ct_ip_address_increment",
    "ct_ip_address_range",
    "ct_ip_address_to_str",
    "ct_ip_address_to_str_r",
    "ct_ip_str_to_hostname",
    "ct_is_ipv4",
    "ct_is_ipv6",
    "ct_num_ips",
    "ct_range_to_cidrs",
    "ct_sort",
    "ct_split_by_family",
    "ct_str_to_cidr_block",
    "ct_str_to_cidr_parts",
    "ct_str_to_ip_address",
    "ct_subnets_split",
    "ct_version",
]
