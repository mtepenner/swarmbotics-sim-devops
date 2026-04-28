# Swarmbotics Simulation & DevOps

`swarmbotics-sim-devops` provides the pre-deployment proving ground for the swarm stack. The repository now contains a tracked simulation environment, headless behavior tests and GitHub Actions workflows, and an OTA subsystem spanning rollout orchestration, an edge agent, partition management, and payload verification.

## Components

- `simulation-environment/`: Fireant UGV model assets, tactical worlds, large-swarm spawn planning, HITL bridge configuration, and Mininet-style mesh degradation simulation.
- `ci-cd-pipelines/`: GitHub Actions workflows and behavior test suites for flanking logic and communications failover.
- `ota-update-system/`: Go rollout services, a Rust edge client, partition rollback handling, and key/signature verification scripts.

## Validation

Use the root validation targets:

```bash
make validate
make smoke
```

`make validate` checks Python syntax, Go package compilation via `go test`, shell syntax, and XML validity of the SDF assets. `make smoke` runs the spawn planner, network degradation simulator, and behavior tests once with sample inputs.

## Usage

Plan a swarm simulation launch:

```bash
python3 simulation-environment/launch-scripts/spawn-swarm.py --count 24 --world urban-canyon --once
```

Preview a degraded network profile:

```bash
python3 simulation-environment/network-sim/mininet-mesh-sim.py --scenario contested-plains --once
```

Run the behavior tests directly:

```bash
python3 ci-cd-pipelines/behavior-test-suites/test-flanking-logic.py
python3 ci-cd-pipelines/behavior-test-suites/test-comms-failover.py
```

Compile the OTA edge agent:

```bash
rustc --edition 2021 ota-update-system/edge-client/ota-agent.rs -o ota-agent
```

## CI/CD

The GitHub Actions workflows under `ci-cd-pipelines/.github/workflows/` cover simulation asset validation, headless behavior tests, and a placeholder C2 container build flow driven by Docker Buildx.

## License

This project is licensed under the MIT License. See `LICENSE` for details.

