# SCENARIO PRODUCTION GOVERNANCE

## Production Objective

The repository is now transitioning from:

manual scenario authoring

to:

taxonomy-driven operational scenario production.

---

# Lifecycle Complexity Model

## Level-1 Visibility

Purpose:

operational visibility establishment

Characteristics:

- telemetry-heavy
- monitoring-oriented
- low orchestration complexity
- single-domain preferred

Avoid:

- recovery orchestration
- resilience governance
- executive continuity workflows

---

## Level-2 Correlation

Purpose:

cross-system operational reasoning

Characteristics:

- dependency analysis
- telemetry correlation
- impact propagation
- cross-component visibility

Avoid:

- distributed failover
- enterprise continuity orchestration

---

## Level-3 Recovery

Purpose:

automated operational restoration

Characteristics:

- recovery orchestration
- rollback automation
- incident coordination
- validation workflows

Avoid:

- enterprise governance workflows
- executive continuity coordination

---

## Level-4 Resilience

Purpose:

distributed survivability coordination

Characteristics:

- multi-site orchestration
- failover coordination
- survivability validation
- resilience-aware workflows

Avoid:

- isolated recovery workflows
- monitoring-only scenarios

---

## Level-5 Continuity

Purpose:

enterprise operational continuity preservation

Characteristics:

- executive visibility
- governance coordination
- cross-domain survivability
- continuity prioritization

Avoid:

- isolated infrastructure operations
- telemetry-only workflows

---

# Naming Governance

Scenario names must:

- use kebab-case
- represent operational intent
- avoid vendor-specific wording
- avoid implementation-specific wording

Good:

vpn-tunnel-recovery-automation

Bad:

fortigate-bgp-script-fix

---

# Capability Governance

Every scenario must define:

- primary capability
- adjacent capabilities
- lifecycle alignment
- operational outcome

Capabilities must exist in:

shared-runtime/registry/capabilities/capability-registry.yaml

---

# README Governance

README generation must preserve:

- section ordering
- workflow consistency
- lifecycle specialization
- validation readability

README structure is now frozen unless governance approval exists.

---

# Topology Governance

Topology diagrams currently serve as:

- operational flow previews
- topology validation artifacts
- orchestration visibility references

Current renderer remains MVP-scoped.

---

# Production Scaling Direction

Future production direction:

taxonomy catalog
→ bulk generation
→ governance validation
→ scenario packaging
→ operational ecosystem expansion

