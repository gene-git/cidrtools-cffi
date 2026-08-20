"""
test_wrapper.py
 - unit test set of basic functions of CidrBlock
"""
import pytest
from cidrtools import CidrBlock


def test_cidr_block_creation():
    """
    Verify that a valid string is correctly created as a CidrBlock.
     - check string repr comes back the same as went int
    """
    block = CidrBlock("192.168.1.0/24")
    assert str(block) == "192.168.1.0/24"
    assert block.to_string() == "192.168.1.0/24"
    assert repr(block) == "<CidrBlock: 192.168.1.0/24>"


def test_cidr_block_invalid_creation():
    """
    Confirm an invalid cidr triggers a ValueError.
    """
    with pytest.raises(ValueError, match="Invalid CIDR block string"):
        CidrBlock("999.999.999.999/99")


@pytest.mark.parametrize("cidr, expected_v4, expected_v6", [
    ("10.0.0.0/8", True, False),
    ("2001:db8::/32", False, True)
    ])
def test_cidr_block_family_checks(cidr, expected_v4, expected_v6):
    """
    Verify family validation correct for both IPv4 and IPv4
    """
    block = CidrBlock(cidr)
    assert block.is_ipv4 is expected_v4
    assert block.is_ipv6 is expected_v6


@pytest.mark.parametrize("cidr,expected_count", [
    ("192.168.1.0/24", 256),
    ("10.0.0.0/30", 4),
    ("192.168.1.1/32", 1)
    ])
def test_cidr_block_num_ips(cidr, expected_count):
    """
    Verify the returned number of IPs in cidr blocks
    """
    block = CidrBlock(cidr)
    assert block.num_ips == expected_count


def test_cidr_block_subnet_check():
    """
    Check Python 'in' operator works to check is_subnet().
    """
    parent = CidrBlock("192.168.1.0/24")
    child = CidrBlock("192.168.1.128/25")
    other = CidrBlock("10.0.0.0/8")

    assert "192.168.1.50" in parent
    assert "10.0.0.1" not in parent
    assert "invalid-ip-string" not in parent

    assert child in parent
    assert other not in parent
