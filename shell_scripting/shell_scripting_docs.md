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

## Case Statements
```bash
# Example 1
case "$1" in
    start|START)
        /usr/sbin/sshd
        ;;
    stop|STOP)
        kill $(cat /var/run/sshd.pid)
        ;;
    *) # Matches anything else
        echo "Usage: $0 start|stop"; exit 1
        ;;
esac

# Example 2
read -p "Enter y or n: " ANSWER
case "$ANSWER" in
    [yY] | [yY] [eE] [sS])
        echo "You answered yes."
        ;;
    [nN] | [nN] [oO])
        echo "You answered no."
        ;;
    *)
        echo "Invalid answer."
        ;;
esac
```

## While Loop
```bash
# Basic syntax
while [ CONDITION_IS_TRUE ]
do
    command 1
    command N
done

# Example
NUMBER=0
while [ ${NUMBER} -lt 6 ]
do
    echo "${NUMBER}"
    ((NUMBER++))
done
```

Use the statement `break` to interrupt the loop, but not the script. On the other hand, use the statement `continue` to go to the next loop iteration.

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

### Variables
Variables defined within a function are globally available.
```bash
function my_function(){
    GLOBAL_VAR=1
}

# Not available yet, because the function is not been called
echo ${GLOBAL_VAR} # Output: 

my_function

echo ${GLOBAL_VAR} # Output: 1
```

In order to declare a local variable use the keyword `local`.

```bash
function my_function(){
    local LOCAL_VAR=1
}
```

### Return Codes
```bash
function my_function(){
    return 0
}
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

# Wildcards
## Definition
They are character or string used for pattern matching.

The *Globbing* is the process of expands the wildcard pattern into a list of files amd/or directories.

## List
### * Wildcard
It matches zero or more characters
```bash
*.txt # All .txt files
a* # All files starting with "a"
a*.txt # All .txt files starting with "a"

ls *.lock # Match all files ending with ".lock"
```

### ? Wildcard
It matches exactly one characeter
```bash
?.txt # All .txt files with a single character name
a? # All file starting with "a" followed by a single character
a?.txt # All .txt files starting with "a" followed by a single character
```

### [] Wildcard
It matches any of the characters included between brackets.
```bash
ca[nt]* # can, cat, candy, catch
```
It can be used to define a range of characters/numberes.
```bash
[a-g]* # abaco, baseball, cricket
[3-6]* # 3_test, 5, 6_test2
```
It is possible to use predefined *Named Character Classes*.
```bash
[[:alpha:]] # Match alphabetic letters
[[:alnum:]] # Match alphanumeric digits
[[:digit:]] # Match numbers
[[:lower:]] # Match lowercase letters
[[:space:]] # Match spaces
[[:upper:]] # Match uppercase letters
```

### [!] Wildcard
It matches any of the characters NOT included between the brackets.
```bash
# Exclude all files starting with a vowel
[!aeiou]* # baseball, cricket
```

### \ Wildcard
It is used to escape wildcard character and match them.
```bash
*\? # done?
```

# Logging
## Definition
They store the following information about something that has occurred:
- Who
- What
- When
- Where
- Why

## Syslog
The `Syslog` is a Logging system that uses facilities (what part of the system the log comes from) and severities to categorize messages

**Facilities:** kern, user, mail, daemon, auth, local0, local7

**Severities:** emerg, alert, crit, err, warning, notice, info, debug

Logs are usually stored under: `/var/log/messages` and `/var/log/syslog`.

## Usage
```bash
# Pass a text to the logger
logger "Message"

# Specify <facility>.<severity> through the -p option
logger -p local0.info "Message"

# Tag the message with the name of your script (e.g., myscript) with the -t option
logger -t myscript -p local0.info "Message"

