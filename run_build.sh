#!/bin/bash

rm -rf build cryptoString.egg-info dist
echo "clean dist folder!"
python setup.py sdist bdist_wheel
echo "build successfully!"