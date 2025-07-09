#!/usr/bin/env bash

set -e
set -x

export PYTHONPATH=./examples
coverage run -m pytest tests ${@}
