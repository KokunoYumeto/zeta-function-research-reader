"""Explicit mathematical prose transcription for AP Sections 5–7 and provenance."""
from pathlib import Path
import hashlib,json,re
ROOT=Path(__file__).resolve().parent
SOURCE=Path('F:/user/Documents/Papors/Chatnotes/Zeta-Function-Foundation/agents/zenodo_workspace_publication/integration_20260913_next/post_pr26_intake/parent_review/f1_unit_gauge/ANALYTIC_POLE_RESIDUE_TRANSPORT.md')
raw=SOURCE.read_bytes();digest=hashlib.sha256(raw).hexdigest()
if digest!='357923aead35c77f2fa98598fbc4ed8bc1f7cd6ebc04760da504a0ded765a652':raise RuntimeError('Accepted source changed')
text=raw.decode('utf-8');start=text.index('## 5.');mask=[False]*len(text)
for m in re.finditer(r'(?m)^    .*(?:\n|$)|^#+ .*(?:\n|$)',text):
    for i in range(m.start(),m.end()):mask[i]=True
for m in re.finditer(r'(?m)^.*(?:SHA256|^[0-9a-f]{64}|\.md(?:,|$)).*$',text):
    for i in range(m.start(),m.end()):mask[i]=True
entries=[]
PAIRS={
"K'_a=-C_a B_0-K_a P":r"K'_a=-C_a B_0-K_a P",'K_0=0':r'K_0=0',
'-C_a^-1 K_a exp(aP)':r'-C_a^{-1}K_a\exp(aP)',
'exp(aL)F=e^(-as)F(u,t+ua,s)':r'\exp(aL)F=e^{-as}F(u,t+ua,s)',
'w(p;u,t+ua)=w(p;u,t)e^(-ap)':r'w(p;u,t+ua)=w(p;u,t)e^{-ap}',
'C_ext,a(0,0)=exp(-a A_ext(0))':r'C_{\mathrm{ext},a}(0,0)=\exp(-a A_{\mathrm{ext}}(0))',
'w(p)=exp((Phi(p)-tp)/u)':r'w(p)=\exp((\Phi(p)-tp)/u)',
'(w/nu)nu/(s-p)=w/(s-p)':r'(w/\nu)\nu/(s-p)=w/(s-p)',
'd/dt+A_ext(t)^T/u':r'\frac{d}{dt}+A_{\mathrm{ext}}(t)^T/u',
"(0,W^T alpha')":r"(0,W^T\alpha')",'(0,W^T alpha)':r'(0,W^T\alpha)',
'C[s,nu^-1][[u,t]]':r'\mathbb C[s,\nu^{-1}][[u,t]]',
'C[s][[u,t]]':r'\mathbb C[s][[u,t]]',
'sum_{n>=0}(-HE)^n H':r'\sum_{n\ge0}(-HE)^n H',
'E=u d/ds-t':r'E=u\frac{d}{ds}-t','gcd(h,nu)=1':r'\gcd(h,\nu)=1',
'u d_t w(p)=-p w(p)':r'u d_t w(p)=-p w(p)',
'w(p)(h(p)-t)^n/u^n':r'w(p)(h(p)-t)^n/u^n',
'J_0=[I_d Q_0]':r'J_0=[I_d\;Q_0]',
'c -> (-Q_0 c,c)':r'c\mapsto(-Q_0 c,c)',
'Phi(p)-tp!=0':r'\Phi(p)-tp\ne0','Phi(0)=0':r'\Phi(0)=0',
'exp(Phi(0)/u)':r'\exp(\Phi(0)/u)',
'D(1/(s-p))':r'D(1/(s-p))','1-h(s)/h(p)':r'1-h(s)/h(p)',
'1/(s-p)':r'1/(s-p)','nu/(s-p)':r'\nu/(s-p)',
'e^(-as)F':r'e^{-as}F','e^(-ap)':r'e^{-ap}',
'w^{(n)}(p)':r'w^{(n)}(p)','h(p)!=0':r'h(p)\ne0',
'C_a(u,t)':r'C_a(u,t)','A_ext(0)':r'A_{\mathrm{ext}}(0)',
'u=t=0':r'u=t=0','u!=0':r'u\ne0','r>0':r'r>0','r=0':r'r=0',
't=0':r't=0','u=0':r'u=0','p=0':r'p=0','w(p)=1':r'w(p)=1',
'w(0)':r'w(0)','w(p)':r'w(p)','h(p)':r'h(p)',
'nu^-1':r'\nu^{-1}','w/nu':r'w/\nu','O(1/s)':r'O(1/s)',
'2 pi i':r'2\pi i','-P W/u':r'-P W/u','P W/u':r'P W/u',
'd+r':r'd+r','u,t':r'u,t','s-p':r's-p',
'C_a':r'C_a','K_a':r'K_a','Pi_pol':r'\Pi_{\mathrm{pol}}','H_pol':r'H_{\mathrm{pol}}',
'B_loc':r'B_{\mathrm{loc}}','P_nu':r'P_\nu','Q_0':r'Q_0','J_0':r'J_0',
'upsilon_h':r'\upsilon_h','Phi':r'\Phi','nu':r'\nu','gamma_p':r'\gamma_p',
'alpha':r'\alpha','tau':r'\tau','theta':r'\theta',
}
def add(a,b,original,tex,reason):
    if a<start or any(mask[a:b]):return False
    if text[a:b]!=original:raise RuntimeError('Span mismatch')
    entries.append({'source_byte_start':len(text[:a].encode('utf-8')),'source_byte_end':len(text[:b].encode('utf-8')),
      'original':original,'tex':tex,'reason':reason})
    for i in range(a,b):mask[i]=True
    return True
