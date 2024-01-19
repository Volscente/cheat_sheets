#!/bin/bash
#
# This script includes solutions to the exercises of the Udemy Course - Section 7

# Retrieve argument
COMMAND=${1}

# Switch arguments
case "$COMMAND" in
    start|START)
        echo "Starting the server."
        ;;
    stop|STOP)
        echo "Stop the server."
        ;;
    *)
        echo "Invalid command. Use start or stop."exit 1
        ;;
esac
