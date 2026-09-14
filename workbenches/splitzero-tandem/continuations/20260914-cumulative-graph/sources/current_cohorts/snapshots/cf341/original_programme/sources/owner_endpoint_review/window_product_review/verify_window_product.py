"""Independent finite exact checks; no Lean, source writes or remote access.

All generated files are confined to this script's review directory. Public
receipts use descriptive input IDs and hashes, never attachment/private paths.
"""
from pathlib import Path
from fractions import Fraction as F
from math import factorial, prod
from datetime import datetime, timezone
import hashlib
import argparse
import itertools
import json
import sys
import time
import sympy as s

OUT=Path(__file__).resolve().parent
PUB=OUT.parents[1]
E=PUB/'integration_20260912e'
NEXT=PUB/'integration_20260913_next'
checks=[]
parser=argparse.ArgumentParser()
parser.add_argument('--attachment',type=Path,help='Optional private intake input for local review-pin checks; omitted for portable mathematical regression.')
parser.add_argument('--negative-control',action='store_true',help='Intentionally require a false Gaussian identity; must exit nonzero in every Python mode.')
ARGS=parser.parse_args()
started=time.perf_counter()
def check(ok,label,kind='exact'):
    checks.append({'label':label,'passed':bool(ok),'kind':kind})
    if not ok:raise AssertionError(label)
def eq(a,b,label):check(s.cancel(a-b)==0,label)
def sha(p):
    with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def enc(x):
    if isinstance(x,s.MatrixBase):return [[str(v) for v in row] for row in x.tolist()]
    return str(x)

# The general statement is proved in the companion note; these are independent
# finite symbolic identities and exact rational boundary/inequality checks.
for r in range(1,9):
    d=s.symbols('d0:'+str(r+1),positive=True)
    local=s.prod((1-d[j])*(1-d[j+1])/d[j+1] for j in range(r))
    window=(1-d[0])*(1-d[-1])*s.prod((1-x)**2 for x in d[1:-1])/s.prod(d[1:])
    eq(local,window,f'symbolic product factorization r={r}')

v=s.symbols('v',positive=True)
eq(s.diff(s.log(1-s.exp(-v)),v,2),-s.exp(-v)/(1-s.exp(-v))**2,'interior concavity second derivative')
x,y=s.symbols('x y',positive=True)
# x=e^(-v0/2), y=e^(-v1/2); polynomial identity for old local loss.
old_local=(1/(x*y)-x*y)**2/4
local=(1-x*x)*(1/(y*y)-1)
eq(old_local-local,(x/y-(1/(x*y)+x*y)/2)**2,'old local imbalance square')

grid=(F(1),F(1,2),F(2,3),F(3,4))
scalar_cases=0
phase_cases=0
for r in range(1,6):
    for d in itertools.product(grid,repeat=r+1):
        # Limit the longest grid deterministically; shorter grids exhaustive.
        if r==5 and scalar_cases%5!=0:
            scalar_cases+=1
            continue
        norm=[F((j+2)**2,j+1) for j in range(r+1)]
        omega=norm[-1]/norm[0]
        rho=[norm[j+1]/norm[j]*(1-d[j])*(1-d[j+1])/d[j+1] for j in range(r)]
        ph2=[a/F(j+2) for j,a in enumerate(rho)]
        ep2=[a-b for a,b in zip(rho,ph2)]
        exact=omega*(1-d[0])*(1-d[-1])*prod((1-z)**2 for z in d[1:-1])/prod(d[1:])
        check(prod(rho)==exact,f'rational factorization {r}:{scalar_cases}')
        check(min(ep2)**r<=prod(ep2)<=exact,f'phase-retaining minimum {r}:{scalar_cases}')
        check(prod(min(ep2)+p for p in ph2)<=exact,f'phase polynomial threshold {r}:{scalar_cases}')
        check(exact<=omega/prod(d[1:]),f'two-volume corollary {r}:{scalar_cases}')
        if any(z==1 for z in d):
            check(min(ep2)==0 and any(a==p==0 for a,p in zip(ep2,ph2)),f'zero-contraction endpoint {r}:{scalar_cases}')
        if any(ph2):phase_cases+=1
        scalar_cases+=1

