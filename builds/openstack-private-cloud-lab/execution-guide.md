# OpenStack Private Cloud Lab Execution Guide

## Purpose

This guide provides an execution-oriented path for building and validating the OpenStack Private Cloud Lab.

The goal is to connect a practical OpenStack lab with the SNSD Hybrid Infrastructure operational platform model.

This guide focuses on host preparation, Kolla-Ansible deployment flow, OpenStack baseline resource creation, observability integration, automation validation, evidence capture, and scenario linkage.

## Execution Boundary

This guide is intended for a lab-grade OpenStack environment.

It does not claim production-grade OpenStack readiness. All results should be interpreted as lab execution evidence unless explicitly connected to a production environment.

## Phase 0 - Prepare Host

### Objective

Prepare the Linux host for OpenStack deployment.

### Checklist

- Confirm CPU virtualization support.
- Confirm RAM and disk capacity.
- Configure static IP.
- Configure hostname.
- Configure DNS.
- Configure time synchronization.
- Install base packages.
- Confirm SSH and sudo access.

### Example Commands

- lscpu
- grep -E 'vmx|svm' /proc/cpuinfo
- ip addr
- ip route
- hostnamectl
- timedatectl

### Evidence to Capture

- host CPU and memory summary
- disk capacity
- IP address configuration
- hostname
- time sync status

## Phase 1 - Install Base Packages

### Objective

Install packages required for lab preparation.

### Example Package Set

- git
- curl
- wget
- vim
- python3
- python3-pip
- python3-venv
- net-tools
- iproute2
- bridge-utils
- tcpdump
- jq
- chrony

### Validation

- Python is available.
- Git is available.
- Network troubleshooting tools are available.
- Time synchronization is active.

### Evidence to Capture

- package installation result
- python version
- git version
- time sync status

## Phase 2 - Prepare Kolla-Ansible

### Objective

Prepare Kolla-Ansible installation and configuration.

### Execution Flow

1. Create a Python virtual environment.
2. Install Ansible-compatible dependencies.
3. Install Kolla-Ansible for the selected OpenStack release.
4. Prepare Kolla configuration directory.
5. Prepare inventory.
6. Prepare globals.yml.
7. Generate passwords.yml.

### Key Files

| File | Purpose |
|---|---|
| /etc/kolla/globals.yml | Main Kolla-Ansible deployment configuration |
| /etc/kolla/passwords.yml | Service passwords |
| inventory file | Deployment target definition |
| clouds.yaml or openrc | OpenStack CLI authentication after deployment |

### Validation

- Kolla-Ansible command is available.
- Inventory file is readable.
- globals.yml is reviewed.
- passwords.yml exists.
- Host network interface names are confirmed.

### Evidence to Capture

- selected OpenStack release
- Kolla-Ansible version
- inventory summary
- sanitized globals.yml summary
- generated passwords.yml existence, not secret values

## Phase 3 - Run Bootstrap and Prechecks

### Objective

Validate that the host and configuration are ready for deployment.

### Execution Flow

1. Run bootstrap step.
2. Run prechecks.
3. Resolve any failures.
4. Re-run prechecks until clean.

### Validation

- Bootstrap completes.
- Prechecks complete.
- No blocking network, disk, permission, or runtime errors remain.

### Evidence to Capture

- bootstrap result
- precheck result
- failed checks and resolution notes
- final successful precheck output

## Phase 4 - Deploy OpenStack

### Objective

Deploy OpenStack services.

### Execution Flow

1. Run Kolla-Ansible deploy.
2. Verify containers.
3. Inspect service health.
4. Run post-deploy.
5. Prepare OpenStack CLI credentials.

### Validation

- Core containers are running.
- Keystone responds.
- Service catalog is available.
- Horizon is reachable.
- OpenStack CLI authentication works.

### Evidence to Capture

- container status
- OpenStack service catalog
- endpoint list
- Horizon reachability
- OpenStack CLI authentication result

## Phase 5 - Create OpenStack Resource Baseline

### Objective

Create a minimal tenant environment for workflow validation.

### Resource Tasks

- Create project.
- Create user.
- Assign role.
- Upload image.
- Create flavor.
- Create tenant network.
- Create subnet.
- Create router.
- Attach router to provider network.
- Create security group rules.
- Boot test instance.
- Allocate floating IP.
- Associate floating IP.
- Validate reachability.

### Validation

- Project exists.
- User can authenticate.
- Image is available.
- Flavor is available.
- Tenant network exists.
- Router path exists.
- Instance reaches ACTIVE state.
- Floating IP is associated.
- Reachability test succeeds or failure is documented.

