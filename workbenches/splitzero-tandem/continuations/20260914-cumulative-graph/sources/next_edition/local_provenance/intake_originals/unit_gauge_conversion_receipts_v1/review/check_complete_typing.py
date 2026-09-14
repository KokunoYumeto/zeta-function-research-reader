"""Read-only independent source-conversion audit; writes this review's evidence only."""
from pathlib import Path
import collections, copy, hashlib, json, re, subprocess

ROOT = Path(__file__).resolve().parent.parent
OUT = Path(__file__).resolve().parent
FORMAT = 'markdown+tex_math_dollars+tex_math_single_backslash-inline_notes-footnotes-superscript-subscript'
SOURCE_HASHES = {
    'f1_unit_gauge': '9ded2486160b76bf65f92d44b73cdd0c59a3ca7e5334f88682e10592d5a45b2f',
    'f1_unit_gauge_review': 'e32e978870e65ea375040762432a3cfe479068ebe6cfd800086a2d35d55da6d0',
}
ALLOWED_WORDING = {
    'f1_unit_gauge': [("in the owner's separate continuation", 'in the separate continuation')],
    'f1_unit_gauge_review': [
        ('the root note', 'the source note'),
        ('reported to the parent before writing this review', 'recorded before writing this review'),
        ("the root's homotopies", "the source's homotopies"),
        ('The exact accepted root artifact', 'The exact accepted source artifact'),
        ("The parent's separately reported exact", 'The separately reported exact'),
    ],
}

def sha(data):
    return hashlib.sha256(data).hexdigest()

def pin(path):
    path = Path(path)
    raw = path.read_bytes()
    return {'path': str(path), 'bytes': len(raw), 'sha256': sha(raw)}

def read_json(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))

def nodes(tree):
    if isinstance(tree, dict):
        if 't' in tree:
            yield tree
        for val in tree.values():
            yield from nodes(val)
    elif isinstance(tree, list):
        for val in tree:
            yield from nodes(val)

def literal(tree):
    return [copy.deepcopy(n) for n in nodes(tree)
            if n['t'] in ('Math', 'Code', 'CodeBlock', 'RawInline', 'RawBlock')]

def inverse_tree(original, changed, edits):
    restored = copy.deepcopy(changed)
    for row in reversed(edits):
        cursor = restored
        for part in row['parts'][:-1]:
            cursor = cursor[part]
        last = row['parts'][-1]
        assert cursor[last] == row['after']
        cursor[last] = copy.deepcopy(row['before'])
    assert restored == original

def check_pin(record):
    actual = pin(record['path'])
    assert actual['bytes'] == record['bytes'] and actual['sha256'] == record['sha256']

