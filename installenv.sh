#!/bin/sh

#admin
echo "This script installs a virtual environment that matches the requirements for the CIRA-TeleConfigurator project"
echo "Script verion: 2.1"
echo "Created by Nick Clarke"
echo "Last edited: 6/09/2021"

##Colours

YEL='\033[1;33m' #yellow
RED='\033[0;31m'
GRE='\033[1;32m'
NC='\033[0m' #no colour

##FUNCTIONS
#checks if name is null and returns default of 'env', else it leaves it alone
check_name () { 
    if [ -z "$name" ]
    then 
        name="env"
    fi
}

activate () {
    . $name/bin/activate
}

##COMMANDS
#name the virtualenv
echo "What is the name for your environment? recommended: env"
read name
check_name

#start the virtual env and install requirements - does not leave shell in virtualenv prompt
virtualenv $name && . $name/bin/activate && pip install -r requirements.txt

##FINSIH
#clean up - no error handling yet
echo "Virtual environment '$name' created successfully"

#instructions for starting virtualenv
echo "Start the virtual environment using \"${GRE}. $name/bin/activate${NC}\""
