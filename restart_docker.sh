#!/usr/bin/env bash
set -e

# Script to restart Docker Compose for the wcw_bot project.
# This script brings down and then brings up the services defined in docker-compose.yml.
cd "$(dirname "$0")"

# Use absolute path to docker binary to ensure the command runs under cron
DOCKER_BIN=/usr/bin/docker

"$DOCKER_BIN" compose -f docker-compose.yml down
"$DOCKER_BIN" compose -f docker-compose.yml up -d