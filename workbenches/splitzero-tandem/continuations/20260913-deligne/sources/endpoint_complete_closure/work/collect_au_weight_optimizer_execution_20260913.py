"""Recover completed original executions from their recorded command events."""
from pathlib import Path
import json, hashlib, re, datetime

W=Path(__file__).resolve().parent
SESSION=Path('local:user-profile/.codex/sessions/2026/09/13/rollout-2026-09-13T02-01-00-01a09811-387d-7f52-86c5-a8a27444046d.jsonl')
DEST=W/'au_weight_optimizer_execution_history_20260913'
DEST.mkdir(exist_ok=True)
def sha(data): return hashlib.sha256(data).hexdigest()
def pin(p):
    b=p.read_bytes(); return {'path':str(p),'bytes':len(b),'sha256':sha(b)}
events=[]
for line_number,line in enumerate(SESSION.read_bytes().splitlines(),1):
    if b'check_au_weight_optimizer_20260913.py' not in line: continue
    row=json.loads(line); payload=row.get('payload',{}); item=payload.get('item',{})
    if row.get('type')!='event_msg' or payload.get('type')!='item_completed' or item.get('type')!='CommandExecution': continue
    command=item.get('command',[])
    if not command or not re.search(r"python\.exe['\"]?\s+(?:-O\s+)?['\"]?work/check_au_weight_optimizer_20260913.py",command[-1]): continue
    # Keep exactly the execution event and raw emitted output, without unrelated session content.
    number=len(events)+1
    raw=DEST/f'command-{number:02}.event.json'
    raw.write_bytes(line+b'\n')
    stdout=DEST/f'command-{number:02}.stdout'; stderr=DEST/f'command-{number:02}.stderr'
    stdout.write_text(item.get('stdout',''),encoding='utf-8',newline='')
    stderr.write_text(item.get('stderr',''),encoding='utf-8',newline='')
    try: observed=json.loads(item.get('stdout',''))
    except json.JSONDecodeError: observed=None
    events.append({'session_line':line_number,'timestamp':row['timestamp'],
       'event':pin(raw),'command':command,'cwd':item.get('cwd'),
       'process_id':item.get('process_id'),'status':item.get('status'),
       'exit_code':item.get('exit_code'),'started_at_ms':payload.get('started_at_ms'),
       'completed_at_ms':payload.get('completed_at_ms'),'stdout':pin(stdout),'stderr':pin(stderr),
       'observed_result':observed})
current=[]
for p in sorted(W.glob('au_weight_optimizer_checks_*_20260913.json')):
    r=json.loads(p.read_text(encoding='utf-8'))
    candidates=[e for e in events if p.name in e['command'][-1] and e['observed_result'] and
       e['observed_result'].get('checks')==r['check_count'] and
       e['observed_result'].get('status')==r['status'] and e['observed_result'].get('failures')==r['failures']]
    current.append({'result':pin(p),'check_count':r['check_count'],'fault':r['fault'],
                    'optimized':r['optimized'],'failures':r['failures'],
                    'checker_sha256_matches':r['checker_sha256']==pin(W/'check_au_weight_optimizer_20260913.py')['sha256'],
                    'solver_sha256_matches':r['solver_sha256']==pin(W/'au_weight_optimizer_20260913.py')['sha256'],
                    'matching_actual_events':[e['event']['path'] for e in candidates]})
receipt={'schema':'au-optimizer-original-execution-recovery-v1',
 'collected_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'source_session':{'path':str(SESSION),'note':'Only listed completed command events were extracted; unrelated session material was not copied.'},
 'scope':'Read-only recovery of original completed executions. No mathematical checker was rerun.',
 'runtime_scope':'The recorded command names the concrete interpreter and -O switch; original results record __debug__. The historical events do not independently record Python or SymPy version strings.',
 'events':events,'current_results':current,
 'historical_counts':sorted(set(e['observed_result']['checks'] for e in events if e['observed_result']))}
(DEST/'EXECUTION.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'events':len(events),'counts':receipt['historical_counts'],'current_results':len(current),
 'unmatched':[r['result']['path'] for r in current if not r['matching_actual_events']],
 'events_summary':[{k:e[k] for k in ('timestamp','exit_code','observed_result')} for e in events]}))
if any(not r['matching_actual_events'] or not r['checker_sha256_matches'] or not r['solver_sha256_matches'] for r in current):
    raise RuntimeError('Unmatched current result or source hash')
