"""Verify the included proof/program bytes and honest source provenance."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path


PACKAGE = Path(__file__).resolve().parent
ROOT = PACKAGE.parents[1]
MANIFEST = PACKAGE / 'package_manifest.json'


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def bounded_path(relative: str) -> Path:
    path = (ROOT / relative).resolve()
    if not path.is_relative_to(ROOT):
        raise ValueError(f'Package path leaves replay root: {relative}')
    return path


def mathematical_block(path: Path, start: str, end: str) -> bytes:
    data = path.read_bytes()
    # Original files can use CRLF; preserve every byte in the retained block.
    start_bytes, end_bytes = start.encode('utf-8'), end.encode('utf-8')
    if data.count(start_bytes) != 1 or data.count(end_bytes) != 1:
        raise AssertionError(f'Nonunique computation delimiters: {path.name}')
    left = data.index(start_bytes)
    right = data.index(end_bytes, left)
    if right <= left:
        raise AssertionError(f'Invalid computation interval: {path.name}')
    return data[left:right]


def verify_inventory() -> dict:
    manifest = json.loads(MANIFEST.read_text(encoding='utf-8'))
    if manifest['schema'] != 'coupled-viscous-portable-package-v1':
        raise AssertionError('Unexpected portable package schema')
    files = manifest['files_sha256']
    for relative, expected in files.items():
        actual = sha256(bounded_path(relative))
        if actual != expected:
            raise AssertionError(f'Included file SHA-256 mismatch: {relative}')
    for adaptation in manifest['replay_adaptations']:
        original = bounded_path(adaptation['original'])
        portable = bounded_path(adaptation['portable'])
        delimiters = adaptation['mathematical_block_delimiters']
        original_block = mathematical_block(original, **delimiters['original'])
        portable_block = mathematical_block(portable, **delimiters['portable'])
        if original_block != portable_block:
            raise AssertionError(f'Mathematical computation bytes changed: {portable.name}')
        if hashlib.sha256(original_block).hexdigest() != adaptation['mathematical_block_sha256']:
            raise AssertionError(f'Computation-block receipt mismatch: {portable.name}')
    source = json.loads((PACKAGE / 'provenance' / 'source_hash_receipt.json').read_text(encoding='utf-8'))
    if source['pdf_sha256'] != manifest['primary_source_pdf_sha256']:
        raise AssertionError('Historical source-hash receipts disagree')
    if source['pdf_included'] or source['pdf_verified_during_portable_replay']:
        raise AssertionError('Portable package cannot claim a fresh source PDF check')
    proofs = {relative: digest for relative, digest in files.items()
              if relative in manifest['canonical_proof_files']}
    if set(proofs) != set(manifest['canonical_proof_files']):
        raise AssertionError('Canonical proof inventory is incomplete')
    return {
        'package_manifest_sha256': sha256(MANIFEST),
        'verified_included_files': len(files),
        'canonical_proof_sha256': proofs,
        'mathematical_computation_blocks_byte_preserved': True,
        'source_pdf_sha256_historical': source['pdf_sha256'],
        'source_pdf_verified_during_this_replay': False,
        'source_pdf_included': False,
    }


def start_replay(script: str) -> tuple[dict, Path]:
    context = verify_inventory()
    context['portable_script_sha256'] = sha256(Path(script))
    output = ROOT / 'checks' / 'coupled_viscous'
    output.mkdir(parents=True, exist_ok=True)
    return context, output
