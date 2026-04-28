#!/usr/bin/env python3

import argparse
import json
import math
import time
from dataclasses import asdict, dataclass


@dataclass
class SpawnSpec:
    namespace: str
    x: float
    y: float
    yaw_deg: float


def build_spawn_plan(count: int, spacing: float) -> list[SpawnSpec]:
    columns = max(1, math.ceil(math.sqrt(count)))
    plan: list[SpawnSpec] = []
    for index in range(count):
        row = index // columns
        column = index % columns
        plan.append(
            SpawnSpec(
                namespace=f"fireant-{index + 1:03d}",
                x=round(column * spacing, 2),
                y=round(row * spacing, 2),
                yaw_deg=round((index * 17) % 360, 1),
            ),
        )
    return plan


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate a swarm spawn plan for simulation namespaces.")
    parser.add_argument("--count", type=int, default=24)
    parser.add_argument("--world", default="urban-canyon")
    parser.add_argument("--spacing", type=float, default=2.8)
    parser.add_argument("--once", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    while True:
        plan = build_spawn_plan(args.count, args.spacing)
        print(
            json.dumps(
                {
                    "component": "spawn_swarm",
                    "world": args.world,
                    "count": args.count,
                    "entities": [asdict(item) for item in plan],
                },
            ),
            flush=True,
        )
        if args.once:
            return 0
        time.sleep(2)


if __name__ == "__main__":
    raise SystemExit(main())
