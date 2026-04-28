#!/usr/bin/env python3

import json
import math


def classify_sector(x: float, y: float) -> str:
    angle = (math.degrees(math.atan2(y, x)) + 360.0) % 360.0
    if angle < 90:
        return "north-east"
    if angle < 180:
        return "north-west"
    if angle < 270:
        return "south-west"
    return "south-east"


def main() -> int:
    target = (0.0, 0.0)
    swarm_positions = [(5.0, 4.0), (-6.2, 3.4), (-4.5, -5.8), (5.4, -4.2)]
    occupied_sectors = {classify_sector(x - target[0], y - target[1]) for x, y in swarm_positions}

    assert len(occupied_sectors) == 4, "flanking pattern did not surround the target"

    print(
        json.dumps(
            {
                "test": "flanking_logic",
                "target": target,
                "occupied_sectors": sorted(occupied_sectors),
                "result": "pass",
            },
        ),
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
