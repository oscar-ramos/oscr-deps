This file provides basic information about where to download the original
libraries, the current version that is used, and the changes to the original
files. For more information about each library, please refer to the original
projects.


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

  + Line 14 of addons/urdfreader/urdfreader.cc was commented out since it
    causes problems when ros.h is not found (e.g. with ros kinetic)

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
