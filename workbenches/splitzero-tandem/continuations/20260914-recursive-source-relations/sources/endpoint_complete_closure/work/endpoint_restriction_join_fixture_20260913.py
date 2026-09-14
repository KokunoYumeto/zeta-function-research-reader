"""Exact independent restriction/lower-source fixture; no imported project code."""
from fractions import Fraction as F
from itertools import combinations
from math import comb, factorial
from pathlib import Path
import argparse
import datetime
import hashlib
import json
import subprocess
import sys


def zero(r, c):
    return [[F(0) for _ in range(c)] for _ in range(r)]


def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def tr(a):
    return sum((a[i][i] for i in range(len(a))), F(0))


def transpose(a):
    return [list(v) for v in zip(*a)]


def add(a, b):
    return [[x+y for x,y in zip(r,s)] for r,s in zip(a,b)]


def scale(a, t):
    return [[t*x for x in r] for r in a]


def sub(a, b):
    return add(a, scale(b, F(-1)))


def mul(a, b):
    return [[sum((x*y for x,y in zip(r,c)), F(0)) for c in zip(*b)] for r in a]


def inv(a):
    n=len(a)
    b=[list(a[i])+eye(n)[i] for i in range(n)]
    for j in range(n):
        pivot=next(i for i in range(j,n) if b[i][j])
        b[j],b[pivot]=b[pivot],b[j]
        t=b[j][j]
        b[j]=[v/t for v in b[j]]
        for i in range(n):
            if i != j:
                t=b[i][j]
                b[i]=[u-t*v for u,v in zip(b[i],b[j])]
    return [r[n:] for r in b]


def det(a):
    n=len(a)
    b=[list(r) for r in a]
    result=F(1)
    for j in range(n):
        pivots=[i for i in range(j,n) if b[i][j]]
        if not pivots:
            return F(0)
        p=pivots[0]
        if p!=j:
            result=-result
            b[j],b[p]=b[p],b[j]
        v=b[j][j]
        result*=v
        for i in range(j+1,n):
            t=b[i][j]/v
            for k in range(j+1,n):
                b[i][k]-=t*b[j][k]
    return result


def leading(a,n):
    return [r[:n] for r in a[:n]]


def diag(values):
    return [[v if i==j else F(0) for j in range(len(values))] for i,v in enumerate(values)]


def powmat(a,n):
    b=eye(len(a))
    for _ in range(n):
        b=mul(b,a)
    return b


def rising(a,n):
    ans=1
    for j in range(n):
        ans*=a+j
    return ans


def moments(alpha,mass,degree):
    coeff=[F(1)]+[F(0)]*(degree+1)
    out=[]
    for n in range(degree+1):
        out.append(mass*coeff[0])
        nxt=[F(0)]*len(coeff)
        for j,v in enumerate(coeff):
            if j+1<len(coeff):
                nxt[j+1]+=v
            if j:
                nxt[j-1]+=v*j*(j+alpha-1)
        coeff=nxt
    return out


def gram_s(moment,n):
    a=zero(n+1,n+1)
    imaginary=zero(n+1,n+1)
    for i in range(n+1):
        for j in range(n+1):
            for x in range(i+1):
                for y in range(j+1):
                    v=comb(i,x)*comb(j,y)*(-1)**x*moment[x+y]
                    parity=(x+y)%4
                    if parity in (0,2):
                        a[i][j]+=v*(1 if parity==0 else -1)
                    else:
                        imaginary[i][j]+=v*(1 if parity==1 else -1)
    return a,imaginary


def monic_coeff(alpha,n):
    ps=[[F(1)]]
    if n:
        ps.append([F(-1),F(1)])
    for j in range(1,n):
        p=[F(0)]*(j+2)
        for a,v in enumerate(ps[-1]):
            p[a]-=v
            p[a+1]+=v
        for a,v in enumerate(ps[-2]):
            p[a]+=j*(j+alpha-1)*v
        ps.append(p)
    a=zero(n+1,n+1)
    for j,p in enumerate(ps):
        for i,v in enumerate(p):
            a[i][j]=v
    return a


def remainder(n):
    a=[[F(1),F(0)],[F(0),F(1)]]
    for j in range(2,n+1):
        a.append([2*a[-1][i]+a[-2][i] for i in range(2)])
    return transpose(a[:n+1])


