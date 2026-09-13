#!/usr/bin/env python3
"""Apply the same fail-closed parser to the seven spectral comparison targets."""
import json
import sys
from pathlib import Path
import check_restriction as core

core.TARGETS = {name:'SplitZero.RestrictionSpectrum.' for name in (
    'conjugate_power','moment_eq','prefix_eq','determinant_eq','log_volume_eq',
    'matrix_certificate','matrix_stopping_degree')}
if len(sys.argv) != 2:
    raise SystemExit('usage: check_spectrum_audit.py LOG')
reports = core.audit(Path(sys.argv[1]).read_text())
print(json.dumps({'status':'PASS','reports':reports},sort_keys=True))
