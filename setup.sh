#!/bin/bash

NAME="Amethyst Environment Setup"
DESCRIPTION="Handles installation of tools for portfolio website development (amethyst)."
CREATED="07-29-19"
LAST_UPDATED="08-22-19"
AUTHOR="Alex Bennett"

###################
## Configuration ##
###################

# Name of conda environment if not already set
CONDA_ENV_NAME=${CONDA_ENV_NAME-"amethyst"}

############################
## Define paths and names ##
############################

# Miniconda
CONDA_PATH="$HOME/miniconda3"

# Define tools directory
TOOLS_DIR_NAME="tools"
TOOLS_PATH=$PWD"/"$TOOLS_DIR_NAME

# Environment file name
ENV_FILE_NAME="environment"

# Requirements
REQUIREMENTS_FILE_NAME="requirements.txt"

###########
## Setup ##
###########

source $CONDA_PATH/etc/profile.d/conda.sh

######################
## Define functions ##
######################

function usage
{
    echo " _______  __   __  _______  _______  __   __  __   __  _______  _______ "
    echo "|   _   ||  |_|  ||       ||       ||  | |  ||  | |  ||       ||       |"
    echo "|  |_|  ||       ||    ___||_     _||  |_|  ||  |_|  ||  _____||_     _|"
    echo "|       ||       ||   |___   |   |  |       ||       || |_____   |   |  "
    echo "|       ||       ||    ___|  |   |  |       ||_     _||_____  |  |   |  "
    echo "|   _   || ||_|| ||   |___   |   |  |   _   |  |   |   _____| |  |   |  "
    echo "|__| |__||_|   |_||_______|  |___|  |__| |__|  |___|  |_______|  |___|  "
    echo ""
    echo "Name: $NAME"
    echo "Description: $DESCRIPTION"
    echo "Author: $AUTHOR"
    echo "Created: $CREATED"
    echo "Last updated: $LAST_UPDATED"
    echo " "
    echo "Required:"
    echo "  - GNU/Linux (developed on Linux 4.18.20-041820-generic x86_64)"
    echo "    - You are running: $(uname -srm)"
    echo "  - Miniconda3 (assumed to be in /opt/miniconda3)"
    echo " "
    echo "Usage: ./setup.sh [-r|--reset] [-i|--install] [-h|--help]"
    echo "  -r, --reset     fully reset development environment"
    echo "  -i, --install   install development tools"
    echo "  -h, --help      display help"
}

function reset
{
    echo "[WARN] Resetting build tools!"

    # Remove tools
    rm -rf $TOOLS_PATH
    echo "[INFO] Removed directory: $TOOLS_PATH"

    # Remove conda environment
    conda deactivate
    conda remove -y -q -n $CONDA_ENV_NAME --all
    echo "[INFO] Removed conda environment: $CONDA_ENV_NAME"

    echo "[INFO] Build tools reset"
}

function summary
{
    echo "--- Tools installed! --------------------------------------------------"
    echo ""
    echo "    To activate, run \"source $TOOLS_DIR_NAME/$ENV_FILE_NAME\""
    echo ""
    echo "-----------------------------------------------------------------------"
}

function install
{
    ####################
    ## Perform checks ##
    ####################

    # If directories exist, assume tools installed. Not the best but it works.
    if [ -d "$TOOLS_PATH" ] ; then
        echo "[WARN] Looks like the tools are already installed, nothing to do"
        summary
        echo "[INFO] Otherwise you can reset using '-r' on this script and try again"

        # (Re)create environment file
        create_env_file

        exit 0
    fi

    # Create conda environment
    echo "[INFO] Creating conda environment: $CONDA_ENV_NAME"
    conda create -y -q -n $CONDA_ENV_NAME python

    # Switch environment
    conda deactivate
    conda activate $CONDA_ENV_NAME
    echo "[INFO] Activated conda environment: $CONDA_ENV_NAME"

    if ! [ -d "$TOOLS_PATH" ]; then
        # Setup toolchain directory
        mkdir -p $TOOLS_PATH
        echo "[INFO] Created tools directory: $TOOLS_PATH"
    fi

    ##############################
    ###### BEGIN INSTALLERS ######
    ##############################

    install_depends

    ##############################
    ####### END INSTALLERS #######
    ##############################

    # Enter tools directory
    cd $TOOLS_PATH

    # Create environment file
    create_env_file
    echo "[INFO] Created environment file: $TOOLS_PATH/$ENV_FILE_NAME"

    # Deactivate
    conda deactivate
    echo "[INFO] Deactivated conda environment: $CONDA_ENV_NAME"

    # Back out of tools directory
    cd ../

    # Show summary
    echo ""
    summary

    # Clean exit
    exit 0
}

function create_env_file
{
    # Create sourceable .env file to add paths
    echo "# Activate conda environment" > $TOOLS_PATH/$ENV_FILE_NAME
    echo "conda activate $CONDA_ENV_NAME" >> $TOOLS_PATH/$ENV_FILE_NAME
    echo "" >> $TOOLS_PATH/$ENV_FILE_NAME
    echo "# Display confirmation" >> $TOOLS_PATH/$ENV_FILE_NAME
    echo "echo \"Development environment activated: $CONDA_ENV_NAME\n\"" >> $TOOLS_PATH/$ENV_FILE_NAME
}

function in_progress
{
    pid=$1
    spin='-\|/'

    # Account for indicator
    printf "  "

    i=0
    while kill -0 $pid 2>/dev/null
    do
        i=$(( (i+1) % 4 ))
        printf "\b${spin:$i:1}"
        sleep .1
    done

    sleep 1

    echo ""
}

function install_depends
{
    echo -n "[INFO] Installing dependencies:"

    # Install from requirements file
    pip install --user -r $REQUIREMENTS_FILE_NAME
}

# Print usage if no command provided
if [ "$1" == "" ]; then
    usage
fi

# Parse commands
while [ "$1" != "" ]; do
    case $1 in
        -r | --reset )          reset
                                ;;
        -i | --install )        install
                                ;;
        -h | --help )           usage
                                exit
                                ;;
    esac
    shift
done
