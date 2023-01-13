#!/bin/bash

git clone https://github.com/michellab/biosimspace -b feature-2023_1
cd biosimspace/python
python setup.py install
cd ../..
rm -rf biosimspace
