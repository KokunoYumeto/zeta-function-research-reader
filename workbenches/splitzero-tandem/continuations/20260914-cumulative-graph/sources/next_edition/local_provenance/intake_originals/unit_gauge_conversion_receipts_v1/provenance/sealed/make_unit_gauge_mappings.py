"""Complete literal Code-to-Math dictionaries; original source bytes are read only."""
import hashlib,json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parent
SOURCE=Path('F:/user/Documents/Papors/Chatnotes/Zeta-Function-Foundation/agents/zenodo_workspace_publication/integration_20260913_next/post_pr26_intake/parent_review/f1_unit_gauge')
TYPED={
'f1_unit_gauge':{
0:r'j_h(g/h)',1:r'd=\deg h',2:r'E_h=\mathbb C[s]/(h)',3:r'\operatorname{rem}_h',
4:r'g/h',5:r'\nu',6:r'a,b',7:r'a h+b\nu=1',8:r's',9:r'(u,t)',10:r'(u,t)',
11:r'P/\nu^n',12:r'\deg(\nu^n)',13:r'\nu^n',14:r'hP/\nu^n',15:r'\nu^n',
16:r'a_n,b_n',17:r'[P/\nu^n]',18:r'[a_n P/\nu^n]',19:r'-b_n P',20:r'E_h',
21:r'\partial_s',22:r'E=u\partial_s-t',23:r'(u,t)',24:r'M[[u,t]]',
25:r'D_M=M_h(I+HE)',26:r'J D_M=I',27:r'D_M J=I',28:r'\pi r^1=\pi-D_M J\pi=0',
29:r'DK',30:r'KD',31:r'\pi i=0',32:r'Ki=0',33:r'\widehat B_\nu',
34:r"\partial_s(P/\nu)=P'/\nu-P\nu'/\nu^2",35:r'\nu^{-1}',
36:r'[\mathbb C[s]\xrightarrow{h}\mathbb C[s]\,ds]',37:r'E_h',38:r'D^\nu=h',
39:r'\nu,\nu s,\ldots',40:r'\nu s^j',41:r'M_{\upsilon_h}',42:r'p^{\pm A_h}',
43:r'a=\log p',44:r'(u,t)',45:r's_i',46:r'(u_i,t_i)',47:r'(u_i,t_i)^{n_i+1}=0',
48:r'P_i=i_i r_i',49:r'd K_{\mathrm{total}}+K_{\mathrm{total}}d=I-P_1\otimes\cdots\otimes P_k',
50:r'r_i i_i=I',51:r'Q^{\otimes k}',52:r'(\mathrm{mask},v)\mapsto(\mathrm{mask},f(v))',
53:r'\mathbf F_{1,\tau}',54:r'g=h(g/h)',55:r'g/h',56:r'M_{\upsilon_h}^{-T}',
57:r'K_{\tau,k}(L_k)',58:r'p^k',59:r'(u,t)'},
'f1_unit_gauge_review':{
2:r'E_h',3:r'E_h',4:r'h^\dagger(s)=(-1)^d\overline{h(1-\overline s)}',
5:r'E_{h^\dagger}',6:r'E_h',7:r'A=\mathbb C[s]',8:r'A_\nu=\mathbb C[s,\nu^{-1}]',
9:r'M=A_\nu/A',10:r'(u,t)',11:r'M=0',12:r'\gcd(h,\nu)=1',13:r'hP/\nu^n',
14:r'\nu^n\mid P',15:r'a_n h+b_n\nu^n=1',16:r'[a_n P/\nu^n]',17:r'M_h',18:r'E_h',
19:r'E=u\partial_s-t',20:r'D_M=M_h(I+HE)',21:r'(I+HE)^{-1}H',22:r'HE',
23:r'\pi D=D_M\pi',24:r'J D_M=D_M J=I',25:r'KD=\sigma\pi',26:r'r^0=I-\sigma\pi',
27:r'\pi r^1=0',28:r'r^1D=Dr^0',29:r'ri=I',30:r'ir=I-dK-Kd',31:r'u\partial_s-t',
32:r"\nu D\nu^{-1}=u\partial_s+h-t-u\nu'/\nu",33:r'\nu^{-1}',34:r'u=t=0',
35:r'\upsilon_h',36:r'r M_{\nu^{-1}}',37:r'M_\nu K M_{\nu^{-1}}',38:r'L=u\partial_t-s',
39:r'D^\nu',40:r'\nu s^j',41:r'C_a',42:r'(u_i,t_i)^{n_i}',43:r'P_i=i_i r_i',44:r'K_i',
45:r'K_{\mathrm{tot}}=K_1\otimes I+P_1\otimes K_2',
46:r'(P_1\otimes K_2)(x\otimes y)=(-1)^{\deg x}P_1x\otimes K_2y',
47:r'dK_{\mathrm{tot}}+K_{\mathrm{tot}}d=(I-P_1)\otimes I+P_1\otimes(I-P_2)',
48:r'=I-P_1\otimes P_2',49:r'P_1,\ldots,P_{j-1}',50:r'K_j',51:r'I-\bigotimes_i P_i',
52:r'D_i^\nu',53:r'M_{\upsilon_h}^{\otimes k}',54:r'[P]\mapsto P(\sum A_i)1',
55:r'g=h(g/h)',58:r'dK_{\mathrm{total}}+K_{\mathrm{total}}d=I-\bigotimes_i P_i'}
}
FILES={'f1_unit_gauge':('ACTUAL_TAYLOR_UNIT_FORMAL_GAUGE.md','9ded2486160b76bf65f92d44b73cdd0c59a3ca7e5334f88682e10592d5a45b2f'),
       'f1_unit_gauge_review':('INDEPENDENT_REVIEW.md','e32e978870e65ea375040762432a3cfe479068ebe6cfd800086a2d35d55da6d0')}
