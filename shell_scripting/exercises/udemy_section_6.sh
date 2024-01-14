#!/bin/bash
#
# This script includes solutions to the exercises of the Udemy Course - Section 6

function rename_jpg_current_date(){
    # Append .jpg files in the current directory with the current date

    # Check if there are .jpg files
    if [ $(ls -A *.jpg) ]
    then

        # Retrieve current date
        local CURRENT_DATE=$(date '+%Y%m%d')

        # Loop through .jpg files
        for FILE in $(ls *.jpg)
        do
            mv ${FILE} ${CURRENT_DATE}${FILE}     
        done
        
    else
        echo "no files found"
        exit 0
    fi
}

rename_jpg_current_date
