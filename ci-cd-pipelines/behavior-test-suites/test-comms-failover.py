#!/usr/bin/env python3

import json


def choose_link(mesh_packet_loss_pct: float, satcom_available: bool) -> str:
    if mesh_packet_loss_pct >= 15.0 and satcom_available:
        return "satcom"
    return "mesh"


def main() -> int:
    selected = choose_link(mesh_packet_loss_pct=18.4, satcom_available=True)
    assert selected == "satcom", "mesh failover did not escalate to SATCOM"

    print(
        json.dumps(
            {
                "test": "comms_failover",
                "selected_link": selected,
                "mesh_packet_loss_pct": 18.4,
                "result": "pass",
            },
        ),
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
