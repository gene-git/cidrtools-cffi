# SPDX-License-Identifier: GPL-2.0-or-later
# SPDX-FileCopyrightText: © 2026-present Gene C <arch@sapience.com>
"""
ct_ip_address_increment.py
"""
from ._core import lib


def ct_ip_address_increment(addr_ptr, num: int, addr_inc_ptr) -> int:
    """
    Wrap the correspnding cidrtools library function.
    """
    return lib.ct_ip_address_increment(addr_ptr, num, addr_inc_ptr)
