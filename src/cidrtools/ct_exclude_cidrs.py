# SPDX-License-Identifier: GPL-2.0-or-later
# SPDX-FileCopyrightText: © 2026-present Gene C <arch@sapience.com>
"""
ct_exclude_cidrs.py
"""
from ._core import lib


def ct_exclude_cidrs(all_ptr, excluded_ptr) -> int:
    """
    Wrap the correspnding cidrtools library function.
    """
    return lib.ct_exclude_cidrs(all_ptr, excluded_ptr)