# Include the PID with the -i option
logger -i -t myscript -p local0.info "Message"
```

# Debugging
## Built In Debugging Help
Through the option `-x`, the x-trace or tracing would be called, offering debugging functionalities to the code.

Such debugging can be activated for the whole script, by add `-x` to the Shebang.
```bash
#!/bin/bash -x
TEST_VAR="test"
echo "${TEST_VAR}"

# OUPUT
+ TEST_VAR=test
+ echo test
test
```

Another option is to activate and deactivate the debugging just for the lines we need to debug.
```bash
#!/bin/bash
TEST_VAR="test"

# Activate debugging
set -x

echo "${TEST_VAR}"

# Deactivate the debug
set +x
```

The `-x` option can be combined with the `-e` option in order to output the error and exit the code.
```bash
#!/bin/bash -ex
FILE_NAME="/not/here"
ls ${FILE_NAME}
echo ${FILE_NAME}

# OUTPUT
+ FILE_NAME=/not/here
+ ls /not/here
ls: cannot access /not/here: No such file or directory
```

The `-v` option diplays on the console whatever is inside the script.

## Tips
### DEBUG Variable
It is possible to use a variable to control what commands to execute depending if you want the debug mode on or off.
```bash
DEBUG=true
$DEBUG && echo "Debug mode ON." # The command after "&&" is executed only if DEBUG=true
$DEBUG || echo "Debug mode OFF." # The command after "||" is executed only if DEBUG=false
```

### Echo Variable
Another possibility is to set a variable equals to "echo" and then prepend it to every command. In this way, if the variable is created, every command will be printed instead of being executed.
```bash
DEBUG="echo"
$DEBUG ls # output: "ls"

#DEBUG="echo"
$DEBUG ls # output: execution of "ls" command
```

### PS4
The PS4 variable holds the content of the debugging line and we can change it.
```bash
#!bin/bash -x
PS4='+ $BASH_SOURCE : $LINENO : '
TEST_VAR="test"
echo "${TEST_VAR}"

# OUTPUT
#+ PS4='+ $BASH_SOURCE : $LINENO : '
#+ ./udemy_section_10_debugging.sh : 14 : TEST_VAR=test
#+ ./udemy_section_10_debugging.sh : 15 : echo test
#test
```

### Return Character
Most of the OS add some special characters when creating a new file. Your script might give some strange errors due to these characters. Remember to check for such invisible special characters through the command: `cat -v my_script.sh` or `file my_script.sh`.

# SED
## Definition
It stands for *Stream Editor* and it is used to manipulate especially text stream of data, which are text data that travels from:
- One process to another
- One file to another
- One device to another

## Usage
```bash
# The 's/.../' is called "Search Pattern" and it is a REGEX
# The '/.../' is the new content to replace the Search Pattern with
# NOTE: SED is not altering the content of the file, just display the replaced version
sed 's/assistant/assistant to the/' ./data/manager.txt

# Same as using the pipe
cat ./data/manager.txt | sed 's/assistant/assistant to the/'
```

**NOTE:** Remember that the SED commands works line by line in the text file &rarr; Use the `g` flag for Global Replace.

```bash
# ./data/love.txt: 'I love my wife and my wife loves me. Also, my wife loves the cat'

# SED just substitute the first occurence in each line by default
sed 's/my wife/sed/i' ./data/love.txt

# Output: 'I love sed and my wife loves me. Also, my wife loves the cat'

# Use the 'g' flag for Global Replacement
sed 's/my wife/sed/ig' ./data/love.txt

# Output: I love sed and sed loves me. Also, sed loves the cat

# You can even specify wich occurent to replace
sed 's/my wife/sed/2' ./data/love.txt

