# OpenStack Private Cloud Lab Execution Checklist

## Purpose

This checklist guides the operational execution of the OpenStack Private Cloud Lab for scenario validation.  
It ensures that each step is performed, validated, and recorded for evidence.

## Phase 0 - Host Preparation

- [ ] Verify CPU supports virtualization (vmx/svm flags)
- [ ] Confirm available memory and storage
- [ ] Install base OS (Ubuntu Server LTS recommended)
- [ ] Configure static IP and hostname
- [ ] Configure DNS and NTP
- [ ] Install Git, Python, pip, curl, wget, vim
- [ ] Disable firewall or adjust rules if needed for lab
- [ ] Confirm SSH access and sudo privileges

## Phase 1 - OpenStack Deployment Foundation

- [ ] Select deployment method (Kolla-Ansible recommended)
- [ ] Install deployment tool
- [ ] Prepare inventory and configuration files
- [ ] Review enabled services and network configuration
- [ ] Confirm container runtime availability

## Phase 2 - OpenStack Resource Baseline

- [ ] Create project and user with proper roles
- [ ] Upload or register cloud image
- [ ] Create flavor
- [ ] Create tenant network and subnet
- [ ] Create router and attach to external network
- [ ] Create security group rules
- [ ] Boot test instance
- [ ] Allocate and associate floating IP
- [ ] Validate instance reachability (SSH, ICMP)

## Phase 3 - Observability Baseline

- [ ] Deploy node-exporter
- [ ] Deploy openstack-exporter
- [ ] Deploy blackbox-exporter
- [ ] Deploy Prometheus and configure scrape targets
- [ ] Deploy Grafana dashboards and validate data

## Phase 4 - Log and Event Visibility

- [ ] Configure log forwarding to OpenSearch
- [ ] Validate log ingestion from OpenStack services
- [ ] Confirm event search functionality
- [ ] Capture service events for correlation scenarios

## Phase 5 - Automation Baseline

- [ ] Prepare Ansible inventory and playbooks
- [ ] Test instance restart workflow
- [ ] Test floating IP reassignment workflow
- [ ] Test security group remediation workflow
- [ ] Test volume reattach workflow
- [ ] Validate post-action state

## Phase 6 - Evidence Integration

- [ ] Capture command outputs
- [ ] Collect dashboard screenshots
- [ ] Collect log / OpenSearch query results
- [ ] Generate validation-evidence.md and execution-evidence.md
- [ ] Link evidence to specific scenario README

## Phase 7 - Scenario Mapping

- [ ] Map lab workflows to lifecycle levels
- [ ] Verify scenario Operational Decision Matrix
- [ ] Verify Operational Review Notes presence
- [ ] Confirm scenario evidence integration

## Phase 8 - Validation Check

- [ ] Run repository validation workflow
- [ ] Verify portfolio baseline PASS
- [ ] Verify Markdown links, top-level structure, and README alignment
- [ ] Update reports if necessary

## Notes

- Check each box only when the step is complete and validated
- Document any deviations or errors in the evidence files
- Use this checklist as a guide, not a replacement for operational understanding
