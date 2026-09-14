"""Explicit full-source Code-to-Math typesetting dictionary; no source edits."""
import hashlib, json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
inventory=json.loads((ROOT/'f1_inventory/SOURCE_INVENTORY.json').read_text(encoding='utf-8'))['files']['reflection']
typed={
1:r'1/u',4:r'U_p F(x)=F(x/p)',5:r'(U_p\phi,pU_{1/p}\psi)',6:r'U_p',7:r'p^s',
8:r'\int\phi(x)\,dx',9:r'p',10:r'L_k',11:r'p^k',12:r'p^k',13:r'U_p^{-1}',14:r'(-1)^q',
15:r'\eta[P]=\upsilon_h^{\otimes k}P(A_h^{(k)})1',16:r'\Phi(0)=0',17:r'\mathbb C[u,t]',
18:r'1,S,\ldots,S^{q-1}',19:r'A(t)',20:r'\mathbb C[S]/(\chi-t)',21:r'RP(S)=P(k-S)',
22:r'(-\varepsilon u)\varepsilon(-RP\prime)=uRP\prime',
23:r'\varepsilon(\chi-\varepsilon t)RP=(\varepsilon\chi-t)RP',24:r'\varepsilon R',25:r'(u,t)=(0,0)',
26:r'(u,t)\mapsto(-\varepsilon\overline u,\varepsilon\overline t)',27:r'(k-S)P(k-S)',
28:r'\chi-\varepsilon t',29:r'\Phi(k)',30:r'k',31:r'dt\prime=\varepsilon\,dt',32:r'u\ne0',33:r'-k/u',
34:r'(r^*\nabla)(\mathcal Fv)=\mathcal F\nabla v',35:r'\Gamma\prime=k-\Gamma',
36:r'S_{\mathrm{old}}=k-S_{\mathrm{new}}',37:r'dS_{\mathrm{old}}=-dS_{\mathrm{new}}',
38:r'L=u\partial_t-S',39:r'C_{a+b}',40:r'C_a(0,t)=\exp(-aA(t))',41:r'u\prime=-\varepsilon u',
42:r't\prime=\varepsilon t',43:r'C_{-a}(u\prime,t\prime)',44:r'C_{-a}(u\prime,t\prime)A(t\prime-u\prime a)',
45:r't\mapsto t+ua',46:r'\exp(-ka)',47:r'a=\log p',48:r'p^{-k}',49:r'p^k',
50:r'T_av(t)=C_a(u,t)v(t+ua)',51:r'T_a^Lz(t)=\exp(-ka)z(t+ua)',52:r'p^k(p^A)^{-T}',
53:r'K_{(\tau,k)}(L_k)',54:r'(-1)^{q(q-1)/2}',55:r'A(t)^T\mathsf S=\mathsf SA(t)',56:r'S^{-2}',
57:r'J=R^T\mathsf S',58:r'RA(t)=(kI-A(\varepsilon t))R',59:r'A(\varepsilon t)',
60:r'j_h(g/h)',61:r'-n+(2N-i)-2N=-n-i',
}
# The source apostrophes denote primes, not a variable named ``prime``.
typed={k:v.replace(r'\prime',"'") for k,v in typed.items()}
mapping=[]; retained=[]
for index,row in enumerate(inventory['inline_code']):
    if row['classification']=='mathematical_expression':
        if index+1 not in typed: raise ValueError(f'Missing Code index {index}')
        mapping.append({'code_index':index,'original':row['code'],'tex':typed[index+1],
                        'mode':'inline','source_byte_start':row['byte_start'],
                        'source_byte_end':row['byte_end_exclusive'],
                        'reason':'Explicit notation transcription of this complete original mathematical Code payload.'})
    else: retained.append({'code_index':index,'original':row['code'],'classification':row['classification']})
if len(mapping)!=59 or len(retained)!=3 or len(typed)!=59: raise ValueError('Incomplete reflection classification')
result={'schema':'complete-ascii-code-to-math-map-v1','source':{k:inventory[k] for k in ('path','bytes','sha256')},
        'math_code_mappings':mapping,'retained_code':retained,
        'notation_dictionary':[
            {'original':'Phi, chi, epsilon, eta, upsilon, tau, Gamma, nabla, phi, psi',
             'typed':r'\Phi,\chi,\varepsilon,\eta,\upsilon,\tau,\Gamma,\nabla,\phi,\psi',
             'meaning':'The Greek letters already defined by the unchanged displayed formulas or controlling source.'},
            {'original':'C in C[u,t] and C[S]/(chi-t)','typed':r'\mathbb C',
             'meaning':'Complex coefficient field; no coefficient specialization.'},
            {'original':'S in Code indices 54 and 56 (zero-based)','typed':r'\mathsf S',
             'meaning':'The unchanged residue matrix defined by RW22, not the scalar polynomial coordinate S. The same source locally overloads ASCII S.'},
            {'original':'F in Code index 33 (zero-based)','typed':r'\mathcal F',
             'meaning':'The exact horizontal reflection map defined by RW12, with its full scalar.'},
            {'original':'tensor k and A_h^(k)','typed':r'\otimes k and A_h^{(k)}',
             'meaning':'Original tensor power and parenthesized tensor-sum operator index; no scalar power substitution.'},
            {'original':'-> in element-coordinate formulas','typed':r'\mapsto',
             'meaning':'The original element map; all source and target coordinates are retained.'},
            {'original':'integral phi(x) dx','typed':r'\int\phi(x)\,dx',
             'meaning':'No integral bounds are added; the unchanged surrounding source supplies its existing moment convention.'},
            {'original':'K_(tau,k)(L_k)','typed':r'K_{(\tau,k)}(L_k)',
             'meaning':'The original grouped subscript is retained literally; it is the stated right adjoint.'},
        ],
        'scope':'Every original mathematical Code span is typed once; all original Math payloads and full proof prose remain unchanged. This dictionary changes notation presentation only, with exact inverse supplied by per-node originals.'}
(ROOT/'reflection_math_mapping.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='')
print(json.dumps({'mapping_count':len(mapping),'retained_code_count':len(retained),'path':str(ROOT/'reflection_math_mapping.json')}))
