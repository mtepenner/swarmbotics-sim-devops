#!/usr/bin/env bash
set -euo pipefail

CURRENT_SLOT="${CURRENT_SLOT:-A}"
TARGET_VERSION="${TARGET_VERSION:-1.0.0}"

if [[ "${CURRENT_SLOT^^}" == "A" ]]; then
  NEXT_SLOT="B"
else
  NEXT_SLOT="A"
fi

printf '%s\n' "current_slot=${CURRENT_SLOT^^}"
printf '%s\n' "next_slot=${NEXT_SLOT}"
printf '%s\n' "target_version=${TARGET_VERSION}"

if [[ "${AB_PROMOTE:-0}" == "1" ]]; then
  printf '%s\n' "promotion=scheduled"
else
  printf '%s\n' "promotion=dry-run"
fi