### Evidence to Capture

- project list
- image list
- flavor list
- network list
- subnet list
- router show
- security group rules
- server list
- floating IP list
- ping or SSH test result

## Phase 6 - Add Observability

### Objective

Collect operational telemetry from the lab.

### Tools

- Prometheus
- node-exporter
- openstack-exporter
- blackbox-exporter
- Grafana

### Execution Flow

1. Deploy node-exporter.
2. Deploy openstack-exporter.
3. Deploy blackbox-exporter.
4. Configure Prometheus scrape targets.
5. Configure Grafana dashboard views.
6. Validate targets and dashboards.

### Validation

- Prometheus is reachable.
- node-exporter target is UP.
- openstack-exporter target is UP.
- blackbox probe target is UP or failure is explained.
- Grafana dashboard displays metric data.

### Evidence to Capture

- Prometheus target status
- metric query result
- dashboard reference
- blackbox probe result
- exporter service status

## Phase 7 - Add Log and Event Visibility

### Objective

Enable log and event investigation for correlation workflows.

### Tools

- OpenSearch
- Fluent Bit or compatible log forwarder

### Execution Flow

1. Identify OpenStack service logs.
2. Configure log forwarding.
3. Validate OpenSearch ingestion.
4. Create useful query examples.
5. Capture event evidence.

### Validation

- Logs are searchable.
- Time filtering works.
- OpenStack service events are visible.
- Log evidence can support correlation scenarios.

### Evidence to Capture

- OpenSearch index status
- sample query result
- service error or event example
- time-windowed search result

## Phase 8 - Add Automation Workflows

### Objective

Automate selected operational actions.

### Candidate Workflows

- instance restart
- instance rebuild
- floating IP reassignment
- security group remediation
- volume detach and reattach
- post-action validation

### Validation

- Automation authenticates to OpenStack.
- Target resource is explicit.
- Action result is captured.
- Failure output is preserved.
- Post-action validation runs.

### Evidence to Capture

- Ansible playbook output
- changed or failed result
- target resource state before action
- target resource state after action
- validation script output

## Phase 9 - Connect to SNSD HybridInfra Scenarios

### Objective

Map lab execution results to selected lifecycle scenarios.

### Candidate Mapping

| Lifecycle | Candidate Workflow |
|---|---|
| Level 1 Visibility | OpenStack API, compute, network, instance, and floating IP monitoring |
| Level 2 Correlation | Instance reachability plus router, security group, and floating IP context |
| Level 3 Recovery | Instance rebuild, restart, floating IP reassignment, or security group remediation |
| Level 4 Resilience | Compute host or network path degraded-state validation |
| Level 5 Continuity | Private cloud service continuity and governance-facing evidence summary |

### Validation

- Scenario README has operational interpretation.
- Decision matrix matches lab condition.
- Evidence file explains lab execution boundary.
- Validation evidence links to observed result.
- Execution evidence does not overstate production execution.

### Evidence to Capture

- selected scenario path
- mapped lab workflow
- observed condition
- operator decision
- action taken
- validation result
- evidence files updated

## Phase 10 - Repository Validation

### Objective

Validate that repository quality remains clean after lab integration.

### Commands

- python tools/content-generator/check_markdown_links.py
- python tools/content-generator/check_top_level_structure.py
- python tools/content-generator/run_repository_validation.py
- python tools/content-generator/generate_repository_summary_report.py

### Expected Result

- Markdown Broken Links: 0
- Top-Level Extra Directories: 0
- Top-Level Missing Directories: 0
- Root README Missing Links: 0
- Repository Language Hits: 0
- Portfolio Baseline Status: PASS

## Evidence Storage Policy

Lab-wide documentation should stay under:

- builds/openstack-private-cloud-lab/

Scenario-specific evidence should be stored under the matching scenario directory:

- scenarios/<level>/<scenario>/evidence/generated/

Do not place unstable command output directly in the root README.

## Failure Recording Policy

Failures should be documented when they provide operational value.

For each failure, record:

- phase
- command or action
- observed error
- suspected cause
- corrective action
- validation after correction
- whether scenario evidence was updated

## Completion Criteria

The lab execution guide is considered complete when:

- OpenStack baseline is deployed.
- A test instance can be created.
- Network and floating IP behavior can be validated.
- Metrics are collected.
- At least one automation workflow is tested.
- Evidence is generated.
- One or more SNSD HybridInfra scenarios are linked to lab execution.
- Repository validation remains PASS.
