"""Reproduce the included, reviewed mathematical checks in a fresh directory."""
from pathlib import Path
import json,hashlib,tempfile,sys,subprocess,argparse
P=Path(__file__).resolve().parent
parser=argparse.ArgumentParser()
parser.add_argument('--extract-only',action='store_true')
parser.add_argument('--output',type=Path)
args=parser.parse_args()
meta=json.loads((P/'SOURCE_MANIFEST.json').read_text(encoding='utf-8'))
bank=(P/'RETAINED_COMPLETE_PROOF_SOURCES.tex').read_bytes()
if hashlib.sha256(bank).hexdigest()!=meta['bank_sha256']:raise ArithmeticError('Source bank hash mismatch')
R=args.output.resolve() if args.output else Path(tempfile.mkdtemp(prefix='splitzero029-checks-'))
R.mkdir(parents=True,exist_ok=True)
scripts=['check_native_source_step.py','check_native_word_activation.py','check_direct_word_grams.py','check_whole_space_identities.py','check_rational_currents.py','check_reduced_pencils.py','check_profile_constants.py','check_evolution_diagnostics.py']
receipts=[]
for name in scripts:
    candidates=[b for b in meta['new_blocks'] if b['name']=='checks/'+name]
    if len(candidates)!=1:raise ArithmeticError('Missing or ambiguous script '+name)
    b=candidates[0];data=bank[b['offset']:b['offset']+b['bytes']]
    if hashlib.sha256(data).hexdigest()!=b['sha256']:raise ArithmeticError(name)
    dest=(R/name).resolve()
    if dest.parent!=R.resolve():raise ArithmeticError('Extraction target')
    dest.write_bytes(data)
    if not args.extract_only:
        cmd=[sys.executable,'-B','-X','utf8']
        if sys.flags.optimize:cmd+=['-O']
        result=subprocess.run(cmd+[str(dest)],capture_output=True,text=True,encoding='utf-8')
        (R/(name+'.log')).write_text(result.stdout+result.stderr,encoding='utf-8')
        if result.returncode:raise ArithmeticError(name+': '+result.stderr[-1800:])
    receipts.append({'script':name,'sha256':b['sha256'],'executed':not args.extract_only})
    print(name+(' extracted' if args.extract_only else ' passed'),flush=True)
(R/'RUN_RECEIPT.json').write_text(json.dumps({'scripts':receipts,'optimized':bool(sys.flags.optimize),'output':str(R)},indent=2),encoding='utf-8')
print(str(R))
