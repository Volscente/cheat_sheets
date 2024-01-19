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
# Read from file line by line
echo "Reading the ./../data/test_passwd file"
echo

# Initialise line number
LINE_NUM=1

# Loop through the file line by line
while read LINE
do
    echo "${LINE_NUM}: ${LINE}"
    ((LINE_NUM++))
done < /Users/s.porreca/Projects/cheat_sheets/shell_scripting/data/test_paswd
echo
# ----------------------------

# -------- Exercise 2 --------
# Read the inserted number of lines

# Retrieve number of lines to read
read -p "Enter the number of lines to read from ./../data/test_passwd " NUM_LINES
echo

# Initialise iterator
ITERATOR=0

while [ "$ITERATOR" -lt "$NUM_LINES" ] && read LINE_READ
do
    echo "${LINE_READ}"
    ((ITERATOR++))
done < /Users/s.porreca/Projects/cheat_sheets/shell_scripting/data/test_paswd
echo
# ----------------------------

# -------- Exercise 3 --------
# Read user input and execute 1, 2, 3 commands as long as "q" is not typed

# Initialise loop variable
while TRUE
do
    echo "1. Show disk usage."
    echo "2. Shopw system uptime."
    echo "3. Show the users logged into the system."

    read -p "What would you like to do? (Enter 1 to quit.) " OPTION
    echo

    case ${OPTION} in
        1)
            echo "You choose option 1."
            echo
            df
            echo
            ;;
        2)
            echo "You choose option 2."
            echo
            uptime
            echo
            ;;
        3)
            echo "You choose option 3."
            echo
            who
            echo
            ;;
        q)
            echo "Goodbye!"
            echo
            break
            ;;
        *)
            echo "Invalid option."
            echo
            ;;
    esac
done
# ----------------------------