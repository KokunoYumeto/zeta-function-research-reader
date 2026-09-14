"""Exact original q=36 Gamma joint-Schur calibration; no asserted zeta zero."""
from pathlib import Path
from flint import fmpq as Q, fmpq_poly as Poly, fmpq_mat as Mat
import json,hashlib,sys,time,datetime,math
sys.set_int_max_str_digits(0)
OUT=Path(__file__).parent
START=time.perf_counter()
def say(s):print(f'{time.perf_counter()-START:.3f}s {s}',flush=True)
def require(ok,what):
    if not ok:raise ArithmeticError(what)
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def qstr(a):return str(a)
def mat_col(a):return Mat([[t] for t in a])
def bits(a):return {'numerator_bits':abs(int(a.numerator)).bit_length(),'denominator_bits':int(a.denominator).bit_length()}
def dump(name,obj):
    target=OUT/name;tmp=target.with_suffix(target.suffix+'.tmp')
    tmp.write_text(json.dumps(obj,indent=2),encoding='utf-8');tmp.replace(target)
def rising(a,n):
    r=Q(1)
    for j in range(n):r*=a+j
    return r
N_LIST=[35,36,71,72]; EPS=[1,1,-1,-1]
k,l,m,q=5,1,1,36
delta2=Q(1,16);gamma2=Q(9);alpha=Q(1,2)
x=Poly([0,1]);chi=Poly([1])
for a in [1,3,5]:
    for b in [1,3,5]:
        chi*= (x*x+a*a*delta2+b*b*gamma2)**2-4*a*a*delta2*x*x
require(chi.degree()==q and chi[q]==1,'complete degree36 packet')
require(all(chi[j]==0 for j in range(1,q,2)),'original packet evenness')
require(chi(alpha)!=0,'original boundary node coprime')
p=[Poly([1]),x];norm=[Q(1),Q(1,2)]
for n in range(1,74):
    p.append(x*p[-1]+Q(n)*Q(2*n-1,2)*p[-2])
    norm.append(norm[-1]*Q(n+1)*Q(2*(n+1)-1,2))
require(len(p)==75 and len(norm)==75,'degrees0through74')
values=[];rem=[]
for n in range(75):
    values.append(p[n](alpha));rp=p[n]%chi
    rem.append([rp[j] for j in range(q)])
    require(values[n]==rising(alpha,n),'exact p_n(1/2)')
    require(norm[n]==Q(math.factorial(n))*rising(alpha,n),'complete original monic norm factor')
say('Original packet, monic recurrence, remainder vectors and real-node values complete')

K=Mat(q,q);C=Mat(q,1);A=Q(0)
snap={};needed=set(N_LIST+[n+1 for n in N_LIST])
for n in range(74):
    vv=mat_col(rem[n]);K+=vv*vv.transpose()/norm[n]
    C+=vv*(values[n]/norm[n]);A+=values[n]**2/norm[n]
    require(A==rising(alpha,n+1)/(alpha*Q(math.factorial(n))),f'freeA product at {n}')
    if n in needed:snap[n]=(Mat(K),Mat(C),A)
say('All original finite covariances through degree73 formed; all74 freeA formulas exact')

results={};signed=Q(1)
for N,ep in zip(N_LIST,EPS):
    Kn,Cn,An=snap[N];Km,Cm,Am=snap[N+1];vn=mat_col(rem[N+1])
    X=(vn.transpose()*Kn.solve(vn))[0,0]/norm[N+1]
    Y=(Cm.transpose()*Km.solve(Cm))[0,0]/Am
    gap=1-Y;factor=(1+X)*gap
    require(X>=0,f'X positive at {N}')
    require(Y>=0 and gap>0,f'conditional Schur positive at {N}')
    # Rank-one determinant update is independently checked in exact arithmetic.
    detK=Kn.det();detKm=Km.det()
    require(detK>0 and detKm>0,f'positive determinant at {N}')
    require(detKm/detK==1+X,f'fullq36 determinant lemma at {N}')
    # The first joint endpoint has an exactly one-dimensional relation.
    if N==q-1:
        require(factor==chi(alpha)**2/(norm[q]*Am),'first endpoint resultant/freeA identity')
    signed*=factor**ep
    row={'N':N,'M':N+1,'epsilon':ep,'X':qstr(X),'Y':qstr(Y),'one_minus_Y':qstr(gap),'Ahat_M':qstr(Am),'conditional_Lhat_M':qstr(Am*gap),'factor':qstr(factor),'factor_bits':bits(factor),'full_q_determinant_update_verified':True,'positive_schur_verified':True}
    results[str(N)]=row
    dump('ENDPOINTS_PARTIAL.json',{'parameters':{'k':5,'l':1,'m':1,'q':36,'delta_squared':'1/16','gamma_squared':'9','center':'5/2','centered_boundary':'1/2'},'completed':results})
    say(f'Endpoint N={N}: exact X/Y, positivity and36x36 determinant update passed')

