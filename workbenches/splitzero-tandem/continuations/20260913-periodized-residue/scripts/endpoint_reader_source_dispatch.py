"""Complete endpoint source dispatch; imported only by the copied reader."""
import hashlib
import json
from pathlib import Path
from endpoint_source_appendix_adapter import prepare_endpoint_witness

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def prepare_endpoint_sources(builder):
    root = builder.ROOT
    spec = json.loads((root / 'sources/endpoint_reader_integration/CONVERSION_SPEC.json').read_text(encoding='utf-8'))
    inherited = json.loads((root / 'sources/endpoint_reader_baseline/SOURCE_RECEIPT.json').read_text(encoding='utf-8'))
    wrapper = root / 'sources/endpoint_reader_baseline/SOURCE_APPENDICES.tex'
    if sha(wrapper) != spec['inherited_wrapper_sha256']:
        raise RuntimeError('Inherited complete appendix wrapper changed')
    for name, expected in spec['inherited_source_inputs'].items():
        path = root / name
        if sha(path) != expected['sha256'] or path.stat().st_size != expected['bytes']:
            raise RuntimeError('Inherited complete raw/converted source changed: ' + name)
    appended = [wrapper.read_text(encoding='utf-8')]
    rows = list(inherited)
    conversions = []
    for witness in spec['witnesses']:
        full_wrapper, row = prepare_endpoint_witness(builder, witness)
        target = builder.BUILD / ('endpoint_' + witness['key'] + '_wrapper.tex')
        target.write_text(full_wrapper, encoding='utf-8', newline='')
        row['reader_location'] = witness['location']
        row['wrapper'] = target.relative_to(root).as_posix()
        row['wrapper_sha256'] = sha(target)
        if witness['location'] == 'appendix':
            appended.append(full_wrapper)
        rows.append(row)
        conversions.append(row)
    (builder.BUILD / 'source_appendices.tex').write_text('\n'.join(appended), encoding='utf-8', newline='')
    (builder.BUILD / 'source_receipt.json').write_text(json.dumps(rows, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    (builder.BUILD / 'endpoint_source_conversion_index.json').write_text(json.dumps(conversions, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    return rows
