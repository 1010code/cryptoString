#!/usr/bin/env python
# coding: utf-8

from setuptools import setup

setup(
    name='crypto-string',
    version='0.0.1',
    author='andy6804tw',
    author_email='andy6804tw@yahoo.com.tw',
    url='https://github.com/andy6804tw',
    description='A module that returns alphanumeric strings.',
    packages=['crypto-string'],
    install_requires=[],
    entry_points={
        'console_scripts': [
            'crypto-string=crypto-string:version'
        ]
    }
)