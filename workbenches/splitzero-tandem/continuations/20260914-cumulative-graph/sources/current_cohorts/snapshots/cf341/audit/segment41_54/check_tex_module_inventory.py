from pathlib import Path
import hashlib
import json
import re

root=Path(__file__).resolve().parent
names={
    'conormal_jacobian_symmetric_trace.tex':'C',
    'multiplicity_boundary_floor.tex':'BF',
    'symmetric_frontier_determinant.tex':'FD',
}
seen_tags={}
seen_labels={}
result=[]
for name,prefix in names.items():
    path=root/name
    content=path.read_text(encoding='utf-8')
    if not content.lstrip().startswith(r'\section'):
        raise RuntimeError(f'{name}: does not start with section')
    if any(x in content for x in [r'\documentclass',r'\usepackage',r'\begin{document}',r'\newtheorem']):
        raise RuntimeError(f'{name}: not an includable proof module')
    tags=re.findall(r'\\tag\{([^}]+)\}',content)
    labels=re.findall(r'\\label\{([^}]+)\}',content)
    if not all(t.startswith(prefix) for t in tags):
        raise RuntimeError(f'{name}: unexpected equation prefix')
    for items,seen,typ in [(tags,seen_tags,'tag'),(labels,seen_labels,'label')]:
        for item in items:
            if item in seen:
                raise RuntimeError(f'duplicate {typ}: {item} ({seen[item]}, {name})')
            seen[item]=name
    if prefix=='C':
        expected={f'C{i}' for i in range(1,26)}|{'C17a','C17b'}
        if set(tags)!=expected:
            raise RuntimeError(f'Conormal proof tag preservation mismatch: {set(tags)^expected}')
    result.append({'module':name,'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
                   'bytes':path.stat().st_size,'characters':len(content),'equation_tags':tags,
                   'labels':labels,'starts_with_section':True,'no_preamble':True})
(root/'tex_module_inventory.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({'status':'passed','modules':len(result),'unique_equation_tags':len(seen_tags),
                  'unique_labels':len(seen_labels),'all_C1_through_C25_preserved':True}))
