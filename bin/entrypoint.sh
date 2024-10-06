#!/bin/bash
# Intended to run in a docker container. Is a Dockerfile entrypoint.

# Flag to make errors stop the execution
set -e

# Variable to
RUN_MANAGE_PY='poetry run python -m src.manage'

echo 'ENTRY: Collecting static file'
$RUN_MANAGE_PY collectstatic --no-input

echo 'ENTRY: Running migrations'
$RUN_MANAGE_PY migrate --no-input

echo 'ENTRY: Running Django server'
$RUN_MANAGE_PY runserver 0.0.0.0:8000
