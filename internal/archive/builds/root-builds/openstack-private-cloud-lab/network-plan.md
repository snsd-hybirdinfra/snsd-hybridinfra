# OpenStack Private Cloud Lab Network Plan

## Purpose

This document defines the network plan for the OpenStack Private Cloud Lab.

The goal is to provide a clear and repeatable network baseline for OpenStack API access, tenant networking, router connectivity, floating IP usage, observability access, and operational validation scenarios.

## Network Design Principle

The lab network should separate the following concerns:

- management access
- OpenStack API access
- provider or external network access
- tenant workload networking
- monitoring and dashboard access
- future storage or backend traffic

The initial lab can start with a simplified single-NIC design, but the documentation should preserve a clean separation of network roles.

## Recommended Network Roles

| Network Role | Purpose |
|---|---|
| Management Network | Host SSH, OpenStack API, Horizon, Prometheus, Grafana, and operational access |
| Provider / External Network | Floating IP allocation and external access to tenant instances |
| Tenant Network | Internal VM-to-VM traffic inside OpenStack project networks |
| Monitoring Access | Access path for Prometheus, Grafana, exporters, and validation checks |
| Storage / Backend Optional | Future Cinder, image, or backend traffic separation |

## Example CIDR Plan

These values are examples. Adjust them to avoid conflict with the local environment.

| Network | Example CIDR | Gateway | Purpose |
|---|---|---|---|
| Management | 192.168.56.0/24 | 192.168.56.1 | Host access, OpenStack APIs, dashboards |
| Provider / External | 192.168.100.0/24 | 192.168.100.1 | Floating IP and external workload access |
| Tenant Network | 10.10.0.0/24 | 10.10.0.1 | Internal OpenStack VM network |
| Optional Storage | 192.168.57.0/24 | 192.168.57.1 | Future storage or backend separation |

## Single-NIC Lab Option

A single-NIC design can be used for a local or nested lab.

### Characteristics

- Easier to start
- Lower hardware requirement
- More dependent on Linux bridge or virtual network configuration
- Higher chance of confusion between management and provider access

### Recommended Use

Use this option when:

- running on a laptop or desktop hypervisor
- only one physical NIC is available
- the goal is initial OpenStack workflow validation
- production-like separation is not required

### Risk

Single-NIC designs can make floating IP and provider network behavior harder to understand. Document any bridge, NAT, or hypervisor network assumptions clearly.

## Two-NIC Lab Option

A two-NIC design is cleaner for OpenStack networking.

### Characteristics

- One NIC for management/API access
- One NIC or bridge for provider/external network
- Cleaner Neutron external network mapping
- Easier to reason about floating IP behavior

### Recommended Use

Use this option when:

- the host has two physical NICs
- the hypervisor can provide two virtual adapters
- the lab is intended for network-focused validation
- Neutron router and floating IP behavior should be explicit

## Logical OpenStack Network Topology

The initial topology should follow this pattern:

| Layer | Component |
|---|---|
| External Access | Provider network |
| OpenStack Routing | Neutron router |
| Tenant Isolation | Project tenant network |
| Instance Access | Floating IP or internal IP |
| Security Boundary | Security group rules |
| Validation | Ping, SSH, HTTP, blackbox-exporter probe |

## Tenant Network Flow

Expected tenant traffic flow:

1. Instance is connected to tenant network.
2. Tenant subnet uses Neutron router as gateway.
3. Neutron router connects tenant network to provider network.
4. Floating IP is allocated from provider network.
5. Floating IP is associated with the instance port.
6. External client reaches the instance through floating IP if security group rules allow it.

## Security Group Baseline

Initial security group rules should be minimal.

| Rule | Purpose |
|---|---|
| ICMP ingress | Basic reachability validation |
| SSH ingress from management network | Controlled administrative access |
| HTTP ingress optional | Web workload validation |
| Egress allowed | Package installation and external connectivity testing |

Avoid opening broad ingress ranges unless the lab is isolated.

## Floating IP Plan

Floating IPs should be allocated from the provider or external network range.

Recommended documentation for each floating IP:

| Field | Description |
|---|---|
| Floating IP | Assigned external address |
| Instance | Target VM |
| Project | OpenStack project |
| Purpose | SSH, HTTP, validation, or monitoring |
| Security Group | Applied access policy |
| Evidence | Command output or reachability result |

## DNS Plan

The lab should define whether DNS is provided by:

- local router
- public resolver
- internal DNS server
- OpenStack DHCP namespace
- manually configured resolver

DNS failures can look like application or network failures, so DNS behavior should be validated separately.

## Routing Validation

Routing validation should include:

- host to OpenStack API
- host to Horizon
- host to Prometheus and Grafana
- instance to tenant gateway
- instance to external network if allowed
- external access to floating IP
- router namespace path if troubleshooting is required

## Observability Network Checks

The monitoring layer should include:

- OpenStack API endpoint checks
- floating IP reachability checks
- instance TCP or HTTP checks
- node-exporter scrape checks
- openstack-exporter scrape checks
- Grafana dashboard availability checks

## Troubleshooting Commands

Useful Linux commands:

- ip addr
- ip route
- ping
- traceroute or tracepath
- ss -tulpen
- tcpdump
- bridge link
- ip netns
- ovs-vsctl show if Open vSwitch is used

Useful OpenStack commands:

- openstack network list
- openstack subnet list
- openstack router list
- openstack router show
- openstack floating ip list
- openstack server list
- openstack port list
- openstack security group list
- openstack security group rule list

## Common Failure Patterns

| Symptom | Likely Area |
|---|---|
| Instance ACTIVE but unreachable | Security group, floating IP, router, provider network |
| Floating IP allocated but no ping | Security group, external routing, Neutron router path |
| Instance cannot reach internet | Router SNAT, provider network, DNS, security group egress |
| Horizon reachable but API commands fail | Keystone auth, clouds.yaml, endpoint URL |
| Prometheus target DOWN | Exporter binding, firewall, wrong scrape address |
| DNS resolution fails inside VM | DHCP options, resolver config, tenant network settings |

## Network Evidence

Network validation evidence should include:

- OpenStack network topology command output
- router and subnet configuration
- floating IP association result
- security group rule output
- ping or TCP check result
- blackbox-exporter probe result
- Prometheus target state
- Grafana dashboard reference

## Scenario Mapping

| Scenario Type | Network Evidence |
|---|---|
| Visibility | API endpoint, router, floating IP, and instance reachability status |
| Correlation | Instance unreachable plus router, security group, DNS, and floating IP context |
| Recovery | Floating IP reassignment or security group remediation result |
| Resilience | Provider path, router path, and degraded connectivity validation |
| Continuity | Private cloud network service availability and governance-facing summary |

## Validation Boundary

This network plan is for lab-grade OpenStack validation.

It should not be treated as production network architecture guidance. Production environments require additional design for HA, routing domains, segmentation, firewalls, address management, provider redundancy, and security governance.
