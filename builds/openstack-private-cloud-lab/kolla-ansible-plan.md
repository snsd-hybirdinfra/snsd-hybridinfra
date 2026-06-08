# Kolla-Ansible Deployment Plan

## Purpose

This document defines the Kolla-Ansible deployment plan for the OpenStack Private Cloud Lab.

The goal is to use an operations-oriented, open-source deployment method for building an OpenStack lab that can support SNSD Hybrid Infrastructure scenario validation, observability, recovery automation, and evidence generation.

## Why Kolla-Ansible

Kolla-Ansible is selected because it aligns with the repository direction:

- open-source infrastructure operations
- Ansible-based deployment and automation
- containerized OpenStack service management
- repeatable deployment workflow
- practical service health validation
- operational troubleshooting value
- observability and recovery workflow integration

## Deployment Boundary

This plan targets a lab-grade OpenStack deployment.

It is not intended to claim production-grade OpenStack readiness. The purpose is to create a stable enough private cloud environment for operational scenario validation.

## Target Deployment Profile

| Item | Target |
|---|---|
| Deployment Type | Single-node or small-scale OpenStack lab |
| Primary Method | Kolla-Ansible |
| Base OS | Ubuntu Server LTS or compatible Linux distribution |
| Runtime | Docker or compatible container runtime supported by selected Kolla-Ansible version |
| Automation | Ansible |
| Network Mode | Single-NIC or two-NIC lab design |
| Observability | Prometheus, openstack-exporter, node-exporter, Grafana |
| Logs | OpenSearch added after baseline stability |

## Deployment Phases

## Phase 1 - Host Baseline

### Objective

Prepare the host for Kolla-Ansible deployment.

### Tasks

- Confirm host requirements.
- Confirm virtualization support.
- Configure static IP.
- Configure hostname.
- Configure DNS.
- Configure time synchronization.
- Install base packages.
- Install Python tooling.
- Install Ansible dependencies.
- Prepare SSH access.
- Confirm sudo access.
- Confirm selected network design.

### Validation

- Host IP is stable.
- DNS resolution works.
- Time synchronization works.
- Python is available.
- Ansible is available.
- Host can pull required packages and container images.
- Network interface names are documented.

## Phase 2 - Kolla-Ansible Installation

### Objective

Install Kolla-Ansible and prepare configuration files.

### Tasks

- Create Python virtual environment if used.
- Install Kolla-Ansible according to the selected OpenStack release.
- Create or copy the Kolla configuration directory.
- Prepare inventory file.
- Prepare globals.yml.
- Generate passwords.yml.
- Review network interface values.
- Review enabled services.
- Review container image source.
- Pin versions where appropriate.

### Key Files

| File | Purpose |
|---|---|
| /etc/kolla/globals.yml | Main deployment configuration |
| /etc/kolla/passwords.yml | Generated service credentials |
| inventory file | Defines deployment target nodes |
| clouds.yaml | Used later for OpenStack CLI authentication |

### Validation

- Kolla-Ansible command is available.
- Inventory parses correctly.
- globals.yml has expected interface and service values.
- passwords.yml exists.
- Deployment release or branch is documented.

## Phase 3 - Configuration Design

### Objective

Define the minimal OpenStack service configuration for the lab.

### Configuration Areas

- network interfaces
- internal VIP or API address
- external network interface
- base distribution
- container engine
- enabled OpenStack services
- Cinder enablement decision
- Horizon enablement
- Neutron provider network configuration
- TLS decision
- logging and monitoring decision

### Initial Service Scope

| Service | Initial Decision |
|---|---|
| Keystone | Enabled |
| Nova | Enabled |
| Neutron | Enabled |
| Glance | Enabled |
| Horizon | Enabled |
| Placement | Enabled |
| Cinder | Optional in early phase |
| Prometheus | Add after OpenStack baseline |
| Grafana | Add after OpenStack baseline |
| OpenSearch | Add after baseline stability |

### Validation

- Configuration is minimal.
- Unnecessary services are not enabled early.
- Network settings match the network plan.
- Optional services are staged rather than enabled all at once.

## Phase 4 - Bootstrap Servers

### Objective

Prepare the host for OpenStack deployment.

### Expected Action

Run the Kolla-Ansible bootstrap step after configuration is ready.

### Validation

- Required packages are installed.
- Container runtime is ready.
- Required directories are prepared.
- Host is ready for prechecks.