def logbox(x,terms=90):
    if x<=0:
        raise ValueError("positive rational logarithm required")
    if x<1:
        lo,hi=logbox(1/x,terms)
        return -hi,-lo
    e=0
    y=x
    while y>=2:
        y/=2
        e+=1
    def direct(v):
        t=(v-1)/(v+1)
        partial=2*sum((t**(2*a+1)/F(2*a+1) for a in range(terms)),F(0))
        tail=2*t**(2*terms+1)/((2*terms+1)*(1-t*t))
        return partial,partial+tail
    lo,hi=direct(y)
    l2,h2=direct(F(2))
    return lo+e*l2,hi+e*h2


def encode(v):
    if isinstance(v,F):
        return str(v)
    if isinstance(v,dict):
        return {k:encode(x) for k,x in v.items()}
    if isinstance(v,(list,tuple)):
        return [encode(x) for x in v]
    return v


def check_run(mutation):
    checks=[]
    def check(label,condition,actual=None,expected=None):
        checks.append(dict(label=label,passed=bool(condition),actual=encode(actual),expected=encode(expected)))
    def equal(label,a,b):
        check(label,a==b,a,b)
    def psd(label,a):
        equal(label+".symmetric",a,transpose(a))
        values=[]
        for r in range(1,len(a)+1):
            for inds in combinations(range(len(a)),r):
                value=det([[a[i][j] for j in inds] for i in inds])
                check(label+".minor."+"_".join(map(str,inds)),value>=0,value)
                values.append(dict(indices=inds,value=value))
        return values
    mass=F(1) if mutation=="mass_one" else F(9,16)
    lower_mass=F(1) if mutation=="comparator_mass_one" else F(27,70)
    actual_mom=moments(8,mass,8)
    low_mom=moments(4,lower_mass,8)
    raw_ref=moments(2,F(1,2),10)
    factor=[raw_ref[d]+raw_ref[d+2]/4 for d in range(9)]
    convolution=[sum((comb(d,j)*factor[j]*factor[d-j] for j in range(d+1)),F(0)) for d in range(9)]
    reference=moments(4,F(1,4),12)
    pointwise=[F(54,35)*reference[d]+F(39,280)*reference[d+2]+F(3,1120)*reference[d+4] for d in range(9)]
    equal("source.literal_mass",actual_mom[0],F(9,16))
    equal("source.factor_mass",factor[0],F(3,4))
    equal("comparator.literal_mass",low_mom[0],F(27,70))
    for d in range(9):
        equal(f"source.convolution_moment.{d}",actual_mom[d],convolution[d])
        equal(f"source.pointwise_density_moment.{d}",actual_mom[d],pointwise[d])
        equal(f"comparator.pointwise_density_moment.{d}",low_mom[d],F(54,35)*reference[d])
    h4,imag=gram_s(actual_mom,4)
    hlo4,lowimag=gram_s(low_mom,4)
    equal("source.original_S_imaginary",imag,zero(5,5))
    equal("comparator.original_S_imaginary",lowimag,zero(5,5))
    lower_difference=psd("source.lower_form_difference",sub(h4,hlo4))
    c=[[F(1),F(-1)],[F(0),F(1)]]
    ci=inv(c)
    bhat=mul(transpose(c),mul(leading(h4,2),c))
    equal("chart.quotient_determinant",det(c),F(1))
    equal("chart.remainder_source",bhat,diag([F(9,16),F(9,2)]))
    expected_k={1:diag([F(16,9),F(2,9)]),2:diag([F(244,81),F(2,9)]),3:diag([F(244,81),F(662,1215)]),4:diag([F(56102,13365),F(662,1215)])}
    expected_low={3:diag([F(133,27),F(763,486)]),4:diag([F(3619,486),F(763,486)])}
    data={}
    for n in range(1,5):
        h=leading(h4,n+1)
        hn=leading(hlo4,n+1)
        j=remainder(n)
        p=monic_coeff(8,n)
        o=diag([mass*factorial(a)*rising(8,a) for a in range(n+1)])
        b=mul(j,p)
        k=mul(j,mul(inv(h),transpose(j)))
        knu=mul(j,mul(inv(hn),transpose(j)))
        g=inv(k)
        rr=mul(inv(h),mul(transpose(j),g))
        rmon=mul(inv(o),mul(transpose(b),g))
        khat=mul(ci,mul(k,transpose(ci)))
        klnhat=mul(ci,mul(knu,transpose(ci)))
        equal(f"degree.{n}.monic_orthogonality",mul(transpose(p),mul(h,p)),o)
        equal(f"degree.{n}.monic_kernel",mul(b,mul(inv(o),transpose(b))),k)
        equal(f"degree.{n}.kernel_oracle",khat,expected_k[n])
        equal(f"degree.{n}.right_inverse",mul(j,rr),eye(2))
        equal(f"degree.{n}.least_lift_gram",mul(transpose(rr),mul(h,rr)),g)
        equal(f"degree.{n}.representative_chart",mul(p,rmon),rr)
        if n>=3:
            equal(f"degree.{n}.comparator_kernel_oracle",klnhat,expected_low[n])
        for a in range(1,n+2):
            check(f"degree.{n}.source_leading_minor.{a}",det(leading(h,a))>0,det(leading(h,a)))
            check(f"degree.{n}.comparator_leading_minor.{a}",det(leading(hn,a))>0,det(leading(hn,a)))
        data[n]=dict(H=h,Hnu=hn,J=j,P=p,O=o,B=b,K=k,Knu=knu,G=g,R=rr,Rmon=rmon,Khat=khat,Knu_hat=klnhat,V=det(g))
    pairs=[]
    eigenvalues={(1,3):[F(36,61),F(135,331)],(2,4):[F(20130,28051),F(135,331)]}
    summed_loss=F(1)
    cert_totals={"comparator":[F(0),F(0)],"sharp":[F(0),F(0)]}
    direct_total=F(0)
    for i,jj in [(1,3),(2,4)]:
        a,b=data[i],data[jj]
        prefix=f"pair.{i}_{jj}"
        ki,gj=a["K"],b["G"]
        t=mul(b["K"],a["G"]) if mutation=="restriction_inverse" else mul(ki,gj)
        h=sub(eye(2),t)
        li=zero(jj+1,i+1)
        for z in range(i+1):
            li[z][z]=F(1)
        kept=diag([F(z<=i) for z in range(jj+1)])
        projection=kept if mutation=="projection_truncate" else mul(b["P"],mul(kept,inv(b["P"])))
        lower=mul(li,a["R"])
        old=mul(projection,b["R"])
        difference=sub(lower,b["R"])
        that=mul(ci,mul(t,c))
        equal(prefix+".spectrum_matrix",that,diag(eigenvalues[(i,jj)]))
        equal(prefix+".metric_adjoint",mul(a["G"],t),gj)
        equal(prefix+".source_restriction",mul(lower,t),old)
        equal(prefix+".projection_idempotent",mul(projection,projection),projection)
        equal(prefix+".projection_H_adjoint",mul(transpose(projection),b["H"]),mul(b["H"],projection))
        equal(prefix+".restriction_gram",mul(transpose(old),mul(b["H"],old)),mul(gj,mul(ki,gj)))
        equal(prefix+".relation_remainder",mul(b["J"],difference),zero(2,2))
        equal(prefix+".relation_gram",mul(transpose(difference),mul(b["H"],difference)),sub(a["G"],gj))
        equal(prefix+".relation_decomposition",difference,sub(mul(lower,h),sub(b["R"],old)))
        ratio=a["V"]/b["V"]
        equal(prefix+".determinant_volume",det(t),1/ratio)
        eigen=eigenvalues[(i,jj)]
        equal(prefix+".determinant_spectral",det(t),eigen[0]*eigen[1])
        action=[[F(0),F(1)],[F(1),F(2)]]
        ai=add(mul(transpose(action),a["G"]),mul(a["G"],action))
        aj=add(mul(transpose(action),gj),mul(gj,action))
        wi=sub(ai,scale(a["G"],F(2)))
        wj=sub(aj,scale(gj,F(2)))
        defects=sub(mul(mul(ki,wi),t),mul(t,mul(b["K"],wj)))
        equal(prefix+".action_commutator",sub(mul(action,t),mul(t,action)),defects)
        spectrum_products=mul(bhat,b["Knu_hat"])
        equal(prefix+".comparator_product_diagonal",spectrum_products,diag([spectrum_products[0][0],spectrum_products[1][1]]))
        products=[spectrum_products[z][z] for z in range(2)]
        cap=min(products) if mutation=="gap_use_smaller" else max(products)
        equal(prefix+".remainder_operator_squared_norm",cap,F(763,108))
        gap=1/cap
        equal(prefix+".comparator_gap_oracle",gap,F(108,763))
        remainder_gap_matrix=sub(scale(b["Hnu"],cap),mul(transpose(b["J"]),mul(leading(h4,2),b["J"])))
        remainder_certificate=psd(prefix+".remainder_norm_certificate",remainder_gap_matrix)
        quotient_certificate=psd(prefix+".comparison_quotient_certificate",sub(ki,scale(b["K"],gap)))
        sharp=min(eigen)
        sharp_certificate=psd(prefix+".sharp_gap_certificate",sub(ki,scale(b["K"],sharp)))
        y=mul(transpose(b["J"]),mul(leading(h4,2),[[F(-1)],[F(1)]]))
        witness=mul(inv(b["Hnu"]),y)
        witness_rem=mul(b["J"],witness)
        numerator=mul(transpose(witness_rem),mul(leading(h4,2),witness_rem))[0][0]
        denominator=mul(transpose(witness),mul(b["Hnu"],witness))[0][0]
        equal(prefix+".remainder_extremizer",numerator/denominator,cap)
        check(prefix+".remainder_extremizer_nonzero",denominator>0,denominator)
        trace_values=[]
        for power in range(1,7):
            actual=tr(h)**power if mutation=="trace_square" and power>=2 else tr(powmat(h,power))
            expected=sum(((1-g)**power for g in eigen),F(0))
            equal(prefix+f".trace_power.{power}",actual,expected)
            trace_values.append(actual)
        loss=logbox(ratio)
        check(prefix+".log_positive",loss[0]>0,loss)
        check(prefix+".log_width",loss[1]-loss[0]<F(1,10**70),loss[1]-loss[0])
        direct=tr(sub(mul(a["G"],b["K"]),eye(2)))
        direct_total+=direct
        certificates=[]
        for label,g0 in [("comparator",gap),("sharp",sharp)]:
            r=1-g0
            lglo,lghi=logbox(1/g0)
            for power in [1,2,3,5]:
                lower=sum((trace_values[v-1]/v for v in range(1,power+1)),F(0))
                rpartial=sum((r**v/v for v in range(1,power+1)),F(0))
                exponent=power if mutation=="tail_exponent" else power+1
                clo=(lglo-rpartial)/r**exponent
                chi=(lghi-rpartial)/r**exponent
                exact_clo=(lglo-rpartial)/r**(power+1)
                exact_chi=(lghi-rpartial)/r**(power+1)
                equal(prefix+f".{label}.p{power}.tail_coefficient",(clo,chi),(exact_clo,exact_chi))
                upperlo=lower+clo*trace_values[power]
                upperhi=lower+chi*trace_values[power]
                check(prefix+f".{label}.p{power}.lower_certificate",lower<=loss[0],lower,loss)
                check(prefix+f".{label}.p{power}.upper_certificate",loss[1]<=upperlo,upperlo,loss)
                check(prefix+f".{label}.p{power}.upper_width",upperhi-upperlo<F(1,10**65),upperhi-upperlo)
                certificates.append(dict(gap_type=label,p=power,gap=g0,lower=lower,upper=(upperlo,upperhi),excess=(upperlo-loss[1],upperhi-loss[0]),tail_coefficient=(clo,chi)))
                if power==2:
                    cert_totals[label][0]+=upperlo
                    cert_totals[label][1]+=upperhi
        summed_loss*=ratio
        pairs.append(dict(i=i,j=jj,T=t,H_loss=h,spectrum=eigen,projection=projection,lower_representative=lower,restricted_representative=old,relation_difference=difference,ratio=ratio,loss=loss,trace_powers=trace_values,comparator_products=products,C=cap,gap=gap,sharp_gap=sharp,remainder_matrix=remainder_gap_matrix,remainder_certificate=remainder_certificate,quotient_certificate=quotient_certificate,sharp_certificate=sharp_certificate,extremizer=witness,extremizer_norm=denominator,extremizer_remainder_norm=numerator,certificates=certificates,direct_trace_bound=direct))
    equal("pair.composition.1_2_4",mul(mul(data[1]["K"],data[2]["G"]),mul(data[2]["K"],data[4]["G"])),mul(data[1]["K"],data[4]["G"]))
    equal("endpoint.four_volume_ratio",summed_loss,F(3073295611,216513000))
    total_loss=logbox(summed_loss)
    check("endpoint.sharp_trace_improves_direct",cert_totals["sharp"][1]<direct_total,cert_totals["sharp"],direct_total)
    check("endpoint.comparator_trace_improves_direct",cert_totals["comparator"][1]<direct_total,cert_totals["comparator"],direct_total)
    check("endpoint.sharp_improves_comparator",cert_totals["sharp"][1]<cert_totals["comparator"][0],cert_totals["sharp"],cert_totals["comparator"])
    failed=[c["label"] for c in checks if not c["passed"]]
    labels=[c["label"] for c in checks]
    result=dict(mutation=mutation,mathematical_check_count=len(checks),unique_labels=len(set(labels))==len(labels),failed_count=len(failed),failed_labels=failed,source_mass=mass,comparator_mass=lower_mass,source_moments=actual_mom,lower_moments=low_mom,original_H4=h4,original_Hnu4=hlo4,source_lower_difference_minors=lower_difference,quotient_basis_matrix=c,degree_data=data,pairs=pairs,total_ratio=summed_loss,total_loss=total_loss,p2_totals=cert_totals,direct_total=direct_total,checks=checks)
    return encode(result)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def replay():
    script=Path(__file__).resolve()
    mutations=["none","mass_one","comparator_mass_one","restriction_inverse","projection_truncate","gap_use_smaller","trace_square","tail_exponent"]
    jobs=[]
    for opt in (False,True):
        for mutation in mutations:
            command=[sys.executable]+(["-O"] if opt else [])+[str(script),"--run","--mutation",mutation]
            start=datetime.datetime.now(datetime.timezone.utc).isoformat()
            proc=subprocess.run(command,capture_output=True)
            end=datetime.datetime.now(datetime.timezone.utc).isoformat()
            result=json.loads(proc.stdout)
            jobs.append(dict(command=command,optimized=opt,mutation=mutation,started_utc=start,finished_utc=end,returncode=proc.returncode,stdout_sha256=sha(proc.stdout),stderr_sha256=sha(proc.stderr),stdout=proc.stdout.decode("utf-8"),stderr=proc.stderr.decode("utf-8"),result=result))
    count=jobs[0]["result"]["mathematical_check_count"]
    checks=[]
    def check(label,cond):
        checks.append(dict(label=label,passed=bool(cond)))
    for job in jobs:
        prefix=("optimized" if job["optimized"] else "ordinary")+"."+job["mutation"]
        r=job["result"]
        check(prefix+".complete_count",r["mathematical_check_count"]==count)
        check(prefix+".unique_labels",r["unique_labels"])
        good=job["mutation"]=="none"
        check(prefix+".expected_mathematical_outcome",r["failed_count"]==0 if good else r["failed_count"]>0)
        check(prefix+".exit_matches_mathematical_outcome",job["returncode"]==(0 if good else 1))
        check(prefix+".stderr_empty",job["stderr"]=="")
    for a,b in zip(jobs[:8],jobs[8:]):
        check(a["mutation"]+".mode_equality",a["result"]==b["result"])
    receipt=dict(script=script.name,script_sha256=sha(script.read_bytes()),python=sys.executable,distinct_mathematical_checks=count,actual_job_count=len(jobs),receipt_checks=checks,receipt_passed=all(c["passed"] for c in checks),jobs=jobs)
    out=script.with_suffix(".json")
    out.write_text(json.dumps(receipt,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(dict(receipt=str(out),sha256=sha(out.read_bytes()),passed=receipt["receipt_passed"],checks=count,jobs=[dict(mutation=j["mutation"],optimized=j["optimized"],failed=j["result"]["failed_count"],returncode=j["returncode"]) for j in jobs]),indent=2))
    return 0 if receipt["receipt_passed"] else 1


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--run",action="store_true")
    parser.add_argument("--mutation",default="none")
    args=parser.parse_args()
    if args.run:
        result=check_run(args.mutation)
        print(json.dumps(result,indent=2))
        raise SystemExit(0 if result["failed_count"]==0 else 1)
    raise SystemExit(replay())
