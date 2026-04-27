# Simulation & DevOps Infrastructure

## Description
`swarmbotics_sim_devops` is a comprehensive orchestration, simulation, and continuous deployment pipeline designed for massive-scale robotic swarms. It enables developers to test the "Hive Mind" in contested, GPS-denied tactical environments before securely deploying over-the-air (OTA) updates to a global fleet of Unmanned Ground Vehicles (UGVs).

## Table of Contents
- [Features](#-features)
- [Technologies Used](#%EF%B8%8F-technologies-used)
- [Installation](#%EF%B8%8F-installation)
- [Usage](#-usage)
- [Contributing](#-contributing)
- [License](#-license)

## 🚀 Features
* **Tactical Simulation Environment**: SITL (Software-In-The-Loop) and HITL (Hardware-In-The-Loop) simulation using Ignition/Gazebo. Includes 3D visuals, collision geometry, and physics for the `fireant_ugv`.
* **Contested Environments**: Test swarms in custom worlds like GPS-denied urban canyons (multipath errors) and open plains featuring adversary EW jammers.
* **Network Degradation Sim**: Built-in Mininet mesh simulations that artificially inject latency, packet loss, and jamming to mimic chaotic tactical communications.
* **Automated Behavior Testing**: Comprehensive CI/CD suites that run headless Gazebo tests to validate swarm flanking logic and communication failovers (e.g., switching to SATCOM when the mesh drops).
* **Zero-Trust OTA Updates**: A highly secure fleet management backend paired with an ultra-reliable Rust edge client (`ota_agent.rs`) running on Ubuntu Core. Ensures updates are cryptographically verified and utilizes dual-bank A/B partitions for bulletproof rollbacks.

## 🛠️ Technologies Used
* **Simulation & Robotics**: ROS, Ignition/Gazebo, C++
* **Networking**: Mininet, Python
* **CI/CD**: GitHub Actions / GitLab CI, Docker
* **OTA & Edge**: Go, Rust, Bash, Ubuntu Core

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone [https://github.com/your-org/swarmbotics_sim_devops.git](https://github.com/your-org/swarmbotics_sim_devops.git)
   cd swarmbotics_sim_devops
   ```
2. Install simulation dependencies (Ignition/Gazebo and ROS).
3. Set up the Mininet mesh simulator for network testing.
4. Ensure Docker is installed for building the C2 backend containers.

## 💻 Usage

### Launching the Swarm Simulation
To instantiate 100+ UGVs with unique namespaces in a simulated environment:
```bash
python3 simulation_environment/launch_scripts/spawn_swarm.py
```

### Running Automated Behavior Tests
Run the automated test suite locally to validate the swarm's "Hive Mind" logic:
```bash
python3 ci_cd_pipelines/behavior_test_suites/test_flanking_logic.py
python3 ci_cd_pipelines/behavior_test_suites/test_comms_failover.py
```

### Edge Device Hardware-In-The-Loop
To route simulated sensor data into a physical edge compute board:
```bash
ros2 launch simulation_environment/launch_scripts/hitl_bridge.launch.py
```

## 🤝 Contributing
Contributions to improve the simulation accuracy, add new tactical scenarios, or harden the OTA pipeline are welcome. Please ensure that any new behavior logic is accompanied by a headless simulation test in the `ci_cd_pipelines` folder.

## 📄 License
This project is licensed under the [MIT License](LICENSE) - see the LICENSE file for details.
