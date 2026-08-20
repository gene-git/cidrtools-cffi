# SPDX-License-Identifier: GPL-2.0-or-later
# SPDX-FileCopyrightText: © 2026-present Gene C <arch@sapience.com>
"""
ct_hostname_to_address.py
"""
from ._core import ffi, lib


def ct_hostname_to_address(hostname_str: str, cidrs_ptr) -> int:
    """
    Wrap the correspnding cidrtools library function.
    """
    c_host = ffi.new("char[]", hostname_str.encode('utf-8'))
    return lib.ct_hostname_to_address(c_host, cidrs_ptr)
