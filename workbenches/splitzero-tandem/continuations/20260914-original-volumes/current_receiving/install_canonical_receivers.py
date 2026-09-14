"""Build complete cut22 NOTE/JSR successors with byte-reversible exact edits."""
from pathlib import Path
import hashlib, json, re, difflib

HERE = Path(__file__).resolve().parent
GW = HERE.parent.parent
OLD = GW / 'receiving'
sha = lambda b: hashlib.sha256(b).hexdigest()
lf = lambda b: b.decode('utf-8').replace('\r\n', '\n')

def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(text.encode('utf-8'))

for name in ['spans', 'providers/canonical', 'predecessors/cut21']:
    (HERE / name).mkdir(parents=True, exist_ok=True)

predecessor_pins = {
    'CURRENT_JOINT_SCHUR_NOTE.tex': '221c2c799dda3cd175d1d52592a95de51ad98e687f616928ee0228a8e8e9576b',
    'SIGNED_RETURN_RECEIVER.tex': '242281e4b7d090058aecd5d20ad299bc0c1ecb63f7a4555a62a08b0328c92a6a',
}
docs = {}
records = []
for name, pin in predecessor_pins.items():
    raw = (OLD / name).read_bytes()
    assert sha(raw) == pin, (name, sha(raw))
    target = HERE / 'predecessors/cut21' / name
    if target.exists():
        assert target.read_bytes() == raw, ('changed preserved predecessor', name)
    else:
        target.write_bytes(raw)
    docs[name] = lf(raw)
    records.append({'file': name, 'predecessor_source': str(OLD / name),
                    'predecessor_copy': str(target.relative_to(HERE)),
                    'predecessor_sha256': pin})
old_receipt = OLD / 'FULL_RECEIVING_RECEIPT.json'
snapshot_receipt = HERE / 'predecessors/cut21/FULL_RECEIVING_RECEIPT.json'
if snapshot_receipt.exists():
    assert snapshot_receipt.read_bytes() == old_receipt.read_bytes()
else:
    snapshot_receipt.write_bytes(old_receipt.read_bytes())

providers = []
def copy_provider(src, dest, expected=None):
    raw = src.read_bytes()
    if expected:
        assert sha(raw) == expected, (str(src), sha(raw))
    target = HERE / 'providers' / dest
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        assert target.read_bytes() == raw, ('frozen provider mismatch', str(target))
    else:
        target.write_bytes(raw)
    providers.append({'source': str(src), 'copy': str(target.relative_to(HERE)),
                      'sha256': sha(raw), 'bytes': len(raw)})

for src in sorted((OLD / 'providers').rglob('*')):
    if src.is_file():
        copy_provider(src, src.relative_to(OLD / 'providers'))

manifest = json.loads((HERE / 'CANONICAL_PROVIDER_MANIFEST.json').read_text(encoding='utf-8'))
provider_display_transports = []
for entry in manifest:
    copy_provider(Path(entry['source']), 'canonical/' + entry['name'], entry['sha256'])
    raw = (HERE / 'providers/canonical' / entry['name']).read_bytes()
    source_text = raw.decode('utf-8')
    entry['input'] = 'providers/canonical/' + entry['name']
    if entry.get('typeset', True) and r'\begin{document}' in source_text:
        prefix, fragment = source_text.split(r'\begin{document}', 1)
        fragment, suffix = fragment.rsplit(r'\end{document}', 1)
        trims = [{'before': prefix + r'\begin{document}', 'after': ''},
                 {'before': r'\end{document}' + suffix, 'after': ''}]
        if r'\maketitle' in fragment:
            trims.append({'before': r'\maketitle', 'after': ''})
        current = source_text
        for trim in trims:
            assert current.count(trim['before']) == 1
            trim['offset'] = current.index(trim['before'])
            current = current.replace(trim['before'], trim['after'], 1)
        back = current
        for trim in reversed(trims):
            i = trim['offset']
            assert back[i:i+len(trim['after'])] == trim['after']
            back = back[:i] + trim['before'] + back[i+len(trim['after']):]
        assert back.encode('utf-8') == raw
        entry['input'] = 'providers/canonical/body/' + entry['name']
        write(HERE / entry['input'], current)
        provider_display_transports.append({'original': 'providers/canonical/' + entry['name'],
             'input': entry['input'], 'changes': trims,
             'original_sha256': sha(raw), 'input_sha256': sha((HERE / entry['input']).read_bytes()),
             'exact_original_byte_roundtrip': True})

