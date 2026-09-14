"""Verify the AT clarification using bytes only; no TeX or mathematical code runs."""
import argparse
import base64
import hashlib
import json
from pathlib import Path


def require(value, message):
    if not value:
        raise ValueError(message)


def pin(data):
    return {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}


def check(data, expected, label):
    require(pin(data) == {k: expected[k] for k in ('bytes', 'sha256')}, label)


def decode(value):
    return base64.b64decode(value, validate=True)


def verify(artifact_root, recipe):
    root = Path(artifact_root).resolve()
    inputs = {}
    for label, spec in recipe['sealed_inputs'].items():
        path = (root / spec['path']).resolve()
        require(path.is_relative_to(root), 'Input leaves the named artifact root')
        data = path.read_bytes()
        check(data, spec, label + ': sealed input pin')
        inputs[label] = data
    original = inputs['original_source']
    reader = inputs['accepted_reader']
    extraction = json.loads(inputs['body_extraction'])
    layout = json.loads(inputs['layout_map'])
    original_body = extraction['original_body'].encode('utf-8')
    prefix = decode(recipe['body_prefix_removed_base64'])
    require(original_body.startswith(prefix), 'Exact original title prefix')
    pre_lf = original_body[len(prefix):]
    require(b'\r' not in pre_lf, 'The retained original body uses LF')
    pre_crlf = pre_lf.replace(b'\n', b'\r\n')
    check(pre_lf, recipe['frames']['pre_layout_LF'], 'Complete pre-layout LF body')
    check(pre_crlf, recipe['frames']['pre_layout_CRLF'], 'Complete pre-layout CRLF body')
    lf, crlf = pre_lf, pre_crlf
    require(len(layout['changes']) == len(recipe['layout_steps']) == 10, 'All ten layout edits')
    for i, (source_change, step) in enumerate(zip(layout['changes'], recipe['layout_steps']), 1):
        require(step['step'] == i, 'Layout order')
        old, new = (source_change[k].encode('utf-8') for k in ('old', 'new'))
        require(old == decode(step['old_LF_base64']) and new == decode(step['new_LF_base64']),
                'Complete original layout payloads')
        old_crlf, new_crlf = (s.replace(b'\n', b'\r\n') for s in (old, new))
        require(lf.count(old) == crlf.count(old_crlf) == 1, 'Unique layout source spans')
        require(lf.index(old) == step['source_span_LF']['start'] and
                crlf.index(old_crlf) == step['source_span_CRLF']['start'], 'Exact layout span starts')
        check(lf, step['before_LF'], 'Intermediate LF source')
        check(crlf, step['before_CRLF'], 'Intermediate CRLF source')
        lf, crlf = lf.replace(old, new), crlf.replace(old_crlf, new_crlf)
        check(lf, step['after_LF'], 'Intermediate LF target')
        check(crlf, step['after_CRLF'], 'Intermediate CRLF target')
    check(lf, recipe['frames']['post_layout_LF'], 'Complete final LF body')
    check(crlf, recipe['frames']['post_layout_CRLF'], 'Complete final CRLF body')
    require(crlf == reader, 'Final CRLF body is every accepted reader byte')
    require(reader.replace(b'\r\n', b'\n') == lf, 'Exact final reader LF frame')
    require(hashlib.sha256(lf).hexdigest() == extraction['pre_layout_reader_body_sha256'],
            'The legacy-named field identifies final LF bytes')
    backwards = reader
    for step in reversed(recipe['layout_steps']):
        old = decode(step['old_LF_base64']).replace(b'\n', b'\r\n')
        new = decode(step['new_LF_base64']).replace(b'\n', b'\r\n')
        require(backwards.count(new) == 1, 'Unique reverse layout target')
        backwards = backwards.replace(new, old)
    require(backwards == pre_crlf, 'All ten inverse transformations recover pre-layout CRLF bytes')
    inverse_body = prefix + backwards.replace(b'\r\n', b'\n')
    require(inverse_body == original_body, 'Full original body including removed title prefix')
    parts = [extraction['preamble'].encode('utf-8'), b'\\begin{document}', inverse_body,
             b'\\end{document}', extraction['postamble'].encode('utf-8')]
    cursor = 0
    for component, data in zip(recipe['original_file_components'], parts):
        require(component['start'] == cursor and component['end'] == cursor + len(data),
                'Exact source component offsets')
        check(data, component, 'Exact source component pin')
        require(original[cursor:cursor + len(data)] == data, 'Exact source component bytes')
        cursor += len(data)
    require(cursor == len(original) and b''.join(parts) == original,
            'Complete original preamble, boundaries, body and postamble reconstructed')
    return {
        'status': 'verified-exact-current-AT-source-reconstruction',
        'legacy_field_identified_as': 'post-layout complete reader body in LF encoding',
        'all_ten_layout_steps_and_inverses_verified': True,
        'full_original_file_restored_byte_for_byte': True,
        'original_file': pin(original), 'accepted_reader': pin(reader),
        'frames': recipe['frames'], 'mathematical_code_executed': False,
        'TeX_or_other_build_executed': False, 'sealed_inputs_modified': False,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--artifact-root', required=True)
    parser.add_argument('--recipe', default=str(Path(__file__).with_name('CLARIFICATION.json')))
    args = parser.parse_args()
    recipe = json.loads(Path(args.recipe).read_bytes())
    print(json.dumps(verify(args.artifact_root, recipe), indent=2))


if __name__ == '__main__':
    main()
