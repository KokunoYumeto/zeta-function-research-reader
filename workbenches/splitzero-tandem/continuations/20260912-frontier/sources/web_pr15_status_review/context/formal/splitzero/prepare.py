#!/usr/bin/env python3
"""Materialize the byte-pinned original SplitZero core; never modify its contents."""
import hashlib
import pathlib
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent
URL = ('https://raw.githubusercontent.com/KokunoYumeto/modern-latex-manuscripts/'
       'f7ff59b176c7dc3941babd4cb9272dffc653070d/formalization/lean/'
       'classical_candidates_20260626/split_support_sidecar/SplitZero.lean')
EXPECTED = 'ff991f7383922e71cdf0e4a3bc85e89e18f808ef'
p = ROOT / 'SplitZero.lean'
data = p.read_bytes() if p.exists() else urllib.request.urlopen(URL, timeout=60).read()
blob = hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()
if blob != EXPECTED:
    raise SystemExit(f'Original SplitZero blob mismatch: {blob}')
data.decode('utf-8')
p.write_bytes(data)
print(f'Original SplitZero verified: {blob}; {len(data)} bytes')
