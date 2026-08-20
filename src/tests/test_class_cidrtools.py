"""
src/tests/test_wrapper_2.py
Unit tests for CidrTools class.
"""
import pytest
from cidrtools import CidrBlocks, CidrTools


def test_cidr_tools_version():
    """
    Verify that CidrTools can fetch the cidrtools c-library version
    """
    version = CidrTools.ct_version()
    assert isinstance(version, str)
    assert len(version) > 0


def test_range_to_cidrs():
    """
    Verify convert a range of IP addresses to list of CIDR blocks
    """
    cidrs = CidrTools.range_to_cidrs("192.168.1.0", "192.168.1.255")

    assert isinstance(cidrs, CidrBlocks)
    assert len(cidrs) == 1
    assert list(cidrs) == ["192.168.1.0/24"]


def test_range_to_cidrs_invalid():
    """
    Confirm invalid IP address(es) in a range raise a ValueError
    """
    with pytest.raises(ValueError):
        CidrTools.range_to_cidrs("not-an-ip", "192.168.1.255")
