#!/bin/sh -e
set -x

ruff readyapi tests docs_src scripts --fix
black readyapi tests docs_src scripts
