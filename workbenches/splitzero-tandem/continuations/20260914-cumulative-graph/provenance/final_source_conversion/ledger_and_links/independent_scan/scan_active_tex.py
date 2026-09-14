"""Read-only TeX inclusion and exponent/footnote occurrence audit."""
from pathlib import Path
import re, json, hashlib
from datetime import datetime, timezone

BASE = Path('workspace:')
OUT = Path(__file__).resolve().parent
ROOTS = {
    'stage': BASE/'work/backpropagation_20260913/cumulative_source_v1',
    'delivery': BASE/'output/Split_Zero_Recursive_Integration_2026-09-13/repository',
}

def sha(raw):
    return hashlib.sha256(raw).hexdigest()

def without_comments(text):
    # Preserve source coordinates. A percent preceded by an even number of
    # backslashes starts a TeX comment.
    return re.sub(r'(?<!\\)((?:\\\\)*)%[^\n]*', lambda m: m[1]+' '*(len(m[0])-len(m[1])), text)

def occurrences(text, regex):
    matches=[]
    for m in re.finditer(regex,text):
        a=text.rfind('\n',0,m.start())+1
        b=text.find('\n',m.end())
        if b<0: b=len(text)
        matches.append({'line':text.count('\n',0,m.start())+1,
                        'column':m.start()-a+1,'match':m[0],
                        'source_line':text[a:b]})
    return matches

def scan(root):
    queue=['tex/main.tex']
    files={}
    edges=[]
    missing=[]
    control=[]
    while queue:
        relative=queue.pop(0)
        if relative in files: continue
        path=root/relative
        if not path.is_file():
            missing.append(relative)
            continue
        raw=path.read_bytes()
        text=raw.decode('utf-8-sig')
        clean=without_comments(text)
        row={'path':relative,'sha256':sha(raw),'bytes':len(raw),'lines':len(text.splitlines())}
        row['footnote_commands']=occurrences(clean,r'\\footnote(?:text|mark)?\b')
        row['raw_caret_bracket']=occurrences(clean,r'\^\[')
        row['escaped_caret_bracket']=occurrences(clean,r'\\textasciicircum\{\}\s*\[')
        row['superscript_commands']=occurrences(clean,r'\\textsuperscript\b')
        files[relative]=row
        for m in re.finditer(r'\\(input|include)\s*\{([^{}]+)\}',clean):
            target=m[2]
            if not Path(target).suffix: target += '.tex'
            if not (root/target).is_file() and (path.parent/target).is_file():
                target=(path.parent/target).relative_to(root).as_posix()
            edges.append({'source':relative,'line':text.count('\n',0,m.start())+1,'command':m[1],'target':target})
            queue.append(target)
        row['other_include_controls']=occurrences(clean,r'\\(?:includeonly|import|subimport|InputIfFileExists|IfFileExists|input\s+[^\s{][^\n]*|include\s+[^\s{][^\n]*)\b')
        if row['other_include_controls']: control.append({'path':relative,'matches':row['other_include_controls']})
    return {'root':str(root),'files':list(files.values()),'inclusion_edges':edges,'missing_targets':missing,
            'other_include_controls':control,
            'summary':{'included_file_count':len(files),'include_edge_count':len(edges),
                       'footnote_commands':sum(len(r['footnote_commands']) for r in files.values()),
                       'raw_caret_bracket':sum(len(r['raw_caret_bracket']) for r in files.values()),
                       'escaped_caret_bracket':sum(len(r['escaped_caret_bracket']) for r in files.values()),
                       'superscript_commands':sum(len(r['superscript_commands']) for r in files.values()),
                       'bytes':sum(r['bytes'] for r in files.values())}}

def main():
    result={'created_utc':datetime.now(timezone.utc).isoformat(),
            'method':'Recursive literal input/include graph rooted at tex/main.tex; comments stripped with source coordinates preserved; all original file hashes recorded; no active writes or PDF compilation.',
            'roots':{name:scan(root) for name,root in ROOTS.items()}}
    left={f['path']:f for f in result['roots']['stage']['files']}
    right={f['path']:f for f in result['roots']['delivery']['files']}
    result['comparison']={'stage_only':sorted(left.keys()-right.keys()),'delivery_only':sorted(right.keys()-left.keys()),
                          'hash_differences':[{'path':p,'stage_sha256':left[p]['sha256'],'delivery_sha256':right[p]['sha256']}
                                               for p in sorted(left.keys()&right.keys()) if left[p]['sha256']!=right[p]['sha256']]}
    (OUT/'ACTIVE_TEX_SCAN.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    for name,scan_result in result['roots'].items():
        print(name,json.dumps(scan_result['summary']))
        print('missing_targets',scan_result['missing_targets'])
        print('other_include_controls',json.dumps(scan_result['other_include_controls']))
        for f in scan_result['files']:
            for key in ('footnote_commands','raw_caret_bracket','escaped_caret_bracket','superscript_commands'):
                if f[key]: print(json.dumps({'path':f['path'],'type':key,'matches':f[key]},ensure_ascii=False))
    print('comparison',json.dumps(result['comparison']))

if __name__=='__main__': main()
