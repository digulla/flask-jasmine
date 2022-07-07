#!/bin/bash

export PYTHONPATH="$PWD"

echo "To run the tests, browse http://127.0.0.1:5000/jasmine/testrunner/"
pipenv run python tests/jasmine_tests.py
