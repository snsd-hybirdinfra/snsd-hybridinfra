# OpenStack Private Cloud Lab Deployment Options

## Purpose

This document compares OpenStack deployment options for the OpenStack Private Cloud Lab.

The goal is to select a deployment method that supports SNSD Hybrid Infrastructure operational scenario validation, open-source infrastructure operations learning, automation, observability, and evidence generation.

## Selection Criteria

Deployment options should be evaluated against the following criteria:

- installation complexity
- repeatability
- operational realism
- resource requirement
- troubleshooting value
- observability integration
- automation compatibility
- suitability for portfolio validation
- long-term maintainability

## Candidate Options

| Option | Summary |
|---|---|
| Kolla-Ansible | Containerized OpenStack deployment using Ansible |
| DevStack | Developer-focused single-node OpenStack deployment |
| Packstack | RHEL-family oriented OpenStack deployment tool |
| Manual Install | Direct service-by-service OpenStack installation |

## Option 1 - Kolla-Ansible

### Description

Kolla-Ansible deploys OpenStack services as containers and uses Ansible for orchestration.

### Strengths

- Strong fit for infrastructure operations learning
- Uses Ansible, which aligns with repository automation direction
- Containerized service model is easier to inspect and restart
- Better long-term portfolio value than one-off developer installation
- Good fit for operational validation, service health checks, and automation workflows

### Weaknesses

- Requires more resources than DevStack
- Initial configuration can be more complex
- Network configuration must be planned carefully
- Troubleshooting requires understanding containers, Ansible, and OpenStack services together

### Best Use

Use Kolla-Ansible when the lab should demonstrate operational capability, repeatable deployment structure, service management, and infrastructure automation.

### Portfolio Fit

High.

Kolla-Ansible fits the SNSD Hybrid Infrastructure direction because it supports an operations-oriented private cloud lab rather than a temporary developer sandbox.

## Option 2 - DevStack

### Description

DevStack is designed for quickly deploying an OpenStack environment for development and experimentation.

### Strengths

- Fastest way to start
- Good for API testing
- Good for learning basic OpenStack workflows
- Useful when hardware resources are limited
- Easier initial setup than Kolla-Ansible

### Weaknesses

- Less suitable for long-term operations-style portfolio validation
- Not ideal for stable repeatable lab documentation
- Can feel like a temporary developer sandbox
- Service layout may not represent operations-oriented deployment patterns

### Best Use

Use DevStack for fast OpenStack CLI, API, Horizon, Nova, Neutron, and Glance workflow validation.

### Portfolio Fit

Medium.

DevStack is useful for early testing, but it should not be the final lab direction if the goal is infrastructure operations credibility.

## Option 3 - Packstack

### Description

Packstack is commonly associated with RHEL-family OpenStack lab deployments.

### Strengths

- Useful for RHEL-like environments
- Can provide a relatively guided installation path
- Good for learning traditional OpenStack deployment concepts

### Weaknesses

- Less aligned with the current repository automation direction
- Less portable if the main lab OS is Ubuntu
- May not fit the intended Kolla-Ansible and containerized operations path

### Best Use

Use Packstack only if the lab environment is RHEL-family based and the goal is quick all-in-one OpenStack exploration.

### Portfolio Fit

Low to Medium.

Packstack can be useful, but it is not the preferred direction for this repository.

## Option 4 - Manual Install

### Description

Manual installation means installing and configuring OpenStack services directly one by one.

### Strengths

- Strong educational value
- Deep understanding of service dependencies
- Useful for learning Keystone, Nova, Neutron, Glance, Cinder, and RabbitMQ relationships

### Weaknesses

- Time-consuming
- Error-prone
- Harder to reproduce
- Not ideal for finishing a portfolio-grade lab quickly
- Can delay operational scenario validation

### Best Use

Use manual installation only for targeted learning or troubleshooting, not as the primary portfolio lab deployment method.

### Portfolio Fit

Medium for learning, low for repeatable lab delivery.

## Decision Matrix

| Criteria | Kolla-Ansible | DevStack | Packstack | Manual Install |
|---|---:|---:|---:|---:|
| Fast Start | Medium | High | Medium | Low |
| Repeatability | High | Medium | Medium | Low |
| Operational Realism | High | Low-Medium | Medium | Medium |
| Automation Alignment | High | Medium | Medium | Low |
| Observability Fit | High | Medium | Medium | Medium |
| Troubleshooting Value | High | Medium | Medium | High |
| Portfolio Value | High | Medium | Low-Medium | Medium |
| Long-Term Maintainability | High | Low | Medium | Low |

## Recommended Decision

The recommended primary deployment path is:

- Kolla-Ansible

The recommended fallback path is:

- DevStack

## Recommended Usage Pattern

Use the following phased approach:

1. Use DevStack only if fast OpenStack API validation is needed.
2. Use Kolla-Ansible as the main portfolio lab deployment method.
3. Avoid Packstack unless the host environment is RHEL-family based.
4. Avoid full manual installation as the main path.

## Selected Direction

The SNSD Hybrid Infrastructure OpenStack Private Cloud Lab should use Kolla-Ansible as the primary deployment approach.

This aligns with:

- open-source infrastructure operations
- Ansible-based automation
- containerized service management
- repeatable deployment documentation
- observability and recovery workflow validation
- portfolio-grade operational credibility

## Fallback Strategy

If Kolla-Ansible is blocked by hardware, network, or time constraints:

1. Deploy DevStack for initial workflow validation.
2. Validate OpenStack CLI, Horizon, Nova, Neutron, Glance, and basic VM lifecycle.
3. Document the limitation clearly.
4. Return to Kolla-Ansible when resources allow.

## Validation Expectations

A deployment option is acceptable when it supports:

- OpenStack CLI authentication
- Horizon access
- instance lifecycle testing
- tenant network creation
- floating IP assignment
- security group rule validation
- monitoring integration
- automation testing
- evidence generation
- repository scenario mapping

## Operational Boundary

This document selects a lab deployment method.

It does not claim that the selected deployment is production-grade. The selected method is intended to support operational scenario validation, open-source platform learning, automation testing, and portfolio evidence generation.
