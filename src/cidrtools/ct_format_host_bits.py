# SPDX-License-Identifier: GPL-2.0-or-later
# SPDX-FileCopyrightText: © 2026-present Gene C <arch@sapience.com>
"""
ct_format_host_bits.py
"""
# pylint: disable=duplicate-code
from ._core import ffi, lib


def ct_format_host_bits(cidr_ptr) -> str:
    """
    Wrap the correspnding cidrtools library function.
    """
    c_str = lib.ct_format_host_bits(cidr_ptr)
    if c_str == ffi.NULL:
        return ""
    try:
        return ffi.string(c_str).decode('utf-8')
    finally:
        lib.free(c_str)
