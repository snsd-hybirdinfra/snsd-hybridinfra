# Kolla OpenStack Lab Evidence

This directory stores lab-local evidence generated during Kolla OpenStack validation execution.

## Evidence Focus

Kolla-Ansible readiness, OpenStack service containers, control plane APIs, service catalog, endpoints, compute visibility, network validation, service recovery, and OpenStack evidence.

## Evidence Areas

| Directory | Purpose |
|---|---|
| raw/ | Raw Kolla-Ansible output, OpenStack CLI output, API checks, service container state, compute output, network output, and recovery records |
| processed/ | Parsed service health summaries, endpoint validation summaries, compute visibility summaries, network validation summaries, and recovery summaries |
| summary/ | Reviewer-readable OpenStack operational evidence summaries |

## Current Status

| Area | Status |
|---|---|
| Documentation Status | documentation-ready |
| Implementation Status | planned |
| Execution Status | not yet executed |
| Evidence Status | placeholder until lab execution |

## Evidence Policy

Evidence files in this directory should be generated from actual Kolla-Ansible and OpenStack operational validation once the lab is implemented.

Before implementation, this directory defines the expected evidence boundary only.
