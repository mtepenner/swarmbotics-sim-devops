FROM debian:bookworm-slim

RUN apt-get update \
    && apt-get install -y --no-install-recommends ca-certificates curl \
    && rm -rf /var/lib/apt/lists/*

LABEL org.opencontainers.image.title="swarmbotics-c2-placeholder"
LABEL org.opencontainers.image.description="Placeholder control-plane image built by the simulation/devops pipeline scaffold."

CMD ["bash", "-lc", "echo swarmbotics c2 placeholder container ready"]
