# SPDX-License-Identifier: GPL-2.0-or-later
# SPDX-FileCopyrightText: © 2026-present Gene C <arch@sapience.com>
"""
ct_ip_address_range.py
"""
from ._core import lib


def ct_ip_address_range(addr_ptr, prefix: int, first_ptr, last_ptr) -> int:
    """
    Wrap the correspnding cidrtools library function.
    """
    return lib.ct_ip_address_range(addr_ptr, prefix, first_ptr, last_ptr)
