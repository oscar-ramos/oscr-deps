*oscr-deps* - Third-party (external) software needed for the
[*oscr*](https://github.com/oscar-ramos/oscr) library

Introduction
============

**OSCR-DEPS** is a set of C++ packages composed of third-party libraries which
are **dep**endencies of the **oscr** (**O**perational **S**pace **C**ontrol for
**R**obots) library. It is highly recommended to use this package for
compatibility with OSCR. However, if this package is not used, the required
libraries need to be separately installed and available in your system (special
care should be taken when linking).

Note that these third-party libraries have been reduced to contain the minimum
functionalities needed by the *OSCR* library. The reduction refers to the
elimination of some files but not the modification of the source code. For more
details on each library, please refer to the documentation provided by the
original library source.


Setup: Building and Installation
================================

The oscr-deps package can be installed as:

    ./install-deps  your_prefix  SET_BASH

where *your_prefix* is the PATH where the third-party libraries will be
installed (for example: ~/devel/control/install), and *SET_BASH* is an optional
parameter that must be included only the very first time the instruction is
run.

Note: When *SET_BASH* is used, the *pkg-config* path is added to the
*.bashrc*. When *SET_BASH* is omitted, nothing will be copied to *.bashrc*.


References
==========

For information about every library used in this package and the
*modifications* that were done, please refer to [DIFFS.md](DIFFS.md).


