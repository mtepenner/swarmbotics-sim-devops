PYTHON ?= python

.PHONY: validate python-check xml-check go-check shell-check smoke

validate: python-check xml-check go-check shell-check

python-check:
	$(PYTHON) -m compileall simulation-environment ci-cd-pipelines ota-update-system

xml-check:
	$(PYTHON) -c "from pathlib import Path; import xml.etree.ElementTree as ET; [ET.parse(str(path)) for path in Path('simulation-environment').rglob('*.sdf')]; print('Validated SDF XML files.')"

go-check:
	go test ./...

shell-check:
	bash -n ota-update-system/edge-client/a-b-partition-manager.sh
	bash -n ota-update-system/crypto-security/key-generation.sh

smoke:
	$(PYTHON) simulation-environment/launch-scripts/spawn-swarm.py --count 6 --world urban-canyon --once
	$(PYTHON) simulation-environment/network-sim/mininet-mesh-sim.py --once
	$(PYTHON) ci-cd-pipelines/behavior-test-suites/test-flanking-logic.py
	$(PYTHON) ci-cd-pipelines/behavior-test-suites/test-comms-failover.py
