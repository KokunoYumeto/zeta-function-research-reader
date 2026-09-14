"""Read-only static source inventory; writes audit results beside this script."""
from pathlib import Path
import collections, hashlib, json, re, unicodedata

ROOT = Path(r'workspace:')
BASE = ROOT / 'output/Split_Zero_Recursive_Integration_2026-09-13/repository'
CAND = ROOT / 'work/backpropagation_20260913/next_phase_graph_intake/reader_v2'
OUT = Path(__file__).parent

def decomment(s):
    return re.sub(r'(?<!\\)%[^\n]*', '', s)

def inventory(path):
    raw = path.read_bytes()
    s = raw.decode('utf-8-sig')
    clean = decomment(s)
    controls = collections.Counter(re.findall(r'\\([A-Za-z@]+|[^\sA-Za-z])', clean))
    envs = collections.Counter(re.findall(r'\\begin\{([^}]+)\}', clean))
    definitions = []
    for i, line in enumerate(s.splitlines(), 1):
        if re.search(r'\\(?:def|gdef|xdef|edef|let|newcommand|renewcommand|providecommand|newenvironment|renewenvironment|newtheorem|Declare\w+)', decomment(line)):
            definitions.append({'line': i, 'text': line})
    unicode_chars = collections.Counter(c for c in clean if ord(c) > 127)
    return {'path': str(path.relative_to(ROOT)).replace('\\','/'), 'sha256': hashlib.sha256(raw).hexdigest(), 'bytes':len(raw), 'controls':dict(controls), 'environments':dict(envs), 'definitions':definitions, 'unicode':{f'U+{ord(k):04X}':{'char':k,'name':unicodedata.name(k,'?'),'count':v} for k,v in sorted(unicode_chars.items())}}

candidates = [inventory(p) for p in sorted((CAND/'tex/bodies').glob('*.tex'))]
candidate_commands = collections.Counter()
candidate_envs = collections.Counter()
candidate_unicode = {}
for item in candidates:
    candidate_commands.update(item['controls'])
    candidate_envs.update(item['environments'])
    for code, data in item['unicode'].items():
        entry = candidate_unicode.setdefault(code, {'char':data['char'],'name':data['name'],'count':0,'files':[]})
        entry['count'] += data['count']
        entry['files'].append({'path':item['path'],'count':data['count']})

# Baseline preamble and explicit preamble inputs, plus full source use inventory.
preamble_paths = [BASE/'tex/main.tex', BASE/'tex/source_unicode_math_glyphs.tex', BASE/'sources/current_cohorts/macro_context/REQUIRED_READER_SETUP.tex']
preamble = '\n'.join(p.read_text(encoding='utf-8-sig').split('\\begin{document}')[0] for p in preamble_paths)
base_controls = set()
for p in BASE.rglob('*.tex'):
    base_controls.update(re.findall(r'\\([A-Za-z@]+|[^\sA-Za-z])', decomment(p.read_text(encoding='utf-8-sig',errors='replace'))))
data = {'scope':'Static source inventory, not a TeX compilation', 'candidate_main':inventory(CAND/'tex/main.tex'), 'baseline_preamble_files':[inventory(p) for p in preamble_paths], 'body_count':len(candidates),'bodies':candidates,'candidate_controls':dict(sorted(candidate_commands.items())),'candidate_environments':dict(sorted(candidate_envs.items())),'candidate_unicode':candidate_unicode,'candidate_controls_not_seen_anywhere_in_baseline_tex':sorted(set(candidate_commands)-base_controls)}
(OUT/'control_inventory.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'body_count':len(candidates),'candidate_controls':dict(sorted(candidate_commands.items())),'candidate_environments':dict(sorted(candidate_envs.items())),'unicode_summary':{k:{kk:vv for kk,vv in v.items() if kk!='files'} for k,v in candidate_unicode.items()},'controls_not_seen_in_baseline':data['candidate_controls_not_seen_anywhere_in_baseline_tex']},ensure_ascii=False,indent=2))