for key,(name,digest) in FILES.items():
    path=SOURCE/name;raw=path.read_bytes()
    if hashlib.sha256(raw).hexdigest()!=digest:raise RuntimeError('Accepted source changed')
    rows=[];retained=[];spans=list(re.finditer(rb'`([^`\r\n]+)`',raw))
    for index,m in enumerate(spans):
        original=m.group(1).decode('utf-8')
        row={'code_index':index,'original':original,'source_byte_start':m.start(),'source_byte_end':m.end()}
        if index in TYPED[key]:
            row.update(tex=TYPED[key][index],mode='inline',reason='Complete notation transcription of the exact original mathematical Code payload.')
            if key=='f1_unit_gauge_review' and index==48:
                row['whitespace_typing']='The initial ASCII space in this standalone continuation Code payload is presentation whitespace. The complete mathematical equality is retained; the exact original initial space is retained in original and restored by the byte inverse.'
            rows.append(row)
        else:
            row['classification']='source_hash' if re.fullmatch('[0-9a-f]{64}',original) else 'relative_source_locator'
            retained.append(row)
    if len(rows)!=len(TYPED[key]):raise RuntimeError('Incomplete dictionary')
    if (len(rows),len(retained))!=((60,2) if key=='f1_unit_gauge' else (55,4)):raise RuntimeError('Unexpected complete Code inventory')
    result={'schema':'complete-ascii-code-to-math-map-v1','key':key,
      'source':{'path':str(path),'bytes':len(raw),'sha256':digest},
      'math_code_mappings':rows,'retained_code':retained,
      'notation_dictionary':[
        {'original':'nu; upsilon_h','typed':r'\nu;\upsilon_h','meaning':'The degree-below-d full Hermite representative and its distinct jet-algebra unit in UG2, respectively. These are not interchanged.'},
        {'original':'C in coefficient rings','typed':r'\mathbb C','meaning':'The unchanged complex coefficient field of UG4 and UG5.'},
        {'original':'Bhat_nu','typed':r'\widehat B_\nu','meaning':'The exact coefficientwise completed localized ring of UG4, with no uniform denominator bound imposed.'},
        {'original':'r1 in gauge Code index 28','typed':r'r^1','meaning':'The degree-one retraction of UG10; the nearby source prose uses r1 for that exact operator.'},
        {'original':'partial_s, partial_t, sigma, pi, dagger','typed':r'\partial_s,\partial_t,\sigma,\pi,\dagger','meaning':'The unchanged differential, proper-part section, quotient map and original dagger operation.'},
        {'original':'F_(1,tau)','typed':r'\mathbf F_{1,\tau}','meaning':r'The original absolute base defined as \mathbf F_{1,\tau} in the complete tau-base note. The ASCII _(...) delimiters group the multi-index; the exact original typed definition supplies the base notation. No new base object is introduced.'},
        {'original':'M_(upsilon_h)^(-T); K_(tau,k)(L_k)','typed':r'M_{\upsilon_h}^{-T};K_{\tau,k}(L_k)','meaning':'The same inverse-transpose multiplication transport and tau-base right adjoint, with ASCII grouping delimiters rendered as TeX grouping braces; the full original indices and inverse-transpose exponent are retained.'},
        {'original':'tensor; tensor_i; tensor k','typed':r'\otimes;\bigotimes_i;\otimes k','meaning':'The original signed tensor homotopy and tensor powers; no symmetric or cyclic replacement is made.'},
        {'original':'degree x; conjugate(...)','typed':r'\deg x;\overline{\phantom{x}}','meaning':'The original cochain degree sign and the full outer complex conjugation in the reflected polynomial.'},
      ],
      'scope':'Complete source typing only. Original proof prose and original Math nodes remain intact except for explicitly reversible public wording edits. Per-node originals and source byte offsets supply the exact inverse.'}
    target=ROOT/(key+'_math_mapping.json')
    target.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='')
    print(key,len(rows),len(retained),str(target))
