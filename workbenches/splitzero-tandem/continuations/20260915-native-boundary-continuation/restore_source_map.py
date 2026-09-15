"""Restore the complete public source map, or one exact chosen provenance object.

Run beside SOURCE_MAP_TRANSPORT.json and its declared gzip part files:
    python restore_source_map.py
Default writes 11_SOURCE_MAP.json only after its exact digest is verified.
Use --folder RESTORED_17 to create a separate folder containing exactly the
seventeen logical files, with no decoder or transport helper in that folder.
Optional --object ORIGINAL_SHA --output FILE restores one chosen object, never
an archived path. Original object keys are lineage identities; a locator-only
public derivative has explicit public_sha256/public_bytes fields.
"""
import argparse
import base64
import gzip
import hashlib
import json
from pathlib import Path


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def checked(raw, identity):
    if len(raw) != identity['bytes'] or digest(raw) != identity['sha256']:
        raise ValueError('Length or SHA-256 mismatch')
    return raw


def decode_object(obj):
    if obj['encoding'] == 'utf8':
        raw = obj['text'].encode('utf-8')
    elif obj['encoding'] == 'gzip+base64':
        raw = gzip.decompress(base64.b64decode(obj['payload'], validate=True))
    else:
        raise ValueError('Unknown object encoding')
    return checked(raw, {'bytes': obj.get('public_bytes', obj['bytes']),
                         'sha256': obj.get('public_sha256', obj['sha256'])})


def restore_map(directory):
    manifest = json.loads((directory/'SOURCE_MAP_TRANSPORT.json').read_bytes())
    compressed_identity = manifest['compressed']
    if 'parts' in compressed_identity:
        chunks = []
        names = set()
        for row in compressed_identity['parts']:
            name = row['path']
            if (not isinstance(name, str) or name in ('', '.', '..')
                    or any(char in name for char in '/\\:\0') or name in names):
                raise ValueError('Unsafe or repeated gzip part name')
            names.add(name)
            source = directory/name
            if source.is_symlink():
                raise ValueError('Refusing a linked gzip part')
            chunks.append(checked(source.read_bytes(), row))
        compressed = checked(b''.join(chunks), compressed_identity)
    else:
        compressed = checked((directory/compressed_identity['path']).read_bytes(), compressed_identity)
    return checked(gzip.decompress(compressed), manifest['logical_source_map'])


def restore_folder(directory, target):
    directory = directory.resolve()
    if target.is_symlink():
        raise ValueError('Refusing a linked restore folder')
    target = target.resolve()
    if target == directory:
        raise ValueError('Choose a separate seventeen-file folder')
    manifest = json.loads((directory/'SOURCE_MAP_TRANSPORT.json').read_bytes())
    rows = manifest['logical_files']
    payload = {}
    for row in rows:
        name = row['path']
        if (not isinstance(name, str) or name in ('', '.', '..')
                or any(char in name for char in '/\\:\0') or name in payload):
            raise ValueError('Unsafe or repeated logical filename')
        source = directory/name
        if name == '11_SOURCE_MAP.json':
            raw = restore_map(directory)
        else:
            if source.is_symlink():
                raise ValueError('Refusing a linked source file')
            raw = source.read_bytes()
        payload[name] = checked(raw, row)
    if len(payload) != 17 or '11_SOURCE_MAP.json' not in payload:
        raise ValueError('Not the complete seventeen-file logical edition')
    if target.exists():
        if not target.is_dir() or any(p.name not in payload for p in target.iterdir()):
            raise ValueError('Restore target has unrelated entries')
        for name, raw in payload.items():
            existing = target/name
            if existing.exists() and (existing.is_symlink() or not existing.is_file()
                                      or existing.read_bytes() != raw):
                raise ValueError('Refusing to overwrite different existing bytes')
    else:
        target.mkdir(parents=True)
    for name, raw in payload.items():
        output = target/name
        if not output.exists():
            with output.open('xb') as stream:
                stream.write(raw)
    if {p.name for p in target.iterdir()} != set(payload):
        raise ValueError('Restored folder does not contain exactly seventeen files')
    return {'status': 'restored_exact_seventeen_logical_files', 'files': 17,
            'directory': str(target)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--object', help='Original SHA-256 object key')
    parser.add_argument('--output', type=Path)
    parser.add_argument('--folder', type=Path, help='Separate exact seventeen-file restore folder')
    args = parser.parse_args()
    if args.folder is not None:
        if args.object or args.output:
            raise ValueError('--folder cannot be combined with --object or --output')
        print(json.dumps(restore_folder(Path(__file__).resolve().parent, args.folder)))
        return
    raw = restore_map(Path(__file__).resolve().parent)
    if args.object:
        if args.output is None:
            raise ValueError('--output is required when extracting an object')
        data = json.loads(raw)
        obj = data['objects'][args.object]
        if obj['sha256'] != args.object:
            raise ValueError('Original object key mismatch')
        raw = decode_object(obj)
        target = args.output
    else:
        target = args.output or Path(__file__).resolve().parent/'11_SOURCE_MAP.json'
    if target.exists():
        if target.read_bytes() != raw:
            raise ValueError('Refusing to overwrite different existing bytes')
    else:
        with target.open('xb') as stream:
            stream.write(raw)
    print(json.dumps({'status': 'restored_verified_public_bytes',
                      'bytes': len(raw), 'sha256': digest(raw),
                      'output': str(target)}))


if __name__ == '__main__':
    main()
