#!/usr/bin/env bash
set -x

ruff check readyapi tests examples scripts --fix
ruff format readyapi tests examples scripts
