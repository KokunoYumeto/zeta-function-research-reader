"""Verify a complete successor and restore its exact immediate predecessor.

Run beside a logical 11_SOURCE_MAP.json, or beside the split-map transport:
  python restore_predecessor.py --destination predecessor19
With --verify-only no files are written. Objects are never executed.
Public restoration recovers the accepted public predecessor, not withheld
private historical bytes. All destinations must be new, unlinked directories.
"""
import argparse
import base64
import gzip
import hashlib
import json
from pathlib import Path


def require(ok, text):
    if not ok:
        raise ValueError(text)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def encode(value):
    return (json.dumps(value, ensure_ascii=False, indent=2) + '\n').encode('utf-8')


def checked(raw, row):
    require(type(row['bytes']) is int and row['bytes'] >= 0, 'Invalid size')
    require(len(raw) == row['bytes'] and sha(raw) == row['sha256'], 'Byte identity mismatch')
    return raw


def leaf(name):
    require(isinstance(name, str) and name not in ('', '.', '..') and
            not any(c in name for c in '/\\:<>"|?*') and
            not any(ord(c) < 32 for c in name) and not name.endswith((' ', '.')), 'Unsafe filename')
    require(name.split('.')[0].upper() not in {'CON','PRN','AUX','NUL','CLOCK$'} |
            {p+str(i) for p in ('COM','LPT') for i in range(1,10)}, 'Reserved filename')
    return name


def decode(obj):
    if obj['encoding'] == 'gzip+base64':
        packed = base64.b64decode(obj['payload'], validate=True)
        require(len(packed) == obj['compressed_bytes'], 'Compressed size mismatch')
        raw = gzip.decompress(packed)
    elif obj['encoding'] == 'utf8':
        raw = obj['text'].encode('utf-8')
    else:
        raise ValueError('Object is not publicly supplied')
    return checked(raw, {'sha256': obj.get('public_sha256', obj['sha256']),
                         'bytes': obj.get('public_bytes', obj['bytes'])})


def predecessor_map(mapping):
    recipe = mapping['immediate_predecessor_recipe']
    require(recipe['serialization'] == 'json-utf8-indent2-ensure_ascii_false-final_newline', 'Unknown serializer')
    result = {}
    for key in recipe['top_level_key_order']:
        result[key] = ({h: mapping['objects'][h] for h in recipe['object_key_order']}
                       if key == 'objects' else recipe['metadata_except_objects'][key])
    return checked(encode(result), recipe)


def verify(mapping, current):
    require(mapping['schema'] in ('native-rgc-complete-proof-archive-v1',
                                  'native-rgc-public-proof-archive-v1'), 'Unknown map schema')
    verified = withheld = 0
    for h, obj in mapping['objects'].items():
        require(h == obj['sha256'], 'Object key mismatch')
        if obj['encoding'] == 'withheld-private-provenance':
            require(not obj.get('supplied', True) and 'payload' not in obj and 'text' not in obj,
                    'Withheld object contains payload')
            withheld += 1
        else:
            decode(obj)
            verified += 1
    rows = mapping['output_manifest_except_self']
    require(len(rows) == 18 and len({r['name'].casefold() for r in rows}) == 18, 'Current membership mismatch')
    for row in rows:
        checked(current[leaf(row['name'])], row)
    old_raw = predecessor_map(mapping)
    old = json.loads(old_raw)
    require(mapping['aliases'][:len(old['aliases'])] == old['aliases'], 'Inherited aliases changed')
    old_rows = {r['name']: r for r in old['output_manifest_except_self']}
    old_rows['11_SOURCE_MAP.json'] = {'sha256': sha(old_raw), 'bytes': len(old_raw)}
    entries = mapping['complete_immediate_predecessor19']
    require(len(entries) == 19 and {r['name'] for r in entries} == set(old_rows), 'Predecessor membership mismatch')
    restored = {}
    for row in entries:
        require(all(row[k] == old_rows[row['name']][k] for k in ('sha256','bytes')), 'Predecessor row mismatch')
        raw = old_raw if row['name'] == '11_SOURCE_MAP.json' else decode(mapping['objects'][row['sha256']])
        restored[leaf(row['name'])] = checked(raw, row)
    reversals = mapping['rgc_source_reversals']
    require(len(reversals) == 3 and {r['name'] for r in reversals} ==
            {'09_UPDATED_JOINT_NOTE.tex','10_UPDATED_SIGNED_RETURN.tex','14_CURRENT_KERNEL_AND_MULTIPLICITY_PROOFS.tex'},
            'Source reversal membership mismatch')
    for row in reversals:
        raw = checked(current[row['name']], row)
        for op in reversed(row['operations']):
            data = decode(mapping['objects'][op['sha256']])
            require(len(data) == op['bytes'], 'Insertion size mismatch')
            start = op['offset']
            require(type(start) is int and 0 <= start <= len(raw)-len(data), 'Bad insertion offset')
            require(raw[start:start+len(data)] == data, 'Insertion byte mismatch')
            raw = raw[:start] + raw[start+len(data):]
        require(raw == restored[row['name']], 'Source reversal mismatch')
    return restored, {'verified_supplied_objects':verified, 'withheld_hash_only_objects':withheld,
                      'current_files':19, 'predecessor_files':19, 'exact_source_reversals':3}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--destination', type=Path)
    p.add_argument('--verify-only', action='store_true')
    p.add_argument('--source', type=Path, help='Logical edition directory; default is beside this script')
    args = p.parse_args()
    here = args.source.resolve() if args.source else Path(__file__).resolve().parent
    map_path = here/'11_SOURCE_MAP.json'
    if map_path.exists():
        raw = map_path.read_bytes()
    else:
        import importlib.util
        spec = importlib.util.spec_from_file_location('source_decoder', here/'restore_source_map.py')
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        restore_map = module.restore_map
        raw = restore_map(here)
    mapping = json.loads(raw)
    current = {r['name']: (here/leaf(r['name'])).read_bytes() for r in mapping['output_manifest_except_self']}
    restored, result = verify(mapping, current)
    if not args.verify_only:
        require(args.destination is not None, 'Destination required')
        unresolved = args.destination.absolute()
        require(not any(p.is_symlink() or getattr(p,'is_junction',lambda:False)()
                        for p in (unresolved, *unresolved.parents)), 'Linked unresolved destination ancestry')
        target = args.destination.resolve()
        require(not target.exists() and not args.destination.is_symlink(), 'Destination must be new')
        require(not any(p.is_symlink() or getattr(p,'is_junction',lambda:False)() for p in target.parents), 'Linked parent')
        target.mkdir(parents=True)
        for name, data in restored.items():
            with (target/name).open('xb') as stream:
                stream.write(data)
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