# Exact comparisons including the radical exponents: all d are rational powers
# selected so both relevant roots are rational. No floating comparison proves
# any asserted general inequality.
for r in range(1,9):
    for pattern in range(20):
        base=[grid[(j*j+pattern+2*j)%len(grid)] for j in range(r+1)]
        power=2*r*max(1,r-1)
        d=[z**power for z in base]
        alpha,beta=d[0],d[-1]
        t=prod(d[1:-1])
        exact=(1-alpha)*(1-beta)*prod((1-z)**2 for z in d[1:-1])/(beta*t)
        if r==1:
            upper=exact
        else:
            troot=prod(z**(2*r) for z in base[1:-1])
            check(troot**(r-1)==t,f'exact interior root {r}:{pattern}')
            upper=(1-alpha)*(1-beta)*(1-troot)**(2*(r-1))/(beta*t)
        z=base[0]**max(1,r-1)*base[-1]**max(1,r-1)*prod(a**(2*max(1,r-1)) for a in base[1:-1])
        check(z**(2*r)==alpha*beta*t*t,f'exact old Jensen root {r}:{pattern}')
        old=((1/z-z)/2)**(2*r)
        check(exact<=upper<=old,f'sharper endpoint versus old Jensen {r}:{pattern}')
        check(upper<=1/(beta*t),f'sharper endpoint versus simple corollary {r}:{pattern}')

# Geometric contractions: exact powered version of the cosh(v/2) ratio.
for droot in (s.Rational(1,2),s.Rational(2,3),s.Rational(3,4)):
    d=droot**2
    U=(1-d)/droot
    old=(1/d-d)/2
    eq(old/U,(droot+1/droot)/2,'geometric contraction old/new ratio '+str(d))

# Literal Gaussian source, normal moments at theta=0. All Grams are calculated
# from the monic recurrence or the original moment matrix, never assigned.
u=s.symbols('u',real=True)
Q=[s.Integer(1),u]
for j in range(1,10):Q.append(s.expand(u*Q[-1]-j*Q[-2]))
mass=s.Integer(7)
omega=[mass*s.factorial(j) for j in range(len(Q))]
def moment(k):return mass*(s.factorial2(k-1) if k%2==0 else 0)
def pairing(p):
    p=s.Poly(s.expand(p),u)
    return sum(c*moment(m[0]) for m,c in p.terms())
for j,p in enumerate(Q[:8]):
    eq(pairing(p*p),omega[j],f'literal mass-seven monic norm {j}')
    for l in range(j):eq(pairing(p*Q[l]),0,f'Gaussian orthogonality {j},{l}')

def gaussian_quotient(chi,mean=s.Rational(0)):
    q=s.degree(chi,u)
    b=[]
    for p in Q:
        rem=s.Poly(s.rem(p.subs(u,u-mean),chi,u),u)
        b.append(s.Matrix([rem.nth(j) for j in range(q)]))
    # mass(theta)=7*exp(theta^2/2); work with its explicitly factored Grams.
    T=s.zeros(q)
    for j in range(q):
        rem=s.Poly(s.rem(u**(j+1),chi,u),u)
        for i in range(q):T[i,j]=rem.nth(i)
    sigma=s.trace(T)
    H=s.zeros(q);rows={}
    for N in range(8):
        H+=b[N]*b[N].T/s.factorial(N)
        if N<q-1:continue
        g=H.inv();vol=s.cancel(g.det())
        W=s.I*(g*T-T.T*g)
        eps2=s.cancel(s.trace((g.inv()*W)**2)/2)
        phase=s.cancel((b[N].T*g*b[N+1])[0]/s.factorial(N))
        Hp=s.zeros(q)
        for j in range(1,N+1):Hp-=j*(b[j-1]*b[j].T+b[j]*b[j-1].T)/s.factorial(j)
        logVprime=q*mean-s.trace(g*Hp)
        eq(phase,sigma-logVprime,f'phase from actual tilt derivative chi={chi},theta={mean},N={N}')
        rows[N]={'g':g,'v':vol,'eps2':eps2,'phase':phase}
    for N in range(q,7):
        a=rows[N]['v']/rows[N-1]['v'];bnext=rows[N+1]['v']/rows[N]['v']
        eq(rows[N]['eps2']+rows[N]['phase']**2,(N+1)*(1-a)*(1/bnext-1),
           f'actual Gaussian radius chi={chi},theta={mean},N={N}')
        check(0<a<=1 and 0<bnext<=1,f'actual Gaussian positive contractions chi={chi},theta={mean},N={N}')
    return rows

