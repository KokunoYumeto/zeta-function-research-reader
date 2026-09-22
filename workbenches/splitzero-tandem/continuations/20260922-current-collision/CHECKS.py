from pathlib import Path
import json,hashlib,tempfile,subprocess,sys,argparse
P=Path(__file__).resolve().parent
args=argparse.ArgumentParser();args.add_argument('--extract-only',action='store_true');opts=args.parse_args()
meta=json.loads((P/'SOURCE_MANIFEST.json').read_text())
bank=(P/'RETAINED_COMPLETE_PROOF_SOURCES.tex').read_bytes()
if hashlib.sha256(bank).hexdigest()!=meta['bank_sha256']:raise ArithmeticError('Bank hash')
b=next(x for x in meta['new_blocks'] if x['name']=='checks/check_phase_overlap.py')
data=bank[b['offset']:b['offset']+b['bytes']]
if hashlib.sha256(data).hexdigest()!=b['sha256']:raise ArithmeticError('Checker hash')
R=Path(tempfile.mkdtemp(prefix='splitzero030-check-'));f=R/'check_phase_overlap.py';f.write_bytes(data)
if not opts.extract_only:
    cmd=[sys.executable,'-B','-X','utf8']+(['-O'] if sys.flags.optimize else [])+[str(f)]
    subprocess.run(cmd,check=True)
print(str(R))
