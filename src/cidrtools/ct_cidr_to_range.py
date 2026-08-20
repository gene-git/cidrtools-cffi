# SPDX-License-Identifier: GPL-2.0-or-later
# SPDX-FileCopyrightText: © 2026-present Gene C <arch@sapience.com>
"""
ct_cidr_to_range.py
"""
from ._core import lib


def ct_cidr_to_range(cidr_ptr, first_ptr, last_ptr) -> int:
    """
    Wrap the correspnding cidrtools library function.
    """
    return lib.ct_cidr_to_range(cidr_ptr, first_ptr, last_ptr)


def ct_cidr_to_range_mid(cidr_ptr, first_ptr, mid_ptr, last_ptr) -> int:
    """
    Wrap the correspnding cidrtools library function.
    """
    return lib.ct_cidr_to_range(cidr_ptr, first_ptr, mid_ptr, last_ptr)