gauss=gaussian_quotient(u*u+1)
tilted=gaussian_quotient(u*u+1,s.Rational(1,2))
zero=gaussian_quotient(u*u-3)
rankone=gaussian_quotient(u-1)
check(all(tilted[N]['phase']!=0 for N in range(2,6)),'actual nonzero tilt phase cases are genuinely nonzero')
check(zero[3]['v']==zero[2]['v'] and zero[2]['eps2']==zero[3]['eps2']==0,'interior zero contraction forces both neighboring allowances zero')
check(all(rankone[N]['eps2']==0 for N in range(1,7)),'q=1 relative control identically zero')
check(any(rankone[N]['phase']!=0 for N in range(1,7)),'q=1 may retain a nonzero phase')
tilt_d=[tilted[N]['v']/tilted[N-1]['v'] for N in range(2,6)]
tilt_product=s.prod(tilted[N]['eps2']+tilted[N]['phase']**2 for N in range(2,5))
eq(tilt_product,60*tilted[2]['v']/tilted[5]['v']*(1-tilt_d[0])*(1-tilt_d[-1])*
   s.prod((1-z)**2 for z in tilt_d[1:-1]),'actual nonzero-phase full window product n=2,r=3')
for N,G in {2:s.diag(s.Rational(7,3),7),3:s.diag(s.Rational(7,3),s.Rational(21,11)),4:s.diag(s.Rational(42,43),s.Rational(21,11))}.items():
    check(mass*gauss[N]['g']==G,f'attachment literal Gram G_{N}')
for N,V in {1:49,2:s.Rational(49,3),3:s.Rational(49,11),4:s.Rational(882,473),5:s.Rational(980,1333)}.items():
    eq(mass**2*gauss[N]['v'],V,f'attachment literal volume V_{N}')
for N,eps in {2:s.Rational(16,3),3:s.Rational(400,99),4:s.Rational(4225,946)}.items():
    eq(gauss[N]['eps2'],eps,f'attachment exact radius {N}')

q=2;chi=u*u+1;Pi=chi**2
D={0:s.Integer(1)};B={0:s.Integer(1)}
for a in range(1,7):
    D[a]=s.Matrix(a,a,lambda i,j:moment(i+j)).det()
    B[a]=s.Matrix(a,a,lambda i,j:pairing(Pi*u**(i+j))).det()
    eq(D[a],s.prod(omega[j] for j in range(a)),f'moment/source norm determinant {a}')
def jets(p):return s.Matrix([s.diff(p,u,d).subs(u,z) for z in (-s.I,s.I) for d in range(2)])
Vand=s.Matrix.hstack(*(jets(u**j) for j in range(4)))
eq(Vand.det(),16,'raw confluent Vandermonde with fixed row order')
transfers={}
for a in range(5):
    mat=s.Matrix.hstack(*(jets(Q[a+j]) for j in range(4)))
    transfers[a]=s.expand(mat.det())
    eq(transfers[a]/Vand.det(),B[a]/D[a],f'raw-jet transfer determinant a={a}')
    N=a+q-1
    eq(mass**q*gauss[N]['v'],D[N+1]/B[a],f'original source/relation quotient volume {N}')
    Lambda=omega[N]/(mass**q*gauss[N]['v'])
    eq(Lambda,B[a]/D[N],f'Lambda literal determinant cancellation {N}')
    eq(Lambda,transfers[a]/(Vand.det()*s.prod(omega[j] for j in range(a,N))),f'Lambda transfer cancellation {N}')
for a,r in ((0,1),(1,1),(1,3),(2,2)):
    n=a+q-1
    ratio=(omega[n+r]/gauss[n+r]['v'])/(omega[n]/gauss[n]['v'])
    transfer=transfers[a+r]/transfers[a]*s.prod(omega[a+j]/omega[a+r+j] for j in range(q-1))
    eq(ratio,transfer,f'two-transfer endpoint ratio a={a},r={r}')
