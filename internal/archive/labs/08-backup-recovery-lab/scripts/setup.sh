#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

source configs/backup-policy.env

mkdir -p "$BACKUP_SOURCE_DIR"
mkdir -p "$BACKUP_OUTPUT_DIR"
mkdir -p "$RESTORE_OUTPUT_DIR"
mkdir -p runtime-workspace/logs
mkdir -p evidence/generated/raw
mkdir -p evidence/generated/summary

echo "[INFO] backup recovery setup started"

cat > "$BACKUP_SOURCE_DIR/app-config.txt" <<EOF
service_name=snsd-backup-recovery-lab
environment=local-runtime
validation_marker=$VALIDATION_MARKER
EOF

cat > "$BACKUP_SOURCE_DIR/runtime-state.txt" <<EOF
state=healthy
node=local-backup-target
backup_policy=filesystem-archive
validation_marker=$VALIDATION_MARKER
EOF

cat > "$BACKUP_SOURCE_DIR/operational-events.log" <<EOF
2026-06-11T10:00:00Z event=backup_source_created status=ready marker=$VALIDATION_MARKER
2026-06-11T10:01:00Z event=backup_policy_loaded status=ready marker=$VALIDATION_MARKER
EOF

{
  echo "# Backup Recovery Setup"
  echo
  echo "source_dir=$BACKUP_SOURCE_DIR"
  echo "backup_output_dir=$BACKUP_OUTPUT_DIR"
  echo "restore_output_dir=$RESTORE_OUTPUT_DIR"
  echo
  echo "## Source Files"
  find "$BACKUP_SOURCE_DIR" -maxdepth 1 -type f -print | sort
} | tee runtime-workspace/logs/setup.log

cp runtime-workspace/logs/setup.log evidence/generated/raw/backup-recovery-setup.log

echo "[INFO] backup recovery setup completed"