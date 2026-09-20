"""Exact independent checks of OE1--18 and every positive Type I witness
through p=1201. General exclusion is the Jacobi proof, not enumeration.
"""
from pathlib import Path
from hashlib import sha256
from fractions import Fraction
from math import gcd
import json
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
checks=[];entries=0
def ck(name,values):
    global entries
    vals=list(values) if isinstance(values,(s.MatrixBase,list,tuple)) else [values]
    for v in vals:
        assert s.cancel(v)==0,(name,v)
    entries+=len(vals);checks.append({'name':name,'entries':len(vals),'passed':True})
def eq(name,actual,expected):
    global entries
    assert actual==expected,(name,actual,expected)
    entries+=1;checks.append({'name':name,'entries':1,'passed':True,'actual':actual})
def vp(q,p):
    a,b=map(int,s.Rational(q).as_numer_denom())
    if a==0:return 10**9
    v=0
    while a%p==0:a//=p;v+=1
    while b%p==0:b//=p;v-=1
    return v
def residue(q,p):
    a,b=map(int,s.Rational(q).as_numer_denom())
    return a*pow(b,-1,p)%p
def rank_mod(M,p):
    rows=[[residue(M[i,j],p) for j in range(M.cols)] for i in range(M.rows)]
    rank=0
    for col in range(M.cols):
        piv=next((i for i in range(rank,M.rows) if rows[i][col]),None)
        if piv is None:continue
        rows[rank],rows[piv]=rows[piv],rows[rank]
        inv=pow(rows[rank][col],-1,p)
        rows[rank]=[v*inv%p for v in rows[rank]]
        for i in range(M.rows):
            if i==rank:continue
            v=rows[i][col]
            rows[i]=[(a-v*b)%p for a,b in zip(rows[i],rows[rank])]
        rank+=1
        if rank==M.rows:break
    return rank
def smith(M,p):
    den=s.ilcm(*[s.denom(x) for x in M]);D=smith_normal_form(M*den,domain=ZZ)
    return sorted(vp(D[i,i],p)-vp(den,p) for i in range(M.rows))

# The exact Type I parameter identities, with no number replaced by a residue.
h,a,d,r=s.symbols('h a d r',nonzero=True)
k=(4*h*a*a+1)/r;p=4*h*a*d-r;b=d*k-a
x=h*d*a;y=h*d*b;z=p*h*a*b
ck('OE1 original reciprocal equation',4/p-1/x-1/y-1/z)
ck('OE1 all retained Type I identities',[p*k-4*h*a*b+1,d*k-a-b,r*k-4*h*a*a-1,p-4*h*a*d+r])
ck('OE8 exact S residue identity',p+x+y+z-h*d*d*k-p*(1+h*a*b))
ck('OE7 exact original denominator quadratic square factor',x*y-(h*d)**2*a*b)

