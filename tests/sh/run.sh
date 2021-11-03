#!/usr/bin/env bash


# TODO: instead of something custom, consider a framework like bash_unit or bashtub
# this script may not be necessary depending on the run_sh_unit_tests.sh script

SCRIPT_DIR="$(dirname "$(readlink -f "$0")")";


find "${SCRIPT_DIR}" -type f -executable -name "test_*.sh" | while read script; do
  printf "Running SH test script '%s'\\n" "${script}";
  ${script};
  EXIT_CODE="$?";
  if [ "${EXIT_CODE}" -ne "0" ]; then
    printf "Test script '%s' failed with code '%d'\\n" "${script}" "${EXIT_CODE}";
    exit "${EXIT_CODE}";
  fi
  printf "Script passed '%s'\\n" "${script}";
done;

