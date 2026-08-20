# SPDX-License-Identifier: GPL-2.0-or-later
# SPDX-FileCopyrightText: © 2026-present Gene C <arch@sapience.com>
"""
ct_is_ipv6.py
"""
from ._core import lib


def ct_is_ipv6(cidr_ptr) -> bool:
    """
    Wrap the correspnding cidrtools library function.
    """
    return bool(lib.ct_is_ipv6(cidr_ptr))