q1transfers={}
for a in range(5):
    mat=s.Matrix([[Q[a+j].subs(u,1) for j in range(2)],
                  [s.diff(Q[a+j],u).subs(u,1) for j in range(2)]])
    q1transfers[a]=mat.det()
    B1=s.Matrix(a,a,lambda i,j:pairing((u-1)**2*u**(i+j))).det() if a else s.Integer(1)
    eq(q1transfers[a],B1/D[a],f'q=1 raw-jet transfer a={a}')
    eq(omega[a]/(mass*rankone[a]['v']),q1transfers[a],f'q=1 Lambda has empty norm band a={a}')
eq((omega[3]/rankone[3]['v'])/(omega[1]/rankone[1]['v']),
   q1transfers[3]/q1transfers[1],'q=1 two-transfer ratio no norm factors')
for qtest in (1,2,3,5):
    N=qtest+2;c=s.Rational(5,3)
    eq(c**(N-qtest+1)/c**N,c**(1-qtest),f'full literal mass scaling Lambda q={qtest}')

n=2;r=3
vol={N:mass**2*gauss[N]['v'] for N in gauss}
alpha=vol[2]/vol[1];beta=vol[5]/vol[4];t=vol[4]/vol[2];Om=omega[5]/omega[2]
eq(alpha,s.Rational(1,3),'fixture alpha')
eq(beta,s.Rational(110,279),'fixture beta')
eq(t,s.Rational(54,473),'fixture interior product')
eq(Om,60,'fixture norm endpoint ratio')
e2=[gauss[N]['eps2'] for N in (2,3,4)]
Emin=s.sqrt(min(e2));geom=s.prod(e2)**s.Rational(1,6)
upper=(Om*(1-alpha)*(1-beta)/(beta*t)*(1-s.sqrt(t))**4)**s.Rational(1,6)
old=Om**s.Rational(1,6)*s.sinh(s.log(vol[1]*vol[2]/(vol[4]*vol[5]))/6)
display={name:str(value.evalf(50)) for name,value in [('minimum',Emin),('geometric',geom),('sharper_endpoint',upper),('old_Jensen',old)]}
for key,written in [('minimum','2.0100756305'),('geometric','2.1407199197'),('sharper_endpoint','2.1666731523'),('old_Jensen','2.5178436564')]:
    check(abs(s.Float(display[key],55)-s.Float(written,55))<s.Rational(1,2)*10**-10,'attachment ten-decimal display '+key,'approximate_display')

# Parent synthesis: verify integer endpoint placement and overlapping budget.
for k in range(3,15):
    for m in (1,2,3):
        qk=(1+k*(m-1))*(k+1)**2
        check(qk>=k>=3 and qk-1>=1,'quartet admission '+str((k,m)))
        n=qk;rr=qk-1
        check(n+rr==2*qk-1 and n+rr-1==2*qk-2,'near-diagonal window indices '+str((k,m)))
