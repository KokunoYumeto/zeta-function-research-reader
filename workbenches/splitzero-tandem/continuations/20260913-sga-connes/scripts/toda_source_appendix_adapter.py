"""Exact source specification for the September 12 Toda volume delivery."""
TODA_TEX_SPEC={
    'pr':None,'key':'toda_volume','stage':'web_toda_volume_delivery',
    'archive_entry':'Tau_Toda_Volume_Control/NOTE.tex',
    'title':'Source and relation volume dynamics for the original arithmetic control',
    'revision':'027cd27a5fc104c5ebdf0102ee43aafd7b6218da4929ceb1b8913e3448cd2375',
    'revision_role':'Complete delivered source witness SHA-256; no new remote revision is assigned',
    'source_sha256':'027cd27a5fc104c5ebdf0102ee43aafd7b6218da4929ceb1b8913e3448cd2375',
    'revision_receipt_name':'HANDOFF.md','receipt_format':'text',
    'receipt_expected_strings':[
        '# Handoff: source–boundary volume control',
        '2abc351424ba87aeda948a5cfb846e15ed9373d1',
        'No new Lean execution is claimed.',
        'The uniform subcubic arithmetic estimate has not been proved.',
    ],
    'attribution':(
        'Complete source note from the original Toda Volume Control archive. '
        'The source and relation Hankel determinants, tilt derivatives, imaginary '
        'cross term, first-degree endpoint, both loss squares and original theta '
        'input are retained. Its endpoint proof uses a vector symbol for a scalar '
        'norm; the explicit typed correction is proved in the integrated Toda '
        'bridge, while these original source bytes remain unchanged. '
        'The delivered floating evaluations are historical computations without '
        'interval or tail certification. The new local theta-tail proof and its '
        'separately scoped interval certificate supply that additional evidence '
        'for the analytic seed. Neither source asserts the growing-degree '
        'arithmetic estimate, and no local Lean execution is attributed to this edition.'
    ),
}
PARENT_JOIN_SPEC={
    'key':'toda_parent_join',
    'source':'sources/web_toda_parent_join/PARENT_EXACT_JOIN.md',
    'provenance':'sources/web_toda_parent_join/SOURCE_PROVENANCE.json',
    'title':'The coordinating Zeta contribution: determinant losses and spectral coupling',
    'sha256':'71e275a8543448e57bcfafc5ead8cf3c7f98d594ae994582d1180999d98c6370',
    'bytes':5459,'lean_source_blocks':0,
    'protect_literal_ascii_underscores':True,
    'revision':'71e275a8543448e57bcfafc5ead8cf3c7f98d594ae994582d1180999d98c6370',
    'revision_role':'Complete coordinating-task source witness SHA-256',
    'formal_status':'Complete written join of Toda (28) and frozen exterior identity E8; no new Lean execution.',
    'attribution':(
        'Complete mathematical note supplied by the coordinating Zeta task '
        'on 13 September 2026. The direct sum of the two exact identities '
        'retains the original quotient metric, phase, spectral coupling '
        'and compression remainder. Its full formulas, domains, endpoint '
        'scope and Sylvester comparison are reproduced as supplied. '
        'The integrated bridge gives the same join with its complete '
        'derivation. No asymptotic estimate or novelty claim is inferred.'
    ),
}
