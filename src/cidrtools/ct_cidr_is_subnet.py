# SPDX-License-Identifier: GPL-2.0-or-later
# SPDX-FileCopyrightText: © 2026-present Gene C <arch@sapience.com>
"""
ct_cidr_is_subnet.py
"""
from ._core import lib


def ct_cidr_is_subnet(cidr_ptr, cidrs_ptr) -> bool:
    """
    Wrap the correspnding cidrtools library function.
    """
    return bool(lib.ct_cidr_is_subnet(cidr_ptr, cidrs_ptr))
