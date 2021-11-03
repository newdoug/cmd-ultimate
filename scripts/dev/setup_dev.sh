#!/usr/bin/env bash


# TODO: run pip install on dependencies, etc.
#   apt or yum install for system dependencies
#   enters user into virtual environment will all necessary dependencies to develop features, run tests, etc.

SCRIPT_DIR="$(dirname "$(readlink -f "$0")")";
UTILS_FILE="${SCRIPT_DIR}/../utils.sh";
# shellcheck disable=SC1090
source "${UTILS_FILE}" || exit "$?";

