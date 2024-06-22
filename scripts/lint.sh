#!/usr/bin/env bash

set -e
set -x

mypy readyapi
ruff readyapi tests docs_src scripts
black readyapi tests --check
