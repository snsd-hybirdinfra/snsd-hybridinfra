# OpenStack Private Cloud Lab Implementation Plan

## Purpose

This document defines the implementation plan for building an open-source OpenStack-based private cloud lab that supports SNSD Hybrid Infrastructure operational scenario validation.

The lab is designed to provide a practical execution target for visibility, correlation, recovery, resilience, continuity, evidence generation, and validation workflows.

## Implementation Strategy

The implementation should start small and expand in controlled phases.

The recommended approach is:

1. Build a minimal OpenStack lab.
2. Validate OpenStack core operations.
3. Add observability.
4. Add automation.
5. Generate evidence.
6. Connect selected workflows to SNSD HybridInfra scenarios.

## Phase 0 - Host Preparation

### Objective

Prepare the base Linux host or virtualized lab environment.

### Tasks

- Confirm CPU virtualization support.
- Confirm available memory and storage.
- Install base OS.
- Configure hostname.
- Configure static IP address.
- Configure DNS resolution.
- Configure NTP or time synchronization.
- Install Git, Python, pip, curl, wget, vim, and basic troubleshooting tools.
- Disable or adjust local firewall only when required by the selected OpenStack deployment method.
- Prepare SSH access.

### Validation

- Host can reach the internet or package mirror.
- Host has stable IP configuration.
- Hostname resolution is consistent.
- Time synchronization is active.
- Git and Python are available.

## Phase 1 - OpenStack Deployment Foundation

### Objective

Deploy a minimal OpenStack environment suitable for lab validation.

### Candidate Deployment Options

| Option | Use Case |
|---|---|
| Kolla-Ansible | Preferred for containerized OpenStack deployment and operational learning |
| DevStack | Useful for fast single-node experimentation |
| Packstack | Useful for RHEL-like environments, but less preferred for long-term portfolio direction |

### Recommended Direction

Use Kolla-Ansible when hardware resources are sufficient.

Use DevStack only if the goal is quick API and workflow testing.

### Core Services

- Keystone
- Nova
- Neutron
- Glance
- Cinder
- Horizon
- Placement

### Validation

- OpenStack CLI authentication works.
- Horizon dashboard is reachable.
- Service catalog is available.
- Nova service list is healthy.
- Neutron agent list is healthy.
- Glance image list works.
- Cinder service list works if block storage is enabled.

## Phase 2 - OpenStack Resource Baseline

### Objective

Create a minimal tenant environment for operational testing.

### Tasks

- Create project.
- Create user and assign role.
- Upload or register a cloud image.
- Create flavor.
- Create tenant network.
- Create subnet.
- Create router.
- Attach router to external network.
- Create security group rules.
- Boot test instance.
- Allocate floating IP.
- Associate floating IP to instance.
- Validate SSH or ICMP reachability depending on security policy.

### Validation

- Instance reaches ACTIVE state.
- Floating IP is assigned.
- Security group rules are applied.
- Instance is reachable through the intended access path.
- Router and network topology are visible.

## Phase 3 - Observability Baseline

### Objective

Collect health and availability signals from the OpenStack lab.

### Tools

- Prometheus
- node-exporter
- openstack-exporter
- blackbox-exporter
- Grafana

### Tasks

- Deploy node-exporter on the OpenStack host.
- Deploy openstack-exporter for OpenStack service metrics.
- Deploy blackbox-exporter for endpoint and floating IP reachability.
- Configure Prometheus scrape jobs.
- Create Grafana dashboard references.
- Define baseline metrics for compute, network, API, and instance health.

### Validation

- Prometheus targets are UP.
- OpenStack metrics are visible.
- Node metrics are visible.
- Reachability probes are visible.
- Grafana dashboard displays baseline state.

## Phase 4 - Log and Event Visibility

### Objective

Add log search and event investigation capability.

### Tools

- OpenSearch
- Fluent Bit or compatible log forwarder

### Tasks

- Identify important OpenStack logs.
- Configure log forwarding.
- Create OpenSearch index pattern.
- Validate event search.
- Capture service error, authentication, API, and network-related log events.

### Validation

- Logs are searchable.
- Time window filtering works.
- OpenStack service events are visible.
- Logs can support correlation scenarios.

## Phase 5 - Automation Baseline

### Objective

Automate selected OpenStack operational actions.

### Tools

- Ansible
- OpenStack CLI
- Python validation scripts

### Candidate Automation Workflows

- instance restart
- instance rebuild
- floating IP reassignment
- security group rule remediation
- volume detach and reattach
- service health check
- post-recovery validation

### Validation

- Automation can authenticate to OpenStack.
- Automation targets the intended project and resource.
- Automation result is captured.
- Failure output is preserved.
- Post-action validation is executed.

## Phase 6 - Scenario Evidence Integration

### Objective

Connect lab execution results to SNSD HybridInfra scenario evidence.

### Evidence Types

- command output
- Prometheus target status
- Grafana dashboard reference
- OpenSearch query result
- Ansible execution output
- Python validation result
- post-recovery state confirmation

### Candidate Scenario Connections

| Lifecycle | Candidate OpenStack Workflow |
|---|---|
| Level 1 Visibility | OpenStack API and compute health monitoring |
| Level 2 Correlation | Instance reachability and Neutron router path correlation |
| Level 3 Recovery | Instance rebuild or floating IP reassignment automation |
| Level 4 Resilience | Compute host or network path resilience validation |
| Level 5 Continuity | Private cloud service continuity review |

### Validation

- Evidence is linked to a specific scenario.
- Evidence does not overstate production execution.
- Evidence includes operator decision context.
- Evidence includes validation result.
- Evidence can be reviewed from the repository.

## Phase 7 - Repository Integration

### Objective

Keep OpenStack lab documentation aligned with the SNSD HybridInfra platform structure.

### Tasks

- Update build documentation.
- Add implementation notes.
- Add command references only when stable.
- Add scenario mapping references.
- Refresh reports.
- Run repository validation.

### Validation Commands

- python tools/content-generator/check_markdown_links.py
- python tools/content-generator/check_top_level_structure.py
- python tools/content-generator/run_repository_validation.py
- python tools/content-generator/generate_repository_summary_report.py

## Execution Boundary

This implementation plan defines a lab validation path.

It does not claim that the OpenStack environment is production-grade. The lab exists to support operational scenario validation, evidence generation, automation testing, and open-source infrastructure operations learning.

## Success Criteria

The lab is considered successful when:

- OpenStack core services are accessible.
- A tenant VM can be created and reached.
- Metrics are collected through Prometheus.
- Dashboards are available in Grafana.
- At least one recovery workflow is automated.
- Validation output is generated.
- Evidence can be connected to selected SNSD HybridInfra scenarios.
- Repository validation remains PASS.
