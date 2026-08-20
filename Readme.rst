===============
cidrtools-cffi
===============

Python CFFI bindings for the high-performance `cidrtools <https://github.com/gene-git/cidrtools>`_
C library. 

This module provides a suite of tools to examine and manipulate 
network cidr blocks. It has the same functionality as the *cidrtools* library.

The source is available in `Github cidrtools-cffi <https://github.com/gene-git/cidrtools-cffi>`_ as 
well as `Arch AUR <https://aur.archlinux.org/packages/py-cidr>`_

This package exposes the complete ``cidrtools`` API. It provides an fast bridge to the underlying 
C structures and all the functions in the shared library.

Features
========

* **Zero-Overhead Performance:** Runs complex operations (like block compacting) at native C speeds.
* **Highly Maintainable:** Written in pure Python via CFFI ABI mode — no compilation needed.
* **Modern Tooling :** managed by ``uv``, ``meson``, and ``meson-python``.
* **Robust Interface:** Memory handling, garbage collection provided via three classes.

The python module is named *cudrtools* to match the underlying c-library.
It provides these classes:

* CidrBlock - for a single cidr.
* CidrBlocks - for collection of cidrs.
* CidrTools - convenient DNS lookup (forward and reverse).

Performance Benchmarks
======================

The following benchmarks measure the execution time required to process a random sample of **100,000 subnets** and compact them down to **54,941 subnets**.

Compared to native Python architectures, this CFFI implementation achieves a near **80x performance increase**:

.. code-block:: text

    Version Used            Seconds        Relative
    -------------------     --------       --------    
    (a) Raw C-Code          0.011892861     1.0 x
    (b) CFFI Wrapper        0.011995342     1.0 x
    (c) Cython/C Bridge     0.021802806     1.8 x
    (d) Pure Cython         0.026872699     2.3 x
    (e) Pure Python         0.935538276    78.7 x

    *100,000 subnets compacted to 54,941 subnets


Installation
============

The package is available in the Arch linux AUR using the PKGBUILD provided in the *packaging* 
directory. It can also be used locally directly from the git repo.. 

It can also be installed locally using the the provided scripts:

.. code-block:: bash

   ./scripts/do-build
   ./scripts/do-install
   ./scripts/run-tests

The default install directory is *build/pkg*, but *do-install* takes the destination directory
as an argument as well.


Usage Example
=============

High-Level API
--------------

.. code-block:: python

   from cidrtools import CidrBlock, CidrBlocks

   # Instantiating one cidr block from a string.
   cidr = CidrBlock("192.168.1.0/24")
   print(f"IPs within network: {cidr.num_ips}")

   # Check if ip or cidr is in the cidr subnet.
   ip_str = "192.168.1.50" 
   is_in = "is" if (ip_str in cidr) else "is not"
   print(f' {ip_str} {is_in} in {cidr}')  

   # Similarly
   subcidr = CidrBlock("192.168.1.50")
   subcidr in cidr 
   => True

   => 192.168.1.50 is in 192.168.1.0/24

   cidrs = CidrBlocks(["192.168.1.0/23", "10.0.0.0/24"])
   is_subnet = "is" if cidr.is_subnet_of(cidrs) else "is not"
   print(f' {str(cidr)} {is_subnet} a subnet of {list(cidrs)}')  

   => 192.168.1.0/24 is a subnet of ['192.168.0.0/23', '10.0.0.0/24']

   cidrs.add('10.0.2.0/24')
   list(cidrs)
   
   => ['192.168.0.0/23', '10.0.0.0/24', '10.0.2.0/24']

   cidrs.compact()
   list(cidrs)

   => ['10.0.0.0/24', '10.0.2.0/24', '192.168.0.0/23']

   cidrs = CidrCollection(["192.168.1.0/25", "192.168.1.128/25"])
   cidrs.sort()
   cidrs.compact()

   # back to a standard Python list of strings
   print(list(cidrs))  # Output: ['192.168.1.0/24']

API Reference
=============

Documentation is built with Sphinx. The PDF manual is in
*src/data/docs* and installed to */usr/share/cidrtools-cffi*. 

To create a local copy of the html and PDF documentation:

.. code-block:: bash

   cd src/data/docs 
   ./buld-manual.sh

AI Tooling
==========

Assisted by:

* Anthropic's `Claude <https://claude.ai>`_

* Google's `Gemini <https://gemini.google.com/>`_

.. rubric:: Footnotes

