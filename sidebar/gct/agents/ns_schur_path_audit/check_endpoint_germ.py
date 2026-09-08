"""Independent exact endpoint descent, valuation and scalar-germ audit.

No author checker is imported. The full tableau census is independently
computed by the sibling cell-recursion checker.
"""
from pathlib import Path
import sympy as S
import hashlib,json

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
PROOF=ROOT/'tex/ns_schur_path.tex'
tau,m,q,u,e0,h=S.symbols('tau m q u e0 h')
checks=0
def z(f):
    global checks
    checks+=1
    assert S.cancel(S.expand(f))==0,f
def ck(p):
    global checks
    checks+=1
    assert p
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()

Hr=((m+4)**3-5*(m+4)**2+6*(m+4)-1)*(m+3)
H=21-98*tau+140*tau**2-80*tau**3+16*tau**4
B=-42+196*tau-280*tau**2+160*tau**3-32*tau**4
C=tau*B
z(Hr.subs(m,-2*tau)-H)
z(H+B/2)
z(-2*tau*H-C)
qi=lambda n:sum(q**(n-1-2*j) for j in range(n))
z(Hr.subs(m,(q-q**-1)**2)-qi(7)*qi(3))
z((q-q**-1)**2*Hr.subs(m,(q-q**-1)**2)-(q**10-q**4-q**-4+q**-10))
ck(H.subs(tau,0)==21)
ck(B.subs(tau,0)==-42)

profile=[27,81,162,270,300,252,126,42]
ck(sum(profile)==1260)
ck(sum(k*n for k,n in enumerate(profile))==4725)
ck(sum(profile[::2])==615)
ck(sum(profile[1::2])==645)
ck(sum(profile[1:])==1233)
z(4725-15*1260*(S.Rational(1,2)+h)-(-4725-18900*h))
ck(15*1260==18900)
leading=[]
for k in range(8):
    ck(S.Poly(C**k,tau).terms()[-1][0][0]==k)
    ck(S.Poly(C**k,tau).coeff_monomial(tau**k)==(-42)**k)
    z(C**k-(-2*tau)**k*H**k)
    # Two-variable exact remainder certificate, independent of fractional
    # powers or continuity of epsilon. Substitute u=tau^(2h)*epsilon later.
    difference=S.expand(B**k*(e0+u)**15-(-42)**k*e0**15)
    Qtau=S.cancel((B**k-(-42)**k)/tau)*(e0+u)**15
    Qu=(-42)**k*S.cancel(((e0+u)**15-e0**15)/u)
    ck(S.denom(S.cancel(Qtau))==1)
    ck(S.denom(S.cancel(Qu))==1)
    z(difference-tau*Qtau-u*Qu)
    exponent=k-15*(S.Rational(1,2)+h)
    z(exponent-((7-15*(S.Rational(1,2)+h))-(7-k)))
    ck(exponent.subs(h,0)<=-S.Rational(1,2))
    leading.append({'weight':k,'multiplicity':profile[k],
                    'scalar_coefficient_integer':(-42)**k,
                    'e0_degree':15,'tau_exponent':str(exponent),
                    'relative_remainder':'O(tau^(2h))'})

# Formal ramification comparison, using tau=v^2 and the branch q→1.
v=S.symbols('v')
q_series=S.sqrt(1-v*v/2)+S.I*v/S.sqrt(2)
qi_series=S.sqrt(1-v*v/2)-S.I*v/S.sqrt(2)
z(q_series*qi_series-1)
z((q_series-qi_series)**2+2*v*v)
z(q_series+qi_series-2*S.sqrt(1-v*v/2))
ck(S.expand(q_series.series(v,0,2).removeO()).coeff(v,1)==S.I/S.sqrt(2))
for k in range(8):
    ck(S.Poly((C**k).subs(tau,v*v),v).terms()[-1][0][0]==2*k)

receipt={'status':'passed','checks':checks,
         'reviewed_tex_sha256':sha(PROOF) if PROOF.exists() else None,
         'formal_base':'R[[tau]] after exact descent through Z[1/2][m], m=(q-q^-1)^2, m↦-2tau',
         'profile':profile,'rank':1260,'weighted_length':4725,'inertia_unscaled':[615,645,0],
         'rank_at_tau_zero':27,'kernel_dimension_at_tau_zero':1233,
         'cokernel_dimension_at_tau_zero':1233,
         'leading_eigenvalue_data':leading,
         'scope':'Algebraic endpoint and exact relative-remainder certificates. Strict sine interval and bounded-error estimates are proved in proof_audit.tex.',
         'findings':[]}
(HERE/'endpoint_verification.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'passed','checks':checks,'reviewed_tex_sha256':receipt['reviewed_tex_sha256']}))
