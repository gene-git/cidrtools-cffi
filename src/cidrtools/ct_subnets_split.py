# SPDX-License-Identifier: GPL-2.0-or-later
# SPDX-FileCopyrightText: © 2026-present Gene C <arch@sapience.com>
"""
ct_subnets_split.py
"""
from ._core import ffi, lib


def ct_subnets_split(cidr_ptr, prefix: int):
    """
    Wrap the correspnding cidrtools library function.
    Returns a pointer to a newly allocated CtCidrs struct.
    """
    res_ptr = lib.ct_subnets_split(cidr_ptr, prefix)
    if res_ptr == ffi.NULL:
        return None
    return res_ptr
