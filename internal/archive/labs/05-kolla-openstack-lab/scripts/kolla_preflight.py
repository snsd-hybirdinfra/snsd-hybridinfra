#!/usr/bin/env python3
from pathlib import Path
import os
import re
import shutil
import subprocess

BASE = Path(__file__).resolve().parents[1]
RAW_DIR = BASE / "evidence" / "generated" / "raw"
SUMMARY_DIR = BASE / "evidence" / "generated" / "summary"

RAW_DIR.mkdir(parents=True, exist_ok=True)
SUMMARY_DIR.mkdir(parents=True, exist_ok=True)

POLICY = BASE / "configs" / "kolla-lab-policy.env"
GLOBALS = BASE / "configs" / "globals.yml"
INVENTORY = BASE / "inventory" / "multinode.ini"

RAW_REPORT = RAW_DIR / "kolla-preflight-raw.txt"
SUMMARY = SUMMARY_DIR / "kolla-openstack-execution-summary.md"

REQUIRED_POLICY_KEYS = [
    "KOLLA_MODE",
    "KOLLA_TARGET_MODEL",
    "KOLLA_BASE_DISTRO",
    "KOLLA_INSTALL_TYPE",
    "KOLLA_INTERNAL_VIP_ADDRESS",
    "KOLLA_NETWORK_INTERFACE",
    "KOLLA_NEUTRON_EXTERNAL_INTERFACE",
    "VALIDATION_MARKER",
]

REQUIRED_GLOBAL_KEYS = [
    "kolla_base_distro",
    "kolla_install_type",
    "openstack_release",
    "kolla_internal_vip_address",
    "network_interface",
    "neutron_external_interface",
    "enable_prometheus",
    "enable_grafana",
]

REQUIRED_INVENTORY_GROUPS = [
    "control",
    "network",
    "compute",
    "monitoring",
    "storage",
    "deployment",
]

def read_text(path):
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""

def parse_env(path):
    values = {}
    for line in read_text(path).splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        values[key.strip()] = value.strip()
    return values

def command_available(name):
    return shutil.which(name) is not None

def main():
    raw_lines = ["# Kolla OpenStack Preflight Raw Report", ""]

    policy_values = parse_env(POLICY)
    policy_status = "PASS" if all(key in policy_values for key in REQUIRED_POLICY_KEYS) else "CHECK"

    globals_text = read_text(GLOBALS)
    globals_status = "PASS" if all(re.search(rf"^{key}:", globals_text, re.MULTILINE) for key in REQUIRED_GLOBAL_KEYS) else "CHECK"

    inventory_text = read_text(INVENTORY)
    inventory_status = "PASS" if all(f"[{group}]" in inventory_text for group in REQUIRED_INVENTORY_GROUPS) else "CHECK"

    marker_status = "PASS" if "SNSD_KOLLA_OPENSTACK_PREFLIGHT_VALIDATION_MARKER" in policy_values.get("VALIDATION_MARKER", "") else "CHECK"

    python_status = "PASS" if command_available("python3") else "CHECK"
    ansible_status = "PASS" if command_available("ansible") else "CHECK"
    docker_status = "PASS" if command_available("docker") else "CHECK"

    kolla_command_status = "PASS" if command_available("kolla-ansible") else "OPTIONAL"

    vip = policy_values.get("KOLLA_INTERNAL_VIP_ADDRESS", "")
    vip_status = "PASS" if re.match(r"^\d+\.\d+\.\d+\.\d+$", vip) else "CHECK"

    raw_lines.extend([
        "## Policy",
        f"policy_file={POLICY}",
        f"policy_status={policy_status}",
        f"target_model={policy_values.get('KOLLA_TARGET_MODEL', 'unknown')}",
        f"validation_marker={policy_values.get('VALIDATION_MARKER', 'missing')}",
        "",
        "## Globals",
        f"globals_file={GLOBALS}",
        f"globals_status={globals_status}",
        "",
        "## Inventory",
        f"inventory_file={INVENTORY}",
        f"inventory_status={inventory_status}",
        "",
        "## Local Commands",
        f"python3={python_status}",
        f"ansible={ansible_status}",
        f"docker={docker_status}",
        f"kolla-ansible={kolla_command_status}",
        "",
    ])

    statuses_for_overall = [
        policy_status,
        globals_status,
        inventory_status,
        marker_status,
        python_status,
        ansible_status,
        docker_status,
        vip_status,
    ]

    overall_status = "PASS" if all(status == "PASS" for status in statuses_for_overall) else "CHECK"

    RAW_REPORT.write_text("\n".join(raw_lines) + "\n", encoding="utf-8")

    summary_lines = [
        "# Kolla OpenStack Execution Summary",
        "",
        "Execution Mode: kolla-ansible-preflight-validation",
        "Evidence Policy: local-only",
        f"Overall Status: {overall_status}",
        "",
        "## Validation Signals",
        "",
        "| Signal | Status |",
        "|---|---|",
        f"| Kolla lab policy available | {policy_status} |",
        f"| Kolla globals configuration available | {globals_status} |",
        f"| Kolla inventory model available | {inventory_status} |",
        f"| Internal VIP address format valid | {vip_status} |",
        f"| Validation marker present | {marker_status} |",
        f"| Python runtime available | {python_status} |",
        f"| Ansible command available | {ansible_status} |",
        f"| Docker command available | {docker_status} |",
        f"| kolla-ansible command available | {kolla_command_status} |",
        "",
        "## Kolla Target Model",
        "",
        "| Field | Value |",
        "|---|---|",
        f"| Mode | {policy_values.get('KOLLA_MODE', 'unknown')} |",
        f"| Target model | {policy_values.get('KOLLA_TARGET_MODEL', 'unknown')} |",
        f"| Base distro | {policy_values.get('KOLLA_BASE_DISTRO', 'unknown')} |",
        f"| Install type | {policy_values.get('KOLLA_INSTALL_TYPE', 'unknown')} |",
        f"| Internal VIP | {policy_values.get('KOLLA_INTERNAL_VIP_ADDRESS', 'unknown')} |",
        "",
        "## Boundary",
        "",
        "This summary records local-only preflight validation for the Kolla OpenStack Lab.",
        "",
        "Full OpenStack deployment is intentionally outside this first execution boundary.",
    ]

    SUMMARY.write_text("\n".join(summary_lines) + "\n", encoding="utf-8")

    print(f"[INFO] policy_status={policy_status}")
    print(f"[INFO] globals_status={globals_status}")
    print(f"[INFO] inventory_status={inventory_status}")
    print(f"[INFO] overall_status={overall_status}")
    print(f"[INFO] summary={SUMMARY}")

if __name__ == "__main__":
    main()