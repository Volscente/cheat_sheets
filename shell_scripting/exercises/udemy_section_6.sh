#!/bin/bash
#
# This script includes solutions to the exercises of the Udemy Course - Section 6

function rename_jpg_current_date(){
    # Rename .jpg files in the given directory with the current date

    local DIR_PATH=${1}

    # Check if the argument is passed
    if [ -z ${DIR_PATH} ]
    then
        echo "No directory path is passed."
        return 1
    fi

    # Check if the argument is a directory
    
}