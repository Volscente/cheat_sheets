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

# Read STDIN
```bash
read -p "Insert your input here: " USER_INPUT
echo "You've inserted: ${USER_INPUT}"
```