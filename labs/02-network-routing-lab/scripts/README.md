# Network Routing Lab Scripts

This directory contains lab-local execution entrypoints for the Network Routing Lab.

## Script Roles

| Script | Purpose |
|---|---|
| setup.sh | Prepare routing lab prerequisites |
| validate.sh | Execute routing, reachability, DNS, VPN, and latency validation checks |
| cleanup.sh | Clean temporary routing lab execution outputs |

## Execution Boundary

These scripts belong only to:

labs/02-network-routing-lab/

They are intended to coordinate lab-local modules, adapters, shared runtime utilities, and evidence generation workflows.

## Future Implementation

Future implementation may include:

- Linux routing node preparation
- FRR installation and configuration
- interface and route table validation
- endpoint reachability checks
- DNS resolution checks
- VPN tunnel checks
- latency and packet loss checks
- route failure and recovery checks
- evidence generation
