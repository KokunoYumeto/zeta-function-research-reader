from pathlib import Path
import hashlib, json, re, datetime

BASE = Path(__file__).resolve().parent
NEXT = BASE.parent.parent
sha = lambda b: hashlib.sha256(b).hexdigest()
sources = {
    'ACM.tex': NEXT/'use_site_audit/acm_hc_overlay/replacement/owner_current/ACM.tex',
    'HC.tex': NEXT/'use_site_audit/acm_hc_overlay/replacement/owner_current/HC.tex',
    'R63_R66_COMPLETE_NEXT_WAVE.tex': NEXT/'next_wave_overlay/R63_R66_COMPLETE_NEXT_WAVE.tex',
}
expected = {
    'ACM.tex': 'ba2e03184d963b61cb78a94c0340d55fc38d0f11091375c503a205faf936fe21',
    'HC.tex': '5f01c1fe8a777cee9b84ed825e0be341514ceba65d3e1188b36e65f97a7bc1a5',
    'R63_R66_COMPLETE_NEXT_WAVE.tex': '459ca7a20f534334a0abfdf2dd74d4f392b422e3009d67983613567f1a693d47',
}
plans = {
 'ACM.tex': [
  (b'At every independent coefficient face', ['ACM_relation_rows.tex','ACM_row_correlations.tex'])],
 'HC.tex': [
  (b'\\subsection{The holonomy energy is tied', ['HC_relation_interval.tex','HC_correlation_interval.tex']),
  (b'For the averaged original phase metrics', ['HC_relation_phase.tex','HC_correlation_phase.tex'])],
 'R63_R66_COMPLETE_NEXT_WAVE.tex': [
  (b'\\paragraph{Result R66:', ['R65_relation_generator.tex','R65_correlation_inputs.tex']),
  (None, ['R66_relation_tail.tex','R66_correlation_return.tex'])]
}
for d in ['snapshots/baseline','snapshots/proof_inputs','replacement']:
    (BASE/d).mkdir(parents=True, exist_ok=True)

def write_identical_or_new(p, data):
    if p.exists() and p.read_bytes()!=data:
        raise RuntimeError(f'Refusing to replace different sealed output {p}')
    p.write_bytes(data)

# Authoring transport only: a terminal single TeX slash in the new fragments
# was a serialization artifact; every such line is a displayed row separator.
for p in (BASE/'fragments').glob('*.tex'):
    data=p.read_text(encoding='utf-8')
    data=re.sub(r'(?<!\\)\\(?=\n|$)', lambda m: '\\\\', data)
    p.write_text(data, encoding='utf-8', newline='\n')

receipt_path = BASE/'INSERTION_RECEIPT.json'
created_utc = (json.loads(receipt_path.read_text(encoding='utf-8'))['created_utc']
               if receipt_path.exists() else datetime.datetime.now(datetime.timezone.utc).isoformat())
receipt = {'status':'complete_source_insertions_checked_not_typeset',
 'created_utc':created_utc,
 'scope':'Insertion-only PGRT/PGGL/PGRC propagation into the complete ACM, HC and R63-R66 bodies. No live owner, frozen delivery or reader edits.',
 'mathematical_order':'exact_graph subset correlation subset relation_rows subset Gamma; strict negative mixed correction retained, no false refinement of exact graph input.',
 'files':[], 'proof_inputs':[]}
for name, src in sources.items():
    old=src.read_bytes()
    assert sha(old)==expected[name], (name,sha(old))
    write_identical_or_new(BASE/'snapshots/baseline'/name, old)
    newline=b'\r\n' if b'\r\n' in old else b'\n'
    insertions=[]
    for anchor, fragments in plans[name]:
        if anchor is None: offset=len(old)
        else:
            assert old.count(anchor)==1,(name,anchor,old.count(anchor))
            offset=old.index(anchor)
        chunks=[]
        for fragment in fragments:
            raw=(BASE/'fragments'/fragment).read_bytes()
            normalized=raw.replace(b'\r\n',b'\n').replace(b'\n',newline)
            chunks.append(normalized)
        addition=newline.join(chunks)+newline
        insertions.append({'offset':offset,'anchor':anchor.decode() if anchor else 'EOF',
          'fragment_paths':fragments,'addition':addition})
    output=old
    for ins in sorted(insertions,key=lambda x:x['offset'],reverse=True):
        pos=ins['offset'];output=output[:pos]+ins['addition']+output[pos:]
    # Exact insertion-removal replay verifies EVERY baseline byte.
    recovered=bytearray(output)
    added_before=0
    offsets=[]
    for ins in sorted(insertions,key=lambda x:x['offset']):
        pos=ins['offset']+added_before
        assert output[pos:pos+len(ins['addition'])]==ins['addition']
        offsets.append((pos,len(ins['addition'])))
        ins['output_offset']=pos
        added_before+=len(ins['addition'])
    for pos,count in reversed(offsets): del recovered[pos:pos+count]
    assert bytes(recovered)==old
    oldtags=re.findall(rb'\\tag\{([^}]+)\}',old)
    newtags=re.findall(rb'\\tag\{([^}]+)\}',output)
    additions=[x for x in newtags if x not in oldtags]
    assert len(additions)==len(set(additions)), (name,'duplicate addition tags')
    assert all(newtags.count(x)==oldtags.count(x) for x in oldtags)
    assert not re.search(rb'(?<!\\)\\\r?\n',b''.join(x['addition'] for x in insertions))
    dest=BASE/'replacement'/name
    write_identical_or_new(dest,output)
    receipt['files'].append({'name':name,'baseline_path':str(src),
     'baseline_sha256':sha(old),'baseline_bytes':len(old),
     'replacement_path':str(dest),'replacement_sha256':sha(output),'replacement_bytes':len(output),
     'baseline_removal_replay':'every byte identical','all_original_tags_retained':True,
     'new_tags':[x.decode() for x in additions],
     'insertions':[{k:v for k,v in ins.items() if k!='addition'}|{'added_bytes':len(ins['addition']),'added_sha256':sha(ins['addition'])} for ins in insertions]})
for name in ['relation_tail_control.tex','generator_degree_limit.tex','relation_row_correlations.tex']:
    p=BASE.parent/name; b=p.read_bytes()
    dest=BASE/'snapshots/proof_inputs'/name
    write_identical_or_new(dest,b)
    receipt['proof_inputs'].append({'path':str(p),'snapshot':str(dest),'bytes':len(b),'sha256':sha(b)})
rp=BASE/'INSERTION_RECEIPT.json'
write_identical_or_new(rp,(json.dumps(receipt,indent=2)+'\n').encode())
print(json.dumps({'receipt':str(rp),'sha256':sha(rp.read_bytes()),'files':receipt['files'],'proof_inputs':receipt['proof_inputs']},indent=2))
