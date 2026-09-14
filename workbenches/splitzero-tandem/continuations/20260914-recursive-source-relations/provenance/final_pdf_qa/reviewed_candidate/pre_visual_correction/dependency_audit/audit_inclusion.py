"""Read-only TeX inclusion and historical-preservation audit.

Run once without --assembly to pin the historical source.  With --assembly,
walk the actual successor main file and verify every expected lane patch at
its compiled path.  Lexical tag candidates are discovery data, not proof.
"""
from __future__ import annotations
import argparse, hashlib, json, re
from pathlib import Path

HERE = Path(__file__).resolve().parent
WORKSPACE = HERE.parents[2]
BASE = WORKSPACE / 'output/split_zero_rh_tandem_2026-09-12/current_source_20260913_periodized_residue'
V19 = WORKSPACE / 'work/cumulative_next_edition_staging_20260913_v19/reader'

def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def write(name, value):
    (HERE / name).write_text(json.dumps(value, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')

def uncomment(s):
    return re.sub(r'(?<!\\)%[^\n]*', '', s)

def graph(root, main='tex/main.tex'):
    root = root.resolve()
    found, edges, missing = {}, [], []
    queue = [root/main]
    while queue:
        p = queue.pop(0)
        key = str(p.relative_to(root)).replace('\\', '/')
        if key in found:
            continue
        if not p.is_file():
            missing.append(key)
            continue
        raw = p.read_text(encoding='utf-8-sig')
        text = uncomment(raw)
        found[key] = {'sha256':digest(p), 'bytes':p.stat().st_size,
                      'lines':len(raw.splitlines()), 'labels':[], 'tags':[], 'refs':[]}
        for kind, rx in [('labels',r'\\label\{([^{}]+)\}'),('tags',r'\\tag\*?\{([^{}]+)\}'),
                         ('refs',r'\\(?:eqref|ref|pageref)\{([^{}]+)\}')]:
            for m in re.finditer(rx,text):
                found[key][kind].append({'value':m.group(1),'line':text.count('\n',0,m.start())+1})
        for m in re.finditer(r'\\(?:input|include)\{([^{}]+)\}',text):
            target = m.group(1)
            if not Path(target).suffix:
                target += '.tex'
            candidates = [root/target,p.parent/target]
            dest = next((c.resolve() for c in candidates if c.is_file()), candidates[0].resolve())
            try:
                destkey = str(dest.relative_to(root)).replace('\\','/')
            except ValueError:
                destkey = str(dest)
            edges.append({'from':key,'line':text.count('\n',0,m.start())+1,'to':destkey})
            if dest.is_relative_to(root): queue.append(dest)
            else: missing.append('external: '+destkey)
    return {'root':str(root),'main':main,'files':found,'edges':edges,'missing':sorted(set(missing))}

def baseline_pin():
    manifest = HERE/'HISTORICAL_821_BASELINE_PINS.json'
    if not manifest.exists():
        files = {str(p.relative_to(BASE)).replace('\\','/'):
                 {'sha256':digest(p),'bytes':p.stat().st_size}
                 for p in sorted(BASE.rglob('*')) if p.is_file()}
        write(manifest.name,{'root':str(BASE),'files':files})
    original = json.loads(manifest.read_text(encoding='utf-8'))
    changed, absent = [], []
    for name, pin in original['files'].items():
        p=BASE/name
        if not p.is_file(): absent.append(name)
        elif digest(p)!=pin['sha256']: changed.append(name)
    return {'pinned_files':len(original['files']), 'changed':changed, 'absent':absent,
            'pass':not changed and not absent}

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--assembly',type=Path)
    parser.add_argument('--expected',type=Path)
    parser.add_argument('--compact',action='store_true')
    args=parser.parse_args()
    historical=baseline_pin()
    write('HISTORICAL_PRESERVATION_CHECK.json',historical)
    if not args.assembly:
        write('BASELINE_821_INCLUSION_GRAPH.json',graph(BASE))
        write('V19_INCLUSION_GRAPH.json',graph(V19))
        print(json.dumps({'historical':historical,'graphs_written':True}))
        return
    actual=graph(args.assembly)
    expected=json.loads(args.expected.read_text(encoding='utf-8')) if args.expected else {'patches':[]}
    checks=[]
    for row in expected['patches']:
        rel=row['reader_path']
        p=args.assembly/rel
        got=digest(p) if p.is_file() else None
        required=row.get('include_required',True)
        checks.append({'reader_path':rel,'expected_sha256':row['sha256'],'actual_sha256':got,
                       'included':rel in actual['files'],'include_required':required,
                       'pass':got==row['sha256'] and (not required or rel in actual['files'])})
    result={'historical':historical,'patch_checks':checks,
            'missing_inputs':actual['missing'],
            'pass':historical['pass'] and not actual['missing'] and all(x['pass'] for x in checks)}
    write('FINAL_ASSEMBLY_INCLUSION_GRAPH.json',actual)
    write('FINAL_ASSEMBLY_CHECK.json',result)
    if args.compact:
        print(json.dumps({'pass':result['pass'],'included_files':len(actual['files']),
                          'input_edges':len(actual['edges']),'historical':historical,
                          'patches_checked':len(checks),'failed_patches':[r for r in checks if not r['pass']],
                          'missing_inputs':actual['missing']},indent=2))
    else:print(json.dumps(result,indent=2))
    if not result['pass']: raise SystemExit(1)

if __name__=='__main__': main()
