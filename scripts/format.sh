#!/usr/bin/env bash
set -x

ruff check readyapi tests docs_src scripts --fix
ruff format readyapi tests docs_src scripts
