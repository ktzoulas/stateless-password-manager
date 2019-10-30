#!/bin/sh
# .....................................start db docker
docker run --rm --name pg-docker \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=postgres \
  -p 5432:5432 -d postgres
  # -v ~/docker/volumes/postgresql/data:/var/lib/postgresql/data

echo "[*] Wait for container to be initialized..." && sleep 3

# .....................................create database
PGPASSWORD="postgres" psql -h localhost -U postgres -c "CREATE DATABASE spamandb;"
PGPASSWORD="postgres" psql -h localhost -U postgres -c "CREATE DATABASE spamandb_test;"