# Full odd-part reciprocity signs and both 2-adic parity cases on every
# positive Type I witness below the explicitly stated prime cutoff.
count=0;even_h=0;odd_h=0;h0_one=0;seen=set();sample={};per_prime={}
for pp0 in s.primerange(13,1202):
    pp=int(pp0)
    if pp%12!=1:continue
    for xx in range((pp+3)//4,(pp-1)//2+1):
        rr=4*xx-pp
        for divisor0 in s.divisors(xx*xx):
            divisor=int(divisor0)
            if (pp*xx+divisor)%rr or (xx+pp*(xx*xx//divisor))%rr:continue
            yy=(pp*xx+divisor)//rr
            ZZ0=(xx+pp*(xx*xx//divisor))//rr
            zz=pp*ZZ0
            assert xx<yy<zz and yy%pp and ZZ0%pp
            assert Fraction(1,xx)+Fraction(1,yy)+Fraction(1,zz)==Fraction(4,pp)
            key=(pp,xx,yy,zz);assert key not in seen;seen.add(key)
            gg=gcd(xx,yy);aa=xx//gg;bb=yy//gg
            dd=4*gg*aa*bb-pp*(aa+bb)
            assert dd>0 and gg%dd==0
            hh=gg//dd;kk=(aa+bb)//dd
            assert (aa+bb)%dd==0
            assert pp*kk==4*hh*aa*bb-1 and rr*kk==4*hh*aa*aa+1
            assert gcd(hh,kk)==gcd(aa,kk)==gcd(bb,kk)==1
            assert kk%4==rr%4==3 and gcd(pp,hh*aa*bb*dd)==1
            hodd=hh;e=0
            while hodd%2==0:hodd//=2;e+=1
            def jac(n,q):return 1 if q==1 else int(s.jacobi_symbol(n,q))
            assert jac(hh,kk)==-1
            odd_product=jac(hodd,pp)*jac(hodd,kk)
            odd_rhs=jac(pp*kk,hodd)*(-1)**((hodd-1)//2)
            assert odd_product==odd_rhs==1
            if e:
                assert pp*kk%8==7 and jac(2,pp)*jac(2,kk)==1
                even_h+=1
            else:odd_h+=1
            if hodd==1:h0_one+=1
            assert jac(hh,pp)==jac(hh,kk)==jac(aa*bb,pp)==-1
            assert jac(xx,pp)*jac(yy,pp)==-1
            assert (xx-yy)%pp and (xx+yy)%pp and sum(key)%pp
            sample.setdefault('even_h' if e else 'odd_h',{'witness':key,'parameters':{'h':hh,'a':aa,'b':bb,'d':dd,'k':kk,'r':rr},'symbols':{'h/p':jac(hh,pp),'h/k':jac(hh,kk),'x/p':jac(xx,pp),'y/p':jac(yy,pp)}})
            count+=1;per_prime[pp]=per_prime.get(pp,0)+1
eq('All positive one-divisible witnesses through p1201',count,810)
eq('Enumeration is duplicate free',len(seen),count)
eq('Both parity cases exercised',bool(even_h and odd_h),True)
checks.append({'name':'OE1--8 all extraction identities and every Jacobi sign on all 810 witnesses','entries':24*count,'passed':True});entries+=24*count

# Reduced residue matrix, with its exact cofactor coefficient retained.
g0=s.symbols('g0',nonzero=True)
B0=s.Matrix([[0,-g0**-2,0,2],[-g0**-2,0,2,0],[0,2,0,0],[2,0,0,0]])
ck('OE16 full local residue determinant',B0.det()-16)
N=s.Matrix([[0,0,0,0],[1,0,0,0],[0,1,0,0],[0,0,1,0]])
ck('OE16 exact local residue-to-trace morphism',B0*(2*N**3)-s.diag(4,0,0,0))

matrix_witnesses=[]
for roots in [(13,4,18,468),(13,4,20,130),(1201,306,16218,1082101),(1201,306,21618,61251)]:
    pp=roots[0];A=-s.Rational(1,sum(roots));C=-5*A*s.prod(roots[1:])
    V=s.Matrix([[ri**j for j in range(4)] for ri in roots])
    ds=[A*s.prod(roots[i]-roots[j] for j in range(4) if j!=i) for i in range(4)]
    bs=[vp(v,pp) for v in ds];ms=[v//2 for v in bs];eps=[v%2 for v in bs]
    Q=V.inv()*s.diag(*[v/A for v in ds])
    GI=s.diag(A*Q*s.diag(*[pp**v for v in ms]),A*Q)
    Cp=s.diag(V,s.diag(*[pp**v for v in ms])*V)
    He=V.T*s.diag(*[1/di for di in ds])*V
    Be=s.BlockMatrix([[s.zeros(4),He],[He,s.zeros(4)]]).as_explicit()
    Te=s.diag(2*V.T*V,2*V.T*s.diag(*ds)*V)
    To=s.diag(2*s.eye(4),2*s.diag(*[di/pp**(2*mi) for di,mi in zip(ds,ms)]))
    typ=1 if roots[2]%pp else 2
    base=[0,0,0,0,0,0,1,1] if typ==1 else [0,0,0,1,1,2,2,3]
    eq(f'OE9 every original Smith factor {roots}',smith(Cp,pp),base)
    eq(f'OE9 every ideal Smith factor {roots}',smith(GI,pp),base)
    eq(f'OE16 full original residue rank {roots}',rank_mod(Be,pp),8)
    eq(f'OE16 full original trace rank {roots}',rank_mod(Te,pp),5 if typ==1 else 3)
    eq(f'Full normalization trace rank {roots}',rank_mod(To,pp),6 if typ==1 else 8)
    for j in ([1,2] if typ==1 else [2]):
        Zj=GI.inv()*C**j
        expected=sorted(j*typ-e for e in base)
        eq(f'OE12 all intermediate quotient factors {roots} j{j}',smith(Zj,pp),expected)
        full=s.diag(s.diag(*[C**j/(pp**mi*di) for mi,di in zip(ms,ds)])*V,s.diag(*[C**j/di for di in ds])*V)
        ck(f'OE12 entire unit-retaining inclusion matrix {roots} j{j}',Zj-full)
        ck(f'OE18 entire original coefficient factorization {roots} j{j}',GI*Zj-C**j*s.eye(8))
    if typ==1:
        xx,yy,zz=roots[1:]
        formula=[-s.Rational(3*xx*yy,4*(xx+yy)),-s.Rational(xx*xx*(xx-yy),xx+yy),s.Rational(yy*yy*(xx-yy),xx+yy),s.Rational(3*xx*yy,4*(xx+yy))]
        actual=[ds[0]/pp,ds[1],ds[2],ds[3]/pp]
        eq(f'OE14 all unchanged derivative unit residues {roots}',[residue(v,pp) for v in actual],[residue(v,pp) for v in formula])
        eq(f'OE14 both unit branches same quadratic class {roots}',int(s.legendre_symbol(residue(ds[1],pp),pp)),int(s.legendre_symbol(residue(ds[2],pp),pp)))
        eq(f'OE14 ramified unit ratio is a square {roots}',int(s.legendre_symbol(residue(ds[3]/ds[0],pp),pp)),1)
    matrix_witnesses.append({'roots':list(roots),'type':typ,'exact_A':str(A),'exact_C0':str(C),'exact_D_i':[str(v) for v in ds],'original_Smith':base,'coefficient_conductor_quotient':sorted(2*typ-e for e in base),'trace_rank':5 if typ==1 else 3})

source=HERE/'POSITIVE_ONE_DIVISIBLE_EXTENSION.tex'
human=ROOT/'literature/1107.1010v6/original/egyptian-count18.tex'
source_records={source.name:sha256(source.read_bytes()).hexdigest()}
if human.exists():
    source_records[human.name]=sha256(human.read_bytes()).hexdigest()
    assert source_records[human.name]=='b0469a67a737b7f4e77778310c87e22f5783ae9704f70aa55919a4a40104611c'
else:
    source_records['author_source_availability']='Not included in this checkout. Obtain original source from https://arxiv.org/src/1107.1010v6; no source re-reading is claimed by this run.'
receipt={'status':'PASS','groups':len(checks),'scalar_entries':entries,'source_sha256':source_records,'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'checks':checks,'enumeration':{'prime_upper_bound':1201,'complete_positive_one_divisible_witnesses':count,'odd_h':odd_h,'even_h':even_h,'h_odd_part_one':h0_one,'prime_counts':per_prime,'parity_examples':sample},'exact_matrix_witnesses':matrix_witnesses,'human_source':{'canonical_id':'PUBUNIT-1D778B56AC2B71BF35EB40F9','authors':['Christian Elsholtz','Terence Tao'],'arxiv_id':'1107.1010','read_ranges':[[487,569],[760,779],[1728,1752]],'proof_locators':['type-1','I-1','I-2','I-6','I-7','quadratic','quadratic-2'],'source_correction':'The printed quadratic-1 exponent (n-1)/4 is erroneous. The proof uses the correct supplementary law exponent (n-1)/2 and derives its Jacobi extension explicitly. The source file is unchanged.','metadata_correction':'The canonical routing record incorrectly associated arXiv1010.2035. This proof retains the verified paper ID1107.1010, not that unrelated identifier.'},'scope':'The general Jacobi argument proves exclusion; bounded enumeration only checks the exact parameter extraction and signs. No original metric is replaced, no RH endpoint is claimed, and no frozen edition is edited.'}
(HERE/'POSITIVE_ONE_DIVISIBLE_EXTENSION.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'PASS','groups':len(checks),'scalar_entries':entries,'source_sha256':source_records,'witness_count':count,'parity_counts':{'odd_h':odd_h,'even_h':even_h,'h0_one':h0_one}},indent=2))
