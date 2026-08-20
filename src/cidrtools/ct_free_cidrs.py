# SPDX-License-Identifier: GPL-2.0-or-later
# SPDX-FileCopyrightText: © 2026-present Gene C <arch@sapience.com>
"""
ct_free_cidrs.py
"""
from ._core import ffi, lib


def ct_free_cidrs(cidrs_ptr) -> None:
    """
    Wrap the correspnding cidrtools library function.
    Frees any allocated memory blocks within CtCidrs
    """
    if cidrs_ptr != ffi.NULL:
        lib.ct_free_cidrs(cidrs_ptr)
