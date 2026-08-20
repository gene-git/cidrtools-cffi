"""
test_wrapper_3.py
"""
from cidrtools import CidrBlock


def test_block_host_bits_isolation():
    """
    Double check can retrieve the host bits
    """
    cidr = CidrBlock("192.168.1.50/24")
    assert cidr.get_host_bits() == "0.0.0.50"
    assert cidr.format_host_bits() == "0.0.0.50"

    cidr = CidrBlock("2001:db8::abcd:1234/112")
    assert cidr.get_host_bits() == "::1234"
    assert cidr.format_host_bits() == "::1234"

    # edge case: /32 (result is 0.0.0.0 since no host bits remain)
    cidr = CidrBlock("192.168.1.50/32")
    assert cidr.get_host_bits() == "0.0.0.0"


def test_cidr_parts():
    """
    Verify cidr -> (ip, prefix)
    """
    cidr = CidrBlock("192.168.1.50/24")
    (ip, prefix) = cidr.cidr_parts()
    assert ip == "192.168.1.50"
    assert prefix == 24

    cidr = CidrBlock("2001:db8::abcd:1234/112")
    (ip, prefix) = cidr.cidr_parts()
    assert ip == "2001:db8::abcd:1234"
    assert prefix == 112
