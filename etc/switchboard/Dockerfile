# Builds draw.io's bundles (Ant + the Closure compiler in etc/build) without Java on the host.
FROM eclipse-temurin:21-jdk
RUN apt-get update && apt-get install -y --no-install-recommends ant && rm -rf /var/lib/apt/lists/*
WORKDIR /drawio/etc/build
ENTRYPOINT ["ant"]
