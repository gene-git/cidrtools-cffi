# SPDX-License-Identifier: GPL-2.0-or-later
# SPDX-FileCopyrightText: © 2026-present Gene C <arch@sapience.com>
"""
ct_str_to_cidr_block.py
"""
from ._core import ffi, lib


def ct_str_to_cidr_block(ip_str: str, cidr_ptr) -> int:
    """
    Wrap the correspnding cidrtools library function.
    """
    c_str = ffi.new("char[]", ip_str.encode('utf-8'))
    return lib.ct_str_to_cidr_block(c_str, cidr_ptr)
