"""Exact checks of SLF1--19. Finite searches supplement the written proof.

All arithmetic uses integers or rational numbers. No floating-point test
is used to decide a quadratic field, a lattice, or a matrix identity.
"""
from pathlib import Path
from fractions import Fraction
from hashlib import sha256
from math import gcd
from collections import Counter
import json
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

HERE = Path(__file__).resolve().parent
checks = []
entries = 0


def ck(name, values):
    global entries
    if isinstance(values, s.MatrixBase):
        values = list(values)
    elif not isinstance(values, (list, tuple)):
        values = [values]
    for value in values:
        assert s.cancel(value) == 0, (name, value)
    entries += len(values)
    checks.append({'name': name, 'entries': len(values), 'passed': True})


def eq(name, a, b):
    global entries
    assert a == b, (name, a, b)
    entries += 1
    checks.append({'name': name, 'entries': 1, 'passed': True})


def vp(q, p):
    a, b = map(int, s.Rational(q).as_numer_denom())
    if not a:
        return 10**9
    result = 0
    while a % p == 0:
        a //= p
        result += 1
    while b % p == 0:
        b //= p
        result -= 1
    return result


def res(q, modulus):
    a, b = map(int, s.Rational(q).as_numer_denom())
    return a * pow(b, -1, modulus) % modulus


