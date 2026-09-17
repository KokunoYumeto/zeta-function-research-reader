"""Restore the manifest's complete logical edition or a chosen provenance object.

Run beside SOURCE_MAP_TRANSPORT.json and its declared gzip part files:
    python restore_source_map.py
Default restores the logical source-map filename declared by the manifest.
Use --folder RESTORED to create a separate folder containing exactly the
manifest's logical files, with no decoder or transport helpers in that folder.
Each part, the ordered aggregate and the logical map are digest-checked.
Optional --object ORIGINAL_SHA --output FILE restores one chosen object,
never an archived path. Public locator derivatives retain explicit identities.
No source, archive or restored object is executed.
"""
import argparse
import base64
import gzip
import hashlib
import json
from pathlib import Path

MANIFEST_NAME = 'SOURCE_MAP_TRANSPORT.json'


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def checked(raw, identity):
    size = identity['bytes']
    checksum = identity['sha256']
    if (type(size) is not int or size < 0 or not isinstance(checksum, str)
            or len(checksum) != 64 or any(c not in '0123456789abcdef' for c in checksum)):
        raise ValueError('Invalid declared byte identity')
    if len(raw) != size or digest(raw) != checksum:
        raise ValueError('Length or SHA-256 mismatch')
    return raw


def flat_name(name):
    if (not isinstance(name, str) or name in ('', '.', '..')
            or any(ord(c) < 32 or c in '/\\:<>"|?*' for c in name)
            or name.endswith((' ', '.'))):
        raise ValueError('Unsafe flat filename')
    stem = name.split('.')[0].upper()
    reserved = {'CON', 'PRN', 'AUX', 'NUL', 'CLOCK$'}
    reserved.update(prefix + str(i) for prefix in ('COM', 'LPT') for i in range(1, 10))
    if stem in reserved:
        raise ValueError('Reserved flat filename')
    return name


def linked(path):
    return path.is_symlink() or getattr(path, 'is_junction', lambda: False)()


def read_plain(path):
    if linked(path) or not path.is_file():
        raise ValueError('Expected an unlinked regular input file')
    return path.read_bytes()


def read_manifest(directory):
    if linked(directory) or not directory.is_dir():
        raise ValueError('Expected an unlinked input directory')
    return json.loads(read_plain(directory / MANIFEST_NAME))


def part_rows(manifest):
    compressed = manifest['compressed']
    flat_name(compressed['path'])
    rows = compressed.get('parts', [compressed])
    if not isinstance(rows, list) or not rows:
        raise ValueError('Missing ordered compressed payload')
    names = [flat_name(row['path']) for row in rows]
    if len(set(name.casefold() for name in names)) != len(names):
        raise ValueError('Repeated compressed payload filename')
    return rows


def map_bytes(directory, manifest):
    flat_name(manifest['logical_source_map']['path'])
    chunks = [checked(read_plain(directory / row['path']), row)
              for row in part_rows(manifest)]
    compressed = checked(b''.join(chunks), manifest['compressed'])
    return checked(gzip.decompress(compressed), manifest['logical_source_map'])


def restore_map(directory):
    directory = Path(directory)
    return map_bytes(directory, read_manifest(directory))


def logical_rows(manifest):
    rows = manifest['logical_files']
    count = manifest['logical_file_count']
    if type(count) is not int or count <= 0 or not isinstance(rows, list) or len(rows) != count:
        raise ValueError('Logical membership/count differs from manifest')
    map_identity = manifest['logical_source_map']
    map_name = flat_name(map_identity['path'])
    names = [flat_name(row['path']) for row in rows]
    if len(set(name.casefold() for name in names)) != count or names.count(map_name) != 1:
        raise ValueError('Repeated logical name or missing logical source map')
    helpers = {MANIFEST_NAME, Path(__file__).name, manifest['compressed']['path']}
    helpers.update(row['path'] for row in part_rows(manifest))
    if 'decoder' in manifest:
        helpers.add(flat_name(manifest['decoder']['path']))
    if {name.casefold() for name in names} & {name.casefold() for name in helpers}:
        raise ValueError('Transport helpers are not logical edition files')
    row = rows[names.index(map_name)]
    if any(row[key] != map_identity[key] for key in ('bytes', 'sha256')):
        raise ValueError('Logical source-map identities disagree')
    return rows


def restore_folder(directory, target):
    directory = Path(directory)
    target = Path(target)
    if linked(directory) or linked(target):
        raise ValueError('Refusing a linked input or restore folder')
    directory = directory.resolve()
    target = target.resolve()
    if target == directory:
        raise ValueError('Choose a separate logical-edition folder')
    manifest = read_manifest(directory)
    rows = logical_rows(manifest)
    map_name = manifest['logical_source_map']['path']
    payload = {}
    # Verify every input before creating or changing the destination folder.
    for row in rows:
        name = row['path']
        raw = map_bytes(directory, manifest) if name == map_name else read_plain(directory / name)
        payload[name] = checked(raw, row)
    if target.exists():
        if not target.is_dir() or any(p.name not in payload for p in target.iterdir()):
            raise ValueError('Restore target has unrelated entries')
        for name, raw in payload.items():
            existing = target / name
            if linked(existing) or (existing.exists() and read_plain(existing) != raw):
                raise ValueError('Refusing to overwrite different existing bytes')
    else:
        target.mkdir(parents=True)
    for name, raw in payload.items():
        output = target / name
        if not output.exists():
            with output.open('xb') as stream:
                stream.write(raw)
    if {p.name for p in target.iterdir()} != set(payload):
        raise ValueError('Restored folder differs from exact logical membership')
    return {'status': 'restored_exact_logical_files', 'files': len(payload),
            'directory': str(target)}


def decode_object(obj):
    if obj['encoding'] == 'utf8':
        raw = obj['text'].encode('utf-8')
    elif obj['encoding'] == 'gzip+base64':
        raw = gzip.decompress(base64.b64decode(obj['payload'], validate=True))
    else:
        raise ValueError('Unknown object encoding')
    return checked(raw, {'bytes': obj.get('public_bytes', obj['bytes']),
                         'sha256': obj.get('public_sha256', obj['sha256'])})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--object', help='Original SHA-256 object key')
    parser.add_argument('--output', type=Path)
    parser.add_argument('--folder', type=Path, help='Separate exact logical-edition restore folder')
    args = parser.parse_args()
    directory = Path(__file__).resolve().parent
    if args.folder is not None:
        if args.object or args.output:
            raise ValueError('--folder cannot be combined with --object or --output')
        print(json.dumps(restore_folder(directory, args.folder)))
        return
    manifest = read_manifest(directory)
    raw = map_bytes(directory, manifest)
    if args.object:
        if args.output is None:
            raise ValueError('--output is required when extracting an object')
        obj = json.loads(raw)['objects'][args.object]
        if obj['sha256'] != args.object:
            raise ValueError('Original object key mismatch')
        raw = decode_object(obj)
        target = args.output
    else:
        target = args.output or directory / flat_name(manifest['logical_source_map']['path'])
    if linked(target) or (target.exists() and read_plain(target) != raw):
        raise ValueError('Refusing to overwrite different existing bytes')
    if not target.exists():
        with target.open('xb') as stream:
            stream.write(raw)
    print(json.dumps({'status': 'restored_verified_public_bytes',
                      'bytes': len(raw), 'sha256': digest(raw), 'output': str(target)}))


if __name__ == '__main__':
    main()
