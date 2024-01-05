# Introduction
## Definition
A *Shell Script* is just a list of commands that are executed by an interpreter, which is the Shell itself.

## Shebang
The interpreter is usually set at the top of the script by the so called *"Sharp Bang"* (#!) notation or *"Shebang"* (Contraction of Sharp Bang).
```bash
#!/bin/bash
```

The *Shebang* is used in order to pass the subsequent Shell path to the interpreter, so it knows what to use. So the process would actually be: `/bin/bash <script_path>.ph`.

The example above uses the `bash` shell as interpreter, but it is also possible to use others like `zsh` or `ksh`.

It is also possible to use another interpreter with respect to a Shell's one, like a Python interpreter.
```python
#!/usr/bin/python
print("This is a Python script.")
```
```bash
chmod 755 python_script.py
./python_script.py  # Output: This is a Python script.
```

## Executable
A Shell Script, in order to be executed, it needs to be granted with the *Execution* priviliges:
```bash
chmod 755 <script_path>.sh
```
Then we can execute the script:
```bash
./<script_path>.sh
```

# Syntax
## Variables
```bash
VARIABLE_NAME="Value"
```
It is possible to define a variable inside your script an use curly braces to call it.
```bash
MY_SHELL="bash"
echo "I am ${MY_SHELL}ing on my keyboard."
```
It is also possible to store output of a command in a variable.
```bash
SERVER_NAME=$(hostname)
echo "You are running this script on ${SERVER_NAME}"
```

## Tests
They are used to test conditions:
```bash
MY_SHELL="bash"

if [ ${MY_SHELL} = "bash" ]
then
    echo "You seem to like the bash shell."
fi

```

## For Loop
```bash
NUMBERS="1 2 3"

for NUMBER in ${NUMBERS}
do
    echo "Number: ${NUMBER}"
done
```

## Positional Parameters
```bash
echo "This is the first positional parameter: ${0}" # Script's path
echo
echo "This is the second positional parameter: ${1}" # Empty if not passed
echo
```
The best practice is to store the positional parameters into meaningful variables.
```bash
# Store positional parameter $1
USERNAME=${1}

echo "Received user: ${USERNAME}"
```
It is possible to retrieve also all the positional parameters
```bash
USERS=${@}

for USER IN ${USERS}
do
    echo "Username: ${USER}"
done
```

## Read STDIN
```bash
read -p "Insert your input here: " USER_INPUT
echo "You've inserted: ${USER_INPUT}"
```

## Chain Commands
The exit status is not checked and commands chained would be always executed.
```bash
cp test.txt /tmp/bak ; cp test.txt /tmp

# Same as
cp test.txt /tmp/bak
cp test.txt /tmp
```

## Functions
### Definition
They implement the so called *DRY*: Don't Repeat Yourself! It's the concept associated with the writing of reusable code.
Function advantages:
- Write once, use many times
- Reduces script length
- Single place to edit and troubleshoot
- Easy to maintain

### Syntax
```bash
function function_name(){
    # Code
}

function_name(){
    # Code
}

# Call
function_name
```

# Exit Status
## Introduction
They indicate if the command has been executed with or without errors. The value `0` is associated with *"No Errors"*, while everything different is associated with an error.

It is possible to retrieve the exit status code for a command in a shell script.
```bash
<some command>
EXIT_STATUS=$?

# Example
ping -c 1 "google.com"
EXIT_STATUS=$?
echo ${EXIT_STATUS} # 0
```

Remember to check the documentation of the used command in order to understand the meaning behind each exit status code.

## IF-ELSE Statements
It is possible to use the exit status code for decide which code to execute.
```bash
HOST="google.com"
ping -c 1 ${HOST}
HOST_REACH_RETURN_CODE=$?
echo

if [ ${HOST_REACH_RETURN_CODE} -eq "0" ]
then
    echo "${HOST} reachable."
else
    echo "${HOST} runeachable."
fi
```

## && and ||
They are used to chain commands depending on the exit status code.

The **AND** (&&) operator is used for executing a command after the previous one exists with no errors.
```bash
mdkir /tmp/bak && cp test.txt /tmp/bask
```
The command `cp test.txt /tmp/bask` would be executed only if `mdkir /tmp/bak` exit without errors.

<br>

The **OR** (||) operator is used for executing a command after the previous one fails.
```bash
cp test.txt /tmp/bask || cp test.txt /tmp
```
The command `cp test.txt /tmp` would be executed only if `cp test.txt /tmp/bask` will fail.

<br>

The commands from the previous section can be written as following.
```bash
ping -c 1 "google.com" && echo "Host is reachable"
ping -c 1 "google.com" || echo "Host is unreachable"
```

## Exit Command
```bash
HOST="google.com"
ping -c 1 ${HOST}
HOST_REACH_RETURN_CODE=$?
echo

if [ ${HOST_REACH_RETURN_CODE} -eq "0" ]
then
    echo "${HOST} reachable."
    exit 0
else
    echo "${HOST} runeachable."
    exit 255 # Custom exit status
fi
```
The default value is that of the last command executed.