#!/bin/bash -x
#
# This script includes solutions to the exercises of the Udemy Course - Section 10

# -------- Experiment --------
TEST_VAR="test"
echo "${TEST_VAR}"

DEBUG=true
$DEBUG && echo "Debug mode ON." 
$DEBUG || echo "Debug mode OFF."

PS4='+ $BASH_SOURCE : $LINENO : '
TEST_VAR="test"
echo "${TEST_VAR}"
