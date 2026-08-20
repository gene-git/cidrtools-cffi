# SPDX-License-Identifier: GPL-2.0-or-later
# SPDX-FileCopyrightText: © 2026-present Gene C <arch@sapience.com>
"""
ct_cidr_to_str_r.py
"""
from ._core import ffi, lib


def ct_cidr_to_str_r(cidr_ptr, max_len: int = 128) -> tuple[int, str]:
    """
    Wrap the correspnding cidrtools library function.
    ."""
    buf = ffi.new("char[]", max_len)
    result = lib.ct_cidr_to_str_r(cidr_ptr, buf, max_len)
    return result, ffi.string(buf).decode('utf-8')
