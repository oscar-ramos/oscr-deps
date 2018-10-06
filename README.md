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
installed ), and *SET_BASH* is an optional parameter that must be included only
the very first time the instruction is run since it will add the *pkg-config*
to the *.bashrc*. For example, the following command:

    ./install-deps  ~/devel/control/install  SET_BASH

will install the dependencies to ~/devel/control/install. When *SET_BASH* is
omitted, nothing will be added to *.bashrc*. In the above example, when
recompiling, the *SET_BASH* should be ommited.

Note: it might be useful to check the output of the installation to see if
there has been any issue.


References
==========

For information about every library used in this package and the
*modifications* that were done, please refer to [DIFFS.md](DIFFS.md).


