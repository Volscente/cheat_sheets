#!/bin/bash
#
# This script includes solutions to the exercises of the Udemy Course - Section 4

function file_count(){

    # Check if the argument is pased
    if [ -z ${1} ]
    then
        echo "No directory path is passed."
        return 1
    fi
    
    # TODO Check if it is a directory

}

file_count ${1}