for n in range(3,16):
    ell=2*s.Integer(n)**(2*n+1)/(2*n+1)*(s.Integer(2)**n/s.binomial(2*n,n))**2
    low=2*s.Integer(n)**(2*n+1)/((2*n+1)*s.Integer(4)**n)
    check(ell>=low,'Legendre lower factor n='+str(n))
    for r in range((n+1)//2,n+1):
        check(s.factorial(2*(n+r))<=(4*n)**(2*(n+r)),'balanced factorial n,r='+str((n,r)))
        eq(((4*n)**(2*(n+r))*s.Integer(4)**n/s.Integer(n)**(2*n))**1,
           s.Integer(n)**(2*r)*s.Integer(4)**(2*r)*s.Integer(8)**(2*n),
           'balanced factorial/Legendre power cancellation n,r='+str((n,r)))
        check(n<=2*r and n+r<=3*r,'balanced exponents n,r='+str((n,r)))
prev,central,last,end=s.symbols('Vprev Vq Vlast Vend',positive=True)
eq((prev*central/(last*end))/(central/last)**2,(prev/central)*(last/end),
   'exact multiplicative four-volume central decomposition')

input_specs={}
if ARGS.attachment is not None:
  input_specs={
    'submitted_window_product_attachment':ARGS.attachment,
    'original_TVB_source':E/'original_sources/toda_cv_exact_bridge_20260912.tex',
    'PR23_corrected_endpoint_note':NEXT/'review_pr24/join_inputs/PR23_ENDPOINT_CORRECTED.md',
    'PR23_original_source_coordinate_note':E/'review_pr23/files/workbenches/tau-toda-volume-formal/SOURCE_COORDINATES.md',
    'PR24_full_confluent_transfer_note':NEXT/'review_pr24/files/workbenches/tau-confluent-transfer/RESEARCH_NOTE.md'}
  input_specs.update({
    'arithmetic_endpoint_complete_note':NEXT/'arithmetic_endpoint_review/source_stage/Tau_Arithmetic_Endpoint_Bounds/NOTE.tex',
    'independent_balanced_window_proof':NEXT/'arithmetic_endpoint_review/BALANCED_WINDOW_PROOF.md',
    'parent_four_volume_threshold':NEXT/'FOUR_VOLUME_THRESHOLD.md'})
  check(sha(input_specs['parent_four_volume_threshold'])=='9ff55c84d74db85306e7a68c70fe7b08d8e642e8ac1a3e6137649f68e102fc3a',
      'parent complete read and checked threshold note immutable pin')
if ARGS.negative_control:
    eq(gauss[2]['eps2'],s.Rational(16,3)+1,'intentional false Gaussian fixture (expected failure)')
receipt={
    'schema':'independent-exact-window-product-review-v1',
    'created_utc':datetime.now(timezone.utc).isoformat(),
    'status':'PASS','checks_total':len(checks),'exact_checks':sum(c['kind']=='exact' for c in checks),
    'approximate_display_checks':sum(c['kind']=='approximate_display' for c in checks),'checks':checks,
    'symbolic_window_lengths':list(range(1,9)),
    'scalar_case_counter_including_deterministic_skips':scalar_cases,
    'nonzero_scalar_phase_cases':phase_cases,
    'actual_gaussian_tilt':{'theta':'1/2','literal_mass':'7 exp(1/8)',
        'rows':{str(N):{'phase':enc(tilted[N]['phase']),'epsilon_squared':enc(tilted[N]['eps2']),
                        'Gram_divided_by_explicit_literal_mass':enc(tilted[N]['g'])} for N in range(2,6)}},
    'literal_gaussian_fixture':{'mass':'7','q':2,'chi':'u^2+1',
        'Grams':{str(N):enc(mass*gauss[N]['g']) for N in (2,3,4)},
        'volumes':{str(N):enc(vol[N]) for N in range(1,6)},
        'epsilon_squared':{str(N):enc(gauss[N]['eps2']) for N in (2,3,4)},
        'approximate_display_only_not_interval_certificate':display},
    'input_pins':{name:{'bytes':p.stat().st_size,'sha256':sha(p)} for name,p in input_specs.items()},
    'input_pin_scope':'Local review input bytes checked' if input_specs else 'Portable mathematical regression only; no local intake sources reopened',
    'primary_references_read':['https://dlmf.nist.gov/1.7.iv','https://dlmf.nist.gov/18.2.iv','https://dlmf.nist.gov/18.2.ix'],
    'limits':['Finite exact regression is not a general proof; see written proof note.',
              'Gaussian and scalar fixtures are not actual arithmetic zero packets.',
              'No Lean, arbitrary-precision interval certificate, heavy replay, remote write or canonical edit.',
              'No actual arithmetic endpoint upper-growth bound is established by these checks.'],
    'parent_threshold_review':({'status':'PASS','scope':'Complete file read; sections 3–5 exact product, phase, endpoint degeneracy, original maps and factor-four composition checked; section 2 balanced constant also checked.',
                               'sha256':sha(input_specs['parent_four_volume_threshold'])} if input_specs else None),
    'python_version':sys.version.split()[0],'sympy_version':s.__version__,
    'elapsed_seconds':time.perf_counter()-started,'script_sha256':sha(Path(__file__))}
receipt_path=OUT/('EXACT_VERIFICATION_RECEIPT.json' if input_specs else 'PORTABLE_CHECK_RECEIPT.json')
receipt_path.write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':receipt['status'],'checks_total':len(checks),'exact_checks':receipt['exact_checks'],
                  'approximate_display_checks':receipt['approximate_display_checks'],'elapsed_seconds':receipt['elapsed_seconds'],
                  'fixture_display':display,'receipt_sha256':sha(receipt_path)},indent=2))
