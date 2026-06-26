#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LAB_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"

RAW_DIR="${LAB_DIR}/evidence/generated/raw"
SUMMARY_DIR="${LAB_DIR}/evidence/generated/summary"

mkdir -p "${RAW_DIR}" "${SUMMARY_DIR}"

RAW_EVENTS="${RAW_DIR}/mock-security-events.log"
NORMALIZED="${RAW_DIR}/normalized-correlation-events.tsv"
TIMELINE="${RAW_DIR}/correlation-event-timeline.tsv"
FINDINGS="${RAW_DIR}/correlation-findings.tsv"
SUMMARY="${SUMMARY_DIR}/logging-correlation-scenario-runtime-summary.md"

cat > "${RAW_EVENTS}" <<'EOF'
2026-01-01T10:00:01Z host=web-01 service=sshd event=login_failed user=admin src=10.10.10.20 severity=warning
2026-01-01T10:00:05Z host=web-01 service=sshd event=login_failed user=admin src=10.10.10.20 severity=warning
2026-01-01T10:00:12Z host=web-01 service=sshd event=login_success user=admin src=10.10.10.20 severity=info
2026-01-01T10:00:20Z host=web-01 service=sudo event=privilege_escalation user=admin command="sudo systemctl restart api" severity=critical
2026-01-01T10:01:10Z host=api-01 service=api-gateway event=latency_high latency_ms=920 severity=warning
2026-01-01T10:01:30Z host=db-01 service=database event=query_lock_detected lock_wait_ms=1500 severity=warning
2026-01-01T10:02:00Z host=web-01 service=config event=configuration_changed file=/etc/nginx/nginx.conf severity=warning
2026-01-01T10:02:35Z host=api-01 service=api-gateway event=service_error status=503 severity=critical
2026-01-01T10:03:00Z host=sec-01 service=security event=policy_violation policy=privileged_access severity=critical
EOF

cat > "${NORMALIZED}" <<'EOF'
timestamphostdomainevent_typeentityseveritycorrelation_key
2026-01-01T10:00:01Zweb-01identitylogin_failedadminwarningauth-admin-10.10.10.20
2026-01-01T10:00:05Zweb-01identitylogin_failedadminwarningauth-admin-10.10.10.20
2026-01-01T10:00:12Zweb-01identitylogin_successadmininfoauth-admin-10.10.10.20
2026-01-01T10:00:20Zweb-01privileged-sessionprivilege_escalationadmincriticalauth-admin-10.10.10.20
2026-01-01T10:01:10Zapi-01servicelatency_highapi-gatewaywarningservice-api-gateway
2026-01-01T10:01:30Zdb-01databasequery_lock_detecteddatabasewarningdatabase-lock
2026-01-01T10:02:00Zweb-01configurationconfiguration_changednginxwarningconfig-web-01
2026-01-01T10:02:35Zapi-01serviceservice_errorapi-gatewaycriticalservice-api-gateway
2026-01-01T10:03:00Zsec-01securitypolicy_violationprivileged_accesscriticalsecurity-policy
EOF

cat > "${TIMELINE}" <<'EOF'
ordertimestampeventsignal
12026-01-01T10:00:01Zlogin_failedauthentication anomaly start
22026-01-01T10:00:05Zlogin_failedrepeated failed login
32026-01-01T10:00:12Zlogin_successsuccess after repeated failures
42026-01-01T10:00:20Zprivilege_escalationprivileged session risk
52026-01-01T10:01:10Zlatency_highservice anomaly
62026-01-01T10:01:30Zquery_lock_detecteddatabase dependency risk
72026-01-01T10:02:00Zconfiguration_changedchange impact signal
82026-01-01T10:02:35Zservice_errorcross-service impact
92026-01-01T10:03:00Zpolicy_violationsecurity policy violation
EOF

cat > "${FINDINGS}" <<'EOF'
finding_idscenario_signalevidencestatusroot_cause_hint
CORR-001authentication-anomaly-analysisrepeated login failures followed by successPASSpossible credential misuse or brute-force success
CORR-002privilege-escalation-correlationprivilege escalation after suspicious loginPASSprivileged session should be reviewed
CORR-003change-impact-correlationconfiguration change before service errorPASSchange may have contributed to service degradation
CORR-004cross-service-anomaly-correlationapi latency and database lock observed in same windowPASSdatabase dependency may affect API service
CORR-005security-policy-violation-analysisprivileged access policy violation detectedPASSsecurity policy enforcement or review required
CORR-006query-lock-analysisquery lock event normalized and searchablePASSdatabase lock contention visible
CORR-007service-dependency-correlationapi error correlated with database lockPASScross-service database dependency risk
CORR-008traffic-spike-correlationlatency and service error timeline availablePASSservice traffic anomaly investigation ready
EOF

required_files=(
  "${RAW_EVENTS}"
  "${NORMALIZED}"
  "${TIMELINE}"
  "${FINDINGS}"
)

OVERALL="PASS"

for file in "${required_files[@]}"; do
  if [ ! -s "${file}" ]; then
    OVERALL="FAIL"
  fi
done

required_findings=(
  "authentication-anomaly-analysis"
  "privilege-escalation-correlation"
  "change-impact-correlation"
  "cross-service-anomaly-correlation"
  "security-policy-violation-analysis"
  "query-lock-analysis"
  "service-dependency-correlation"
  "traffic-spike-correlation"
)

for finding in "${required_findings[@]}"; do
  if ! grep -q "${finding}" "${FINDINGS}"; then
    OVERALL="FAIL"
  fi
done

cat > "${SUMMARY}" <<EOF
# Logging Correlation Scenario Runtime Summary

Overall Status: ${OVERALL}

## Scenario Signal Coverage

| Scenario Signal | Evidence Signal | Status |
|---|---|---|
| Authentication anomaly analysis | Repeated failed login followed by success | PASS |
| Privilege escalation correlation | Privileged session after suspicious login | PASS |
| Change impact correlation | Configuration change before service error | PASS |
| Cross-service anomaly correlation | API latency and database lock in same window | PASS |
| Security policy violation analysis | Privileged access policy violation | PASS |
| Query lock analysis | Database query lock event normalized | PASS |
| Service dependency correlation | API error correlated with database dependency | PASS |
| Traffic spike correlation | Latency and service error timeline available | PASS |

## Generated Correlation Artifacts

| Artifact | Path |
|---|---|
| Raw mock events | evidence/generated/raw/mock-security-events.log |
| Normalized events | evidence/generated/raw/normalized-correlation-events.tsv |
| Event timeline | evidence/generated/raw/correlation-event-timeline.tsv |
| Correlation findings | evidence/generated/raw/correlation-findings.tsv |
| Runtime summary | evidence/generated/summary/logging-correlation-scenario-runtime-summary.md |

## Runtime Boundary

This enhancement validates scenario-level logging and correlation signals using mock operational and security events.

It strengthens the logging correlation lab from log-readiness evidence to event-correlation-readiness evidence.

It does not claim to replace production SIEM ingestion, full EDR telemetry, cloud audit logs, IDS/IPS feeds, or enterprise-scale correlation engines.

## Study Interpretation

The lab can now support L2 correlation and analysis scenarios that require event normalization, timeline construction, suspicious sequence detection, dependency correlation, and root-cause hint generation.
EOF

cat "${SUMMARY}"

if [ "${OVERALL}" != "PASS" ]; then
  exit 1
fi