#!/usr/bin/python
"""
Couple of basic function checks
"""
import cidrtools

#
# version
#
print("cidrtools library version:", cidrtools.ct_version())

#
# make a cidr block
#
cidr = cidrtools.CidrBlock("192.168.1.0/24")
print(f"Total dynamic IP addresses inside {cidr}: {cidr.num_ips}")

#
# check if cidr in another cidr
#
print("192.168.1.50 inside cidr block?", "192.168.1.50" in cidr)

#
# Collection of cidr blocks
#
cidrs = cidrtools.CidrBlocks(["10.0.0.0/24", "10.0.1.0/24"])
cidrs.compact()
print("Compacted cidrs:", cidrs)
