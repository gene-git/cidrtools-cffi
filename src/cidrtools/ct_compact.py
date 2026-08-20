# SPDX-License-Identifier: GPL-2.0-or-later
# SPDX-FileCopyrightText: © 2026-present Gene C <arch@sapience.com>
"""
ct_compact.py
"""
from ._core import lib


def ct_compact(cidrs_ptr) -> int:
    """
    Wrap the correspnding cidrtools library function.
    """
    return lib.ct_compact(cidrs_ptr)
