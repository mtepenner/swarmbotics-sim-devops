#!/usr/bin/env python3

from __future__ import annotations

import json


def build_hitl_bridge_config() -> dict:
    return {
        "component": "hitl_bridge",
        "sensor_topics": ["/fireant/lidar", "/fireant/imu", "/fireant/front_camera"],
        "bridge_target": "udp://192.168.88.40:5601",
        "clock_mode": "sim_time",
    }


def generate_launch_description():
    try:
        from launch import LaunchDescription
        from launch.actions import LogInfo

        config = build_hitl_bridge_config()
        return LaunchDescription(
            [
                LogInfo(msg=f"HITL bridge active -> {config['bridge_target']}"),
                LogInfo(msg=f"Topics: {', '.join(config['sensor_topics'])}"),
            ],
        )
    except ModuleNotFoundError:
        return build_hitl_bridge_config()


if __name__ == "__main__":
    print(json.dumps(build_hitl_bridge_config()))
