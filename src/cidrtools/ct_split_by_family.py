# SPDX-License-Identifier: GPL-2.0-or-later
# SPDX-FileCopyrightText: © 2026-present Gene C <arch@sapience.com>
"""
ct_split_by_family.py
"""
from ._core import lib


def ct_split_by_family(cidrs_ptr, v4_ptr, v6_ptr) -> int:
    """
    Wrap the correspnding cidrtools library function.
    """
    return lib.ct_split_by_family(cidrs_ptr, v4_ptr, v6_ptr)
