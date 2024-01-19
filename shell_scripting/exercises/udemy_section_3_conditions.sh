#!/bin/bash
#
# This script includes solutions to the exercises of the Udemy Course - Section 3

# Parse argument
FILENAME=${1}

# Check if it is a regular file
if [ -f ${FILENAME} ]
then
    echo "${FILENAME} is a regular file."
    exit 0
elif [ -d ${FILENAME} ]
then
    echo "${FILENAME} is a directory."
    exit 1
else
    echo "${FILENAME} is another file."
    exit 2
fi
