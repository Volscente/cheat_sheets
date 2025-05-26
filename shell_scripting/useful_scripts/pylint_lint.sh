#!/bin/bash
#
# Run PyLint with specific plugins loaded and message template

echo
echo "-------- PyLint Lint --------"
echo

# Lint
poetry run pylint --load-plugins pylint_pytest \
  --ignore-patterns=".*components.*|.*pipelines.*" \
  --disable='C0301, R0903, R0801, W0212, W0511' \
  --source-roots=./src \
  --output-format=colorized \
  --msg-template='Rule: {msg_id} - Position: [{line},{column}] -  {msg}' \
  ./src ./tests

echo
echo "--------------------------------"
echo