# Independent GSR3 relation Grams in the original chi*x^j columns. Translation
# from chi*S^j to chi*x^j is upper triangular with determinant one.
def coeff_in_p(f):
    work=Poly(f);v=[Q(0)]*75
    while work:
        n=work.degree();a=work[n];v[n]=a;work-=a*p[n]
    return v
rel=[coeff_in_p(chi*x**j) for j in range(37)]
frel=[coeff_in_p((x-alpha)*chi*x**j) for j in range(37)]
def gram(vectors):
    B=Mat(75,len(vectors),[vectors[j][i] for i in range(75) for j in range(len(vectors))])
    weighted=Mat([[norm[i]*B[i,j] for j in range(B.ncols())] for i in range(75)])
    return B.transpose()*weighted
GR=gram(rel);GFR=gram(frel)
require(all(GR[i,j]==0 and GFR[i,j]==0 for i in range(37) for j in range(37) if (i+j)%2),'original parity Gram blocks')
def parity_det(G,r):
    ans=Q(1)
    for parity in [0,1]:
        ind=list(range(parity,r,2))
        if ind:
            piece=Mat([[G[i,j] for j in ind] for i in ind]).det()
            require(piece>0,'positive complete relation parity determinant');ans*=piece
    return ans
gsr_signed=Q(1);gsr={}
for N,ep in zip(N_LIST,EPS):
    r=N+1-q;R=parity_det(GFR,r)/parity_det(GR,r)
    D=Q(1)
    for n in range(N+1):D*=(Q(n)+alpha)*(Q(n)+alpha+1)
    gsr_signed*=(D/R)**ep
    gsr[str(N)]={'relation_rank':r,'R_N':qstr(R),'D_1N':qstr(D),'quotient_determinant_ratio_f_over_sigma':qstr(D/R)}
    # At each endpoint the fixed multiplication determinant must agree.
    fdet=chi(alpha) # even q makes det M_(x-alpha)=chi(alpha)
    factor=Q(results[str(N)]['factor'])
    require((D/R)*factor==fdet**2,f'endpoint Schur-to-GSR identity at {N}')
    say(f'Independent GSR original relation Gram at N={N}, rank={r}, matches Schur exactly')
require(signed*gsr_signed==1,'allfour signed returns are exact reciprocals')

# Evaluate the actual full source f-Gram determinant with its exact parity
# tridiagonal recurrence as a second check on GSR's explicit D_1N factor.
for N in N_LIST:
    detf=Q(1)
    for parity in [0,1]:
        inds=list(range(parity,N+1,2));prevprev=Q(1);prev=None
        for index,n in enumerate(inds):
            an=Q(n)*Q(2*n-1,2)
            diag=norm[n+1]+alpha**2*norm[n]+(an**2*norm[n-1] if n else 0)
            val=diag if index==0 else diag*prev-norm[n]**2*prevprev
            require(val>0,'positive source parity leading determinant')
            prevprev,prev=(Q(1),val) if index==0 else (prev,val)
        if inds:detf*=prev
    detsig=Q(1)
    for n in range(N+1):detsig*=norm[n]
    require(detf/detsig==Q(gsr[str(N)]['D_1N']),f'fullsource factor at {N}')
say('Independent full source parity determinants confirm every D_1N')

# Rigorous fast logarithm enclosure. Binary argument reduction keeps the
# atanh series ratio <= 1/3 even when the Schur gap is very small.
def log_at_small_ratio(s,terms=96):
    t=(s-1)/(s+1);require(0<=t<=Q(1,3),'atanh range')
    power=t;total=Q(0)
    for j in range(terms):total+=2*power/Q(2*j+1);power*=t*t
    error=2*power/(Q(2*terms+1)*(1-t*t))
    return total,total+error
