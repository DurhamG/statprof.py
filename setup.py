#!/usr/bin/env python

import os, sys
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

extra = {}
if sys.version_info >= (3,):
    extra['use_2to3'] = True

setup(
    name="statprof",
    version="0.1.2",
    author="Bryan O'Sullivan",
    author_email="bos@serpentine.com",
    description="Statistical profiling for Python",
    license=read('LICENSE'),
    keywords="profiling",
    url="http://packages.python.org/statprof",
    py_modules=['statprof'],
    long_description=read('README.rst'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
    ],
    **extra
)
