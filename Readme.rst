===============
cidrtools-cffi
===============

Python CFFI bindings for the high-performance `cidrtools <https://github.com/gene-git/cidrtools>`_
C library. 

This module provides a suite of tools to examine and manipulate 
network cidr blocks. It has the same functionality as the *cidrtools* library.

The source is available in `Github cidrtools-cffi <https://github.com/gene-git/cidrtools-cffi>`_ as 
well as `Arch AUR <https://aur.archlinux.org/packages/py-cidr>`_

This package exposes the complete ``cidrtools`` public API using a modular, split-file architecture. It provides an optimized ABI-mode bridge to the underlying C structures alongside an ergonomic, object-oriented Python layer.

Features
========

* **Zero-Overhead Performance:** Runs complex operations (like block compacting) at 100% native C speeds.
* **Highly Maintainable:** Written entirely in pure Python via CFFI ABI mode—no complex Cython generation or compilation needed.
* **Modern Tooling Pipeline:** Fully managed by ``uv``, ``meson``, and ``meson-python``.
* **Robust Object Interface:** Complete memory handling, automatic garbage collection hooks, and native operator overloading.

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

To develop or use this library locally within your virtual environment managed by ``uv``, execute the following commands in the project root:

.. code-block:: bash

   # Sync environment dependencies
   uv sync

   # Install the package in editable development mode
   uv pip install -e .

   # Execute the pytest suite to verify your setup
   uv run pytest

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

   networks = CidrCollection(["192.168.1.0/25", "192.168.1.128/25"])
   networks.sort()
   networks.compact()

   # back to a standard Python list of strings
   print(list(networks))  # Output: ['192.168.1.0/24']

API Reference
=============

Documentation is built ausing Sphinx and the PDF manual is found in
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

