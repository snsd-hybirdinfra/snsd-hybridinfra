# OpenStack Private Cloud Lab

## Build Purpose

This build defines an open-source private cloud lab foundation for validating infrastructure operations scenarios in the SNSD Hybrid Infrastructure repository.

The lab is intended to support practical validation of monitoring, correlation, recovery, resilience, and continuity workflows using OpenStack and open-source operations tooling.

## Architecture Scope

The initial lab scope is a single-node or small-scale OpenStack environment suitable for portfolio validation and operational workflow testing.

The architecture focuses on:

- OpenStack control plane services
- compute instance lifecycle
- tenant network and router configuration
- floating IP access
- security group boundaries
- image and flavor management
- block storage attachment
- operational telemetry collection
- automation and validation workflows

## Core OpenStack Components

| Component | Role |
|---|---|
| Keystone | Identity, authentication, projects, users, and roles |
| Nova | Compute service and instance lifecycle management |
| Neutron | Tenant networking, routers, security groups, and floating IPs |
| Glance | Image registry and VM image management |
| Cinder | Block storage volume lifecycle |
| Horizon | Web dashboard for operational visibility |
| Placement | Resource inventory and scheduling support |

## Open-Source Operations Stack

| Area | Tooling |
|---|---|
| OpenStack Deployment | Kolla-Ansible or DevStack |
| Automation | Ansible |
| Infrastructure Definition | OpenTofu or OpenStack CLI |
| VM Initialization | cloud-init |
| Metrics | Prometheus |
| OpenStack Metrics | openstack-exporter |
| Node Metrics | node-exporter |
| Reachability Checks | blackbox-exporter |
| Alerting | Alertmanager |
| Dashboards | Grafana |
| Logs and Search | OpenSearch |
| Validation | Python scripts |
| Documentation and Evidence | Markdown, generated reports, and scenario evidence |

## Operations Scope

The lab supports the following operational activities:

- project and user creation
- image registration
- flavor creation
- tenant network creation
- router and external network attachment
- floating IP allocation
- security group rule management
- instance provisioning
- cloud-init based VM bootstrap
- volume creation and attachment
- instance reachability validation
- telemetry collection
- dashboard review
- recovery workflow testing
- evidence generation

## Observability Scope

The observability layer should support:

- OpenStack API health visibility
- compute node resource visibility
- instance state visibility
- Neutron network and router visibility
- floating IP reachability checks
- Prometheus metric collection
- Grafana dashboard views
- log collection and event search through OpenSearch

## Automation Scope

The automation layer should support:

- OpenStack resource creation
- instance rebuild or restart workflows
- floating IP reassignment workflow
- security group remediation
- volume detach and reattach workflow
- validation checks after recovery actions
- generated evidence updates

## Scenario Mapping

| Lifecycle Level | OpenStack Lab Mapping |
|---|---|
| Level 1 Visibility | Nova, Neutron, Cinder, Keystone, API, instance, and network health monitoring |
| Level 2 Correlation | Instance reachability, router path, floating IP, compute pressure, and dependency correlation |
| Level 3 Recovery | Instance rebuild, service restart, floating IP reassignment, volume reattach, and access remediation |
| Level 4 Resilience | Multi-compute host behavior, network path resilience, degraded-state handling, and failover validation |
| Level 5 Continuity | Private cloud service continuity, ownership visibility, cross-domain validation, and governance reporting |

## Candidate Validation Scenarios

The following scenario types can be connected to this lab:

- OpenStack compute health monitoring
- OpenStack API health monitoring
- Neutron router reachability monitoring
- instance network correlation
- compute resource pressure correlation
- instance rebuild automation
- floating IP reassignment recovery
- Cinder volume reattach recovery
- private cloud control plane resilience
- private cloud service continuity

## Evidence Strategy

Evidence generated from this lab should be stored in scenario evidence directories only when it is connected to a specific operational scenario.

Generated evidence should distinguish between:

- documentation-level validation
- lab execution evidence
- command output
- monitoring screenshots
- recovery action results
- post-recovery validation results

## Validation Boundary

This lab is not intended to represent a production-grade OpenStack deployment by itself.

Its purpose is to provide an open-source infrastructure operations testbed for validating portfolio scenarios, operational workflows, automation boundaries, telemetry collection, and evidence generation.

## Implementation Phases

### Phase 1 - Lab Foundation

- prepare Linux host
- install prerequisites
- deploy single-node OpenStack
- verify Horizon and OpenStack CLI access
- create initial project, user, image, flavor, network, router, security group, and instance

### Phase 2 - Observability

- deploy Prometheus
- deploy node-exporter
- deploy openstack-exporter
- deploy blackbox-exporter
- create Grafana dashboards
- collect baseline metrics

### Phase 3 - Automation

- create Ansible inventory
- automate OpenStack resource operations
- automate recovery workflows
- automate validation checks

### Phase 4 - Evidence Integration

- capture command output
- collect dashboard references
- generate validation evidence
- connect lab results to selected SNSD HybridInfra scenarios

### Phase 5 - Scenario Expansion

- add OpenStack-specific scenarios if needed
- map lab workflows to existing lifecycle levels
- update reports and validation documentation

## Implementation Documents

- [Execution Checklist](./execution-checklist.md)
- [Kolla-Ansible Deployment Plan](./kolla-ansible-plan.md)
- [Deployment Options](./deployment-options.md)
- [Network Plan](./network-plan.md)
- [Host Requirements](./host-requirements.md)
- [Implementation Plan](./implementation-plan.md)

## Related Repository Layers

- scenarios/: lifecycle-based operational workflows
- modules/: reusable operational capabilities
- adapters/: integration boundaries for OpenStack-related tooling
- shared-runtime/: telemetry, orchestration, evidence, and integration concepts
- tools/: validation and generation workflows
- reports/: generated repository validation outputs
