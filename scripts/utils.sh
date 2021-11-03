#!/usr/bin/env bash
# meant to be sourced, not executed
# shebang is provided for clarity on expected shell


if [ "${DEBUG}" = "1" ]; then
  enable_debug;
fi

function enable_debug() {
  set -x;
}

function disable_debug() {
  set +x;
}

# Usage:
#   file_exists_or_die <path> <optional exit code (default: 1)>
function file_exists_or_die() {
  PATHNAME="$1";
  # default exit code
  EXIT_CODE=1;
  if [ "$#" -ge 2 ]; then
    EXIT_CODE="$2";
  fi
  if [ ! -f "${PATHNAME}" ]; then
    exit "${EXIT_CODE}";
  fi
}

# Usage:
#   file_executable_or_die <path> <optional exit code (default: 1)>
function file_executable_or_die() {
  PATHNAME="$1";
  # default exit code
  EXIT_CODE=1;
  if [ "$#" -ge 2 ]; then
    EXIT_CODE="$2";
  fi
  file_exists_or_die "${PATHNAME}" "${EXIT_CODE}";
  if [ ! -x "${PATHNAME}" ]; then
    exit "${EXIT_CODE}";
  fi
}

# Usage:
#   filedir_exists_or_die <path> <optional exit code (default: 1)>
function dir_exists_or_die() {
  PATHNAME="$1";
  # default exit code
  EXIT_CODE=1;
  if [ "$#" -ge 2 ]; then
    EXIT_CODE="$2";
  fi
  if [ ! -d "${PATHNAME}" ]; then
    exit "${EXIT_CODE}";
  fi
}

