# Repository Tree

This document shows the reviewer-facing repository structure.

## Public Structure

snsd-hybridinfra/
├─ README.md
├─ scenarios/
│  ├─ level-1-visibility/
│  ├─ level-2-correlation/
│  ├─ level-3-recovery/
│  ├─ level-4-resilience/
│  └─ level-5-continuity/
├─ labs/
│  ├─ 01-linux-observability-lab/
│  ├─ 02-network-routing-lab/
│  ├─ 03-ansible-automation-lab/
│  ├─ 04-container-runtime-lab/
│  ├─ 05-kolla-openstack-lab/
│  ├─ 06-monitoring-stack-lab/
│  ├─ 07-logging-correlation-lab/
│  ├─ 08-backup-recovery-lab/
│  ├─ 09-resilience-failover-lab/
│  └─ 10-governance-reporting-lab/
├─ modules/
├─ adapters/
├─ shared-runtime/
├─ builds/
├─ docs/
├─ reports/
├─ validation-reports/
└─ tools/

## Notes

Generated scenario artifacts are intentionally stored inside each scenario directory.

Reviewer-facing generated outputs include:

- operational posters
- generated evidence summaries
- artifact manifests
- validation evidence
- repository validation reports

Deep generated paths are omitted from this public tree to keep the repository structure readable.
