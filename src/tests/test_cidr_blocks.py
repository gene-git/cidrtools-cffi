"""
test_cidr_blocks.py
 - unit test set of basic CidrBlocks functions
"""
import gc
import weakref
from cidrtools import CidrBlock, CidrBlocks


def test_cidr_collection_empty():
    """
    Check CidrBlocks initializes with empty set of cidr blocks.
    """
    cidrs = CidrBlocks()

    assert len(cidrs) == 0
    assert not list(cidrs)


def test_cidr_collection_initialization():
    """
    Check CidrBlocks initialize with list of cidr strings.
    """
    items = ["10.0.0.0/24", "192.168.1.0/24"]
    cidrs = CidrBlocks(items)

    assert len(cidrs) == 2
    assert list(cidrs) == items


def test_cidr_collection_add():
    """
    Check can append both a cidr string and CidrBlock to CidrBlocks
    """
    cidrs = CidrBlocks()
    assert cidrs.add("10.0.0.0/24") is True

    cidr = CidrBlock("192.168.1.0/24")
    assert cidrs.add(cidr) is True
    assert len(cidrs) == 2


def test_cidr_collection_sort_and_clean():
    """
    Validate sorting of cidrs and running clean on the sorted output.
    """
    cidrs = CidrBlocks(["192.168.1.0/24", "10.0.0.0/24"])

    cidrs.sort()
    assert list(cidrs) == ["10.0.0.0/24", "192.168.1.0/24"]
    assert cidrs.clean()


def test_cidr_collection_compact():
    """
    Check compacting cidrs with overlapping and/or adjacent subnets returns the
    minimal set of cidr blocks.
    """
    cidrs = CidrBlocks(["192.168.1.0/25", "192.168.1.128/25", "10.0.0.0/24", "10.0.1.0/24"])

    cidrs.compact()

    assert len(cidrs) == 2
    assert list(cidrs) == ["10.0.0.0/23", "192.168.1.0/24"]


def test_cidr_collection_exclude():
    """
    Check excluding one set of cidrs from another works correctly
    """
    base_pool = CidrBlocks(["192.168.1.0/24"])
    exclusions = CidrBlocks(["192.168.1.0/25"])

    base_pool.exclude(exclusions)

    # Excluding first half a /24 block leaves the other half which is /25
    assert list(base_pool) == ["192.168.1.128/25"]


def test_cidr_blocks_garbage_collection():
    """
    Confirm python garbage collection triggers the underlying C memory to be frees.
    """
    cidr_strings = ["10.0.0.0/24"]
    cidrs = CidrBlocks(cidr_strings)

    # Check has the right data
    assert cidrs.to_strings() == cidr_strings

    # Check garbage collection
    tracker = weakref.ref(cidrs)

    del cidrs
    gc.collect()
    assert tracker() is None
