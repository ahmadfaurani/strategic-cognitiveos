# Heartbeat Notes

## ⛔ DO NOT RUN GATEWAY HEALTH CHECKS
**Gateway health monitoring is handled by the Hermes "Gateway Health Watchdog" no_agent cron job (every 15m).**
Do NOT run `journalctl`, `systemctl status`, or any exec pipeline to check gateway health during heartbeat.
This caused exec pipeline construction failures (mixed print/run steps) on 3 separate occasions.
The Hermes watchdog is silent when healthy and alerts to Telegram when broken. Your job is project continuity, not infrastructure monitoring.

## Last Check
- 2026-08-26 15:49 UTC (23:49 MYT Wed) — ✅ All clear. GLM-5.2 recovered from transient ECONNREFUSED at 14:49 UTC (~2s blip, fallback also failed, auto-recovered by 15:19). GLM-5.2 200 OK since. DeerFlow: 08:19 manual + 12:00 cron both SUCCESS. 0 memory pressure. Gate 4 (Aug 27) tomorrow, Gate 0 Roshdi (Aug 28) in 2 days.
- 2026-08-26 12:49 UTC (20:49 MYT Wed) — ✅ DeerFlow fix confirmed. 08:19 manual run: 664K chars, 25 sources, 441 intel score. 12:00 UTC cron auto-run: SUCCESS, 670K chars, 25 sources, 428 headlines, 483 intel score. Pipeline fully operational. 0 gateway errors, 0 memory pressure. Gate 4 (Aug 27) tomorrow, Gate 0 Roshdi (Aug 28) in 2 days.
- 2026-08-26 08:19 UTC (16:19 MYT Wed) — 🚨 FIXED: DeerFlow cron broken since Aug 20. Crontab used `.venv/bin/bash` (doesn't exist) → all 4 daily runs silently failing for 6 days. Fixed to `/bin/bash`. Manual test run started. 0 gateway errors, 0 memory pressure. Gate 4 (Aug 27) tomorrow, Gate 0 Roshdi (Aug 28) in 2 days.
- 2026-08-26 04:08 UTC (12:08 MYT Wed) — Quiet. 0 gateway errors, 0 memory pressure since last check. All 8 cron jobs healthy. Gate 4 (Aug 27) tomorrow, Gate 0 Roshdi (Aug 28) in 2 days. Nothing new.
