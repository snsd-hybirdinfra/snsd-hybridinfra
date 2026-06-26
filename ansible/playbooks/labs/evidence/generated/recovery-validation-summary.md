# Recovery Validation Summary

Generated At: 2026-06-26 17:18:00 KST +0900

## Backup / Restore Metrics

```text
# HELP node_textfile_mtime_seconds Unixtime mtime of textfiles successfully read.
# TYPE node_textfile_mtime_seconds gauge
node_textfile_mtime_seconds{file="/var/lib/node_exporter/textfile_collector/snsd_backup.prom"} 1.782461113e+09
node_textfile_mtime_seconds{file="/var/lib/node_exporter/textfile_collector/snsd_restore.prom"} 1.782455809e+09
# HELP node_textfile_scrape_error 1 if there was an error opening or reading a file, 0 otherwise
# TYPE node_textfile_scrape_error gauge
node_textfile_scrape_error 0
# HELP snsd_backup_last_duration_seconds Backup duration in seconds.
# TYPE snsd_backup_last_duration_seconds gauge
snsd_backup_last_duration_seconds 2
# HELP snsd_backup_last_run_timestamp_seconds Last backup run timestamp.
# TYPE snsd_backup_last_run_timestamp_seconds gauge
snsd_backup_last_run_timestamp_seconds 1.782461113e+09
# HELP snsd_backup_last_success Backup success status. 1 means success, 0 means failure.
# TYPE snsd_backup_last_success gauge
snsd_backup_last_success 1
# HELP snsd_backup_snapshot_count Restic snapshot count.
# TYPE snsd_backup_snapshot_count gauge
snsd_backup_snapshot_count 9
# HELP snsd_restore_validation_duration_seconds Restore validation duration in seconds.
# TYPE snsd_restore_validation_duration_seconds gauge
snsd_restore_validation_duration_seconds 1
# HELP snsd_restore_validation_last_run_timestamp_seconds Last restore validation timestamp.
# TYPE snsd_restore_validation_last_run_timestamp_seconds gauge
snsd_restore_validation_last_run_timestamp_seconds 1.782455809e+09
# HELP snsd_restore_validation_success Restore validation success status. 1 means success, 0 means failure.
# TYPE snsd_restore_validation_success gauge
snsd_restore_validation_success 1
```

## HAProxy / Probe Continuity

```text
## HAProxy Frontend
  <p>hostname: app-node-02</p>
  <p>status: healthy</p>

## Backend Direct Checks
  <p>hostname: app-node-01</p>
  <p>status: healthy</p>

  <p>hostname: app-node-02</p>
  <p>status: healthy</p>

## Blackbox Probe Success
# HELP probe_success Displays whether or not the probe was a success
# TYPE probe_success gauge
probe_success 1
# HELP probe_success Displays whether or not the probe was a success
# TYPE probe_success gauge
probe_success 1
```