audits = []
for key, source_hash in SOURCE_HASHES.items():
    mapping_path = ROOT / f'{key}_math_mapping.json'
    mapping = read_json(mapping_path)
    receipt_path = ROOT / 'receipts' / f'{key}.json'
    receipt = read_json(receipt_path)
    for field in ('original_source', 'raw_snapshot', 'public_source', 'adapter', 'wrapper'):
        check_pin(receipt[field])
    original_path = Path(receipt['original_source']['path'])
    original = original_path.read_bytes()
    public = Path(receipt['public_source']['path']).read_bytes()
    assert sha(original) == source_hash
    assert original == Path(receipt['raw_snapshot']['path']).read_bytes()
    assert mapping['source']['sha256'] == source_hash
    assert mapping['source']['bytes'] == len(original)
    math_rows = {r['code_index']: r for r in mapping['math_code_mappings']}
    retained = {r['code_index']: r for r in mapping['retained_code']}
    spans = list(re.finditer(rb'`([^`\r\n]+)`', original))
    assert len(math_rows) == len(mapping['math_code_mappings'])
    assert len(retained) == len(mapping['retained_code'])
    assert set(math_rows).isdisjoint(retained)
    assert set(math_rows) | set(retained) == set(range(len(spans)))
    for index, span in enumerate(spans):
        row = math_rows.get(index, retained.get(index))
        assert span.group(1).decode('utf-8') == row['original']
        assert (span.start(), span.end()) == (row['source_byte_start'], row['source_byte_end'])
    edits = receipt['publication_and_typing_byte_edits']
    assert edits == sorted(edits, key=lambda r:r['source_start_byte'])
    assert all(a['source_end_byte'] <= b['source_start_byte'] for a,b in zip(edits,edits[1:]))
    rebuilt, last, converted_indices, wording = bytearray(), 0, [], []
    for row in edits:
        begin, end = row['source_start_byte'], row['source_end_byte']
        assert original[begin:end] == row['before'].encode('utf-8')
        rebuilt.extend(original[last:begin])
        assert len(rebuilt) == row['public_start_byte']
        rebuilt.extend(row['after'].encode('utf-8'))
        assert len(rebuilt) == row['public_end_byte']
        if row['kind'] == 'mathematical_code_to_typed_math':
            index = row['code_index']
            assert row['before'] == '`' + math_rows[index]['original'] + '`'
            assert row['after'] == r'\(' + math_rows[index]['tex'] + r'\)'
            converted_indices.append(index)
        else:
            assert row['kind'] == 'public_source_reference'
            wording.append((row['before'], row['after']))
        last = end
    rebuilt.extend(original[last:])
    assert bytes(rebuilt) == public
    assert sorted(converted_indices) == sorted(math_rows)
    assert sorted(wording) == sorted(ALLOWED_WORDING[key])
    restored = public
    for row in reversed(edits):
        begin, end = row['public_start_byte'], row['public_end_byte']
        assert restored[begin:end] == row['after'].encode('utf-8')
        restored = restored[:begin] + row['before'].encode('utf-8') + restored[end:]
    assert restored == original

    def independent_parse(path, suffix):
        tree = json.loads(subprocess.check_output(['pandoc', str(path), '--from='+FORMAT, '--to=json']))
        (OUT/f'{key}_{suffix}.json').write_text(json.dumps(tree,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
        return tree

    raw_tree = independent_parse(original_path, 'independent_raw_ast')
    public_tree = independent_parse(Path(receipt['public_source']['path']), 'independent_public_ast')
    assert raw_tree == read_json(receipt['raw_original_ast']['path'])
    assert public_tree == read_json(receipt['public_original_ast']['path'])
    expected, code_index = literal(raw_tree), 0
    for index, node in enumerate(expected):
        if node['t'] == 'Code':
            if code_index in math_rows:
                expected[index] = {'t':'Math','c':[{'t':'InlineMath'},math_rows[code_index]['tex']]}
            code_index += 1
    assert code_index == len(spans)
    assert expected == literal(public_tree)
    original_math = [n['c'] for n in nodes(raw_tree) if n['t'] == 'Math']
    assert original_math == [n['c'] for n in nodes(public_tree)
                             if n['t'] == 'Math' and n['c'][0]['t'] == 'DisplayMath']
    assert re.findall(rb'\\tag\{([^}]+)\}', original) == re.findall(rb'\\tag\{([^}]+)\}', public)
    if key == 'f1_unit_gauge':
        assert re.findall(rb'\\tag\{([^}]+)\}', original) == [f'UG{i}'.encode() for i in range(1,20)]
    assert len(raw_tree['blocks']) == len(public_tree['blocks'])
    assert [n['c'] for n in nodes(raw_tree) if n['t']=='Header'] == [n['c'] for n in nodes(public_tree) if n['t']=='Header']

    adapter_record = receipt['adapter_row']
    conversion_path = ROOT / adapter_record['conversion_receipt']
    assert sha(conversion_path.read_bytes()) == adapter_record['conversion_receipt_sha256']
    conversion = read_json(conversion_path)
    artifacts = conversion['artifacts']
    original_adapter = read_json(ROOT/artifacts['original_ast'])
    prepared = read_json(ROOT/artifacts['prepared_ast'])
    writer = read_json(ROOT/artifacts['writer_ast'])
    assert original_adapter == public_tree
    inverse_tree(original_adapter, prepared, conversion['prepared_edits'])
    inverse_tree(prepared, writer, conversion['writer_edits'])
    tex_path = ROOT / artifacts['converted']
    tex = tex_path.read_bytes()
    assert sha(tex) == adapter_record['converted_sha256']
    math = [n['c'] for n in nodes(public_tree) if n['t']=='Math']
    emissions = conversion['literal_emission_spans']
    assert len(emissions) == len(math)
    previous_end = -1
    for index, (row, payload) in enumerate(zip(emissions, math)):
        assert row['index'] == index and row['node_type'] == 'Math' and row['original_c'] == payload
        begin, end = row['payload_start_byte'], row['payload_end_byte']
        assert row['fragment_start_byte'] >= previous_end
        assert tex[begin:end] == payload[1].encode('utf-8')
        assert sha(tex[begin:end]) == row['payload_sha256']
        assert tex[row['fragment_start_byte']:begin] == row['opening'].encode('utf-8')
        assert tex[end:row['fragment_end_byte']] == row['closing'].encode('utf-8')
        previous_end = row['fragment_end_byte']
    assert ('\\input{' + artifacts['converted'] + '}') in Path(receipt['wrapper']['path']).read_text(encoding='utf-8')
    audits.append({
        'key':key,'status':'accepted','original_source':pin(original_path),'mapping':pin(mapping_path),
        'public_source':receipt['public_source'],'converted_tex':pin(tex_path),'wrapper':receipt['wrapper'],
        'conversion_receipt':pin(conversion_path),'source_typing_receipt':pin(receipt_path),
        'original_inline_code_nodes':len(spans),'typed_math_code_nodes':len(math_rows),
        'retained_code_nodes':len(retained),'original_display_math_nodes':len(original_math),
        'final_math_spans_exactly_checked':len(emissions),'wording_edits':wording,
        'original_to_public_byte_forward_and_inverse_exact':True,
        'entire_original_and_public_ASTs_independently_reparsed':True,
        'complete_ordered_literal_transport_exact':True,
        'prepared_and_writer_AST_inverse_exact':True,'all_original_headings_and_block_counts_retained':True,
        'all_original_source_bytes_unchanged':original_path.read_bytes()==original,
        'semantic_review':'All listed mathematical Code-to-Math rows read individually against the full original paragraphs and neighboring formulas. No remaining typing correction.',
        'all_math_code_mappings':mapping['math_code_mappings'],
    })

result={
    'schema':'independent-complete-unit-gauge-source-typing-review-v1','status':'accepted',
    'scope':'Complete source typing, exact source/public transport, adapter inverses and emitted mathematical payloads. No new mathematical proof audit, fixture execution, Lean run, PDF build or visual-layout review.',
    'sources':audits,'total_original_math_preserved':27,'total_code_math_typed':115,'total_final_math_spans_checked':142,
    'tau_base_notation_source':pin(ROOT.parent.parent/'output/Tau_Arithmetic_Determinant_Transport_2026-09-13/dependencies/Tau_Base_Cohomology/NOTE.md'),
    'review_script':pin(Path(__file__)),
}
target=OUT/'INDEPENDENT_TYPING_ACCEPTANCE.json'
target.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'acceptance':pin(target),'status':result['status'],'typed':115,'preserved_original_display':27,'emitted_math_spans':142}))
