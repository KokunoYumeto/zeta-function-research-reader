from pathlib import Path
import hashlib, json, re

ROOT=Path(__file__).resolve().parent
SOURCE=Path(r'local:user-profile\.codex\attachments\0d84cbd9-4bea-48b2-8d49-3443a3ef7514\pasted-text.txt')
raw=SOURCE.read_bytes()
out=ROOT/'provenance'
out.mkdir(parents=True,exist_ok=True)
(out/'USER_PASTE_VERBATIM.md').write_bytes(raw)
text=raw.decode('utf-8')
blocks=re.findall(r'```lean\r?\n(.*?)```',text,re.S)
assert len(blocks)==1
(out/'SplitZeroMetricSandwich.lean').write_bytes(blocks[0].encode('utf-8'))
receipt={'source':str(SOURCE),'source_sha256':hashlib.sha256(raw).hexdigest(),
 'verbatim_copy':str(out/'USER_PASTE_VERBATIM.md'),'verbatim_exact':(out/'USER_PASTE_VERBATIM.md').read_bytes()==raw,
 'lean_file':str(out/'SplitZeroMetricSandwich.lean'),'lean_status':'UNCOMPILED USER-SUPPLIED DRAFT; no Lean/Lake/Elan run performed by this intake',
 'lean_sha256':hashlib.sha256(blocks[0].encode('utf-8')).hexdigest(),
 'historical_execution_claim':'The supplied text reports prior run 34772920706 and Wolfram checks. This intake preserves those claims without claiming a replay.'}
dependencies=[
 (Path(r'workspace:\work\pr29_complete_math_notes_20260913\workbenches\tau-arithmetic-metric-transfer\RESEARCH_NOTE.md'),'PR29_RESEARCH_NOTE.md'),
 (Path(r'workspace:\work\pr29_complete_math_notes_20260913\workbenches\tau-residue-rigidity\ARITHMETIC_VARIATION.md'),'PR29_ARITHMETIC_VARIATION.md'),
 (Path(r'workspace:\work\pr29_complete_math_notes_20260913\workbenches\tau-residue-rigidity\ADAPTIVE_VARIATION.md'),'PR29_ADAPTIVE_VARIATION.md'),
 (Path(r'workspace:\work\backpropagation_20260913\metric\originals\tex\next_edition\AW_complete.tex'),'AW_COMPLETE_ORIGINAL.tex'),
 (Path(r'workspace:\work\tau_signed_projection_control_20260913.tex'),'SP_COMPLETE_ORIGINAL.tex'),
]
receipt['complete_preserved_dependencies']=[]
for dep,name in dependencies:
    data=dep.read_bytes()
    (out/name).write_bytes(data)
    receipt['complete_preserved_dependencies'].append({'source':str(dep),'copy':str(out/name),'sha256':hashlib.sha256(data).hexdigest(),'byte_exact':(out/name).read_bytes()==data})
(ROOT/'PROVENANCE.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps(receipt,indent=2))
