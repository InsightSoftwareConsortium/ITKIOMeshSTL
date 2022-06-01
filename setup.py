# -*- coding: utf-8 -*-
from __future__ import print_function
from os import sys

try:
    from skbuild import setup
except ImportError:
    print('scikit-build is required to build from source.', file=sys.stderr)
    print('Please run:', file=sys.stderr)
    print('', file=sys.stderr)
    print('  python -m pip install scikit-build')
    sys.exit(1)

setup(
    name='itk-iomeshstl',
    version='2.2.0',
    author='Luis Ibáñez',
    author_email='community@itk.org',
    packages=['itk'],
    package_dir={'itk': 'itk'},
    download_url=r'https://github.com/InsightSoftwareConsortium/ITKIOMeshSTL',
    description=r'MeshIO class to read and write ITK meshes into STL files.',
    long_description='itk-stlmeshio provides a class to read and write ITK '
                     'meshes into STL files.\n'
                     'Please refer to:\n'
                     'Ibáñez L. "STL file format MeshIO class for ITK", '
                     'Insight Journal, January-December 2014, https://hdl.handle.net/10380/3452.',
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: C++",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Healthcare Industry",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Software Development :: Libraries",
        "Operating System :: Android",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Operating System :: Unix",
        "Operating System :: MacOS"
        ],
    license='Apache',
    keywords='ITK InsightToolkit STL Mesh',
    url=r'https://github.com/InsightSoftwareConsortium/ITKIOMeshSTL',
    install_requires=[
        r'itk>=5.2rc1'
    ]
    )
