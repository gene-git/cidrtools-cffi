# SPDX-License-Identifier: GPL-2.0-or-later
# SPDX-FileCopyrightText: © 2026-present Gene C <arch@sapience.com>
"""
ct_add_cidr_to_cidrs.py
"""
from ._core import lib


def ct_add_cidr_to_cidrs(cidrs_ptr, cidr_ptr) -> bool:
    """
    Wrap the correspnding cidrtools shared library function.
    """
    return bool(lib.ct_add_cidr_to_cidrs(cidrs_ptr, cidr_ptr))
