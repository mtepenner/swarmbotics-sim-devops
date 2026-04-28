#!/usr/bin/env python3

import argparse
import json
import time


PROFILES = {
    "urban-canyon": {"latency_ms": 68, "packet_loss_pct": 9.5, "jammer_intensity": 0.35},
    "contested-plains": {"latency_ms": 120, "packet_loss_pct": 18.0, "jammer_intensity": 0.72},
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Emit a Mininet-style mesh degradation profile.")
    parser.add_argument("--scenario", default="contested-plains", choices=sorted(PROFILES.keys()))
    parser.add_argument("--mesh-nodes", type=int, default=24)
    parser.add_argument("--once", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    while True:
        profile = PROFILES[args.scenario]
        print(
            json.dumps(
                {
                    "component": "mininet_mesh_sim",
                    "scenario": args.scenario,
                    "mesh_nodes": args.mesh_nodes,
                    **profile,
                },
            ),
            flush=True,
        )
        if args.once:
            return 0
        time.sleep(2)


if __name__ == "__main__":
    raise SystemExit(main())
