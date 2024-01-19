#!/bin/bash
#
# This script includes solutions to the exercises of the Udemy Course - Section 9

# -------- Exercise 0 --------
while [ "${CORRECT}" != "y" ]
do
    read -p "Enter your name: " NAME
    read -p "Is ${NAME} correct? " CORRECT
done

echo "Done"
echo
# ----------------------------

# -------- Exercise 1 --------
echo "Reading the ./../data/test_passwd file"
echo

# Initialise iterator
LINE_NUM=1

# Loop through the file line by line
while read LINE
do
    echo "${LINE_NUM}: ${LINE}"
    ((LINE_NUM++))
done < /Users/s.porreca/Projects/cheat_sheets/shell_scripting/data/test_paswd
# ----------------------------