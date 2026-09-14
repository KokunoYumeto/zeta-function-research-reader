"""Three current display overlays after root restored the complete R62."""
from pathlib import Path
import hashlib,json,re
ROOT=Path(__file__).resolve().parent
ACTIVE=ROOT.parents[1]/'cumulative_source_v1'
SOURCE=ACTIVE/'tex/research_conclusion.tex'
SEALED='a310d094b172289340485cb306881c029de81f1e9eff605716d70d27df0a3aa3'
def sha(b):return hashlib.sha256(b).hexdigest()
def pin(p):b=p.read_bytes();return {'path':str(p),'bytes':len(b),'sha256':sha(b)}
def tokens(s):
    s=s.replace(r'\begin{aligned}','').replace(r'\end{aligned}','')
    s=s.replace('\\\\','').replace('&','')
    s=re.sub(r'\\(?:quad|qquad)\b','',s)
    return re.findall(r'\\[A-Za-z@]+|\\[\s\S]|[A-Za-z0-9]+|[^\s]',s)
def get_display(text,marker):
    matches=[m[0] for m in re.finditer(r'\\\[.*?\\\]',text,re.S) if marker in m[0]]
    assert len(matches)==1,(marker,len(matches))
    return matches[0]
raw=SOURCE.read_bytes();assert sha(raw)==SEALED
text=raw.decode('utf-8')
specs=[('Cyclic connection and flatness',r'\Omega_u=-C_\chi(t)/u^2+B_\chi/u',r'''
 \begin{aligned}
 \Omega_u&=-C_\chi(t)/u^2+B_\chi/u,\qquad
 \Pi_u=\Pi\Omega_u,\\
 \Omega_t&=-A(t)/u,\qquad \Pi_t=\Pi\Omega_t,\\
 \partial_u\Omega_t-\partial_t\Omega_u+
                          [\Omega_u,\Omega_t]&=0 .
 \end{aligned}
'''),('Residual collision annihilator and exact modules',r'\psi_{h,k}(X)=',r'''
 \begin{aligned}
 \psi_{h,k}(X)&=
 \prod_{\mu}
 (X-\mu)^{
 \max_{\alpha(\sum_i\rho_i)=\mu}
            \min(p,1+\sum_i(m_i-1))},\\
 \ker\overline\eta_k&=(\psi_{h,k})/(\overline\chi_{h,k}),\quad
 \operatorname{im}\overline\eta_k\simeq k_0[X]/(\psi_{h,k}).
 \end{aligned}
'''),('Translated metric and all three pure derivatives',r'\psi_a-\psi=2p\operatorname{Re}(h_a(t)/u)',r'''
 \begin{aligned}
 \psi_a-\psi&=2p\operatorname{Re}(h_a(t)/u),\\
 \partial_u(\psi_a-\psi)&=-p h_a(t)/u^2,\\
 \partial_u^2(\psi_a-\psi)&=2p h_a(t)/u^3,\\
 \partial_u\partial_t(\psi_a-\psi)&=pa/u^2 .
 \end{aligned}
''')]
changed=text;records=[];before_parts=[];after_parts=[]
for title,marker,inner in specs:
    old=get_display(text,marker);new=r'\['+inner+r'\]'
    if '\r\n' in text:new=new.replace('\n','\r\n')
    assert tokens(old)==tokens(new),title
    assert changed.count(old)==1;changed=changed.replace(old,new,1)
    records.append({'title':title,'old_display':old,'new_display':new,'content_tokens_identical':True,
                    'token_count':len(tokens(old))})
    before_parts.append(r'\subsection*{'+title+'}\n'+old+'\n')
    after_parts.append(r'\subsection*{'+title+'}\n'+new+'\n')
inverse=changed
for row in reversed(records):inverse=inverse.replace(row['new_display'],row['old_display'],1)
assert inverse.encode('utf-8')==raw
assert tokens(text)==tokens(changed)
assert r'\psi_a-\psi' in text
before=ROOT/'research_conclusion_before.tex';after=ROOT/'research_conclusion_after.tex'
assert not before.exists() or before.read_bytes()==raw
before.write_bytes(raw);after.write_bytes(changed.encode('utf-8'))

historical=ACTIVE/'provenance/previous_active_revisions/4886cfdbdd9b29e842f000b6adcdfc00957c9d2639e693158efe2921d823b417/research_conclusion.tex'
hist_text=historical.read_bytes().decode('utf-8')
hist_old=get_display(hist_text,r'\psi_a-\psi=2p\operatorname{Re}(h_a(t)/u)')
hist_new=r'''\[
 \begin{aligned}
 \psi_a-\psi&=2p\operatorname{Re}(h_a(t)/u),\\
 \partial_u(\psi_a-\psi)&=-p h_a(t)/u^2,\\
 \partial_u^2(\psi_a-\psi)&=2p h_a(t)/u^3,\\
 \partial_u\partial_t(\psi_a-\psi)&=pa/u^2 .
 \end{aligned}
\]'''
assert tokens(hist_old)==tokens(hist_new)
(ROOT/'historical_translated_metric_before.tex').write_bytes(hist_old.encode('utf-8'))
(ROOT/'historical_translated_metric_reflow_not_applied.tex').write_bytes(hist_new.encode('utf-8'))
# Historical witness is kept to document the restored content, but the current
# three-display scratch already includes its active restored version.

rmt=ACTIVE/'tex/recursive_metric_transport.tex'
assert sha(rmt.read_bytes())=='6d477243e7e3bdcee6e4986585cae9d44053a07ed3332a7dc822b0d9303ff1c8'
rmt_display=get_display(rmt.read_bytes().decode('utf-8'),r'\tag{RMT16}')
(ROOT/'RMT16_active_unchanged.tex').write_bytes(rmt_display.encode('utf-8'))
for parts in (before_parts,after_parts):parts.append(r'\subsection*{Existing parent RMT16 overlay (unchanged)}'+'\n'+rmt_display+'\n')
preamble=(ACTIVE/'tex/main.tex').read_bytes().decode('utf-8').split(r'\begin{document}',1)[0]
(ROOT/'ACTIVE_PREAMBLE_SNAPSHOT.tex').write_bytes(preamble.encode('utf-8'))
for name,parts in [('before',before_parts),('after',after_parts)]:
    doc=preamble+r'\begin{document}'+'\n'+r'\section*{Current conclusion display preservation}'+'\n'+'\n'.join(parts)+r'\end{document}'+'\n'
    (ROOT/(name+'.tex')).write_bytes(doc.encode('utf-8'))
receipt={'scope':'Only three assigned displays in the corrected complete frozen conclusion. RMT16 is inspected without edits.',
    'active_source':str(SOURCE),'accepted_before':pin(before),'proposed_after':pin(after),
    'records':records,'full_file_exact_inverse':True,'all_nonpresentation_content_tokens_identical':True,
    'historical_third':{'source':pin(historical),'active_source_has_target':True,
        'before_display':pin(ROOT/'historical_translated_metric_before.tex'),
        'proposed_display_not_applied':pin(ROOT/'historical_translated_metric_reflow_not_applied.tex'),
        'all_nonpresentation_content_tokens_identical':True,'restored_to_active_source_by_owner_before_this_overlay':True},
    'RMT16_readonly':pin(rmt),'active_source_modified':False}
(ROOT/'OVERLAY_PROPOSALS.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'present_displays_reflowed':3,'full_R62_restored_by_owner_before_overlay':True,'RMT16_unchanged':True,
    'all_exact_inverses':True,'proposed_active_sha256':pin(after)['sha256'],'active_modified':False}))
