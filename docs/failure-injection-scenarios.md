# Failure Injection Scenarios

This document describes the controlled failure injection scenarios used by the SNSD Hybrid Infrastructure runtime lab.

Failure injection is intentionally excluded from the default bootstrap flow. These scenarios are executed manually or through the resilience failure suite after the lab is already deployed and healthy.

## Scope

The current failure injection scope covers:

- Web backend failure
- Observability loss
- Database service failure
- Proxy entrypoint failure
- Backup failure and recovery validation

## Why These Failure Scenarios Matter

The failure injection suite is designed to validate operational capability rather than simply demonstrate that a service can be stopped and restarted.

Each failure domain maps to a different infrastructure operations concern.

| Failure Domain | Operational Meaning | Capability Demonstrated |
|---|---|---|
| Web backend failure | Partial application service degradation | Backend failure detection, service continuity through proxy routing, and recovery validation |
| Observability loss | Monitoring blind spot | Telemetry source loss detection and restoration of metric visibility |
| Database failure | Stateful service interruption | Database health detection, exporter signal validation, and service recovery |
| Proxy entrypoint failure | User-facing service entrypoint outage | External HTTPS availability detection, blackbox probing, TLS entrypoint recovery, and stats validation |
| Backup failure | Recovery assurance failure | Backup validation, restore-readiness signal, and recovery evidence generation |

This gives the portfolio coverage across four operational dimensions:

1. Service availability
2. Observability integrity
3. Stateful dependency health
4. Recovery validation

The purpose is not chaos testing at production scale.

The purpose is controlled lab validation of the full operational loop:

    Failure
      -> Detection
      -> Alert signal
      -> Recovery action
      -> Metric recovery
      -> Evidence generation


## Service Entrypoint Hardening

The HAProxy service entrypoint now validates a hardened access path:

- HTTP port 80 redirects to HTTPS
- HTTPS port 443 terminates TLS at HAProxy
- HAProxy forwards traffic to application backends on port 18080
- cAdvisor remains on port 8080
- HAProxy stats are exposed on port 8404
- Blackbox HTTP probing validates `https://192.168.1.20`
- HAProxy Exporter exposes backend and server metrics on `192.168.1.20:9101`

This separates external service availability from internal backend and container telemetry paths.

### Proxy Failure Signal Separation

Proxy-related validation now separates external and internal signals.

| Signal | Meaning |
|---|---|
| `probe_success` from Blackbox | User-facing HTTPS availability |
| HAProxy exporter metrics | Internal HAProxy backend and server visibility |
| HAProxy stats page | Operator-readable backend/server status |

This makes proxy failure validation stronger than a simple process restart check.


## Incident Coordination Validation

Alertmanager is connected to a local webhook receiver mock.

This validates the incident coordination path after alert detection.

    Prometheus Rule
      -> Alertmanager
      -> Webhook Receiver
      -> JSONL Alert Log
      -> Runtime Evidence

The webhook receiver runs on the monitoring node:

    http://192.168.1.40:5001/health
    http://192.168.1.40:5001/alerts

The received alert payloads are stored locally at:

    /var/log/snsd-alert-webhook/alerts.jsonl

This gives the lab a visible alert delivery path instead of stopping at Prometheus alert state only.

## Scenario Matrix

| ID | Playbook | Failure Type | Detection Basis | Expected Alert | Recovery Basis |
|---:|---|---|---|---|---|
| 14 | ansible/playbooks/21-failure-injection-web-recovery.yml | Web backend container stop | HAProxy backend health and blackbox HTTP probe | SNSDBlackboxProbeFailed | Container restart and HAProxy frontend HTTP 200 |
| 15 | ansible/playbooks/22-failure-injection-observability-loss.yml | node_exporter stop | up{job="node_exporter"} = 0 | SNSDNodeExporterDown | node_exporter active and target UP |
| 16 | ansible/playbooks/23-failure-injection-database-recovery.yml | MariaDB stop | mysql_up = 0 | SNSDMariaDBDown | MariaDB active and mysql_up = 1 |
| 17 | ansible/playbooks/24-failure-injection-proxy-recovery.yml | HAProxy stop | blackbox_http probe_success = 0 for `https://192.168.1.20` | SNSDBlackboxProbeFailed | HAProxy active, HTTP 301 redirect, HTTPS 200, and stats page 200 |
| 18 | ansible/playbooks/25-failure-injection-backup-recovery.yml | Restic backup failure | snsd_backup_last_success = 0 | SNSDBackupFailed | backup success = 1 and restore validation success = 1 |

## Individual Execution

Run from WSL at the repository root.

    ansible-playbook -i inventory/lab/hosts.ini ansible/playbooks/21-failure-injection-web-recovery.yml
    ansible-playbook -i inventory/lab/hosts.ini ansible/playbooks/22-failure-injection-observability-loss.yml
    ansible-playbook -i inventory/lab/hosts.ini ansible/playbooks/23-failure-injection-database-recovery.yml
    ansible-playbook -i inventory/lab/hosts.ini ansible/playbooks/24-failure-injection-proxy-recovery.yml
    ansible-playbook -i inventory/lab/hosts.ini ansible/playbooks/25-failure-injection-backup-recovery.yml

## Precheck Only Mode

Before running the full failure suite, use precheck-only mode to validate that the runtime is healthy and that all failure playbooks are available.

    tools/failure/run_resilience_failure_suite.sh --precheck-only

This mode does not inject failures.

## Suite Execution

Run the full resilience failure suite from WSL.

    tools/failure/run_resilience_failure_suite.sh

The suite performs:

1. Runtime smoke check before failure injection
2. Web backend failure and recovery
3. Observability loss and recovery
4. Database failure and recovery
5. Proxy entrypoint failure and recovery
6. Backup failure and recovery validation
7. Runtime smoke check after recovery
8. Runtime validation evidence refresh

## Evidence

The suite writes a local raw runtime summary to:

    labs/evidence/generated/resilience-failure-suite-summary.md

This file is local runtime evidence and is not intended to be committed by default.

Scenario-level reviewer-facing evidence is generated under:

    scenarios/<level>/<scenario>/evidence/generated/lab-runtime-validation.md

## Validation Model

Each failure scenario follows the same validation pattern:

1. Inject controlled failure
2. Wait for scrape and alert evaluation
3. Query Prometheus metrics
4. Confirm expected alert path
5. Recover affected service
6. Confirm metric recovery
7. Run runtime smoke check

## Boundary

These failure scenarios are not destructive production tests.

They are controlled lab validations designed to demonstrate detection, alerting, recovery, and recovery-validation behavior within the local hybrid infrastructure runtime.
