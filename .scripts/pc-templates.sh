#!/bin/sh

# Configuration

EXAMPLES_BASE_URL=https://raw.githubusercontent.com/nd-cse-30872-su26/examples/refs/heads/master/

# Functions

download_template() {
    if curl -sfLO $1 > /dev/null 2>&1; then
    	echo "Success"
    else
    	echo "Failure"
    fi
}

# Main Execution

for exercise in $@; do
    lecture=$(echo $exercise | sed -En 's/exercise([0-9]{2})-.*/lecture\1/p')

    echo -n "Downloading C++ template ... "
    download_template $EXAMPLES_BASE_URL/$lecture/$exercise/template.cpp

    echo -n "Downloading Python template ... "
    download_template $EXAMPLES_BASE_URL/$lecture/$exercise/template.py
done
