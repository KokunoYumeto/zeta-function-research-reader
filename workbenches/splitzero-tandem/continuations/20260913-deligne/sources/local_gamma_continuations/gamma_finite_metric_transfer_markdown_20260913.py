"""Make the complete readable derivative; canonical proof remains the TeX."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess

root=Path(__file__).resolve().parent
source=root/'gamma_finite_metric_transfer_20260913.tex'
output=root/'gamma_finite_metric_transfer_20260913.md'
pandoc=shutil.which('pandoc')
if not pandoc:
    raise RuntimeError('Pandoc is required for the full readable derivative')
command=[pandoc,str(source),'-f','latex','-t','markdown','--wrap=none']
result=subprocess.run(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=True)
raw=result.stdout.decode('utf-8')
# Pandoc expands \R/\C as unbraced \mathbb R / \mathbb C.
# Bracing the same single-letter arguments preserves their exact TeX tokens.
substitutions={r'\mathbb R':r'\mathbb{R}',r'\mathbb C':r'\mathbb{C}'}
counts={a:raw.count(a) for a in substitutions}
for a,b in substitutions.items():
    raw=raw.replace(a,b)
title='# Finite Gamma coefficients, boundary resolvents, and consecutive quotient volumes\n\n'
output.write_text(title+raw,encoding='utf-8')
receipt={'schema':'gmt-complete-readable-derivative-v1','source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
         'output_sha256':hashlib.sha256(output.read_bytes()).hexdigest(),'command':command,
         'stderr':result.stderr.decode('utf-8'),'complete_body_conversion':True,
         'exact_single_argument_bracing_substitutions':counts,'added_title':title.strip()}
(root/'gamma_finite_metric_transfer_markdown_receipt_20260913.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
