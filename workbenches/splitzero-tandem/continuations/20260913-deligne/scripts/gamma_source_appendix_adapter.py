"""Pinned complete Gamma Markdown witness; importing is read-only."""
GAMMA_MARKDOWN_SPEC = {'key': 'gamma_convolution', 'source': 'sources/web_gamma_convolution_delivery/Tau_Gamma_Convolution_Descent/RESEARCH_NOTE.md', 'provenance': 'sources/local_gamma_continuations/GAMMA_MARKDOWN_SOURCE_PROVENANCE.json', 'title': 'Gamma convolution descent and the original arithmetic coefficient correction', 'sha256': '886c82e2562d9b4846adb44640d28a34552e38eb2518a3cd47f90dbbedd95e5b', 'bytes': 30605, 'revision': '886c82e2562d9b4846adb44640d28a34552e38eb2518a3cd47f90dbbedd95e5b', 'revision_role': 'Complete delivered Markdown witness SHA-256; source-reported Git revisions retain their historical role', 'lean_source_blocks': 0, 'formal_status': 'Complete source witness. Finite checker records are separately retained. No new local Lean execution is claimed.', 'attribution': 'Complete original Gamma Convolution Descent Markdown note delivered on 13 September 2026. Its archive and alternate complete TeX note are retained byte-for-byte. The full local coefficient chapter proves the exact coordinate maps, finite derivative indices, cochain primitive and transform domains alongside this unmodified source witness. Source reports about remote revisions and computations retain the verification scope of their original receipts.'}


def apply_gamma_source_layout(builder, row):
    """Break the unchanged five-object source chain at its four arrows."""
    import hashlib
    import re
    path = builder.ROOT / row['converted']
    text = path.read_text(encoding='utf-8')
    original = r"""\[
\text{original split-supported polynomial source}
\longrightarrow\text{full gamma product fibre with arithmetic amplitude}
\longrightarrow\text{sum density and retained relative component}
\longrightarrow\text{exact all-tensor arithmetic coefficients}
\longrightarrow\text{the same source--boundary Toda determinant ratio}.
\]"""
    if text.count(original) != 1:
        raise RuntimeError('Expected the unique full original Gamma five-object chain')
    lines = original.splitlines()[1:-1]
    wrapped = (chr(92)*2+chr(10)).join('&'+line for line in lines)
    formatted = '\\[\n\\begin{aligned}\n'+wrapped+'\n\\end{aligned}\n\\]'
    reconstructed = formatted.replace('\\begin{aligned}\n','').replace('\n\\end{aligned}','').replace('\\\\\n','\n').replace('&','')
    if reconstructed != original:
        raise RuntimeError('Gamma chain layout changed original mathematical tokens')
    text = text.replace(original, formatted, 1)
    path.write_text(text, encoding='utf-8')
    row['reader_layout_refinements'] = [{
        'scope': 'The complete final five-object chain in source section 10.',
        'operation': 'Aligned rows at the four original rightward arrows; every original token remains in its original order.',
        'original_display_sha256': hashlib.sha256(original.encode()).hexdigest(),
        'formatted_display_sha256': hashlib.sha256(formatted.encode()).hexdigest(),
        'inverse_layout_reconstructs_original_display': True,
        'raw_source_and_prepared_Pandoc_math_nodes_changed': False}]
    return row
