.. SPDX-License-Identifier: GPL-2.0-or-later

========
Appendix
========

Installation
============

On Arch you can build using the provided PKGBUILD in the packaging directory or from the AUR.
To build manually, clone the repo and :

 .. code-block:: bash

        rm -f dist/*
        ./scripts/do-build
        ./scripts/do-install [destination]

The default destination is *build/pkg*.

Dependencies
============

**Run Time** :

* cidrtools
* python-cffi
* python          (3.14 or later)

**Building Package** :

* git
* meson
* meson-python
* uv
* python-uv-build
* rsync
* python-pytest
* python-pytest-asyncio


Philosophy
==========

We follow the *live at head commit* philosophy as recommended by
Google's Abseil team [1]_.  This means we recommend using the
latest commit on git master branch. 


.. [1] https://abseil.io/about/philosophy#upgrade-support


