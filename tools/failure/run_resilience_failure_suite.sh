#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
INVENTORY="${REPO_ROOT}/inventory/lab/hosts.ini"
EVIDENCE_DIR="${REPO_ROOT}/labs/evidence/generated"
SUITE_SUMMARY="${EVIDENCE_DIR}/resilience-failure-suite-summary.md"
MODE="${1:-run}"

cd "${REPO_ROOT}"
mkdir -p "${EVIDENCE_DIR}"

print_header() {
  local title="${1:-SNSD Resilience Failure Suite}"

  echo
  echo "============================================================"
  echo "${title}"
  echo "============================================================"
}

check_file_exists() {
  local file="${1:?file path required}"

  if [ -f "${file}" ]; then
    echo "[PASS] ${file}"
  else
    echo "[FAIL] ${file} missing"
    return 1
  fi
}

write_summary_header() {
  cat > "${SUITE_SUMMARY}" <<SUMMARY
# Resilience Failure Suite Summary

Generated At: $(date '+%Y-%m-%d %H:%M:%S %Z %z')

Repository: ${REPO_ROOT}
Inventory: ${INVENTORY}

## Suite Scope

- Web backend failure and recovery
- Observability loss and recovery
- Database failure and recovery
- Proxy entrypoint failure and recovery
- Backup failure and recovery validation

## Execution Log

SUMMARY
}

append_summary_result() {
  local title="${1:?title required}"
  local playbook="${2:?playbook required}"
  local result="${3:?result required}"

  {
    echo
    echo "### ${title}"
    echo
    echo "- Playbook: ansible/playbooks/${playbook}"
    echo "- Result: ${result}"
    echo "- Finished At: $(date '+%Y-%m-%d %H:%M:%S %Z %z')"
  } >> "${SUITE_SUMMARY}"
}

run_failure_playbook() {
  local playbook="${1:?playbook required}"
  local title="${2:?title required}"

  print_header "[FAILURE TEST] ${title}"
  echo "playbook=ansible/playbooks/${playbook}"
  echo "started_at=$(date '+%Y-%m-%d %H:%M:%S %Z %z')"

  if ansible-playbook -i "${INVENTORY}" "ansible/playbooks/${playbook}"; then
    append_summary_result "${title}" "${playbook}" "PASS"
  else
    append_summary_result "${title}" "${playbook}" "FAIL"
    return 1
  fi

  echo
  echo "[OK] ${title}"
  echo "finished_at=$(date '+%Y-%m-%d %H:%M:%S %Z %z')"
}

precheck_only() {
  print_header "SNSD Resilience Failure Suite Precheck"
  echo "repo=${REPO_ROOT}"
  echo "inventory=${INVENTORY}"
  echo "checked_at=$(date '+%Y-%m-%d %H:%M:%S %Z %z')"

  print_header "Check failure playbook files"
  check_file_exists "ansible/playbooks/21-failure-injection-web-recovery.yml"
  check_file_exists "ansible/playbooks/22-failure-injection-observability-loss.yml"
  check_file_exists "ansible/playbooks/23-failure-injection-database-recovery.yml"
  check_file_exists "ansible/playbooks/24-failure-injection-proxy-recovery.yml"
  check_file_exists "ansible/playbooks/25-failure-injection-backup-recovery.yml"

  print_header "Check Ansible connectivity"
  ansible -i "${INVENTORY}" ubuntu_nodes -m ping

  print_header "Check runtime smoke status"
  tools/validation/runtime_smoke_check.sh

  print_header "Check monitoring APIs"
  curl -fsS http://192.168.1.40:9090/-/healthy >/dev/null
  echo "[PASS] Prometheus healthy"

  curl -fsS http://192.168.1.40:9093/-/healthy >/dev/null
  echo "[PASS] Alertmanager healthy"

  echo
  echo "[OK] resilience failure suite precheck passed"
}

run_suite() {
  write_summary_header

  print_header "SNSD Resilience Failure Suite"
  echo "repo=${REPO_ROOT}"
  echo "inventory=${INVENTORY}"
  echo "started_at=$(date '+%Y-%m-%d %H:%M:%S %Z %z')"

  print_header "Precheck: runtime smoke check"
  tools/validation/runtime_smoke_check.sh

  run_failure_playbook "21-failure-injection-web-recovery.yml" "Web backend failure and recovery"
  run_failure_playbook "22-failure-injection-observability-loss.yml" "Observability loss and recovery"
  run_failure_playbook "23-failure-injection-database-recovery.yml" "Database failure and recovery"
  run_failure_playbook "24-failure-injection-proxy-recovery.yml" "Proxy entrypoint failure and recovery"
  run_failure_playbook "25-failure-injection-backup-recovery.yml" "Backup failure and recovery validation"

  print_header "Postcheck: runtime smoke check"
  tools/validation/runtime_smoke_check.sh

  print_header "Refresh runtime validation evidence"
  tools/pipeline/run_runtime_validation_pipeline.sh

  {
    echo
    echo "## Final Result"
    echo
    echo "- Result: PASS"
    echo "- Finished At: $(date '+%Y-%m-%d %H:%M:%S %Z %z')"
    echo "- Runtime Evidence Refreshed: yes"
  } >> "${SUITE_SUMMARY}"

  print_header "Resilience Failure Suite Summary"
  echo "finished_at=$(date '+%Y-%m-%d %H:%M:%S %Z %z')"
  echo "[OK] resilience failure suite completed"
  echo "[OK] suite_summary=${SUITE_SUMMARY}"
}

case "${MODE}" in
  run)
    run_suite
    ;;
  --precheck-only)
    precheck_only
    ;;
  -h|--help)
    echo "Usage:"
    echo "  tools/failure/run_resilience_failure_suite.sh"
    echo "  tools/failure/run_resilience_failure_suite.sh --precheck-only"
    ;;
  *)
    echo "[FAIL] unknown option: ${MODE}"
    echo "Usage:"
    echo "  tools/failure/run_resilience_failure_suite.sh"
    echo "  tools/failure/run_resilience_failure_suite.sh --precheck-only"
    exit 1
    ;;
esac
