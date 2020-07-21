#!/usr/bin/env python
# coding: utf-8
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name='cryptoString',
    version='1.0.1',
    author='andy6804tw',
    author_email='andy6804tw@yahoo.com.tw',
    url='https://github.com/1010code/cryptoString',
    description='A module that returns alphanumeric strings.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=[],
    entry_points={
        'consoleScripts': [
            'cryptoString=cryptoString:version'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)