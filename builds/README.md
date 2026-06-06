# Infrastructure Build Scenarios

This directory contains build-oriented infrastructure scenarios.

Build scenarios document how infrastructure foundations are designed, provisioned, configured, secured, instrumented, and prepared for operational use.

---

## Build Scenario Catalog

| Build Scenario | Purpose |
|---|---|
| [ALB Based Web Service Routing](alb-based-web-service-routing/) | Application load balancing, listener routing, and target health structure |
| [Ansible Server Bootstrap](ansible-server-bootstrap/) | Server bootstrap automation for packages, users, services, and configuration |
| [Backup Automation Foundation](backup-automation-foundation/) | Backup job automation, repository target, retention, and validation boundary |
| [Hybrid VPC Foundation](hybrid-vpc-foundation/) | Baseline hybrid VPC, subnet, routing, gateway, and connectivity foundation |
| [Log Pipeline Foundation](log-pipeline-foundation/) | Log collection, forwarding, indexing, retention, and review pipeline |
| [NAT Gateway Egress Architecture](nat-gateway-egress-architecture/) | Private subnet outbound access through NAT gateway routing |
| [Observability Stack Deployment](observability-stack-deployment/) | Metrics, exporters, dashboards, and operational visibility foundation |
| [Private Web Tier With Bastion](private-web-tier-with-bastion/) | Private web tier with bastion-controlled administrative access |
| [Recovery Validation Lab](recovery-validation-lab/) | Controlled recovery validation environment and evidence workflow |
| [Security Boundary Baseline](security-boundary-baseline/) | Security groups, access boundaries, and baseline network controls |

---

## Build Flow

Infrastructure Build  
→ Baseline Configuration  
→ Security Boundary  
→ Observability Setup  
→ Automation Readiness  
→ Operational Scenario Integration

---

## Relationship to Operational Scenarios

Build scenarios answer how the infrastructure foundation is created.

Operational scenarios answer how that foundation is monitored, analyzed, recovered, validated, and governed.
