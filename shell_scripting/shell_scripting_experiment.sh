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

# -------- Read STDIN --------
read -p "Insert your input here: " USER_INPUT
echo "You've inserted: ${USER_INPUT}"
echo
# --------------------------

# -------- Functions --------
function say_hello(){

    for NAME in $@
    do
        echo "Hello ${NAME}"
        echo
    done
}

say_hello Simone Sarah

# ---------------------------

# -------- Exit Status --------
ls /not/here
echo "Status code: $?"
echo

# Switch based on command execution exit status
read -p "Insert host to reach: " HOST
ping -c 1 ${HOST}
HOST_REACH_RETURN_CODE=$?
echo

if [ ${HOST_REACH_RETURN_CODE} -eq "0" ]
then
    echo "${HOST} reachable."
    exit 0
else
    echo "${HOST} unreachable."
    exit 255
fi
# ----------------
