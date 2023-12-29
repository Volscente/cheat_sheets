#!/bin/bash
#
# This is just an experiment shell script

# -------- Tests --------
MY_SHELL="bash"

if [ ${MY_SHELL} = "bash" ]
then
    echo "You seem to like the bash shell."
fi
echo
# -----------------------


# -------- For Loop --------
NUMBERS="1 2 3"

for NUMBER in ${NUMBERS}
do
    echo "Number: ${NUMBER}"
done
echo
# --------------------------

# -------- Positional Parameters --------
echo "This is the first positional parameter: ${0}"
echo
echo "This is the second positional parameter: ${1}"
echo

USERS=${@}

for USER in ${USERS}
do
    echo "Username: ${USER}"
done
echo
# --------------------------
