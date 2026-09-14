from pathlib import Path
import json
import re
import subprocess

HERE=Path(__file__).resolve().parent
source=(HERE/'part53_54_and_conormal_proof.md').read_text(encoding='utf-8')
source=source[source.index('## New calculation'):source.index('## Limits of this result')]
codes=list(dict.fromkeys(re.findall(r'`([^`]+)`',source)))
M={
'iota(rho)=1-conjugate(rho)':r'\iota(\rho)=1-\bar\rho',
'm_(iota rho)=m_rho':r'm_{\iota\rho}=m_\rho',
'f†(s)=conjugate(f(1-conjugate(s)))':r'f^\dagger(s)=\overline{f(1-\bar s)}',
'h†=(-1)^d h':r'h^\dagger=(-1)^d h',
'E_h':r'E_h','e_rho':r'e_\rho','(s-rho)^{m_rho}':r'(s-\rho)^{m_\rho}',
'z=s-rho':r'z=s-\rho','h_rho(rho)':r'h_\rho(\rho)',
'C[z]/(z^{m_rho})':r'\mathbb C[z]/(z^{m_\rho})',
'm_rho h_rho(rho)z^{m_rho-1}':r'm_\rho h_\rho(\rho)z^{m_\rho-1}',
"(h')":r"(h')",'z^{m_rho-1}':r'z^{m_\rho-1}','m_rho=1':r'm_\rho=1',
'E=E_h^{tensor k}':r'E=E_h^{\otimes k}','delta_S':r'\delta_S',"h'(s_i)b":r"h'(s_i)b",
'kb':r'kb',"(h')E_h":r"(h')E_h",'(rho_1,...,rho_k)':r'(\rho_1,\ldots,\rho_k)',
'C[z_1,...,z_k]/(z_i^{m_rho_i})':r'\mathbb C[z_1,\ldots,z_k]/(z_i^{m_{\rho_i}}:1\le i\le k)',
'm_rho_i-1':r'm_{\rho_i}-1','U':r'U','U^{-1}':r'U^{-1}','U delta_S':r'U\delta_S',
'h(s_i)':r'h(s_i)',"U product_i h'(s_i)=product_i g'(s_i)":r"U\prod_i h'(s_i)=\prod_i g'(s_i)",
"g'=h'(g/h)+h(g/h)'":r"g'=h'(g/h)+h(g/h)'",'v_h=g/h':r'v_h=g/h',
"M_(g')":r"M_{g'}",'mathscr R_k':r'\mathscr R_k','s_1,...,s_k':r's_1,\ldots,s_k',
"g'/g":r"g'/g",'m_rho':r'm_\rho','(-1)^k':r'(-1)^k',
'R_k=(1/k!)sum P_pi':r'R_k=\frac1{k!}\sum_{\pi\in S_k}P_\pi',
'B_k=(E_h^{tensor k})^{S_k}':r'B_k=(E_h^{\otimes k})^{S_k}',
'J^{S_k}':r'\mathcal J^{S_k}','binom(k-1,k)=0':r'\binom{k-1}{k}=0',
'd-r=0':r'd-r=0','k>=1':r'k\ge1','binom(t+k-1,k)':r'\binom{t+k-1}{k}',
'E_h tensor Sym^{k-1}(E_h)':r'E_h\otimes\operatorname{Sym}^{k-1}(E_h)',
"(g')E_h":r"(g')E_h",'n=(n_rho)_(rho in Z)':r'\boldsymbol n=(n_\rho)_{\rho\in Z}',
'n_rho>=0':r'n_\rho\ge0','sum n_rho=k':r'\sum_{\rho\in Z}n_\rho=k',
'e_n':r'e_{\boldsymbol n}','e_n^2=e_n':r'e_{\boldsymbol n}^2=e_{\boldsymbol n}',
'product_rho S_(n_rho)':r'\prod_{\rho\in Z}S_{n_\rho}',
'tensor_rho (C[z]/z^{m_rho})^{tensor n_rho,S_(n_rho)}':r'\bigotimes_{\rho\in Z}\bigl((\mathbb C[z]/(z^{m_\rho}))^{\otimes n_\rho}\bigr)^{S_{n_\rho}}',
'(z_1,...,z_k)':r'(z_1,\ldots,z_k)','a=c+n':r'a=c+n','D_n c':r'D_{\boldsymbol n}c',
'M_(f†u)':r'M_{f^\dagger u}','R_k':r'R_k','R_kM':r'R_kM','Bu':r'Bu',
'P product_i g(s_i)=U P product_i h(s_i)':r'P\prod_i g(s_i)=UP\prod_i h(s_i)',
'phi_*':r'\phi_*','e_(iota n)':r'e_{\iota\boldsymbol n}','D_(iota n)':r'D_{\iota\boldsymbol n}',
'D_n=D_(iota n)':r'D_{\boldsymbol n}=D_{\iota\boldsymbol n}',
'e_n+e_(iota n)':r'e_{\boldsymbol n}+e_{\iota\boldsymbol n}',
'e_n-e_(iota n)':r'e_{\boldsymbol n}-e_{\iota\boldsymbol n}',
'+2D_n':r'+2D_{\boldsymbol n}','-2D_n':r'-2D_{\boldsymbol n}','D_n':r'D_{\boldsymbol n}',
'n_1=n_2':r'n_1=n_2','n_3=n_4':r'n_3=n_4','n_1=n_2=a':r'n_1=n_2=a',
'n_3=n_4=l-a':r'n_3=n_4=l-a','0<=a<=l':r'0\le a\le l','mathsf J_k B f':r'\mathsf J_kBf',
'S=sum s_i':r'S=\sum_i s_i','sum z_i':r'\sum_i z_i','k(m-1)':r'k(m-1)',
'B_bal':r'B_{\rm bal}','n_1+n_3=l':r'n_1+n_3=l','n_2+n_4=l':r'n_2+n_4=l','(l+1)^2':r'(l+1)^2',
'sum_(balanced n) D_n-(l+1)^2':r'\sum_{\boldsymbol n\,\mathrm{balanced}}D_{\boldsymbol n}-(l+1)^2',
'(1,0,0,1)':r'(1,0,0,1)','(0,1,1,0)':r'(0,1,1,0)','k(1/2+delta)':r'k(1/2+\delta)',
'q':r'q','-l<=q<=l':r'-l\le q\le l','l+2i gamma q':r'l+2i\gamma q','N_q=l+1-|q|':r'N_q=l+1-|q|',
'q>=0':r'q\ge0','q<=0':r'q\le0','f_q=1':r'f_q=1','l+q':r'l+q',
'sum_(a+b=l+q)D_(a,b,l-a,l-b)-N_q':r'\sum_{a+b=l+q}D_{(a,b,l-a,l-b)}-N_q',
}
missing=[x for x in codes if x not in M]
if missing: raise RuntimeError(f'Unconverted mathematical code spans: {missing}')
source=re.sub(chr(96)+r'([^'+chr(96)+r']+)'+chr(96),
              lambda m:r'\('+M[m.group(1)]+r'\)',source)
