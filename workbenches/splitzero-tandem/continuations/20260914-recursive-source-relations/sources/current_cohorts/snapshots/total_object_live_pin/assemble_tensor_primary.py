"""Embed the complete reviewed companions, preserving their exact bytes."""
from pathlib import Path
import argparse
import hashlib
import json
import re

ap = argparse.ArgumentParser()
ap.add_argument('--tcl-sha', required=True)
args = ap.parse_args()
base = Path(__file__).resolve().parent
main = base/'tensor_primary_boundary_control.tex'
marker = b'\n% BEGIN COMPLETE TENSOR COMPANIONS\n'
core = main.read_bytes().split(marker)[0]
core_sha = hashlib.sha256(core).hexdigest()
assert core_sha == '89bd831a817fd4882bb627dbf819b5f644ec19f69890ae1e62561c6a3b206868', core_sha
parts = [
    ('TPF', base/'tensor_primary_finite_field'/'tensor_primary_finite_field.tex',
     '5c2fa0e144f74aea4f21604e986a36fd8b5f37ee4e8235a36a605b49eba32b95'),
    ('TCL', base/'tensor_primary_cyclic_lattice'/'tensor_primary_cyclic_lattice.tex',
     args.tcl_sha.lower()),
]
out = core+marker
receipt = {'complex_core_sha256':core_sha,
           'single_primary_dependency_sha256':'80dcbc843df223a8b65fd92f728deba1b28e540c748e08dabbdf47a6f28958ea',
           'companions':[]}
for label,path,expected in parts:
    data = path.read_bytes()
    actual = hashlib.sha256(data).hexdigest()
    assert actual == expected, (label,actual,expected)
    out += ('% BEGIN '+label+' SHA256 '+actual+'\n').encode()+data
    out += ('\n% END '+label+'\n').encode()
    receipt['companions'].append({'label':label,'path':str(path),'sha256':actual})
out += b'% END COMPLETE TENSOR COMPANIONS\n'
main.write_bytes(out)
text = out.decode('utf-8')
labels = re.findall(r'\\label\{([^}]+)\}',text)
assert len(labels) == len(set(labels))
tags = re.findall(r'\\tag\{([^}]+)\}',text)
assert len(tags) == len(set(tags))
for prefix in ['TP','TPF','TCL']:
    numbers = [int(t.split('.')[1]) for t in tags if t.startswith(prefix+'.')]
    assert numbers == list(range(1,len(numbers)+1)), (prefix,numbers)
receipt['combined_sha256'] = hashlib.sha256(out).hexdigest()
receipt['equation_counts'] = {prefix:sum(t.startswith(prefix+'.') for t in tags) for prefix in ['TP','TPF','TCL']}
receipt['unique_labels'] = len(labels)
(base/'tensor_primary_assembly_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps(receipt,indent=2))
