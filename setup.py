#!/usr/bin/env python

from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='touchdown',
    version='1.0',
    description='Mdx compiler and CLI',
    long_description=long_description,
    author='Doug Rudolph',
    url='https://github.com/11/touchdown',
    packages=find_packages()
 )
