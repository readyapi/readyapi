#! /bin/bash

set -ex # fail on first error, print commands

mypy readyapi
ruff check readyapi tests docs_src scripts
ruff format readyapi tests --check

SRC_DIR=${SRC_DIR:-`pwd`}
echo "Checking documentation..."
python -m pydocstyle --convention=numpy ${SRC_DIR}/readyapi/
echo "Success!"

echo "Checking code style with black..."
python -m black -l 100 --check ${SRC_DIR}/readyapi/ ${SRC_DIR}/docs_src/ ${SRC_DIR}/tests/ x${SRC_DIR}/scripts/
echo "Success!"

echo "Checking code style with pylint..."
python -m pylint ${SRC_DIR}/readyapi/
echo "Success!"
