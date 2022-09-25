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
    packages=['touchdown', 'touchdown.utils'],

    # creates the `touchdown` command on the commandline
    entry_points={
        'console_scripts': [
            'touchdown=touchdown.__main__:touchdown',
        ]
    },
 )
