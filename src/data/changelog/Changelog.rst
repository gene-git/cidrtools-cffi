Changelog
=========

Tags
====

.. code-block:: text

	0.3.0 (2026-08-13) -> 1.0.0 (2026-08-20)
	39 commits.

Commits
=======


* 2026-08-20  : **1.0.0**

.. code-block:: text

              - installer - clean before doing install
              - tidy up unit test code
              - Move tests into src/ directory
 2026-08-19   ⋯

.. code-block:: text

              - Update test_cidr_blocks_invalid_parsing_raises() now that excess prefixes are automatically repaired to the max allowed for tha networ family
              - small change in text when ValueError raised by CidrBlock
 2026-08-18   ⋯

.. code-block:: text

              - little fix for uv install to only install runtime python
                  meson handles the manuals etc
              - manual update
              - lint whitespace
 2026-08-17   ⋯

.. code-block:: text

              - snap
 2026-08-16   ⋯

.. code-block:: text

              - fix test now that CidrBlocks no longer errors on bad cidrs in list - it ignored them and keeps the good ones
              - add new test files
              - cleanups
              - update manual
              - prep for actual release - more to do
 2026-08-15   ⋯

.. code-block:: text

              - more optimizing CidrBlocks
              - Add new single buffer to c-array and back
                +    int ct_flat_buffer_to_cidrs(const char *flat_str, size_t count, CtCidrs *cidrs);
                +    char *ct_cidrs_to_flat_buffer(const CtCidrs *cidrs);
              - add the CidrBlocks.to_strings()
              - Use new cidrtools array creator ct_str_array_to_cidrs() for CidrBlocks()
              - snap
              - Add cidr.to_range_mid() wrap of cidrtools:ct_cidr_to_range_mid()
              - remove __pycache__
              - Name change: class CidrCollection -> CidrBlocks
              - Improve the API doc
              - the new mergeed file
              - merge block/collection to avoid cyclic import - python is goofy
 2026-08-14   ⋯

.. code-block:: text

              - almost lint clean
              - linting
              - more lint clean ups
              - Tidy up - add doc strings, license etc
              - drop unused wrapper.py
              - Reorg using protocol - keep type hints etc
 2026-08-13   ⋯

.. code-block:: text

              - snap
              - snap
              - snap
              - drop __pycache__
              - small PKGBUILD change

* 2026-08-13  : **0.3.0**

.. code-block:: text

              - udpates, add docs etc
              - FIrst working version
              - init commit - lots missing


