#!/bin/bash
#
# This script includes solutions to the exercises of the Udemy Course - Section 2

# User input
FILEPATHS=${@}

# Check if it is a regular file
for FILEPATH in ${FILEPATHS}
do
    if [ -f ${FILEPATH} ]
    then
        echo "It is a regualar file."
    else
        echo "It is NOT a regular file."
    fi
done