## Phase 5 - Prechecks

### Objective

Validate whether the host and configuration are ready for deployment.

### Expected Action

Run the Kolla-Ansible prechecks step before deploy.

### Validation

- Prechecks complete successfully.
- Network interface checks pass.
- Service port conflicts are resolved.
- Disk and permission checks pass.
- Container runtime checks pass.
- Any failed check is documented before retry.

## Phase 6 - Deploy

### Objective

Deploy OpenStack services using Kolla-Ansible.

### Expected Action

Run the Kolla-Ansible deploy step after prechecks pass.

### Validation

- Containers are created.
- Core OpenStack services start.
- Service logs do not show blocking errors.
- Keystone, Nova, Neutron, Glance, Horizon, and Placement are reachable or inspectable.

## Phase 7 - Post-Deploy

### Objective

Prepare OpenStack client authentication and baseline validation.

### Tasks

- Run post-deploy step.
- Generate admin credentials.
- Prepare clouds.yaml or openrc.
- Install OpenStack client if needed.
- Authenticate with OpenStack CLI.
- Confirm service catalog.
- Confirm endpoint list.
- Confirm compute service list.
- Confirm network agent list.
- Confirm image list.

### Validation

- OpenStack CLI authentication works.
- Horizon is reachable.
- OpenStack service catalog is visible.
- Core services respond.

## Phase 8 - Resource Baseline

### Objective

Create baseline OpenStack resources for validation scenarios.

### Tasks

- Create project.
- Create user.
- Assign role.
- Upload cloud image.
- Create flavor.
- Create tenant network.
- Create subnet.
- Create router.
- Connect router to provider network.
- Create security group rules.
- Boot test instance.
- Allocate and associate floating IP.
- Validate reachability.

### Validation

- Instance reaches ACTIVE state.
- Instance gets tenant IP.
- Floating IP association works.
- Security group rules are correct.
- Instance reachability is confirmed.

## Phase 9 - Observability Integration

### Objective

Add monitoring after OpenStack baseline is stable.

### Tasks

- Deploy node-exporter.
- Deploy openstack-exporter.
- Deploy Prometheus.
- Configure scrape jobs.
- Deploy Grafana.
- Create dashboard references.
- Add blackbox-exporter for reachability probes.

### Validation

- Prometheus targets are UP.
- OpenStack metrics are visible.
- Node metrics are visible.
- Floating IP probe works.
- Grafana dashboards load.

## Phase 10 - Automation and Evidence

### Objective

Connect lab workflows to SNSD HybridInfra automation and evidence.

### Tasks

- Create Ansible inventory.
- Create validation scripts.
- Test instance restart workflow.
- Test floating IP reassignment workflow.
- Test security group remediation workflow.
- Capture command outputs.
- Generate evidence files.
- Map results to selected scenarios.

### Validation

- Automation action has clear trigger.
- Automation target is explicit.
- Result is captured.
- Failure output is preserved.
- Post-action validation is captured.
- Evidence is linked to scenario documentation.

## Recommended Validation Commands

Use these command categories during validation:

- host validation commands
- container status commands
- Kolla-Ansible precheck output
- OpenStack service list commands
- OpenStack network list commands
- OpenStack server list commands
- OpenStack floating IP commands
- Prometheus target status
- Grafana dashboard references
- Ansible execution output
- Python validation output

## Failure Handling Policy

Deployment failures should be handled as operational evidence.

For each failure, record:

- failed phase
- command or task
- error summary
- suspected cause
- corrective action
- validation after correction

Do not hide failed attempts if they provide useful operational learning.

## Repository Integration

After each stable milestone:

- update OpenStack lab documentation
- update generated reports
- run repository validation
- commit only validated changes
- avoid adding unstable command output directly to root README
- place scenario-specific evidence under the matching scenario evidence directory

## Success Criteria

The Kolla-Ansible lab phase is successful when:

- Kolla-Ansible deployment completes.
- OpenStack CLI authentication works.
- Horizon is reachable.
- A tenant network and instance can be created.
- Floating IP or intended access path works.
- Core service health can be checked.
- Monitoring can be connected.
- At least one automation workflow can be validated.
- Evidence can be connected to SNSD HybridInfra scenarios.

## Notes

Exact package versions, OpenStack release names, and Kolla-Ansible commands should be confirmed against the selected release documentation before execution.

This document defines the operational plan and sequence, not a frozen command transcript.
