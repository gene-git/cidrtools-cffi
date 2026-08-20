# SPDX-License-Identifier: GPL-2.0-or-later
# SPDX-FileCopyrightText: © 2026-present Gene C <arch@sapience.com>
"""
ct_cidr_to_str.py
"""
# pylint: disable=duplicate-code
from ._core import ffi, lib


def ct_cidr_to_str(cidr_ptr) -> str:
    """
    Wrap the correspnding cidrtools library function.
    """
    c_str = lib.ct_cidr_to_str(cidr_ptr)
    if c_str == ffi.NULL:
        return ""
    try:
        return ffi.string(c_str).decode('utf-8')
    finally:
        # Since this returns a fresh char* from the C library,
        # it must be freed to prevent memory leaks.
        # If your library exposes a specific free function, use that instead of ffi.C.free
        lib.free(c_str)