changes = []
def replace(s, old, new, name, label):
    assert s.count(old) == 1, (name, label, s.count(old))
    before = HERE / 'spans' / (name + '.' + label + '.before.tex')
    after = HERE / 'spans' / (name + '.' + label + '.after.tex')
    write(before, old)
    write(after, new)
    changes.append({'file': name, 'label': label,
                    'before': str(before.relative_to(HERE)),
                    'after': str(after.relative_to(HERE)),
                    'before_sha256': sha(before.read_bytes()),
                    'after_sha256': sha(after.read_bytes()),
                    'start_line_at_replacement': s[:s.index(old)].count('\n') + 1})
    return s.replace(old, new, 1)

body_names = ['BASELINE_RECEIVING_BODY.tex', 'LOW_REFINEMENT_RECEIVING_BODY.tex',
              'QUANTITATIVE_RECEIVING_BODY.tex', 'MIXED_ROW_RECEIVING_BODY.tex',
              'INTRINSIC_RECEIVING_BODY.tex']
body = '\n'.join(lf((HERE / 'spans' / x).read_bytes()) for x in body_names)

appendix = r'''
\clearpage
\part*{Complete proofs of the original baseline and its intrinsic mixed return}
The following complete source bodies prove the baseline, the original
finite low and high corrections, and the intrinsic source and mixed-row
maps used above. The packet is unchanged throughout: only the already
present source orders $s=1$ and $s=k$ enter these receiving statements.
The original masses, relation polynomial, observation, four endpoint
signs and fibre kernels are retained in the displayed exact maps.
'''
for entry in manifest:
    if entry.get('typeset', True):
        appendix += '\\input{' + entry['input'] + '}\n'

canonical_status = r'''The original baseline is now evaluated by BRI1--9:
$\mathcal B_k^\sigma/q^2$, $\mathcal B_k^0/q^2$,
$\mathcal B_k^{\rm ar}/q^2$ and $\mathcal R_k/q^2$ tend to
$C_B=9-8\log2+\mathcal F(2,\pi)>769/17010$.
QRI1--9 returns the finite four-block estimate through the original
signed source and arithmetic maps. For every fixed $m\ge2$ it proves
$\mathcal H_k+lq\mathcal C_\Gamma=o(q)$; at $m=1$ its full finite
bound remains explicit. MRI1--5 computes the individual original
kernel and boundary factors from the unchanged coefficient observation.
IGO and IFB give the source order and the complete polynomial and
fibre maps produced by the existing exterior-power and sum operation.
The arithmetic scalar retains its exact signs and allowances.'''

name = 'CURRENT_JOINT_SCHUR_NOTE.tex'
s = docs[name]
s = replace(s, r'\end{abstract}', canonical_status + '\n' + r'\end{abstract}', name,
            'current_abstract_baseline_and_intrinsic_return')
s = replace(s, r'''included in this source through valid local inputs.
All complete proofs accompany this text;''', r'''included in this source through valid local inputs.
The accepted BSL/HBL, GDR/LER, QLG/QGT and intrinsic IGO/IFB/GMB
proofs now evaluate the original baseline, quantify the complete
return, and calculate its original mixed rows. BRI, LRI, QRI and
MRI and IRI below install their exact consequences at the receiving sites.
All complete proofs accompany this text;''', name, 'current_integration_canonical_providers')
anchor = r'\subsection{Return to the original arithmetic criterion}'
s = replace(s, anchor, body + '\n' + anchor, name, 'complete_canonical_receiving_bodies')
s = replace(s, r'''                                      -W_k-b_k^--a_0\},\\
 U_k=\min\{\mathscr U_k,H_k^*+b_k^+,H_k^B+b_{B,k}^+,
                                      -W_k+b_k^++b_0\}.''',
 r'''                 -W_k-b_k^--a_0,\mathsf L_k^\sigma-\mathcal B_k^0\},\\
 U_k=\min\{\mathscr U_k,H_k^*+b_k^+,H_k^B+b_{B,k}^+,
                 -W_k+b_k^++b_0,\mathsf U_k^\sigma-\mathcal B_k^0\}.''',
 name, 'actual_fifth_baseline_interval')
s = replace(s, r'''at least the second. The maximum and minimum thus equal
their previous three-entry values exactly.''', r'''at least the second. Thus the first four entries reproduce
the preceding exact endpoints. BRI2--3 proves that the fifth
interval also contains this same original scalar, on the identical
source threshold. Intersecting it preserves the preceding width
bound and can strengthen the finite endpoints. QRI3 and LRI4
give evaluated enclosures containing the retained exact-$W_k$
interval; they remain available with every explicit error.''', name,
 'actual_fifth_interval_proof')
