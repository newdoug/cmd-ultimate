#!/usr/bin/env bash

GIT_CMD='git config --local'

SCRIPT_DIR="$(dirname "$(readlink -f "$0")")";
REPO_ROOT_DIR="${SCRIPT_DIR}/../../";
cd "${REPO_ROOT_DIR}" || exit 1;

set -x;

${GIT_CMD} core.hooksPath "scripts/hooks";
${GIT_CMD} core.whitespace blank-at-eol,space-before-tab,-blank-at-eof;

