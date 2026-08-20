"""
src/tests/test_wrapper_2.py
 - Test set 2
"""
import pytest
from cidrtools import CidrBlock, CidrBlocks


def test_block_fix_host_bits():
    """
    Fix host bits by setting them to zeros
    """
    #
    # A block with host bits set (i.e. .105 inside a /24)
    # - confirm the fixed cidr has them zerod out.
    # - CidrBlock will fix the host bits - but keeps track of them.
    #   no real need to call fix_host_bits
    #
    block = CidrBlock("192.168.1.105/24")
    block.fix_host_bits()

    assert str(block) == "192.168.1.0/24"


def test_block_set_prefix():
    """
    Change the prefix length
    """
    cidr = CidrBlock("10.0.0.0/8")
    cidr.set_prefix(16)
    assert str(cidr) == "10.0.0.0/16"


def test_block_to_range():
    """
    cidr to ip range. Chcke first and last IP address
    """
    block = CidrBlock("192.168.1.0/24")
    first, last = block.to_range()
    assert first == "192.168.1.0"
    assert last == "192.168.1.255"


def test_block_to_range_mid():
    """
    Get (first, mid, last) ip in cidr block.
    """
    block = CidrBlock("192.168.1.0/24")
    first, mid, last = block.to_range_mid()
    assert first == "192.168.1.0"
    assert mid == "192.168.1.127"
    assert last == "192.168.1.255"


def test_block_subnet_relationships():
    """
    Confirm is_subnet() does the right thing.
    """
    cidrs = CidrBlocks(["10.0.0.0/8"])
    child = CidrBlock("10.1.2.0/24")
    unrelated = CidrBlock("192.168.1.0/24")

    assert child.is_subnet_of(cidrs) is True
    assert unrelated.is_subnet_of(cidrs) is False


def test_block_split():
    """
    Split a cidr into smaller subnets
    """
    cidr = CidrBlock("192.168.1.0/24")
    # Splitting a /24 into /25 subnets should yield exactly two blocks
    subnets = cidr.split(25)
    assert isinstance(subnets, CidrBlocks)
    assert len(subnets) == 2
    assert list(subnets) == ["192.168.1.0/25", "192.168.1.128/25"]


def test_block_host_bits_isolation():
    """
    Get the "host bits" of cidr
    Note that cidr keeps track of the host bits
    """
    cidr = CidrBlock("192.168.1.22/24")
    assert str(cidr) == "192.168.1.0/24"
    assert cidr.format_host_bits() == "0.0.0.22"


def test_block_increment_by():
    """
    Increment an IP address by ionteger steps to get new IP
    Example 1.50 + 10 IPs => 1.60
    """
    cidr = CidrBlock("192.168.1.50/32")
    ip_new = cidr.increment_by(10)
    assert ip_new == "192.168.1.60"


# --- Tests with CidrBlocks ---

def test_collection_indexing_and_slicing():
    """
    Check basic indexing and slicing work as expected
    """
    cidrs = CidrBlocks(["10.0.0.0/24", "192.168.1.0/24", "172.16.0.0/16"])

    # Check absolute direct indexing
    assert cidrs[0] == "10.0.0.0/24"
    assert cidrs[1] == "192.168.1.0/24"

    # Check negative wrap-around indexing
    assert cidrs[-1] == "172.16.0.0/16"

    # Check slice extraction spans
    sliced_items = cidrs[0:2]
    assert isinstance(sliced_items, list)
    assert len(sliced_items) == 2
    assert sliced_items == ["10.0.0.0/24", "192.168.1.0/24"]

    # Out of bounds check
    with pytest.raises(IndexError):
        _ = cidrs[99]


def test_collection_split_by_family():
    """
    Split collection of cidrs into IPv4 and IPv6.
    """
    mixed_cidrs = CidrBlocks(["10.0.0.0/24", "2001:db8::/32", "192.168.1.0/24"])

    v4_cidrs, v6_cidrs = mixed_cidrs.split_by_family()

    assert isinstance(v4_cidrs, CidrBlocks)
    assert isinstance(v6_cidrs, CidrBlocks)

    assert list(v4_cidrs) == ["10.0.0.0/24", "192.168.1.0/24"]
    assert list(v6_cidrs) == ["2001:db8::/32"]
