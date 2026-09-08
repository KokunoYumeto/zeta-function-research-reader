# Publication-only transport adjustment: read the public snapshot manifest;
# hashes below certify the published snapshot bytes, not private local originals.
"""Targeted source-render regression check; this is not a proof checker.

Check the ordered mathematical tokens of every original display and inline
math block after typography conversion, allowing added prose math wrappers.
Grouping braces, alignment, equation tag prefixes and delimiter size commands
are ignored solely for this typography comparison. The original byte hashes
are checked independently, so the complete unmodified source is retained.
"""
from pathlib import Path
import hashlib,json,re

ROOT=Path(__file__).resolve().parents[1]
original=(ROOT/'sources/xi4_source/first_separated_electric_covariance.md').read_text(encoding='utf-8')
render=(ROOT/'tex/xi4_source_proof.tex').read_text(encoding='utf-8')
pattern=r'\\\[([\s\S]*?)\\\]|\\\(([\s\S]*?)\\\)'

def canonical(text):
    text=re.sub(r'\\tag\{S?(\d+)\}',r'\\tag{\1}',text)
    text=re.sub(r'\\(?:begin|end)\{(?:aligned|split)\}', '',text)
    text=re.sub(r'\\(?:left|right|biggl|biggr|bigl|bigr)\b','',text)
    text=text.replace('\\\\','').replace('&','')
    return re.sub(r'[\s{}]','',text)

def blocks(text):
    return [canonical(a or b) for a,b in re.findall(pattern,text)]

source_blocks=blocks(original)
render_blocks=blocks(render)
cursor=0
for index,block in enumerate(source_blocks,1):
    while cursor<len(render_blocks) and render_blocks[cursor]!=block:
        cursor+=1
    if cursor==len(render_blocks):
        raise AssertionError(f'Original math block {index} missing or altered: {block[:160]}')
    cursor+=1

manifest=json.loads((ROOT/'checks/xi4_source_public_manifest.json').read_text(encoding='utf-8'))
for entry in manifest['records']:
    assert hashlib.sha256((ROOT/entry['snapshot']).read_bytes()).hexdigest()==entry['sha256']
assert re.findall(r'\\tag\{S(\d+)\}',render)==[str(i) for i in range(1,26)]
assert 'SU(S2)' not in render and "h(S3)" not in render
assert '10.1016/0550-3213(86)90567-5' in render
result={'passed':True,'original_math_blocks_preserved_in_order':len(source_blocks),
        'equation_tags_preserved':25,'byte_preserving_snapshot_hashes_verified':len(manifest['records']),
        'limitations':__doc__.strip(),
        'appendix_sha256':hashlib.sha256((ROOT/'tex/xi4_source_proof.tex').read_bytes()).hexdigest()}
(ROOT/'checks/xi4_source_render_checks.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result))
