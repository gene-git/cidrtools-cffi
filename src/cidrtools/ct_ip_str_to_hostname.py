# SPDX-License-Identifier: GPL-2.0-or-later
# SPDX-FileCopyrightText: © 2026-present Gene C <arch@sapience.com>
"""
ct_ip_str_to_hostname.py
"""
from ._core import ffi, lib


def ct_ip_str_to_hostname(ip_str: str, max_hostname_len: int = 256) -> tuple[int, str]:
    """
    Wrap the correspnding cidrtools library function.
    """
    c_ip = ffi.new("char[]", ip_str.encode('utf-8'))
    c_host = ffi.new("char[]", max_hostname_len)
    result = lib.ct_ip_str_to_hostname(c_ip, c_host)
    return result, ffi.string(c_host).decode('utf-8')
