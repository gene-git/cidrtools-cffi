# SPDX-License-Identifier: GPL-2.0-or-later
# SPDX-FileCopyrightText: © 2026-present Gene C <arch@sapience.com>
"""
ct_allocate_cidrs.py
"""
from ._core import lib


def ct_allocate_cidrs(count: int, cidrs_ptr) -> bool:
    """
    Wrap the correspnding cidrtools library function.
    Allocates array of CtCidrBlock structs in a CtCidrs container
    """
    return bool(lib.ct_allocate_cidrs(count, cidrs_ptr))
