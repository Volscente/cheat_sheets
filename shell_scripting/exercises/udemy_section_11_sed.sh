#!/bin/bash
#
# This script includes solutions to the exercises of the Udemy Course - Section 11

# The 's/.../' is called "Search Pattern" and it is a REGEX
# The '/.../' is the new content to replace the Search Pattern with
# NOTE: SED is not altering the content of the file, just display the replaced version
sed 's/assistant/assistant to the/' ./data/manager.txt


echo

# After the last slash, you can add as many flags as you want
# The 'i' stands for 'insensitive' and it ignores lower or uppercase
sed 's/ASSISTANT/assistant to the/i' ./data/manager.txt