#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
OUT_DIR="${SCRIPT_DIR}/out"
PRIVATE_KEY_PATH="${OUT_DIR}/update-signing-private.pem"
PUBLIC_KEY_PATH="${OUT_DIR}/update-signing-public.pem"

mkdir -p "${OUT_DIR}"

if command -v openssl >/dev/null 2>&1; then
  openssl genpkey -algorithm ed25519 -out "${PRIVATE_KEY_PATH}"
  openssl pkey -in "${PRIVATE_KEY_PATH}" -pubout -out "${PUBLIC_KEY_PATH}"
else
  printf '%s\n' 'placeholder-private-key' > "${PRIVATE_KEY_PATH}"
  printf '%s\n' 'placeholder-public-key' > "${PUBLIC_KEY_PATH}"
fi

printf '%s\n' "generated_private_key=${PRIVATE_KEY_PATH}"
printf '%s\n' "generated_public_key=${PUBLIC_KEY_PATH}"
