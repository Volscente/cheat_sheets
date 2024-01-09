#!/bin/bash
#
# This script includes solutions to the exercises of the Udemy Course - Section 4

function file_count(){

    local DIR_PATH=${1}

    # Check if the argument is pased
    if [ -z ${DIR_PATH} ]
    then
        echo "No directory path is passed."
        return 1
    fi
    
    # TODO Check if it is a directory
    if [ -d ${DIR_PATH} ]
    then
        echo "${DIR_PATH}:"
        ls ${DIR_PATH} | wc -l
    else
        echo "The passed path is not a directory,"
        exit 2
    fi
}

file_count ${1}