for original,tex in sorted(PAIRS.items(),key=lambda x:-len(x[0])):
    for m in re.finditer(re.escape(original),text[start:]):
        a=start+m.start();b=start+m.end()
        if (a and re.match(r'[A-Za-z0-9_]',text[a-1])) or (b<len(text) and re.match(r'[A-Za-z0-9_]',text[b])):continue
        add(a,b,original,tex,'Complete mathematical prose expression; exact original order, factors, signs and named object retained.')
# Single-letter mathematical names are typed only as isolated prose words;
# the ordinary English article "a" is handled through explicit contexts below.
for m in re.finditer(r'(?<![A-Za-z0-9_])[utspwdrhgHEDQAPLBWFcb](?![A-Za-z0-9_])',text[start:]):
    a=start+m.start();b=start+m.end()
    if (a and text[a-1]=="'") or text[a:a+9]=='A formal ':continue
    add(a,b,text[a:b],text[a:b],'Isolated original mathematical parameter, polynomial, operator, dimension or coefficient name in the source prose.')
for phrase in ('from 0 to a in the complex','a-plane','in a when F','complex a is needed'):
    at=text.find(phrase,start)
    if at<0:raise RuntimeError('Expected parameter-a context not found: '+phrase)
    for m in re.finditer(r'(?<![A-Za-z])a(?![A-Za-z])',phrase):
        a=at+m.start();add(a,a+1,'a','a','The scaling parameter a in this explicitly fixed source context, not the English article.')
for phrase,expr in [('from 0 to a in the complex','0')]:
    at=text.index(phrase,start)+phrase.index(expr);add(at,at+len(expr),expr,expr,'Original endpoint of the displayed scaling integral.')
entries.sort(key=lambda r:r['source_byte_start'])
for x,y in zip(entries,entries[1:]):
    if x['source_byte_end']>y['source_byte_start']:raise RuntimeError('Overlapping mathematical prose spans')
out={'schema':'complete-prose-math-span-map-v1','source':{'path':str(SOURCE),'bytes':len(raw),'sha256':digest},
 'scope':'All ordinary prose mathematical expressions in Sections 5–7 and provenance. CodeBlocks, headings, source locators, hashes and ordinary English article a are excluded.',
 'prose_math_mappings':entries,'entry_count':len(entries),
 'notation_dictionary':'Greek names, mathematical functions, subscripts, powers, tensor/pole operators and matrices retain their source definitions. No expression is simplified, reordered, specialized or normalized.'}
path=ROOT/'mapping/proof_prose_sections_5_7.json';path.parent.mkdir(parents=True,exist_ok=True)
path.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='')
print(json.dumps({'path':str(path),'entries':len(entries)}))
