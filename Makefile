
NAME="Amethyst Build Helper"
DESCRIPTION="Makefile for streamlining build and deployment of portfolio website (amethyst)."
CREATED="07-29-2019"
LAST_UPDATED="08-22-2019"
AUTHOR="Alex Bennett"

###################
## Configuration ##
###################

# Don't touch this, daa nana naa, dun dun, dun dun
SHELL=/bin/sh

# Project information
DOCKER_IMAGE_NAME="amethyst"
VERSION=`cat VERSION`

# Source directory
SRC_DIR := .

###################################
## Building and makefile targets ##
###################################

.PHONY: help

all: header build

header:
	@echo " "
	@echo " _______  __   __  _______  _______  __   __  __   __  _______  _______ "
	@echo "|   _   ||  |_|  ||       ||       ||  | |  ||  | |  ||       ||       |"
	@echo "|  |_|  ||       ||    ___||_     _||  |_|  ||  |_|  ||  _____||_     _|"
	@echo "|       ||       ||   |___   |   |  |       ||       || |_____   |   |  "
	@echo "|       ||       ||    ___|  |   |  |       ||_     _||_____  |  |   |  "
	@echo "|   _   || ||_|| ||   |___   |   |  |   _   |  |   |   _____| |  |   |  "
	@echo "|__| |__||_|   |_||_______|  |___|  |__| |__|  |___|  |_______|  |___|  "
	@echo " "
	@echo "                    ---- Amethyst Build Helper ----"
	@echo " "

help: header
	@echo "Available targets:"
	@echo "    make [all]                perform full build and push routine - does not clean"
	@echo "    make build                build Docker container"
	@echo "    make run                  run Docker container with default options"
	@echo "    make clean                remove old Docker images"
	@echo "    make help                 display this help screen"

build:
	@echo "------------------------------------------------------------------------"
	@echo " Building ${DOCKER_IMAGE_NAME} v${VERSION}..."
	@echo "------------------------------------------------------------------------"
	@echo ""

	@docker build -t ${DOCKER_IMAGE_NAME} .
	@docker tag ${DOCKER_IMAGE_NAME} ${DOCKER_IMAGE_NAME}:${VERSION}
	@docker tag ${DOCKER_IMAGE_NAME} ${DOCKER_IMAGE_NAME}:latest

	@echo ""
	@echo "------------------------------------------------------------------------"
	@echo " Build complete!"
	@echo "------------------------------------------------------------------------"
	@echo ""

run: build
	@echo "------------------------------------------------------------------------"
	@echo " Running ${DOCKER_IMAGE_NAME} v${VERSION}..."
	@echo "------------------------------------------------------------------------"
	@echo ""

	docker run --rm -d \
		--name=amethyst \
		--publish 127.0.0.1:80:8000 \
		${DOCKER_IMAGE_NAME}:${VERSION}

clean:
	@echo "------------------------------------------------------------------------"
	@echo " Removing old container images... "
	@echo "------------------------------------------------------------------------"
	@echo ""

	@docker rmi ${DOCKER_IMAGE_NAME}:${VERSION}
	@docker rmi ${DOCKER_IMAGE_NAME}:latest
