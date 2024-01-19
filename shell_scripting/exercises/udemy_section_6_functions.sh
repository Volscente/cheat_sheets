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

function rename_extension(){
    # Rename files by append current date based on extension

    # Request user for file extension
    read -p "Insert your file extension here: " FILE_EXTENSION
    echo "You've inserted: ${FILE_EXTENSION}."

    # Request user for prefix
    read -p "Insert your prefix here: " PREFIX

    # Check if prefix has been inserted
    if [ -z ${PREFIX} ]
    then
        echo "No prefix inserted."
        local CURRENT_DATE=$(date '+%Y%m%d')
        echo "Default prefix used: ${CURRENT_DATE}."
    else
        echo "You've inserted: ${PREFIX}."
    fi

    # Check if files with the inserted extension are present in the current dir
    if [ $(ls -A *.${FILE_EXTENSION}) ]
    then
        echo "No files with extension ${FILE_EXTENSION} are present."
        exit 0
    else

        # Loop through files
        for FILE in $(ls *.${FILE_EXTENSION})
        do
            echo ${FILE}
        done
    fi
}

rename_extension
