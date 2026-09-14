"""Assemble this local reader from frozen, attributed proof inputs.

Run from the mathematical workspace. This script performs no network or
publication operation. Original proof bytes are retained in the repository;
the included copies only namespace LaTeX cross-reference identifiers.
"""
from pathlib import Path
import hashlib
import json
import re
import shutil

ROOT = Path(__file__).resolve().parents[1]
WORKSPACE = ROOT.parents[1]
AUDIT = WORKSPACE / 'work/rh_counterfactual_20260913/shared_thread_audit'
PEER = WORKSPACE / 'output/tau_f1_transcript_audit_2026-09-13/proofs'
FROZEN = WORKSPACE / 'output/split_zero_rh_tandem_2026-09-12/current_source_20260913_periodized_residue'

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def copy_tree_once(source, target):
    if not target.exists():
        shutil.copytree(source, target)

def assemble():
    for name in ['tex/modules', 'proof_inputs', 'audit', 'provenance', 'build']:
        (ROOT / name).mkdir(parents=True, exist_ok=True)
    copy_tree_once(FROZEN, ROOT / 'original_programme')
    for name in ['Tau_Arithmetic_Determinant_Transport_2026-09-13',
                 'Tau_Relation_Window_Spectral_Transport_2026-09-13']:
        copy_tree_once(WORKSPACE / 'output' / name, ROOT / 'companion_sources' / name)
    for segment in ['segment01_15', 'segment16_28', 'segment29_40', 'segment41_54', 'segment55_67']:
        shutil.copytree(AUDIT / segment, ROOT / 'audit' / segment, dirs_exist_ok=True)
    for name in ['COVERAGE.json', 'INDEPENDENT_CAPTURE_COMPARISON.json',
                 'THIS_SESSION_USER_INPUTS_VERBATIM.md', 'TRANSCRIPT_USER_INPUTS.md',
                 'VISIBLE_TRANSCRIPT.md', 'TRANSCRIPT_FULL.md', 'transcript_records.json',
                 'share_conversation.json', 'shared_public_response.html',
                 'decode_shared_source.py', 'prior_session_attachment.txt',
                 'program_resume_attachment.txt', 'prior_session_audit.md',
                 'balanced_independent_review.md', 'tau_and_cocycle_full_read_review.md']:
        shutil.copy2(AUDIT / name, ROOT / 'provenance' / name)
    shutil.copytree(AUDIT / 'turns', ROOT / 'provenance/turns', dirs_exist_ok=True)
    entries = [
      ('TAU', PEER / 'tau_exact_continuation_fragment.tex', 'The absolute-base restriction fibre and its adjoint'),
      ('SC', PEER / 'theta_scaling_cocycle.fragment.tex', 'Original scaling, the source extension, and the full boundary pairing'),
      ('BK', AUDIT / 'segment29_40/original_balanced_kernel.tex', 'The full-source balanced Mellin kernel'),
      ('DP', AUDIT / 'derived_packet_comparison.tex', 'Finite derived observations and source-label transitions'),
      ('PL', AUDIT / 'proper_label_spectral_kernel.tex', 'An explicit proper-label spectral kernel'),
      ('PS', AUDIT / 'segment16_28/PACKET_SURVIVAL.tex', 'The arithmetic packet through coefficient purity'),
      ('BF', AUDIT / 'segment41_54/multiplicity_boundary_floor.tex', 'The full-multiplicity arithmetic boundary floor'),
      ('FD', AUDIT / 'segment41_54/symmetric_frontier_determinant.tex', 'The original symmetric frontier and determinant growth'),
      ('C', AUDIT / 'segment41_54/conormal_jacobian_symmetric_trace.tex', 'Conormal images, arithmetic Jacobians, and complete symmetric trace fibres'),
      ('HT', AUDIT / 'segment55_67/actual_holonomy_counterfactual.tex', 'The original boundary at every holonomy phase'),
      ('AT', WORKSPACE / 'output/Tau_Arithmetic_Determinant_Transport_2026-09-13/proofs/AT.tex', 'Exact arithmetic transport of all four determinants'),
      ('AW', WORKSPACE / 'output/Tau_Relation_Window_Spectral_Transport_2026-09-13/proofs/AW.tex', 'The full relation-window spectrum and its bound'),
    ]
    extra = AUDIT / 'segment55_67/actual_compatible_bounds.tex'
    if extra.exists():
        entries.append(('HC', extra, 'The actual four-window counterfactual interval'))
    manifest = []
    chapters = []
    for prefix, source, title in entries:
        if not source.is_file():
            raise FileNotFoundError(source)
        original = ROOT / 'proof_inputs' / (prefix + '.tex')
        shutil.copy2(source, original)
        text = source.read_text(encoding='utf-8-sig')
        # Only cross-reference identifiers change in the included copy.
        text = re.sub(r'\\(label|ref|eqref|pageref|autoref)\{([^{}]+)\}',
                      lambda m: '\\' + m[1] + '{' + prefix + ':' + m[2] + '}', text)
        included = ROOT / 'tex/modules' / (prefix + '.tex')
        included.write_text(text, encoding='utf-8')
        manifest.append({'prefix':prefix, 'source':str(source), 'source_sha256':sha(source),
                         'original_copy':str(original.relative_to(ROOT)),
                         'included_copy':str(included.relative_to(ROOT)),
                         'included_sha256':sha(included),
                         'transformation':'namespace LaTeX cross-reference identifiers only'})
        chapters.append('\\chapter{' + title + '}\n\\input{modules/' + prefix + '.tex}\n')
    (ROOT / 'tex/chapters.tex').write_text('\n'.join(chapters), encoding='utf-8')
    (ROOT / 'provenance/PROOF_INPUT_MANIFEST.json').write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps({'assembled_modules':len(manifest), 'output':str(ROOT)}, indent=2))

if __name__ == '__main__':
    assemble()
