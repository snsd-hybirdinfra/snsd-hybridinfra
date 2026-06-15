#!/usr/bin/env bash
set -euo pipefail

LAB_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RAW_DIR="${LAB_DIR}/evidence/generated/raw"
SUMMARY_DIR="${LAB_DIR}/evidence/generated/summary"
LOG_DIR="${LAB_DIR}/runtime-workspace/logs"

COMPOSE_FILE="${LAB_DIR}/compose/docker-compose.yml"
PROJECT_NAME="snsd-container-runtime-lab"
SERVICE_NAME="container-web"
ENDPOINT="http://localhost:18080"

VALIDATE_LOG="${RAW_DIR}/container-runtime-validate.log"
COMPOSE_PS="${RAW_DIR}/container-compose-ps.log"
CONTAINER_LOG="${RAW_DIR}/container-web.log"
WEB_RESPONSE="${RAW_DIR}/container-web-endpoint.html"
RUNTIME_STATUS="${RAW_DIR}/container-runtime-status.tsv"
SUMMARY="${SUMMARY_DIR}/container-runtime-summary.md"
LEGACY_SUMMARY="${SUMMARY_DIR}/container-runtime-execution-summary.md"

mkdir -p "${RAW_DIR}" "${SUMMARY_DIR}" "${LOG_DIR}"

echo "[INFO] container runtime validation started"

DOCKER_AVAILABLE="FAIL"
COMPOSE_AVAILABLE="FAIL"
COMPOSE_FILE_PRESENT="FAIL"
INDEX_FILE_PRESENT="FAIL"
CONTAINER_STARTED="FAIL"
CONTAINER_RUNNING="FAIL"
HTTP_ENDPOINT_RESPONDED="FAIL"
RUNTIME_REPORT_GENERATED="FAIL"

if docker --version >/dev/null 2>&1; then
  DOCKER_AVAILABLE="PASS"
fi

if docker compose version >/dev/null 2>&1; then
  COMPOSE_AVAILABLE="PASS"
fi

if [ -f "${COMPOSE_FILE}" ] && [ -s "${COMPOSE_FILE}" ]; then
  COMPOSE_FILE_PRESENT="PASS"
fi

if [ -f "${LAB_DIR}/configs/index.html" ] && [ -s "${LAB_DIR}/configs/index.html" ]; then
  INDEX_FILE_PRESENT="PASS"
fi

if [ "${DOCKER_AVAILABLE}" = "PASS" ] && \
   [ "${COMPOSE_AVAILABLE}" = "PASS" ] && \
   [ "${COMPOSE_FILE_PRESENT}" = "PASS" ]; then
  docker compose -p "${PROJECT_NAME}" -f "${COMPOSE_FILE}" up -d > "${LOG_DIR}/docker-compose-up.log" 2>&1
  CONTAINER_STARTED="PASS"
fi

docker compose -p "${PROJECT_NAME}" -f "${COMPOSE_FILE}" ps > "${COMPOSE_PS}" 2>&1 || true

CONTAINER_ID="$(docker compose -p "${PROJECT_NAME}" -f "${COMPOSE_FILE}" ps -q "${SERVICE_NAME}" 2>/dev/null || true)"

if [ -n "${CONTAINER_ID}" ]; then
  if [ "$(docker inspect -f '{{.State.Running}}' "${CONTAINER_ID}" 2>/dev/null || echo false)" = "true" ]; then
    CONTAINER_RUNNING="PASS"
  fi

  docker logs "${CONTAINER_ID}" > "${CONTAINER_LOG}" 2>&1 || true
fi

for attempt in $(seq 1 20); do
  if curl -fsS "${ENDPOINT}" > "${WEB_RESPONSE}" 2>/dev/null; then
    HTTP_ENDPOINT_RESPONDED="PASS"
    break
  fi
  sleep 1
done

cat > "${RUNTIME_STATUS}" <<STATUS
signalstatus
docker_available${DOCKER_AVAILABLE}
docker_compose_available${COMPOSE_AVAILABLE}
compose_file_present${COMPOSE_FILE_PRESENT}
index_file_present${INDEX_FILE_PRESENT}
container_started${CONTAINER_STARTED}
container_running${CONTAINER_RUNNING}
http_endpoint_responded${HTTP_ENDPOINT_RESPONDED}
STATUS

cat > "${VALIDATE_LOG}" <<LOG
# Container Runtime Validation Log

project_name=${PROJECT_NAME}
compose_file=${COMPOSE_FILE}
service_name=${SERVICE_NAME}
endpoint=${ENDPOINT}

docker_available=${DOCKER_AVAILABLE}
docker_compose_available=${COMPOSE_AVAILABLE}
compose_file_present=${COMPOSE_FILE_PRESENT}
index_file_present=${INDEX_FILE_PRESENT}
container_started=${CONTAINER_STARTED}
container_running=${CONTAINER_RUNNING}
http_endpoint_responded=${HTTP_ENDPOINT_RESPONDED}
LOG

if [ "${DOCKER_AVAILABLE}" = "PASS" ] && \
   [ "${COMPOSE_AVAILABLE}" = "PASS" ] && \
   [ "${COMPOSE_FILE_PRESENT}" = "PASS" ] && \
   [ "${INDEX_FILE_PRESENT}" = "PASS" ] && \
   [ "${CONTAINER_STARTED}" = "PASS" ] && \
   [ "${CONTAINER_RUNNING}" = "PASS" ] && \
   [ "${HTTP_ENDPOINT_RESPONDED}" = "PASS" ]; then
  OVERALL="PASS"
else
  OVERALL="CHECK"
fi

cat > "${SUMMARY}" <<SUMMARY
# Container Runtime Summary

Overall Status: ${OVERALL}

## Validation Matrix

| Signal | Status |
|---|---|
| Docker CLI available | ${DOCKER_AVAILABLE} |
| Docker Compose available | ${COMPOSE_AVAILABLE} |
| Compose file present | ${COMPOSE_FILE_PRESENT} |
| Web index file present | ${INDEX_FILE_PRESENT} |
| Container started | ${CONTAINER_STARTED} |
| Container running | ${CONTAINER_RUNNING} |
| HTTP endpoint responded | ${HTTP_ENDPOINT_RESPONDED} |

## Runtime Decision

| Decision Field | Value |
|---|---|
| Compose project | ${PROJECT_NAME} |
| Compose service | ${SERVICE_NAME} |
| HTTP endpoint | ${ENDPOINT} |
| Runtime validation result | ${OVERALL} |

## Runtime Boundary

This lab validates a local Docker Compose based container runtime baseline.

Generated runtime evidence remains local-only.

## Evidence Files

| Evidence | Path |
|---|---|
| Runtime status table | evidence/generated/raw/container-runtime-status.tsv |
| Compose process snapshot | evidence/generated/raw/container-compose-ps.log |
| Container log | evidence/generated/raw/container-web.log |
| HTTP response body | evidence/generated/raw/container-web-endpoint.html |
| Validation log | evidence/generated/raw/container-runtime-validate.log |
| Runtime summary | evidence/generated/summary/container-runtime-summary.md |
SUMMARY

cp "${SUMMARY}" "${LEGACY_SUMMARY}"

RUNTIME_REPORT_GENERATED="PASS"

cat "${SUMMARY}"

if [ "${OVERALL}" != "PASS" ]; then
  echo "[CHECK] container runtime validation did not reach PASS"
  cat "${VALIDATE_LOG}" || true
  echo "---- compose ps ----"
  cat "${COMPOSE_PS}" || true
  exit 1
fi

echo "[INFO] container runtime validation completed"