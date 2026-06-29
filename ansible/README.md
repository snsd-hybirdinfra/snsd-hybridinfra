# Ansible Playbooks

This directory contains implementation playbooks for the SNSD Hybrid Infrastructure runtime lab.

## Execution Order

| Order | Playbook | Purpose |
|---:|---|---|
| 01 | `playbooks/01-common-base.yml` | Install common base packages and baseline utilities |
| 02 | `playbooks/02-configure-time-sync.yml` | Configure timezone and chrony time synchronization |
| 03 | `playbooks/03-install-docker.yml` | Install Docker runtime on Ubuntu nodes |
| 04 | `playbooks/04-install-node-exporter.yml` | Install Node Exporter on Ubuntu nodes |
| 05 | `playbooks/05-install-prometheus-grafana.yml` | Install Prometheus and Grafana on data-ops-node |
| 06 | `playbooks/06-configure-grafana-provisioning.yml` | Configure Grafana datasource and dashboard provisioning |
| 07 | `playbooks/07-install-loki-promtail.yml` | Install Loki and Promtail log pipeline |
| 08 | `playbooks/08-install-blackbox-exporter.yml` | Install Blackbox Exporter and Prometheus probe jobs |
| 09 | `playbooks/09-deploy-sample-web-haproxy.yml` | Deploy sample web services and HAProxy load balancer |
| 10 | `playbooks/10-install-cadvisor.yml` | Install cAdvisor for container runtime metrics |
| 11 | `playbooks/11-install-mariadb-exporter.yml` | Install MariaDB and mysqld_exporter |
| 12 | `playbooks/12-configure-restic-backup.yml` | Configure Restic backup and restore validation |
| 13 | `playbooks/13-configure-alertmanager-rules.yml` | Install Alertmanager and configure Prometheus alert rules |
| 14 | `playbooks/14-failure-injection-web-recovery.yml` | Inject web-node failure and validate recovery behavior |
| 15 | `playbooks/15-failure-injection-observability-loss.yml` | Stop node_exporter on app-node-02 and validate observability loss/recovery |
| 16 | `playbooks/16-failure-injection-database-recovery.yml` | Stop MariaDB and validate database failure detection and recovery |
| 17 | `playbooks/17-failure-injection-proxy-recovery.yml` | Stop HAProxy and validate service entrypoint failure detection and recovery |
| 18 | `playbooks/18-failure-injection-backup-recovery.yml` | Break Restic backup configuration and validate backup failure detection and recovery |

## Standard Execution

Run from WSL at the repository root.

    ansible-playbook -i inventory/lab/hosts.ini ansible/playbooks/01-common-base.yml
    ansible-playbook -i inventory/lab/hosts.ini ansible/playbooks/02-configure-time-sync.yml
    ansible-playbook -i inventory/lab/hosts.ini ansible/playbooks/03-install-docker.yml
    ansible-playbook -i inventory/lab/hosts.ini ansible/playbooks/04-install-node-exporter.yml
    ansible-playbook -i inventory/lab/hosts.ini ansible/playbooks/05-install-prometheus-grafana.yml
    ansible-playbook -i inventory/lab/hosts.ini ansible/playbooks/06-configure-grafana-provisioning.yml
    ansible-playbook -i inventory/lab/hosts.ini ansible/playbooks/07-install-loki-promtail.yml
    ansible-playbook -i inventory/lab/hosts.ini ansible/playbooks/08-install-blackbox-exporter.yml
    ansible-playbook -i inventory/lab/hosts.ini ansible/playbooks/09-deploy-sample-web-haproxy.yml
    ansible-playbook -i inventory/lab/hosts.ini ansible/playbooks/10-install-cadvisor.yml
    ansible-playbook -i inventory/lab/hosts.ini ansible/playbooks/11-install-mariadb-exporter.yml
    ansible-playbook -i inventory/lab/hosts.ini ansible/playbooks/12-configure-restic-backup.yml
    ansible-playbook -i inventory/lab/hosts.ini ansible/playbooks/13-configure-alertmanager-rules.yml

Run failure injection only when testing recovery behavior.

    ansible-playbook -i inventory/lab/hosts.ini ansible/playbooks/14-failure-injection-web-recovery.yml

## Boundary

Ansible playbooks are used for VM configuration, service deployment, and controlled failure/recovery validation.

Runtime evidence collection and generated scenario documentation are handled by `tools/evidence/` and `tools/pipeline/`.

## Resilience Failure Suite

The repository provides a wrapper script for running the failure injection scenarios as a resilience validation suite.

Run from WSL:

    tools/failure/run_resilience_failure_suite.sh

The suite runs:

    14-failure-injection-web-recovery.yml
    15-failure-injection-observability-loss.yml
    16-failure-injection-database-recovery.yml
    17-failure-injection-proxy-recovery.yml
    18-failure-injection-backup-recovery.yml

The suite performs a runtime smoke check before and after the failure sequence, then refreshes runtime validation evidence through the runtime validation pipeline.