def leg(q, p):
    a = pow(res(q, p), (p - 1) // 2, p)
    assert a in (1, p - 1), (q, p)
    return 1 if a == 1 else -1


def smith_valuations(M, p):
    den = s.ilcm(*[s.denom(v) for v in M])
    D = smith_normal_form(M * den, domain=ZZ)
    return sorted(vp(D[i, i], p) - vp(den, p) for i in range(M.rows))


def integral(M, p):
    return all(vp(v, p) >= 0 for v in M)


def lift(q, p, precision=6):
    """Retain the full rational target, at every lifting step."""
    a = min(i for i in range(1, p) if (i * i - res(q, p)) % p == 0)
    modulus = p
    for _ in range(1, precision):
        next_modulus = modulus * p
        error = (res(q, next_modulus) - a * a) // modulus
        digit = error * pow(2 * a, -1, p) % p
        a += modulus * digit
        modulus = next_modulus
        assert (a * a - res(q, modulus)) % modulus == 0
    return a, modulus


p, x, y, Y, Z = s.symbols('p x y Y Z')
A1 = -1 / (p + x + y + p * Z)
r1 = [p, x, y, p * Z]
full1 = [A1 * s.prod(r1[i] - r1[j] for j in range(4) if j != i)
         for i in range(4)]
units1 = [A1 * (1-Z) * (p-x) * (p-y),
          A1 * (x-p) * (x-y) * (x-p*Z),
          A1 * (y-p) * (y-x) * (y-p*Z),
          A1 * (Z-1) * (p*Z-x) * (p*Z-y)]
ck('SLF2 full derivative units', [full1[i] - units1[i] * (p if i in (0, 3) else 1)
                                  for i in range(4)])
red1 = [-3*x*y/(4*(x+y)), -x*x*(x-y)/(x+y),
        y*y*(x-y)/(x+y), 3*x*y/(4*(x+y))]
ck('SLF3 all four residues', [units1[i].subs({p: 0, Z: s.Rational(1, 4)}) - red1[i]
                              for i in range(4)])
A2 = -1 / (p + x + p*Y + p*Z)
r2 = [p, x, p*Y, p*Z]
full2 = [A2 * s.prod(r2[i] - r2[j] for j in range(4) if j != i)
         for i in range(4)]
units2 = [A2*(p-x)*(1-Y)*(1-Z), A2*(x-p)*(x-p*Y)*(x-p*Z),
          A2*(p*Y-x)*(Y-1)*(Y-Z), A2*(p*Z-x)*(Z-1)*(Z-Y)]
ck('SLF7 full derivative units', [full2[i] - units2[i]*(1 if i == 1 else p*p)
                                  for i in range(4)])
red2 = [(1-Y)*(1-Z), -x*x, (Y-1)*(Y-Z), (Z-1)*(Z-Y)]
ck('SLF8 all four residues', [units2[i].subs(p, 0) - red2[i] for i in range(4)])
vdet2 = s.prod(r2[j]-r2[i] for i in range(4) for j in range(i+1,4))
ck('SLF9 full-unit square identity', s.prod(units2) - (A2*A2*vdet2/p**3)**2)

r, ra, rb, rj, rx = s.symbols('r ra rb rj rx')
gm = (r-ra)*(r-rb)
gp = (r-rj)*(r-rx)
coeff = lambda q: s.Matrix([s.expand(q).coeff(r, i) for i in range(4)])
Lm = s.Matrix.hstack(coeff(gm), coeff(r*gm), coeff(gp), coeff(r*gp))
ck('SLF14 complete resultant determinant',
   Lm.det() - (ra-rj)*(ra-rx)*(rb-rj)*(rb-rx))

type1_counts = Counter()
type2_counts = Counter()
type1_examples = {}
type2_examples = {}
enumeration_entries = 0
for pp in map(int, s.primerange(13, 1202)):
    if pp % 12 != 1:
        continue
    # Let x<y be the two unit denominators. Since z=pZ>=p,
    # 3/p <= 1/x+1/y <= 2/x, so x<=2p/3. The exact factorization
    # ((4x-p)y-px)((4x-p)Z-x)=p*x^2 parametrizes all such witnesses;
    # its first factor is a p-unit and therefore a positive divisor of x^2.
    for xx in range((pp+3)//4, (2*pp)//3+1):
        rr = 4*xx-pp
        for tt in map(int, s.divisors(xx*xx)):
            if (pp*xx+tt) % rr or (xx+pp*(xx*xx//tt)) % rr:
                continue
            yy = (pp*xx+tt)//rr
            ZZ0 = (xx+pp*(xx*xx//tt))//rr
            if xx >= yy or yy % pp == 0 or ZZ0 % pp == 0:
                continue
            zz = pp*ZZ0
            assert Fraction(1,xx)+Fraction(1,yy)+Fraction(1,zz)==Fraction(4,pp)
            gg = gcd(xx,yy)
            aa, bb = xx//gg, yy//gg
            dd = 4*gg*aa*bb-pp*(aa+bb)
            assert dd > 0 and (aa+bb)%dd == 0
            kk = (aa+bb)//dd
            chi = leg(s.Rational(xx-yy,xx+yy),pp)
            key = (chi,leg(kk,pp))
            roots = [pp,xx,yy,zz]
            AA = -s.Rational(1,sum(roots))
            Ds = [AA*s.prod(roots[i]-roots[j] for j in range(4) if j!=i)
                  for i in range(4)]
            assert [vp(q,pp) for q in Ds]==[1,0,0,1]
            assert leg(Ds[0]/(pp*kk),pp)==leg(Ds[3]/(pp*kk),pp)==1
            assert leg(Ds[2]/Ds[1],pp)==1
            assert leg(Ds[1],pp)==leg(Ds[2],pp)==chi
            type1_counts[key]+=1
            type1_examples.setdefault(key,(pp,xx,yy,zz,kk))
            enumeration_entries += 9
    # In Type II, p/x=4-1/Y-1/Z>=2, hence x<=p/2.
    # (kY-x)(kZ-x)=x^2, with Y<Z and k=4x-p, gives 0<t<x.
    for xx in range((pp+3)//4, pp//2+1):
        kk = 4*xx-pp
        for tt in map(int,s.divisors(xx*xx)):
            if tt >= xx:
                break
            if (xx+tt)%kk or (xx+xx*xx//tt)%kk:
                continue
            YY = (xx+tt)//kk
            ZZ0 = (xx+xx*xx//tt)//kk
            if min(YY,ZZ0)<1 or xx%pp==0 or YY%pp==0 or ZZ0%pp==0:
                continue
            assert YY < ZZ0
            assert Fraction(1,xx)+Fraction(1,pp*YY)+Fraction(1,pp*ZZ0)==Fraction(4,pp)
            roots=[pp,xx,pp*YY,pp*ZZ0]
            AA=-s.Rational(1,sum(roots))
            Ds=[AA*s.prod(roots[i]-roots[j] for j in range(4) if j!=i)
                for i in range(4)]
            assert [vp(q,pp) for q in Ds]==[2,0,2,2]
            us=[Ds[i]/(1 if i==1 else pp*pp) for i in range(4)]
            signs=tuple(leg(u,pp) for u in us)
            assert signs[1]==1 and s.prod(signs)==1
            expected=tuple(leg(q,pp) for q in [(1-YY)*(1-ZZ0),-xx*xx,
                           (YY-1)*(YY-ZZ0),(ZZ0-1)*(ZZ0-YY)])
            assert signs==expected
            type2_counts[signs]+=1
            type2_examples.setdefault(signs,(pp,xx,pp*YY,pp*ZZ0))
            enumeration_entries += 8
eq('all Type I witnesses through 1201',sum(type1_counts.values()),810)
eq('all Type II witnesses through 1201',sum(type2_counts.values()),346)
eq('all Type II patterns',dict(type2_counts),{
    (1,1,1,1):62,(1,1,-1,-1):106,(-1,1,1,-1):96,(-1,1,-1,1):82})
eq('all Type I field-class combinations',dict(type1_counts),{
    (1,1):268,(-1,1):236,(1,-1):156,(-1,-1):150})
eq('SLF18 actual Type I examples',dict(type1_examples),{
    (1,-1):(13,4,18,468,11),(-1,1):(13,4,20,130,3),
    (1,1):(13,5,10,130,3),(-1,-1):(37,16,22,6512,19)})
eq('SLF10 actual Type II examples',dict(type2_examples),{
    (1,1,-1,-1):(13,4,26,52),(-1,1,1,-1):(37,10,148,740),
    (1,1,1,1):(61,16,366,2928),(-1,1,-1,1):(61,18,122,549)})
checks.append({'name':'all defining-prime units and square classes through 1201',
               'entries':enumeration_entries,'passed':True})
entries += enumeration_entries

examples1=list(type1_examples.values())
examples2=list(type2_examples.values())
lifting_receipts=[]
for witness in examples1+examples2:
    pp,xx,yy,zz=witness[:4]
    roots=[pp,xx,yy,zz]
    AA=-s.Rational(1,sum(roots))
    V=s.Matrix([[q**j for j in range(4)] for q in roots])
    ds=[s.prod(roots[i]-roots[j] for j in range(4) if j!=i) for i in range(4)]
    Ds=[AA*d for d in ds]
    name=str(witness[:4])
    f=s.prod(r-q for q in roots)
    if len(witness)==5:
        kk=witness[4]
        chi=leg(Ds[1],pp)
        ratios=[Ds[0]/(pp*kk),Ds[3]/(pp*kk),Ds[2]/Ds[1]]
        patterns=[(1,1,1,1),(-1,1,1,-1)]
        if chi==-1:
            patterns += [(1,-1,-1,1),(-1,-1,-1,-1)]
        else:
            ratios.append(Ds[1])
        for eps in patterns:
            BB=V.inv()*s.diag(*eps)*V
            eq(name+' integral Type I Galois action '+str(eps),integral(BB,pp),True)
            ck(name+' involution '+str(eps),BB*BB-s.eye(4))
    else:
        us=[Ds[i]/(1 if i==1 else pp*pp) for i in range(4)]
        eps=tuple(leg(u,pp) for u in us)
        negatives=[i for i,e in enumerate(eps) if e==-1]
        ratios=[us[i] for i,e in enumerate(eps) if e==1]
        BB=V.inv()*s.diag(*eps)*V
        ck(name+' actual Frobenius square',BB*BB-s.eye(4))
        ck(name+' labelled evaluation action',V*BB-s.diag(*eps)*V)
        if negatives:
            ratios += [us[i]/us[negatives[0]] for i in negatives]
            j=next(i for i in (0,2,3) if eps[i]==1)
            a,b=negatives
            Nj=s.Matrix([[ds[j],-roots[j],0,0],[0,1,-roots[j],0],
                         [0,0,1,-roots[j]],[0,0,0,1]])
            minus=(r-roots[a])*(r-roots[b])
            plus=(r-roots[j])*(r-xx)
            L=s.Matrix.hstack(coeff(minus),coeff(r*minus),coeff(plus),coeff(r*plus))
            eq(name+' complete cyclic intersection Smith',smith_valuations(Nj,pp),[0,0,0,2])
            eq(name+' actual Frobenius relative Smith',smith_valuations(BB,pp),[-2,0,0,2])
            eq(name+' Frobenius preserves intersection',integral(Nj.inv()*BB*Nj,pp),True)
            eq(name+' eigenspace basis inside exact intersection',integral(Nj.inv()*L,pp),True)
            eq(name+' inverse basis change integral',integral(L.inv()*Nj,pp),True)
            ck(name+' exact eigenspace action',BB*L-L*s.diag(1,1,-1,-1))
            ck(name+' exact quotient row',
               s.Matrix([[roots[j]**i for i in range(4)]])*Nj-s.Matrix([[ds[j],0,0,0]]))
            # Exact rational Gram models test the simultaneous-basis identity
            # for full positive matrices; the written proof covers the original
            # moment/Gamma Grams symbolically and does not replace them by these.
            Q=s.Matrix([[1,2,0,1],[0,1,1,0],[0,0,1,3],[0,0,0,1]])
            H1=Q.T*s.diag(2,3,5,7)*Q
            H2=Q*s.diag(11,13,17,19)*Q.T
            ck(name+' full inverse-spectrum basis similarity',
               (Nj.T*H2*Nj).inv()*(Nj.T*H1*Nj)-Nj.inv()*H2.inv()*H1*Nj)
        else:
            ck(name+' split Type II action is identity',BB-s.eye(4))
    for number,q in enumerate(ratios):
        root,modulus=lift(q,pp)
        eq(name+' full rational Hensel target '+str(number),(root*root-res(q,modulus))%modulus,0)
        lifting_receipts.append({'witness':list(witness[:4]),'target':str(q),
                                'root_mod_p6':root,'modulus':modulus})

receipt={
    'status':'passed','proof':'SIGNED_LOCAL_FIELDS.tex','locators':'SLF1--19',
    'group_count':len(checks),'entry_count':entries,'checks':checks,
    'coverage':{
      'symbolic':'all full derivative units, their residues, full product square, exact eigenspace resultant',
      'finite':'every positive Type I and Type II witness up to p=1201, with the declared ordered denominator labels',
      'lattices':'four Type I field-class examples and all four Type II Frobenius patterns; exact rational matrices',
      'metrics':'rational positive Gram examples test the general basis-change identity; original Grams remain symbolic in SLF15--17',
      'not_claimed':'a finite check is not the proof of the exhaustive sign classification or an RH conclusion'},
    'type1_counts':{str(k):v for k,v in type1_counts.items()},
    'type2_counts':{str(k):v for k,v in type2_counts.items()},
    'type1_examples':{str(k):list(v) for k,v in type1_examples.items()},
    'type2_examples':{str(k):list(v) for k,v in type2_examples.items()},
    'full_unit_lifts':lifting_receipts,
    'sha256':{p.name:sha256(p.read_bytes()).hexdigest() for p in
              [HERE/'SIGNED_LOCAL_FIELDS.tex',Path(__file__)]}}
(HERE/'SIGNED_LOCAL_FIELDS_checks.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:receipt[k] for k in ('status','group_count','entry_count','sha256')},indent=2))
