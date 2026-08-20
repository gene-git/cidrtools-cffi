# SPDX-License-Identifier: GPL-2.0-or-later
# SPDX-FileCopyrightText: © 2026-present Gene C <arch@sapience.com>
"""
ct_cidr_fix_host_bits.py
"""
from ._core import lib


def ct_cidr_fix_host_bits(cidr_ptr) -> int:
    """
    Wrap the correspnding cidrtools library function.
    """
    return lib.ct_cidr_fix_host_bits(cidr_ptr)
