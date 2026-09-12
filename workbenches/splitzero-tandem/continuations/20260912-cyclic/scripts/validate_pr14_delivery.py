"""Reproduce untouched PR14 source checks and fresh tensor transport checks."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
STAGE = ROOT / 'sources/web_pr14_delivery'
SOURCE = STAGE / 'Tau_Coherent_Interpolation_Control'
OUT = ROOT / 'checks/pr14_fresh'
OUT.mkdir(parents=True, exist_ok=True)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    provenance = json.loads((STAGE/'LOCAL_STAGING_PROVENANCE.json').read_text(encoding='utf-8-sig'))
    verified = []
    for row in provenance['files']:
        path = STAGE / row['archive_entry']
        if sha(path) != row['sha256']:
            raise RuntimeError('Staged source changed: '+row['archive_entry'])
        verified.append(row['archive_entry'])
    archive = Path(provenance['archive'])
    if sha(archive) != provenance['archive_sha256']:
        raise RuntimeError('Original archive changed')
    runs = []
    for name, optimized, failure in [('normal',False,False),('optimized',True,False),
                                     ('negative-normal',False,True),('negative-optimized',True,True)]:
        report = OUT/(name+'.json')
        command = [sys.executable]+(['-O'] if optimized else [])+[str(SOURCE/'check_interpolation_control.py'),
                                                                '--json',str(report)]
        if failure:
            command.append('--self-test-failure')
        result = subprocess.run(command,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,
                                cwd=ROOT,encoding='utf-8',errors='replace')
        (OUT/(name+'.log')).write_text(result.stdout,encoding='utf-8')
        data = json.loads(report.read_text())
        expected = 1 if failure else 0
        if result.returncode != expected or data['tests_run'] != (20 if failure else 19):
            raise RuntimeError('Unexpected source check result '+name)
        if data['errors'] or data['failures'] != (1 if failure else 0):
            raise RuntimeError('Unexpected source test failure '+name)
        runs.append(dict(name=name,command=command,returncode=result.returncode,record=data))
    if (OUT/'normal.json').read_bytes()!=(OUT/'optimized.json').read_bytes():
        raise RuntimeError('Source normal and optimized JSON differ')
    newruns = []
    for optimized in (False,True):
        for failure in (False,True):
            name = ('negative-' if failure else '')+('optimized' if optimized else 'normal')
            command = [sys.executable]+(['-O'] if optimized else [])+[
                str(ROOT/'scripts/check_coherent_tensor_transport.py'),
                '--json',str(OUT/('transport-'+name+'.json'))]
            if failure:
                command.append('--self-test-failure')
            result = subprocess.run(command,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,
                                    cwd=ROOT,encoding='utf-8',errors='replace')
            (OUT/('transport-'+name+'.log')).write_text(result.stdout,encoding='utf-8')
            if result.returncode != (1 if failure else 0):
                raise RuntimeError('Unexpected transport-check exit '+name)
            if failure and 'RuntimeError: deliberate-failure' not in result.stdout:
                raise RuntimeError('Transport failed before its negative control '+name)
            data = None if failure else json.loads((OUT/('transport-'+name+'.json')).read_text())
            newruns.append(dict(name=name,command=command,returncode=result.returncode,record=data))
    for row in provenance['files']:
        if sha(STAGE/row['archive_entry'])!=row['sha256']:
            raise RuntimeError('Source modified during execution: '+row['archive_entry'])
    receipt = dict(success=True,python_executable=sys.executable,archive_sha256=sha(archive),
                   archive_unchanged=True,staged_files_unchanged=verified,source_runs=runs,
                   transport_runs=newruns,source_checker_sha256=sha(SOURCE/'check_interpolation_control.py'),
                   transport_checker_sha256=sha(ROOT/'scripts/check_coherent_tensor_transport.py'),
                   scope='Fresh exact finite calibrations only; complete analytic results require their written proofs.')
    (OUT/'validation_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'success':True,'source_methods_per_mode':19,'transport_checks_per_mode':37,
                      'negative_controls':'all four exited 1 at their deliberate failure',
                      'original_archive_and_staged_files_unchanged':True}))


if __name__=='__main__':
    main()
