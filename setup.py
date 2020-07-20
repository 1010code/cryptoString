#!/usr/bin/env python
# coding: utf-8

from setuptools import setup



setup(
    name='cryptoString',
    version='0.0.2',
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