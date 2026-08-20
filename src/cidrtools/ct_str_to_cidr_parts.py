# SPDX-License-Identifier: GPL-2.0-or-later
# SPDX-FileCopyrightText: © 2026-present Gene C <arch@sapience.com>
"""
ct_str_to_cidr_parts.py
"""
from ._core import ffi, lib


def ct_str_to_cidr_parts(cidr_str: str, max_ip_len: int = 64) -> tuple[int, str, int]:
    """
    Wrap the correspnding cidrtools library function.
    """
    c_cidr = ffi.new("char[]", cidr_str.encode('utf-8'))
    c_ip_buf = ffi.new("char[]", max_ip_len)
    c_prefix = ffi.new("uint8_t *")

    result = lib.ct_str_to_cidr_parts(c_cidr, c_ip_buf, max_ip_len, c_prefix)
    return result, ffi.string(c_ip_buf).decode('utf-8'), c_prefix[0]
