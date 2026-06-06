# Infrastructure Build Scenarios

This directory contains build-oriented infrastructure scenarios.

Build scenarios demonstrate how infrastructure foundations are designed, provisioned, configured, secured, instrumented, and prepared for operational use.

They complement the operational scenarios under `/scenarios`.

## Build Flow

Infrastructure Build  
→ Baseline Configuration  
→ Security Boundary  
→ Observability Setup  
→ Automation Readiness  
→ Operational Scenario Integration

## Build Scenarios

| Build Scenario | Purpose |
|---|---|
| hybrid-vpc-foundation | Defines baseline hybrid VPC, subnet, routing, and gateway foundation |
| private-web-tier-with-bastion | Builds private server access using bastion-controlled administration |
| nat-gateway-egress-architecture | Configures private outbound access through NAT gateway design |
| alb-based-web-service-routing | Builds application load balancing and web service routing structure |
| security-boundary-baseline | Defines security groups, access rules, and network boundary controls |
| observability-stack-deployment | Deploys metrics, dashboards, exporters, and visibility foundation |
| ansible-server-bootstrap | Automates baseline server package, user, service, and configuration setup |
| log-pipeline-foundation | Builds log collection, forwarding, storage, and review pipeline foundation |
| backup-automation-foundation | Establishes backup job automation, repository target, and validation boundary |
| recovery-validation-lab | Builds controlled recovery test environment and validation evidence workflow |

## Relationship to Operational Scenarios

Build scenarios answer:

> How is the infrastructure foundation created?

Operational scenarios answer:

> How is that foundation monitored, analyzed, recovered, validated, and governed?
