#!/bin/bash
# Workstream: Strategic CognitiveOS — CSCDC Partnership
# Repo: ahmadfaurani/strategic-cognitiveos
# Runs after: CJ-1 (every 6h), CJ-2 (every 12h), CJ-3 (daily 08:00), CJ-4 (every 12h), CJ-5 (daily 10:00), CJ-6 (every 12h), CJ-7 (weekly Mon 09:00)
# Updated: 2026-07-25 — Initial creation. 8 SCOS cronjobs total (7 LLM + 1 script-only).

set -e
WORKDIR="/home/p62operator/.openclaw/workspace/strategic-cognitiveos"
cd "$WORKDIR"

# STEP 1: Export cronjob configurations from Hermes internal state
python3 -c "
import json
try:
    with open('/home/p62operator/.hermes/cron/jobs.json') as f:
        data = json.load(f)
    jobs = data['jobs']
    scos_ids = [
        '95af59753d01',  # CJ-1: CSCDC Leadership & Approval Watch
        '0a0770f21820',  # CJ-2: PQC Sandbox & Sovereign AI Monitor
        'ee49690d9b66',  # CJ-3: Gov Infrastructure & Procurement Watch
        'bb5795421110',  # CJ-4: Anti-Deepfake & Campaign Strategy Watch
        'efb27cfe4011',  # CJ-5: Cyber Drill & Crisis Protocol Monitor
        '656efb0feade',  # CJ-6: CSCDC Programme & Community Champions Monitor
        'ed94da585cad',  # CJ-7: PIR Status Tracker
    ]
    scos_jobs = [j for j in jobs if j.get('id') in scos_ids]
    export = {
        'workstream': 'Strategic CognitiveOS — CSCDC Partnership',
        'exported_at': __import__('datetime').datetime.utcnow().isoformat() + 'Z',
        'repo': 'ahmadfaurani/strategic-cognitiveos',
        'workspace': '/home/p62operator/.openclaw/workspace/strategic-cognitiveos',
        'total_cronjobs': len(scos_jobs) + 1,  # +1 for this script-only job
        'cronjobs': []
    }
    for j in scos_jobs:
        m = j.get('model')
        model_name = m.get('model') if isinstance(m, dict) else None
        provider = m.get('provider') if isinstance(m, dict) else None
        sched = j.get('schedule', {})
        sched_display = sched.get('display', '?') if isinstance(sched, dict) else str(sched)
        export['cronjobs'].append({
            'id': j['id'],
            'name': j['name'],
            'schedule': sched_display,
            'deliver': j.get('deliver', '?'),
            'model': model_name or 'inherit (default)',
            'provider': provider or j.get('provider', 'inherit'),
            'enabled_toolsets': j.get('enabled_toolsets', 'all'),
            'workdir': j.get('workdir', 'default'),
            'enabled': j.get('enabled', True),
            'prompt': j.get('prompt', '')
        })
    # Add this script-only job
    export['cronjobs'].append({
        'id': 'script-only',
        'name': 'Strategic CognitiveOS Git Sync',
        'schedule': '0 11 * * *',
        'deliver': 'local',
        'model': 'N/A (script-only)',
        'provider': 'N/A',
        'enabled_toolsets': ['terminal'],
        'workdir': '/home/p62operator/.openclaw/workspace/strategic-cognitiveos',
        'enabled': True,
        'prompt': ''
    })
    import os
    os.makedirs('/home/p62operator/.openclaw/workspace/strategic-cognitiveos/05-TOOLS-AND-AUTOMATION', exist_ok=True)
    with open('/home/p62operator/.openclaw/workspace/strategic-cognitiveos/05-TOOLS-AND-AUTOMATION/cronjob-configs.json', 'w') as f:
        json.dump(export, f, indent=2, ensure_ascii=False)
    print(f'Exported {len(scos_jobs) + 1} cronjob configs')
except Exception as e:
    print(f'Config export skipped: {e}')
"

# STEP 2: Git sync
TIMESTAMP=$(date -u +%Y-%m-%dT%H:%M:%SZ)
CHANGES=$(git status --porcelain | wc -l)

if [ "$CHANGES" -gt 0 ]; then
    git add -A
    git commit -m "auto: strategic-cognitiveos git-sync $TIMESTAMP"
    git push origin main 2>&1 && echo "✅ Pushed $CHANGES files to strategic-cognitiveos" || echo "⚠️ Committed locally, push deferred (auth pending)"
else
    echo "No changes to sync — strategic-cognitiveos"
fi
