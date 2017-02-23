oscr-deps - Third-party (external) software needed for the oscr library

Introduction
============

OSCR-DEPS is a set of C++ packages composed of third-party libraries which are
dependencies of the OSCR (Operational Space Control for Robots) library. It is
highly recommended to use this package for compatibility with OSCR. However, if
this package is not used, the required libraries need to be separately
installed and available in your system (special care should be taken when
linking).

Note that these third-party libraries have been reduced to contain the minimum
functionalities needed by the OSCR library. The reduction refers to the
elimination of some files but not the modification of the source code. For more
details on each library, please refer to the documentation provided by the
original library source.

Setup: Building and Installation
================================

The oscr-deps package can be installed as:

    ./install-deps  PREFIX  [SET_BASH]

where PREFIX is the PATH where the third-party libraries will be installed (for
example: ~/devel/control/install)

If the option SET_BASH is used, the pkg-config path is added to the .bashrc
(needed to be run at least the first time)

RBDL
====

This library can be obtained from the bitbucket repo (mercurial) at:
     https://bitbucket.org/rbdl/rbdl

The version currently used is 2.5.0 and the mercurial changeset is
    1023:d5550334c3d1 (Sun Dec 11 2016)

Changes to the original RBDL package are:

  + The following folders/files have been removed (they are not used by this
    project): doc, Doxyfile, examples, python, utils, tests, addons/benchmark,
    addons/luamodel, hidden folders,

  + Add line 26 to simply use "lib" to install libraries (instead of
    architecture dependent library paths).

  + Add -lrbdl_urdfreader in line 11 of rbdl.pc.cmake (Libs) since urdf support
    is essential for OSCR

Pinocchio
=========

This library can be obtained from the github repo at:
     https://github.com/stack-of-tasks/pinocchio

The git commit that is currently used is:
    aafd6d818382b84433187792a91f45e4f43c4035 (Fri Oct 14 2016)

Changes to the original Pinocchio package are:

  + The following folders have been removed (they are not used by this
    project): doc, lab, models, travis_custom, cmake/doxygen, hidden folders

  + Commented out lines 23, 103-107, 295, 296, 302, 305 in CMakeLists.txt to
    avoid documentation issues and python bindings.

  + Commented out line 179 in cmake/base.cmake to avoid documentation issues

qpOASES-3.2.0
=============

This software package can be obtained from: 
    https://projects.coin-or.org/qpOASES/

The version that is currently used is 3.2.0

Changes to the original qpOASES package are:

  + The following folders have been removed (they are not used by this
    project): examples, doc, testing, interfaces. The following files have been
    removed: *.txt (except CMakeLists.txt), make*, Makefile

  + The examples are not build: the lines to compile them have been commented
    out in CMakeLists.txt (lines 143-146)
    
  + The library has been changed to SHARED: line 104 in CMakeLists.txt has been
    commented out and line 105 has been added
    
  + For package managing, pkg-config support was added: a new folder called
    pkg-config now contains CMakeLists.txt and qpoases.pc.cmake. Line 149 was
    added in the main CMakeLists.txt