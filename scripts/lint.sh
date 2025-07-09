#!/usr/bin/env bash

set -e
set -x

mypy readyapi
ruff check readyapi tests examples scripts
ruff format readyapi tests --check
