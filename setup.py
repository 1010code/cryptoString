#!/usr/bin/env python
# coding: utf-8


from setuptools import setup, find_packages
from os import path, environ
 
from io import open
 
here = path.abspath(path.dirname(__file__))
 
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='cryptoString',
    version='0.0.3',
    author='andy6804tw',
    author_email='andy6804tw@yahoo.com.tw',
    url='https://github.com/1010code/cryptoString',
    description='A module that returns alphanumeric strings.',
    packages=['cryptoString'],
    install_requires=[],
    entry_points={
        'consoleScripts': [
            'cryptoString=cryptoString:version'
        ]
    }
)