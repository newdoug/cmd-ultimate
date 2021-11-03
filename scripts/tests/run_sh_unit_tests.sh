#!/usr/bin/env bash

SCRIPT_DIR="$(dirname "$(readlink -f "$0")")";
UTILS_FILE="${SCRIPT_DIR}/../utils.sh";
# shellcheck disable=SC1090
source "${UTILS_FILE}" || exit "$?";

TESTS_DIR="${SCRIPT_DIR}/../../tests/sh";

dir_exists_or_die "${TESTS_DIR}";

# TODO: runs the shell script/functions unit tests