old = r'''The next calculation concerns those original
objects and the finer $q$-scale remainder. The finite WGP13/GEL17b
terms, original low moment and all arithmetic allowances remain;
the proved GEL remainder is $o(lq)$ and is not replaced by $o(q)$.'''
new = r'''BSL/HBL now evaluates those original baselines at order $q^2$,
with the full finite packet comparison retained in BRI3--4.
QGT proves the finite $O(l\sqrt q+l^2)$ bound using all four
high blocks and the LER low correction. QRI7 proves the original
$o(q)$ Gamma remainder for fixed $m\ge2$ and keeps the full
$m=1$ uncertainty. MRI and the complete intrinsic providers give
the next original mixed calculation as finite recurrence and fibre
maps, retaining the entire polynomial and observation. QRI8 keeps
the arithmetic scalar in that calculation.'''
s = replace(s, old, new, name, 'current_analytic_continuation')
old = r'''GRI7 proves the actual baseline and HC difference limits and
the necessary bound $\liminf\mathcal B_k^0/(kq)\geq\mathcal C_\Gamma/4$.
Neither the baseline nor the nonnegative residual is set to zero.
The next calculation keeps those objects and the finite $q$-scale
terms retained in WGP13/GEL17b; no sharper remainder is assumed.'''
new = r'''BRI5--8 now proves the common original $q^2$ coefficient
$C_B>769/17010$ for both Gamma baselines, the arithmetic volume,
the HC residual and its full original cost sum. Their finer
GRI7 difference limits remain valid. QRI7--8 supplies the proved
$q$-scale Gamma refinement with its precise multiplicity branches
and its unchanged arithmetic scalar. MRI1--5 computes the actual
individual mixed factors and their exact arithmetic return; the
intrinsic exterior sum retains all polynomial coefficients and
its complete fibre kernel.'''
s = replace(s, old, new, name, 'current_final_mathematical_state')
s = replace(s, r'\end{document}', appendix + '\n' + r'\end{document}', name,
            'complete_new_provider_proofs')
docs[name] = s

name = 'SIGNED_RETURN_RECEIVER.tex'
s = docs[name]
anchor = r'\subsection{The current four-interval receiver}'
s = replace(s, anchor, body + '\n' + r'\subsection{The current original-source interval receiver}',
            name, 'complete_canonical_receiving_bodies')
s = replace(s, r'''              H_k^B-b_{B,k}^-,-W_k-b_k^--a_0\},\\
 U_k^{\rm cur}=\min\{\mathscr U_k,H_k^*+b_k^+,
              H_k^B+b_{B,k}^+,-W_k+b_k^++b_0\},\\''',
 r''' H_k^B-b_{B,k}^-,-W_k-b_k^--a_0,
                  \mathsf L_k^\sigma-\mathcal B_k^0\},\\
 U_k^{\rm cur}=\min\{\mathscr U_k,H_k^*+b_k^+,
 H_k^B+b_{B,k}^+,-W_k+b_k^++b_0,
                  \mathsf U_k^\sigma-\mathcal B_k^0\},\\''',
 name, 'actual_fifth_baseline_interval')
s = replace(s, r'''Thus these maximum and minimum values equal exactly
their previous three-entry values for every finite input.
The extra entry records the universal analytic centre;
it does not narrow the retained exact-low interval.''',
 r'''Thus the first four entries reproduce the previous exact
endpoints. BRI2--3 proves that the fifth interval contains the
same original scalar on BHR1. Its intersection preserves the
earlier width bound and may strengthen the actual finite endpoints.
The evaluated QRI3 and LRI4 intervals contain the exact-$W_k$
interval and retain every finite high and low error. Their explicit
values are available alongside this tighter intersection.''', name,
 'actual_fifth_interval_proof')
old = r'''The original baseline and nonnegative residual remain
present, together with the finite $q$-scale terms and
the proved $o(lq)$ equilibrium remainder.'''
new = r'''The original baseline and residual now have the evaluated
$q^2$ coefficient $C_B>769/17010$ by BRI5--8, with the same
finite asymmetric packet bounds. QRI3--8 supplies the actual
four-block finite Gamma return and its $q$-scale multiplicity
branches. MRI1--5 retains and computes each original mixed
factor through the unchanged observation, and transports their
sum to the same arithmetic and HC identities.'''
s = replace(s, old, new, name, 'actual_final_HC_baseline_return')
s = replace(s, r'''receiver, retaining the smaller-scale terms. The companion JSON''',
 r'''receiver, retaining the smaller-scale terms. BRI1--9, LRI1--4,
QRI1--9, MRI1--5 and IRI1--5 now return the complete canonical BSL/HBL,
GDR/LER, QLG/QGT and IGO/IFB/GMB proofs, all included in full
below. No independently chosen Gamma order enters these formulas.
The companion JSON''', name, 'complete_canonical_provider_statement')
s = replace(s, r'\end{document}', appendix + '\n' + r'\end{document}', name,
            'complete_new_provider_proofs')
