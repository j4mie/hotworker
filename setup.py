#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='hotworker',
    version='0.2.0',
    description='Unix-friendly HotQueue worker processes',
    author='Jamie Matthews',
    author_email='jamie.matthews@gmail.com',
    url='https://github.com/j4mie/hotworker',
    license = 'Public Domain',
    py_modules=['hotworker'],
    install_requires=['hotqueue', 'simplesignals'],
    classifiers = [
        'Programming Language :: Python',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: Public Domain',
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Operating System :: Unix",
    ],
)
