"""
test_wrapper_4.py
"""
from cidrtools import CidrBlocks


def test_intersection():
    """
    Validates a list of CIDR strings is successfully passed
    into the library and back out unaltered. Internally
    this involves mapping to and from a single string of comma separated
    cidr strings.
    """
    cidrs_1_str = ["192.168.1.0/24", "10.1.0.0/24"]
    cidrs_2_str = ["10.1.0.0/22", "100.100.100.0/23"]

    inters_str = ["10.1.0.0/24"]

    cidrs_1 = CidrBlocks(cidrs_1_str)
    cidrs_2 = CidrBlocks(cidrs_2_str)

    cidrs = CidrBlocks()

    assert cidrs_1.intersection(cidrs_2, cidrs) == 0
    cidrs_str = cidrs.to_strings()

    assert len(cidrs_str) == len(inters_str)
    assert cidrs_str == inters_str
    assert cidrs_str == inters_str
