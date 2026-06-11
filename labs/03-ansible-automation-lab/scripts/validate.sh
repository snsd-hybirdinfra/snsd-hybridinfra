#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

mkdir -p runtime-workspace/logs
mkdir -p evidence/generated/raw
mkdir -p evidence/generated/summary

RAW_LOG="evidence/generated/raw/ansible-validate.log"
SUMMARY="evidence/generated/summary/ansible-automation-execution-summary.md"

TARGET_GROUP="ansible_automation_targets"
MARKER_FILE="/tmp/snsd-ansible-automation-lab/automation-marker.txt"
PACKAGE_NAME="curl"
SERVICE_NAME="cron"

SSH_STATUS="CHECK"
PLAYBOOK_STATUS="CHECK"
MARKER_STATUS="CHECK"
PACKAGE_STATUS="CHECK"
SERVICE_STATUS="CHECK"
OVERALL_STATUS="CHECK"
FAILED_COUNT="0"

echo "[INFO] ansible automation validation started"

: > "$RAW_LOG"

{
  echo "# Ansible Automation Validation"
  echo
  echo "## SSH Connectivity"
} | tee -a "$RAW_LOG"

if ansible "$TARGET_GROUP" -m ping | tee -a "$RAW_LOG"; then
  SSH_STATUS="PASS"
fi

{
  echo
  echo "## Validation Playbook"
} | tee -a "$RAW_LOG"

if ansible-playbook playbooks/validate.yml | tee -a "$RAW_LOG"; then
  PLAYBOOK_STATUS="PASS"
fi

{
  echo
  echo "## Direct Marker File Check"
} | tee -a "$RAW_LOG"

if ansible "$TARGET_GROUP" -b -m command -a "grep -q 'Managed By: Ansible' $MARKER_FILE" | tee -a "$RAW_LOG"; then
  MARKER_STATUS="PASS"
fi

{
  echo
  echo "## Direct Package Check"
} | tee -a "$RAW_LOG"

if ansible "$TARGET_GROUP" -b -m command -a "dpkg -s $PACKAGE_NAME" | tee -a "$RAW_LOG"; then
  PACKAGE_STATUS="PASS"
fi

{
  echo
  echo "## Direct Service Check"
} | tee -a "$RAW_LOG"

if ansible "$TARGET_GROUP" -b -m command -a "systemctl is-active $SERVICE_NAME" | tee -a "$RAW_LOG"; then
  SERVICE_STATUS="PASS"
fi

FAILED_COUNT="$(grep -Ec "failed=[1-9]|unreachable=[1-9]|UNREACHABLE|FAILED" "$RAW_LOG" || true)"

if [ "$SSH_STATUS" = "PASS" ] &&
   [ "$PLAYBOOK_STATUS" = "PASS" ] &&
   [ "$MARKER_STATUS" = "PASS" ] &&
   [ "$PACKAGE_STATUS" = "PASS" ] &&
   [ "$SERVICE_STATUS" = "PASS" ] &&
   [ "$FAILED_COUNT" -eq 0 ]; then
  OVERALL_STATUS="PASS"
fi

cat > "$SUMMARY" <<EOF
# Ansible Automation Execution Summary

Execution Mode: ansible-playbook
Evidence Policy: local-only
Overall Status: $OVERALL_STATUS

## Validation Signals

| Signal | Status |
|---|---|
| SSH connectivity to automation targets | $SSH_STATUS |
| Playbook execution completed | $PLAYBOOK_STATUS |
| Managed marker file validated | $MARKER_STATUS |
| Managed package validated | $PACKAGE_STATUS |
| Managed service validated | $SERVICE_STATUS |
| Failed or unreachable hosts | $FAILED_COUNT |

## Target Model

| Target | Role |
|---|---|
| linux-node-01 | automation target |
| linux-node-02 | automation target |

## Boundary

This summary records local-only runtime validation for the Ansible Automation Lab.
EOF

echo "[INFO] ansible automation validation completed"
echo "[INFO] overall_status=$OVERALL_STATUS"
echo "[INFO] ssh_status=$SSH_STATUS"
echo "[INFO] playbook_status=$PLAYBOOK_STATUS"
echo "[INFO] marker_status=$MARKER_STATUS"
echo "[INFO] package_status=$PACKAGE_STATUS"
echo "[INFO] service_status=$SERVICE_STATUS"
echo "[INFO] failed_count=$FAILED_COUNT"