#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
try:
    from setuptools import find_packages, setup
except ImportError:
    from distutils.core import setup, find_packages


with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-pb',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    long_description=README,
    url='',
    author='myyang',
    author_email='ymy1019@gmail.com',
    install_requires=['django>=1.10'],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.10',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