# Output: I love my wife and sed loves me. Also, my wife loves the cat
```

## Create New Files
It is also possible to specify the file name to backup before changing it.
```bash
# my_file.txt would change and a my_file.txt.bak would be created
sed -i.bak 's/<pattern>/<replace>/<flags>' my_file.txt
```

It is also possible to directly redirect the output to a new file through the flag `w`.
```bash
sed 's/<pattern>/<replace>/<flags>w <new_file.txt' <input_file.txt>  
```

## Escape Slash Characters
We might need to replace text with `/`. One way to do it by escaping the `/` character.
```bash
# Replace '/home/jason' with '/export/users/jasonc'
echo '/home/jason' | sed 's/\/home\/jason/\/export\/users\/jasonc/'
```

Another way is to use another delimiter character instead of `/`, for example the `#`.
```bash
# Replace '/home/jason' with '/export/users/jasonc'
echo '/home/jason' | sed 's#/home/jason#/export/users/jasonc#'
```

**NOTE:** You can use any other delimiter, also `:`, as long as it is used in the correct position of the command.

## Templates
They allow to perform some predefined actions on a text file using the SED command.
```bash
# It removes all the lines that match the pattern
sed '/<pattern>/d' <file_path.txt>

# Input:
# """I love sed.
# This is line 2.
# I love sed with all of my heart"""
#
# Command:
#
# sed '/This/d' <file_path.txt>
# 
# Output:
# 
# """I love sed.
# I love sed with all of my heart"""
```

This feature can also be used to manipulate configuration files.

**Configuration File**
```yaml
# User to run services as
User apache

# Group to run service as
Group apache
```

**SED Command**
```bash
# 1. Strip everything that starts with '#' (comments)
sed '/^#/d' config

# 2. Strip blank lines
sed '/^$/d' config

# 3. Combine 1 and 2 by using the ';'
sed '/^#/d ; /^$/d' config

# 4. Change text 'apache' with 'http'
sed '/^#/d ; /^$/d ; s/apache/httpd/g' config
# OR
sed -e '/^#/d' -e '/^$/d' -e 's/apache/httpd/g' config
```

## Read SED Commands from File
```bash
sed -f <script.sed< <input_file>
```

## Specific Lines
```bash
# Replace the word 'run' with 'execute' only for lines 1 and 4
sed '1,4 s/run/execute/' <input_file>

# Replace the word 'run' with 'execute' only between the first line that
# starts with '#User' and the next blank line
sed '/^#User/,/^$/ s/run/execute/' <input_file>
```


# Useful Scripts
## Check Parameters
```bash
local DIR_PATH=${1}

# Check if the argument is passed
if [ -z ${DIR_PATH} ]
then
    echo "No directory path is passed."
    return 1
fi
```

## Check for Directory
```bash
# Check if it is a directory
if [ -d ${DIR_PATH} ]
then
    echo "${DIR_PATH}:"
    ls ${DIR_PATH} | wc -l
else
    echo "The passed path is not a directory,"
    exit 2
fi
```

## Loop Through LS
```bash
for FILE in $(ls *.jpg)
do
    mv ${FILE} ${CURRENT_DATE}${FILE}     
done
```

## Curent Date
```bash
local CURRENT_DATE=$(date '+%Y%m%d')
```

## Test Files with LS
```bash
if [ $(ls -A *.jpg) ]
```

## Test if Variable Exists
```bash
if [ -z ${PREFIX} ]
```

## Log Function
```bash
function logit() {

    local LOG_LEVEL=${1}

    shift

    MSG=$@

    TIMESTAMP=$(date +"%Y-%m-%d %T")

    if [ ${LOG_LEVEL} = 'ERROR' ] || $VERBOSE
    then
        echo "${TIMESTAMP} ${HOST} ${PROGRAM_NAME} [${PID}]: ${LOG_LEVEL} ${MS}
    fi
}
```

## Read File Line by Line
```bash
LINE_NUM=1
while read LINE
do
    echo "${LINE_NUM}: ${LINE}"
    ((LINE_NUM++))
done < /etc/fstab # or another file path
```

## Read Output Command Line by Line
```bash
# Pipe the grep output to the loop command
grep xfs /etc/fstab | while read LINE
do
    echo "xfs: ${LINE}"
done
```