# SPDX-License-Identifier: GPL-2.0-or-later
# SPDX-FileCopyrightText: © 2026-present Gene C <arch@sapience.com>
"""
ct_cidr_contains_ip.py
"""
from ._core import lib


def ct_cidr_contains_ip(cidr_ptr, ip_ptr) -> bool:
    """
    Wrap the correspnding cidrtools library function.
    """
    return bool(lib.ct_cidr_contains_ip(cidr_ptr, ip_ptr))
