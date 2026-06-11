#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

source configs/backup-policy.env

mkdir -p runtime-workspace/logs
mkdir -p evidence/generated/raw
mkdir -p evidence/generated/summary

RAW_LOG="evidence/generated/raw/backup-recovery-validate.log"
SUMMARY="evidence/generated/summary/backup-recovery-execution-summary.md"

BACKUP_ARCHIVE="$BACKUP_OUTPUT_DIR/$BACKUP_ARCHIVE_NAME"
CHECKSUM_PATH="$BACKUP_OUTPUT_DIR/$CHECKSUM_FILE"

SOURCE_FILE_COUNT="0"
RESTORE_FILE_COUNT="0"

SOURCE_STATUS="CHECK"
BACKUP_ARCHIVE_STATUS="CHECK"
CHECKSUM_STATUS="CHECK"
RESTORE_STATUS="CHECK"
INTEGRITY_STATUS="CHECK"
MARKER_STATUS="CHECK"
OVERALL_STATUS="CHECK"

: > "$RAW_LOG"

echo "[INFO] backup recovery validation started"

{
  echo "# Backup Recovery Validation"
  echo
  echo "## Source State"
} | tee -a "$RAW_LOG"

if [ -d "$BACKUP_SOURCE_DIR" ]; then
  SOURCE_FILE_COUNT="$(find "$BACKUP_SOURCE_DIR" -type f -maxdepth 1 | wc -l | tr -d ' ')"
  echo "source_file_count=$SOURCE_FILE_COUNT" | tee -a "$RAW_LOG"
  if [ "$SOURCE_FILE_COUNT" -ge 3 ]; then
    SOURCE_STATUS="PASS"
  fi
fi

{
  echo
  echo "## Backup Archive"
} | tee -a "$RAW_LOG"

if [ -f "$BACKUP_ARCHIVE" ] && [ -s "$BACKUP_ARCHIVE" ]; then
  BACKUP_ARCHIVE_STATUS="PASS"
  ls -lh "$BACKUP_ARCHIVE" | tee -a "$RAW_LOG"
fi

{
  echo
  echo "## Checksum File"
} | tee -a "$RAW_LOG"

if [ -f "$CHECKSUM_PATH" ] && grep -q "app-config.txt" "$CHECKSUM_PATH"; then
  CHECKSUM_STATUS="PASS"
  cat "$CHECKSUM_PATH" | tee -a "$RAW_LOG"
fi

{
  echo
  echo "## Restore State"
} | tee -a "$RAW_LOG"

if [ -d "$RESTORE_OUTPUT_DIR" ]; then
  RESTORE_FILE_COUNT="$(find "$RESTORE_OUTPUT_DIR" -type f -maxdepth 1 | wc -l | tr -d ' ')"
  echo "restore_file_count=$RESTORE_FILE_COUNT" | tee -a "$RAW_LOG"

  if [ "$RESTORE_FILE_COUNT" -eq "$SOURCE_FILE_COUNT" ] && [ "$RESTORE_FILE_COUNT" -ge 3 ]; then
    RESTORE_STATUS="PASS"
  fi
fi

{
  echo
  echo "## Integrity Comparison"
} | tee -a "$RAW_LOG"

SOURCE_DIGEST="evidence/generated/raw/source-digest.sha256"
RESTORE_DIGEST="evidence/generated/raw/restore-digest.sha256"

find "$BACKUP_SOURCE_DIR" -type f -maxdepth 1 -print0 \
  | sort -z \
  | while IFS= read -r -d '' file; do
      sha256sum "$file" | sed "s#$BACKUP_SOURCE_DIR/##"
    done > "$SOURCE_DIGEST"

find "$RESTORE_OUTPUT_DIR" -type f -maxdepth 1 -print0 \
  | sort -z \
  | while IFS= read -r -d '' file; do
      sha256sum "$file" | sed "s#$RESTORE_OUTPUT_DIR/##"
    done > "$RESTORE_DIGEST"

cat "$SOURCE_DIGEST" | tee -a "$RAW_LOG"
cat "$RESTORE_DIGEST" | tee -a "$RAW_LOG"

if diff -u "$SOURCE_DIGEST" "$RESTORE_DIGEST" >> "$RAW_LOG"; then
  INTEGRITY_STATUS="PASS"
fi

{
  echo
  echo "## Marker Validation"
} | tee -a "$RAW_LOG"

if grep -R "$VALIDATION_MARKER" "$RESTORE_OUTPUT_DIR" > evidence/generated/raw/restore-marker-check.log; then
  MARKER_STATUS="PASS"
  cat evidence/generated/raw/restore-marker-check.log | tee -a "$RAW_LOG"
fi

if [ "$SOURCE_STATUS" = "PASS" ] &&
   [ "$BACKUP_ARCHIVE_STATUS" = "PASS" ] &&
   [ "$CHECKSUM_STATUS" = "PASS" ] &&
   [ "$RESTORE_STATUS" = "PASS" ] &&
   [ "$INTEGRITY_STATUS" = "PASS" ] &&
   [ "$MARKER_STATUS" = "PASS" ]; then
  OVERALL_STATUS="PASS"
fi

cat > "$SUMMARY" <<EOF
# Backup Recovery Execution Summary

Execution Mode: filesystem-backup-restore
Evidence Policy: local-only
Overall Status: $OVERALL_STATUS

## Validation Signals

| Signal | Status |
|---|---|
| Backup source files available | $SOURCE_STATUS |
| Backup archive created | $BACKUP_ARCHIVE_STATUS |
| Backup checksum generated | $CHECKSUM_STATUS |
| Restore files recovered | $RESTORE_STATUS |
| Restored data integrity validated | $INTEGRITY_STATUS |
| Validation marker restored | $MARKER_STATUS |

## Runtime Counters

| Counter | Value |
|---|---:|
| Source file count | $SOURCE_FILE_COUNT |
| Restore file count | $RESTORE_FILE_COUNT |

## Backup Artifacts

| Artifact | Path |
|---|---|
| Backup archive | $BACKUP_ARCHIVE |
| Checksum file | $CHECKSUM_PATH |

## Boundary

This summary records local-only runtime validation for the Backup Recovery Lab.
EOF

echo "[INFO] backup recovery validation completed"
echo "[INFO] overall_status=$OVERALL_STATUS"