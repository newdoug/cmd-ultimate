#!/usr/bin/env bash

SCRIPT_DIR="$(dirname "$(readlink -f "$0")")";
UTILS_FILE="${SCRIPT_DIR}/../utils.sh";
# shellcheck disable=SC1090
source "${UTILS_FILE}" || exit "$?";

PY_TEST_SCRIPT="${SCRIPT_DIR}/run_py_unit_tests.sh";
SH_TEST_SCRIPT="${SCRIPT_DIR}/run_sh_unit_tests.sh";

file_executable_or_die "${PY_TEST_SCRIPT}";
file_executable_or_die "${SH_TEST_SCRIPT}";

${PY_TEST_SCRIPT};
${SH_TEST_SCRIPT};

