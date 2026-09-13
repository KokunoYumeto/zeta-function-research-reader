from pathlib import Path
import subprocess,sys,json,hashlib,datetime
W=Path(__file__).resolve().parent
script=W/'gamma_phase_fibre_transport_check_20260913.py'
proof=W/'gamma_phase_fibre_transport_20260913.tex'
out=W/'gamma_phase_fibre_transport_checks_20260913'
out.mkdir(exist_ok=True)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
rows=[]
for optimized in [False,True]:
    for fault in [None,'phase','mass','relative']:
        name=('optimized' if optimized else 'normal')+('-'+fault if fault else '')
        dest=out/(name+'.json')
        command=[sys.executable,'-B']+(['-O'] if optimized else [])+[str(script),'--output',str(dest)]+(['--fault',fault] if fault else [])
        start=datetime.datetime.now(datetime.timezone.utc).isoformat()
        run=subprocess.run(command,capture_output=True)
        log=out/(name+'.log');log.write_bytes(run.stdout+b'\nSTDERR\n'+run.stderr)
        data=json.loads(dest.read_text(encoding='utf-8'))
        expected=1 if fault else 0
        accepted=run.returncode==expected and data['optimized_python']==optimized and data['checks']==61 and ((data['failed']>0)==bool(fault))
        rows.append({'name':name,'command':command,'started_utc':start,'returncode':run.returncode,'expected_returncode':expected,'checks':data['checks'],'failed':data['failed'],'accepted':accepted,'result':str(dest),'result_sha256':sha(dest),'log':str(log),'log_sha256':sha(log),'proof_sha256':sha(proof),'script_sha256':sha(script)})
        if not accepted:raise RuntimeError(rows[-1])
receipt={'schema':'gamma-phase-actual-execution-v1','runs':rows,'all_expected_outcomes':all(r['accepted'] for r in rows),'runner_sha256':sha(Path(__file__)),'scope':'61 finite exact checks each mode; three mathematical formula mutations run the complete suite and fail both modes. Not an analytic zeta certificate.'}
(out/'replay_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'runs':len(rows),'all_expected':True,'checks_per_run':61,'failures':{r['name']:r['failed'] for r in rows}}))
