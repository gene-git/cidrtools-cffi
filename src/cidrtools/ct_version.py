# SPDX-License-Identifier: GPL-2.0-or-later
# SPDX-FileCopyrightText: © 2026-present Gene C <arch@sapience.com>
"""
ct_version.py
"""
from ._core import ffi, lib


def ct_version() -> str:
    """
    Wrap the correspnding cidrtools library function.

    Returns the version string of the cidrtools library
    """
    c_str = lib.ct_version()
    if c_str == ffi.NULL:
        return ""
    return ffi.string(c_str).decode('utf-8')
