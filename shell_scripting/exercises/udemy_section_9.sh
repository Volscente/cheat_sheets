#!/bin/bash
#
# This script includes solutions to the exercises of the Udemy Course - Section 9

while [ "${CORRECT}" != "y" ]
do
    read -p "Enter your name: " NAME
    read -p "Is ${NAME} correct? " CORRECT
done

echo "Done"