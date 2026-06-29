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

## Scenario Matrix

| ID | Playbook | Failure Type | Detection Basis | Expected Alert | Recovery Basis |
|---:|---|---|---|---|---|
| 14 | ansible/playbooks/14-failure-injection-web-recovery.yml | Web backend container stop | HAProxy backend health and blackbox HTTP probe | SNSDBlackboxProbeFailed | Container restart and HAProxy frontend HTTP 200 |
| 15 | ansible/playbooks/15-failure-injection-observability-loss.yml | node_exporter stop | up{job="node_exporter"} = 0 | SNSDNodeExporterDown | node_exporter active and target UP |
| 16 | ansible/playbooks/16-failure-injection-database-recovery.yml | MariaDB stop | mysql_up = 0 | SNSDMariaDBDown | MariaDB active and mysql_up = 1 |
| 17 | ansible/playbooks/17-failure-injection-proxy-recovery.yml | HAProxy stop | blackbox_http probe_success = 0 | SNSDBlackboxProbeFailed | HAProxy active and proxy HTTP 200 |
| 18 | ansible/playbooks/18-failure-injection-backup-recovery.yml | Restic backup failure | snsd_backup_last_success = 0 | SNSDBackupFailed | backup success = 1 and restore validation success = 1 |

## Individual Execution

Run from WSL at the repository root.

    ansible-playbook -i inventory/lab/hosts.ini ansible/playbooks/14-failure-injection-web-recovery.yml
    ansible-playbook -i inventory/lab/hosts.ini ansible/playbooks/15-failure-injection-observability-loss.yml
    ansible-playbook -i inventory/lab/hosts.ini ansible/playbooks/16-failure-injection-database-recovery.yml
    ansible-playbook -i inventory/lab/hosts.ini ansible/playbooks/17-failure-injection-proxy-recovery.yml
    ansible-playbook -i inventory/lab/hosts.ini ansible/playbooks/18-failure-injection-backup-recovery.yml

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