LOG2=log_at_small_ratio(Q(2))
def log_bounds(r,P=128):
    require(r>0,'positive log argument')
    n=int(r.numerator);den=int(r.denominator);ex=n.bit_length()-den.bit_length()
    scaled=r/(Q(2)**ex)
    if scaled<1:ex-=1;scaled*=2
    elif scaled>=2:ex+=1;scaled/=2
    require(1<=scaled<2,'binary argument reduction')
    dyadic=Q(2)**P;floor=int((scaled*dyadic).floor())
    lo=Q(floor)/dyadic;hi=Q(floor+1)/dyadic
    require(1<=lo<=scaled<=hi<=2,'outward dyadic bounds')
    lower,_=log_at_small_ratio(lo);_,upper=log_at_small_ratio(hi)
    if ex>=0:lower+=ex*LOG2[0];upper+=ex*LOG2[1]
    else:lower+=ex*LOG2[1];upper+=ex*LOG2[0]
    require(lower<=upper,'ordered log enclosure')
    return {'lower':qstr(lower),'upper':qstr(upper),'width':qstr(upper-lower),'binary_exponent':ex,'dyadic_bits':P,'atanh_terms':96,'decimal_midpoint_for_display':str(float((lower+upper)/2))}
logdata={'signed_schur_return_log':log_bounds(signed),'free_boundary_log':log_bounds((snap[72][2]*snap[73][2])/(snap[36][2]*snap[37][2])),'endpoints':{}}
for N in N_LIST:
    row=results[str(N)]
    logdata['endpoints'][str(N)]={'log_one_plus_X':log_bounds(1+Q(row['X'])),'log_one_minus_Y':log_bounds(Q(row['one_minus_Y'])),'log_factor':log_bounds(Q(row['factor']))}
elapsed=time.perf_counter()-START
result={'scope':'Exact parameter calibration only; delta=1/4 and gamma=3 are not asserted to be zero coordinates. All original degree36 packet factors and source masses are retained through explicit paired cancellation.','parameters':{'k':k,'l':l,'m':m,'q':q,'delta_squared':qstr(delta2),'gamma_squared':qstr(gamma2),'center':'5/2','centered_boundary':qstr(alpha),'cutoffs':N_LIST,'signs':EPS},'chi_centered_coefficients':[qstr(c) for c in chi.coeffs()],'endpoints':results,'signed_schur_product':qstr(signed),'GSR':gsr,'GSR_signed_product':qstr(gsr_signed),'reciprocal_identity_verified':True,'log_bounds':logdata,'mass_identity':'K=c_sigma^-1 Khat, C=c_sigma^-1 Chat, A=c_sigma^-1 Ahat, omega=c_sigma*d. Therefore X=(c_sigma*d)^-1 v*(c_sigma*Khat^-1)v and Y=(c_sigma^-1*Ahat)^-1(c_sigma^-1*Chat*) (c_sigma*Khat^-1)(c_sigma^-1*Chat). Both exact scalar cancellations give the saved rationals.','positive_schur_reason':'The first36 monic remainder vectors form an invertible unit-triangular matrix; positive d_n make each Khat positive definite. The exact saved scalar gap1-Y is strictly positive at allfour endpoints, proving both joint Schur complements positive.','elapsed_seconds':elapsed,'completed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_files':{'NOTE.tex':digest(OUT.parent/'Tau_Gamma_Joint_Schur_Return'/'NOTE.tex'),'signed_gamma_complete.tex':digest(Path('C:/Users/Floris/Documents/math/work/rh_counterfactual_20260913/total_object/tensor_order_control_20260914/gamma_signed_next/signed_gamma_complete.tex'))},'script_sha256':digest(Path(__file__))}
dump('EXACT_CALIBRATION.json',result)
dump('COMPLETION_RECEIPT.json',{'status':'complete','elapsed_seconds':elapsed,'exact_calibration_sha256':digest(OUT/'EXACT_CALIBRATION.json'),'script_sha256':digest(Path(__file__)),'allfour_endpoints':[35,36,71,72],'fullq36_determinant_checks':4,'all74_free_A_products_verified':True,'independent_relation_gram_returns':4,'independent_source_gram_products':4,'log_method':'96-term exact atanh enclosure after128-bit outward dyadic binary argument reduction; all rational endpoints saved','signed_return_midpoint':logdata['signed_schur_return_log']['decimal_midpoint_for_display']})
say('COMPLETE '+json.dumps({'elapsed_seconds':elapsed,'signed_return':logdata['signed_schur_return_log']['decimal_midpoint_for_display'],'result_sha256':digest(OUT/'EXACT_CALIBRATION.json')}))
