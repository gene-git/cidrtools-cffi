# SPDX-License-Identifier: GPL-2.0-or-later
# SPDX-FileCopyrightText: © 2026-present Gene C <arch@sapience.com>
"""
ct_cidr_set_prefix.py
"""
from ._core import lib


def ct_cidr_set_prefix(cidr_ptr, prefix: int) -> int:
    """
    Wrap the correspnding cidrtools library function.
    """
    return lib.ct_cidr_set_prefix(cidr_ptr, prefix)
