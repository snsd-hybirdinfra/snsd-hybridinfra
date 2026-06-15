#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

source configs/backup-policy.env

BACKUP_ARCHIVE="$BACKUP_OUTPUT_DIR/$BACKUP_ARCHIVE_NAME"

mkdir -p "$RESTORE_OUTPUT_DIR"
mkdir -p runtime-workspace/logs
mkdir -p evidence/generated/raw

echo "[INFO] restore job started"

rm -rf "$RESTORE_OUTPUT_DIR"
mkdir -p "$RESTORE_OUTPUT_DIR"

tar -xzf "$BACKUP_ARCHIVE" -C "$RESTORE_OUTPUT_DIR"

{
  echo "# Restore Job Evidence"
  echo
  echo "backup_archive=$BACKUP_ARCHIVE"
  echo "restore_output_dir=$RESTORE_OUTPUT_DIR"
  echo
  echo "## Restored Files"
  find "$RESTORE_OUTPUT_DIR" -maxdepth 1 -type f -print | sort
} | tee runtime-workspace/logs/restore.log

cp runtime-workspace/logs/restore.log evidence/generated/raw/restore-job.log

echo "[INFO] restore job completed"