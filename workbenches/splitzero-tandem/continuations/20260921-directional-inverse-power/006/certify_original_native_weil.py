"""Certified generalized eigenvalues of the original Fable target Weil receiver.

Complete xi is evaluated by Arb formal series, as proved in MP9--15/WP24--25.
The target Gamma Gram is evaluated independently from the full original
moments RW7--11/NH2--9. No zero tail, Gram correlation or total mass is omitted.
Every interval endpoint is certified by the inertia of T-lambda H using
strict real-ball signs of all four leading principal minors.
"""
from pathlib import Path
from fractions import Fraction
import hashlib,json
import flint
from flint import arb,acb,acb_mat,acb_series,ctx
B=Path(__file__).resolve().parent
ctx.prec=768;ctx.cap=8;ctx.threads=1

def realq(q):
    q=Fraction(q)
    return arb(q.numerator)/q.denominator

def inner_matrix(tau):
    # s=1 is an original permitted Gamma parameter; M is not divided out.
    h=arb(3);d=arb(3)/2;b=arb(1)/2;M=(2*arb.pi()).sqrt()
    mom=[M,arb(0),M*b,arb(0),M*(3*b*b+2*b),arb(0),M*(15*b**3+30*b*b+16*b)]
    K=acb_mat([[mom[j+k] for k in range(4)] for j in range(4)])
    Q=acb_mat(4,4)
    from math import comb
    for j in range(4):
        for k in range(4):
            val=acb(0)
            for r in range(j+1):
                q=k-r
                if 0<=q<=3-j:
                    val+=comb(j,r)*acb(d,-tau)**(j-r)*acb(0,1)**r*comb(3-j,q)*acb(d,tau)**(3-j-q)*acb(0,-1)**q
            Q[k,j]=val
    Qh=acb_mat([[Q[j,i].conjugate() for j in range(4)] for i in range(4)])
    H=(Qh*K*Q)*acb(h)
    expected=12*h**16*M**4*b**3*(b+1)**2*(b+2)
    err=H.det()-expected
    assert err.contains(0)
    return H,expected

def weil_matrix(tau):
    omega=acb(2,tau);z=acb_series([0,1])
    s=(omega+(1-omega.conjugate())*z)/(1+z)
    xi=s*(s-1)/2*(-s/2*arb.pi().log()).exp()*(s/2).gamma()*s.zeta()
    L=xi.derivative()/xi/s.derivative()
    cs=[acb(2*L[0].real)]+[L[j] for j in range(1,4)]
    return acb_mat([[cs[j-i] if j>=i else cs[i-j].conjugate() for j in range(4)] for i in range(4)]),cs

def inertia(T,H,x,keep=False):
    A=T-H*acb(realq(x))
    signs=[1];dets=[]
    for n in range(1,5):
        det=acb_mat([[A[i,j] for j in range(n)] for i in range(n)]).det()
        assert det.imag.contains(0),'Exact Hermitian determinant lost'
        sign=1 if det.real>0 else -1 if det.real<0 else 0
        if not sign:return None
        signs.append(sign);dets.append(str(det))
    negatives=sum(signs[j]!=signs[j-1] for j in range(1,5))
    return (negatives,signs,dets) if keep else negatives

rows=[]
for tau in [0,14,21,100,1000]:
    H,hdet=inner_matrix(tau);T,cs=weil_matrix(tau)
    assert inertia(T,H,0)==0
    high=Fraction(1)
    while inertia(T,H,high)!=4:high*=2
    intervals=[]
    for index in range(1,5):
        lo=Fraction(0);hi=high
        for iteration in range(500):
            mid=(lo+hi)/2;count=inertia(T,H,mid)
            if count is None:
                mid=(2*lo+hi)/3;count=inertia(T,H,mid)
            assert count is not None,'Need higher precision, never infer a sign'
            if count>=index:hi=mid
            else:lo=mid
            if lo>0 and hi-lo<lo/Fraction(10**60):break
        else:raise ArithmeticError('No certified narrow interval')
        lower=inertia(T,H,lo,True);upper=inertia(T,H,hi,True)
        assert lower[0]==index-1 and upper[0]==index
        lam_box=realq((lo+hi)/2)+arb(0,realq((hi-lo)/2))
        A_box=T-H*acb(lam_box)
        cofactor=None
        for column in range(4):
            other=[j for j in range(4) if j!=column]
            principal=acb_mat([[A_box[i,j] for j in other] for i in other]).det()
            if not principal.real.contains(0):
                cofactor={'column_zero_based':column,'principal_cofactor_ball':str(principal),
                  'exact_eigenvector':'adj(T-lambda H) e_'+str(column)}
                break
        assert cofactor is not None,'Refine the eigenvalue box before asserting an eigenvector'
        intervals.append({'index_increasing':index,
          'lower_exact':str(lo),'upper_exact':str(hi),
          'decimal_enclosure':[str(realq(lo).lower()),str(realq(hi).upper())],
          'lower_inertia':lower[0],'upper_inertia':upper[0],
          'lower_leading_minor_signs':lower[1],'upper_leading_minor_signs':upper[1],
          'lower_leading_minor_balls':lower[2],'upper_leading_minor_balls':upper[2],
          'nonzero_eigenvector_certificate':cofactor})
    assert all(Fraction(intervals[j]['upper_exact'])<Fraction(intervals[j+1]['lower_exact']) for j in range(3))
    rows.append({'pole_real':2,'pole_imag':tau,'original_gamma_s':1,
       'coefficients_full_weil':[str(c) for c in cs],
       'native_Gram_entries':[[str(H[i,j]) for j in range(4)] for i in range(4)],
       'native_determinant':str(hdet),'eigenvalue_intervals':intervals,
       'full_signed_state_spectrum':'Four zero eigenvalues plus these four certified positive generalized eigenvalues.'})
    print('tau',tau,'native increasing:',[(float(Fraction(x['lower_exact'])),float(Fraction(x['upper_exact']))) for x in intervals])
report={'result_id':'SZ-20260920-033',
 'library':'python-flint '+flint.__version__,'precision_bits':ctx.prec,'series_cap':ctx.cap,'threads':ctx.threads,
 'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'mathematical_definitions':'RW12–20, NH1–24; source of exact full-Weil coefficient identity MP9–15 and WP24–25.',
 'original_metric':'Original target s=1 Gamma measure, M=sqrt(2*pi), c* retained through Sprime=z+c*−1/2. All sixteen entries are retained.',
 'rigorous_method':'Hermitian generalized pencil T-lambda H. H is positive definite by its positive-density integral. Leading-minor signs give exact LDL inertia at rational endpoints. Each endpoint pair has inertia difference one and encloses exactly one eigenvalue; no approximate eigensolver certifies a sign.',
 'source_metric':'These numbers are target-native only. Actual source metric depends on original conductor moments and is given explicitly in NH26–42 and the native-coercivity proof; no sample conductor moments are invented.',
 'zero_sum':'Complete xi values/series: no zero-list, prime, Gamma or zero-tail truncation.',
 'rows':rows,'all_endpoint_comparisons_passed':True}
(B/'ORIGINAL_NATIVE_WEIL_CERTIFICATES.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
