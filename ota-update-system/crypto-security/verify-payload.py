#!/usr/bin/env python3

import argparse
import hashlib
import json
from pathlib import Path


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Verify a payload against a detached SHA-256 signature file.")
    parser.add_argument("--payload", type=Path, required=True)
    parser.add_argument("--signature", type=Path, required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    expected_hash = args.signature.read_text(encoding="utf-8").strip()
    actual_hash = sha256_file(args.payload)
    verified = actual_hash == expected_hash

    print(
        json.dumps(
            {
                "component": "verify_payload",
                "payload": str(args.payload),
                "verified": verified,
                "actual_hash": actual_hash,
            },
        ),
    )
    return 0 if verified else 1


if __name__ == "__main__":
    raise SystemExit(main())