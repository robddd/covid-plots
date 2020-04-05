#!/bin/bash
set -x
set -e

virtualenv --no-site-packages --distribute --python python3.6 env
source env/bin/activate

pip install --upgrade pip
pip install -r requirements.txt