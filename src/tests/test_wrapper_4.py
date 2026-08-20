"""
test_wrapper_4.py
"""
from cidrtools import CidrBlocks


def test_cidr_blocks_flat_buffer_init_and_export():
    """
    Validates a list of CIDR strings is successfully passed
    into the library and back out unaltered. Internally
    this involves mapping to and from a single string of comma separated
    cidr strings.
    """
    cidrs_in = ["10.0.0.0/24", "192.168.1.0/24", "172.16.0.0/16"]
    cidrs = CidrBlocks(cidrs_in)
    cidrs_out = cidrs.to_strings()

    assert len(cidrs_out) == len(cidrs_in)
    assert cidrs_out == cidrs_in


def test_cidr_blocks_empty_initialization():
    """
    Check that an empty list creates an instannce of
    CidrBlocks class.
    """
    # Input is None
    cidrs = CidrBlocks(None)
    assert cidrs.to_strings() == []

    # Input is empty list
    cidrs = CidrBlocks([])
    assert cidrs.to_strings() == []


def test_cidr_blocks_with_invalid_strings():
    """
    Confirm that bad cidr strings are correctly dropped from CidrBlocks.
    prefix are reset to uppere limit (/32 or /128) if above the max.
    Note that the last cidr below has prefix of /33 which will be
    repaired back to /32
    """
    cidr_list_good = ["10.0.0.0/24", "192.168.1.0/32"]
    cidr_list = ["10.0.0.0/24", "not_a_valid_cidr", "192.168.1.0/33"]

    cidrs = CidrBlocks(cidr_list)
    assert len(cidrs) == len(cidr_list_good)
    assert list(cidrs) == cidr_list_good