source=source.replace('## New calculation: the entire conormal image of an actual zero packet',
                      '## The entire conormal image of an actual zero packet')
source=source.replace('This paragraph does not assert that such a zero exists. It computes what the negation of RH would force on the original objects just proved.',
                      'The existence assumption in this paragraph is exactly the RH counterfactual. The statements below compute its consequences on the original objects.')
source=source.replace('This report','This calculation')
source=source.replace('It is also, by the image/kernel decomposition of the Reynolds projector,',
    r'Here \(\iota\boldsymbol n=(n_{\iota\rho})_{\rho\in Z}\), the induced permutation of the original occupations. It is also, by the image/kernel decomposition of the Reynolds projector,')
for old,new in [('For m>1',r'For \(m>1\)'),('For m=1',r'For \(m=1\)'),
                ('For k=2l',r'For \(k=2l\)'),('For k=2',r'For \(k=2\)'),
                ('B_k',r'\(B_k\)')]:
    # B_k already inside display/inline math is handled by Pandoc; do not
    # insert math delimiters there. Fix its few plain prose occurrences below.
    if old != 'B_k': source=source.replace(old,new)
out=HERE/'conormal_jacobian_symmetric_trace.tex'
raw=HERE/'conormal_jacobian_body.md'
raw.write_text(source,encoding='utf-8')
subprocess.run(['pandoc',str(raw),'-f','markdown+tex_math_single_backslash+raw_tex',
                '-t','latex','--wrap=preserve','-o',str(out)],check=True)
body=out.read_text(encoding='utf-8')
body=re.sub(r'\\hypertarget\{[^}]*\}\{%\n(\\subsection\{[^\n]*\})\\label\{[^}]*\}\}',r'\1',body)
body=body.replace(r'B\_k',r'\(B_k\)')
body=re.sub(r'\\label\{([^}]+)\}',lambda m:r'\label{cmod:'+m.group(1)+'}',body)
header=(HERE/'conormal_source_header.tex').read_text(encoding='utf-8')
out.write_text(header+body,encoding='utf-8')
print(json.dumps({'tex':str(out),'characters':len(header+body),'code_spans_converted':len(codes)}))