docs[name] = s

def expand_inputs(s, trail=()):
    def substitute(match):
        target = match.group(1)
        assert target not in trail, ('input cycle', trail, target)
        path = HERE / target
        assert path.is_file(), ('missing input', target)
        fragment = lf(path.read_bytes())
        assert not re.search(r'\\(?:documentclass|begin\{document\}|end\{document\})', fragment), target
        return expand_inputs(fragment, trail + (target,))
    return re.sub(r'\\input\{([^}]+)\}', substitute, s)

for rec in records:
    name = rec['file']
    s = docs[name]
    raw = (OLD / name).read_bytes()
    restored = s
    for change in reversed(changes):
        if change['file'] != name:
            continue
        after = lf((HERE / change['after']).read_bytes())
        before = lf((HERE / change['before']).read_bytes())
        assert restored.count(after) == 1, (name, change['label'], 'reverse')
        restored = restored.replace(after, before, 1)
    assert restored == lf(raw)
    back = (restored.replace('\n', '\r\n') if b'\r\n' in raw else restored).encode('utf-8')
    assert back == raw, ('predecessor byte reconstruction', name)
    write(HERE / name, s)
    write(HERE / 'predecessors' / (name + '.diff'), ''.join(difflib.unified_diff(
        lf(raw).splitlines(True), s.splitlines(True),
        fromfile='accepted21/' + name, tofile='current22/' + name)))
    expanded = expand_inputs(s)
    tags = re.findall(r'\\tag\{([^}]+)\}', expanded)
    labels = re.findall(r'\\label\{([^}]+)\}', expanded)
    assert len(tags) == len(set(tags)), ('duplicate tags', name, [x for x in set(tags) if tags.count(x)>1])
    assert len(labels) == len(set(labels)), ('duplicate labels', name, [x for x in set(labels) if labels.count(x)>1])
    assert all(x in tags for x in re.findall(r'\\tag\{([^}]+)\}', lf(raw)))
    assert all(x in labels for x in re.findall(r'\\label\{([^}]+)\}', lf(raw)))
    clean = re.sub(r'(?<!\\)%[^\n]*', '', expanded)
    stack = []
    for kind, env in re.findall(r'\\(begin|end)\{([^}]+)\}', clean):
        if kind == 'begin':
            stack.append(env)
        else:
            assert stack and stack.pop() == env, (name, 'unmatched environment', env)
    assert not stack and clean.count(r'\[') == clean.count(r'\]')
    assert s.count(body) == 1
    rec.update({'successor_sha256': sha((HERE / name).read_bytes()),
                'bytes': len((HERE / name).read_bytes()),
                'expanded_tag_count': len(tags), 'exact_predecessor_byte_roundtrip': True})

for name, pin in predecessor_pins.items():
    assert sha((OLD / name).read_bytes()) == pin
receipt = {
    'edition': 'cut22 canonical original-source receiving successors',
    'scope': 'Complete current NOTE/JSR with exact cut21 predecessors and inherited provider tree retained. All new canonical providers included in full. Original packet and sources s=1,k only. Independent-K calculations remain exploratory outside this receiver.',
    'receivers': records, 'changes': changes, 'providers': providers,
    'provider_display_transports': provider_display_transports,
    'receiving_bodies': [{'path': 'spans/' + x, 'sha256': sha((HERE / 'spans' / x).read_bytes())}
                         for x in body_names],
    'checks': ['all immutable predecessor and provider pins matched',
               'every actual-site edit reverses to the exact predecessor bytes',
               'all original equation tags and labels preserved',
               'all local complete-proof inputs resolve with no duplicate tags or labels',
               'expanded TeX environments and display delimiters balance',
               'each full new receiving body occurs once in each current receiver'],
    'mathematics': 'The original q^2 baseline, finite low and high refinements, and exact original mixed row maps are installed at actual current arithmetic/HC sites. The new baseline interval is intersected with preceding endpoints. QGT finite intervals preserve all source, arithmetic and HC constants. Original fixed-m branches retained. All intrinsic polynomial coefficients and fibre kernels are retained.',
    'predecessor_archive_policy': 'Only the immediate complete predecessor sources and receipt are duplicated here for reversibility. Full earlier archive closure is retained unchanged in the cut21 delivery. All provider files from the immediate predecessor are copied exactly here.'
}
write(HERE / 'FULL_RECEIVING_RECEIPT.json', json.dumps(receipt, indent=2) + '\n')
print(json.dumps({'receivers': records, 'changes': len(changes), 'providers': len(providers),
                  'receipt_sha256': sha((HERE / 'FULL_RECEIVING_RECEIPT.json').read_bytes())}, indent=2))
