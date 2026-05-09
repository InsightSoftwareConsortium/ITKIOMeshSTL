ITKIOMeshSTL
============

.. image:: https://github.com/InsightSoftwareConsortium/ITKIOMeshSTL/workflows/Build,%20test,%20package/badge.svg

.. image:: https://img.shields.io/pypi/v/itk-iomeshstl.svg
    :target: https://pypi.python.org/pypi/itk-iomeshstl
    :alt: PyPI

.. image:: https://img.shields.io/badge/License-Apache%202.0-blue.svg
    :target: https://github.com/InsightSoftwareConsortium/ITKIOMeshSTL/blob/master/LICENSE
    :alt: License

Overview
--------

This repository contains an ITK MeshIO class to read and write ITK meshes into
STL files.

For more information, see the `Insight Journal article <https://hdl.handle.net/10380/3452>`_::

  Ibáñez L.
  STL file format MeshIO class for ITK
  The Insight Journal. January-December. 2014.
  https://hdl.handle.net/10380/3452
  https://www.insight-journal.org/browse/publication/913


Installation
------------

To install the Python package::

  python -m pip install itk-iomeshstl

To build the C++ module, either enable the CMake option in ITK's
build configuration::

  Module_IOMeshSTL:BOOL=ON

Or, build the module as a separate project against an ITK build tree::

  git clone https://github.com/InsightSoftwareConsortium/ITKIOMeshSTL
  mkdir ITKIOMeshSTL-bulid
  cd ITKIOMeshSTL-build
  cmake -DITK_DIR=/path/to/ITK-build ../ITKIOMeshSTL
  cmake --build .

License
-------

This software is distributed under the Apache 2.0 license. Please see the
*LICENSE* file for details.
