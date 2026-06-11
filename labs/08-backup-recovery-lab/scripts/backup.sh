#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

source configs/backup-policy.env

mkdir -p "$BACKUP_OUTPUT_DIR"
mkdir -p runtime-workspace/logs
mkdir -p evidence/generated/raw

BACKUP_ARCHIVE="$BACKUP_OUTPUT_DIR/$BACKUP_ARCHIVE_NAME"
CHECKSUM_PATH="$BACKUP_OUTPUT_DIR/$CHECKSUM_FILE"

echo "[INFO] backup job started"

tar -czf "$BACKUP_ARCHIVE" -C "$BACKUP_SOURCE_DIR" .

find "$BACKUP_SOURCE_DIR" -type f -maxdepth 1 -print0 \
  | sort -z \
  | xargs -0 sha256sum > "$CHECKSUM_PATH"

{
  echo "# Backup Job Evidence"
  echo
  echo "backup_archive=$BACKUP_ARCHIVE"
  echo "checksum_file=$CHECKSUM_PATH"
  echo
  echo "## Backup Archive"
  ls -lh "$BACKUP_ARCHIVE"
  echo
  echo "## Source Checksums"
  cat "$CHECKSUM_PATH"
} | tee runtime-workspace/logs/backup.log

cp runtime-workspace/logs/backup.log evidence/generated/raw/backup-job.log

echo "[INFO] backup job completed"