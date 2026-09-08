"""Exact original-source braid checks; standard library only, no source shelf.

Inputs are the complete retained generator JSON and honest-basis JSON.
Default paths are relative to this file. They may be supplied explicitly
with --generator-file and --basis-file; their frozen hashes are checked.
This computes original sparse Laurent vectors, not a substitute L_m model.
"""
from __future__ import annotations
from collections import Counter
from fractions import Fraction
from math import comb
from pathlib import Path
import argparse, hashlib, json, time

HERE=Path(__file__).resolve().parent
GEN_SHA="e26086722e2910dc9ffff7d57314a25e80b79bb00bfb1808a42bf97761377253"
BASIS_SHA="77233bf1fb129fd3dd7077987f1ae2ea62619aaff1ff178432a342fa2f15b767"
COUNTS=Counter()

def check(category, assertion, detail=None):
    if not assertion:
        raise AssertionError((category,detail))
    COUNTS[category]+=1

def add(a,b,scale=1):
    out=dict(a)
    for k,v in b.items():
        out[k]=out.get(k,0)+scale*v
        if not out[k]:
            del out[k]
    return out

def mul(a,b):
    out={}
    for k,v in a.items():
        for j,w in b.items():
            out[k+j]=out.get(k+j,0)+v*w
    return {k:v for k,v in out.items() if v}

def shift(a,degree):
    return {k+degree:v for k,v in a.items()}

def scale(a,value):
    return {k:v*value for k,v in a.items() if v*value}

def power(a,n):
    out={0:1}
    for _ in range(n):
        out=mul(out,a)
    return out

def qi(n):
    return {n-1-2*j:1 for j in range(n)}

def factorial(n):
    out={0:1}
    for k in range(1,n+1):
        out=mul(out,qi(k))
    return out

def divide_exact(a,b):
    if not a:
        return {}
    low_a,low_b=min(a),min(b)
    rem=shift(a,-low_a)
    den=shift(b,-low_b)
    quotient={}
    top=max(den)
    while rem and max(rem)>=top:
        delta=max(rem)-top
        lead=Fraction(rem[max(rem)],den[top])
        if lead.denominator==1:
            lead=lead.numerator
        quotient[delta]=lead
        rem=add(rem,shift(den,delta),-lead)
    if rem:
        raise AssertionError(("nonexact_Laurent_division",a,b,rem))
    return shift(quotient,low_a-low_b)

def gaussian(n,k):
    return divide_exact(factorial(n),mul(factorial(k),factorial(n-k)))

def vector_add(a,b):
    out={i:dict(c) for i,c in a.items()}
    for i,c in b.items():
        out[i]=add(out.get(i,{}),c)
        if not out[i]:
            del out[i]
    return out

def vector_scale(v,c):
    return {i:mul(c,a) for i,a in v.items() if mul(c,a)}

def vector_divide(v,c):
    return {i:divide_exact(a,c) for i,a in v.items()}

def matrix_apply(matrix,vec):
    result={}
    for source,value in vec.items():
        for target,coefficient in matrix[source].items():
            result[target]=add(result.get(target,{}),mul(value,coefficient))
            if not result[target]:
                del result[target]
    return result

def tensor(x,y):
    return {(i,j):mul(a,b) for i,a in x.items() for j,b in y.items() if mul(a,b)}

def tensor_slot(matrix,vec,slot):
    result={}
    for pair,value in vec.items():
        for target,coefficient in matrix[pair[slot]].items():
            output=list(pair)
            output[slot]=target
            output=tuple(output)
            result[output]=add(result.get(output,{}),mul(value,coefficient))
            if not result[output]:
                del result[output]
    return result

def flip(vec):
    return {(j,i):dict(c) for (i,j),c in vec.items()}

def serial(poly):
    return [[k,int(v) if Fraction(v).denominator==1 else str(v)] for k,v in sorted(poly.items())]

def generalized_binomial(n,k):
    out=Fraction(1)
    for j in range(k):
        out*=Fraction(n-j,j+1)
    assert out.denominator==1
    return out.numerator

def jets(poly,n):
    return [sum(c*generalized_binomial(k,j) for k,c in poly.items()) for j in range(n)]

def main():
    start=time.monotonic()
    parser=argparse.ArgumentParser(description=__doc__)
    sibling=HERE.parent/"full_source_generators"
    parser.add_argument("--generator-file",type=Path,default=sibling/"full_generators.json")
    parser.add_argument("--basis-file",type=Path,default=sibling/"source_basis/basis_1260.json")
    args=parser.parse_args()
    blobs=[args.generator_file.read_bytes(),args.basis_file.read_bytes()]
    check("frozen_inputs",hashlib.sha256(blobs[0]).hexdigest()==GEN_SHA,"generator SHA")
    check("frozen_inputs",hashlib.sha256(blobs[1]).hexdigest()==BASIS_SHA,"basis SHA")
    raw=json.loads(blobs[0])
    entries=json.loads(blobs[1])["basis"]
    check("source_dimensions",len(entries)==1260)
    check("source_dimensions",set(raw["matrices"])=={"FV","EV","FW","EW"})
    mats={name:[{row:dict(coefficient) for row,coefficient in column} for column in columns]
          for name,columns in raw["matrices"].items()}
    weights=[tuple(b["weight_V"]+b["weight_W"]) for b in entries]
    for i,b in enumerate(entries):
        check("original_basis_labels",b["index"]==i)
        check("central_degrees",sum(weights[i][:2])==sum(weights[i][2:])==15)
        content=Counter("".join(b["columns"]))
        expected=(content["1"]+content["2"],content["3"]+content["4"],
                  content["1"]+content["3"],content["2"]+content["4"])
        check("original_column_weights",weights[i]==expected)
    for name,mat in mats.items():
        check("source_dimensions",len(mat)==1260)
        delta={"FV":(-1,1,0,0),"EV":(1,-1,0,0),
               "FW":(0,0,-1,1),"EW":(0,0,1,-1)}[name]
        for source,column in enumerate(mat):
            for target,c in column.items():
                check("full_generator_edge_weights",
                      weights[target]==tuple(x+y for x,y in zip(weights[source],delta)),
                      (name,source,target))
                check("integral_source_coefficients",
                      bool(c) and all(type(k) is int and type(v) is int and v for k,v in c.items()))
    T,Q=126,144
    check("retained_original_labels",entries[T]["columns"]==["123","123","124","12","12","1","1"])
    check("retained_original_labels",entries[T]["sign"]==1 and entries[T]["p_power"]==0)
    check("retained_original_labels",entries[Q]["columns"]==["123","123","124","12","13","4","1"])
    check("retained_original_labels",entries[Q]["sign"]==-1 and entries[Q]["p_power"]==-1)
    check("retained_original_labels",weights[T]==(12,3,9,6) and weights[Q]==(10,5,9,6))
    tvec={T:{0:1}}
    check("actual_highest_actions",matrix_apply(mats["EV"],tvec)=={})
    check("actual_highest_actions",matrix_apply(mats["EW"],tvec)=={})
    full_first=mats["FV"][T]
    full_second=matrix_apply(mats["FV"],full_first)
    expected_square={11:1,9:1,5:-1,3:-1,-3:-1,-5:-1,-9:1,-11:1}
    check("full_source_divided_square",full_second[Q]==expected_square)
    y=vector_divide(full_second,qi(2))
    C={10:1,4:-1,-4:-1,-10:1}
    delta={1:1,-1:-1}
    check("full_source_divided_square",y[Q]==C)
    check("full_source_divided_square",mul(qi(2),C)==expected_square)
    check("source_highest_successors",matrix_apply(mats["EW"],y)=={})
    check("source_highest_successors",all(weights[i]==(10,5,9,6) for i in y))
    raised2=vector_divide(matrix_apply(mats["EV"],matrix_apply(mats["EV"],y)),qi(2))
    check("source_highest_successors",raised2=={T:gaussian(9,2)})
    check("source_highest_successors",matrix_apply(mats["EV"],raised2)=={})

    def cartan(vec,inverse=False):
        return {pair:shift(c,(-1 if inverse else 1)*sum(a*b for a,b in
                 zip(weights[pair[0]],weights[pair[1]]))) for pair,c in vec.items()}

    def theta(vec,colour,inverse=False,trace=None):
        current=vec
        output={key:dict(c) for key,c in vec.items()}
        dp={0:1}
        fact={0:1}
        if trace is not None:
            trace.append({"power":0,"input_support":len(current)})
        for k in range(1,11):
            current=tensor_slot(mats["F"+colour],current,0)
            current=tensor_slot(mats["E"+colour],current,1)
            current=vector_divide(current,power(qi(k),2))
            if trace is not None:
                trace.append({"power":k,"input_support":len(current)})
            if not current:
                break
            if k==10:
                raise AssertionError("Full source nilpotence failed")
            fact=mul(fact,qi(k))
            dp=mul(dp,delta)
            multiplier=shift(mul(dp,fact),
                             (-1 if inverse else 1)*k*(k-1)//2)
            if inverse and k%2:
                multiplier=scale(multiplier,-1)
            output=vector_add(output,vector_scale(current,multiplier))
        return output

    def braid(vec):
        return flip(theta(theta(cartan(vec),"W"),"V"))

    def braid_inverse(vec):
        return cartan(theta(theta(flip(vec),"V",True),"W",True),True)

    def coproduct(vec,name):
        colour=name[1]
        idx=0 if colour=="V" else 2
        if name[0]=="F":
            first=tensor_slot(mats[name],vec,0)
            weighted={pair:shift(c,weights[pair[0]][idx]-weights[pair[0]][idx+1])
                      for pair,c in vec.items()}
            return vector_add(first,tensor_slot(mats[name],weighted,1))
        weighted={pair:shift(c,-weights[pair[1]][idx]+weights[pair[1]][idx+1])
                  for pair,c in vec.items()}
        return vector_add(tensor_slot(mats[name],weighted,0),tensor_slot(mats[name],vec,1))

    original_tensor=tensor(tvec,y)
    check("cartan_original_input",cartan(original_tensor)==vector_scale(original_tensor,{252:1}))
    theta_W_trace=[]
    intermediate=theta(cartan(original_tensor),"W",trace=theta_W_trace)
    check("full_theta_W_cancellation",theta_W_trace==[{"power":0,"input_support":len(y)},
                                                     {"power":1,"input_support":0}])
    theta_V_trace=[]
    output=flip(theta(intermediate,"V",trace=theta_V_trace))
    check("full_theta_V_termination",[x["power"] for x in theta_V_trace]==[0,1,2,3])
    check("full_theta_V_termination",theta_V_trace[-1]["input_support"]==0)
    expected=shift(mul(mul(power(delta,2),mul(qi(9),qi(8))),C),253)
    expected_divided=shift(mul(mul(power(delta,2),mul(qi(2),gaussian(9,2))),C),253)
    check("actual_composed_source_entry",output[(T,Q)]==expected)
    check("actual_composed_source_entry",expected==expected_divided)
    check("full_source_braid_inverse",braid_inverse(output)==original_tensor)
    for name in ["EV","FV","EW","FW"]:
        left=braid(coproduct(original_tensor,name))
        right=coproduct(output,name)
        check("actual_source_intertwiner_columns",left==right,name)
    check("integral_braided_column",
          all(type(c) is int for polynomial in output.values() for c in polynomial.values()))
    check("actual_q1_flip",{pair:{0:sum(c.values())} for pair,c in output.items() if sum(c.values())}==
          {pair:{0:sum(c.values())} for pair,c in flip(original_tensor).items() if sum(c.values())})

    check("retained_entry_polynomial",min(expected)==226 and max(expected)==280)
    check("retained_entry_polynomial",sum(c>0 for c in expected.values())==8)
    check("retained_entry_polynomial",sum(c<0 for c in expected.values())==8)
    expansion=jets(expected,20)
    check("ordinary_entry_jet",next(i for i,c in enumerate(expansion) if c)==4)
    check("ordinary_entry_jet",expansion[4]==24192)
    for ell,order,lead in [(3,14,2),(7,10,5)]:
        check("residual_entry_jets",next(i for i,c in enumerate(expansion) if c%ell)==order)
        check("residual_entry_jets",expansion[order]%ell==lead)

    # Algebraic phase/NS-path identity; no floating trigonometric approximation.
    delta2=power(delta,2)
    q3=add({0:3},delta2)
    q7=add(add(add({0:7},scale(delta2,14)),scale(power(delta2,2),7)),power(delta2,3))
    check("phase_polynomial_identities",q3==qi(3))
    check("phase_polynomial_identities",q7==qi(7))
    check("phase_polynomial_identities",C==mul(delta2,mul(q3,q7)))
    tau=scale(delta2,Fraction(-1,2))
    Btau=scale(mul(add(add(add({0:7},scale(tau,-28)),scale(power(tau,2),28)),
                      scale(power(tau,3),-8)),add({0:3},scale(tau,-2))),-2)
    check("phase_polynomial_identities",mul(tau,Btau)==C)
    phase_entry=shift(scale(mul(power(tau,2),mul(mul(qi(9),qi(8)),Btau)),-2),253)
    check("phase_polynomial_identities",phase_entry==expected)
    check("phase_polynomial_identities",sum(Btau.values())==-42)
    exact_quotient=divide_exact(expected,power(tau,2))
    check("phase_germ_limit",sum(exact_quotient.values())==6048)
    check("phase_germ_limit",sum(shift(exact_quotient,-253).values())==6048)
    for n in range(1,10):
        # (q-q^-1)[n]=q^n-q^-n proves the sine quotient at q=exp(i theta).
        check("exact_sine_quotient_identity",mul(delta,qi(n))=={n:1,-n:-1})

    # The actual T strings give an independent no-quadratic witness.
    eigenvalues=[(1,270),(-1,264),(1,260)]
    for i,(sign,exponent) in enumerate(eigenvalues):
        for other_sign,other_exp in eigenvalues[:i]:
            check("retained_T_distinct_eigenvalues",
                  {exponent:sign} != {other_exp:other_sign})
    check("retained_T_eigenvalues",
          [((-1)**s,270-s*(7-s)) for s in (0,1,2)]==eigenvalues)

    result={"status":"pass","scope":"Complete original 1260-basis data; exact composed column, four actual source intertwining checks and inverse; analytic universal proof remains in full_braiding.tex.",
            "checks":sum(COUNTS.values()),"categories":dict(COUNTS),
            "inputs":{"full_generators.json":GEN_SHA,"basis_1260.json":BASIS_SHA},
            "actual_input":"(1 tensor FV^(2))(b126 tensor b126)",
            "output_coordinate":"b126 tensor b144 after c_X",
            "full_FV_squared_T_at_Q":serial(full_second[Q]),
            "retained_C":serial(C),"composed_entry":serial(expected),
            "entry_formula":"q^253 (q-q^-1)^2 [2]! [9 choose 2]_q C = q^253 (q-q^-1)^2 [9][8] C",
            "source_y_support":len(y),"braided_column_support":len(output),
            "theta_W_trace":theta_W_trace,"theta_V_trace":theta_V_trace,
            "ordinary_jet":{"order":4,"lead":24192},
            "residual_jets":{"3":{"order":14,"lead":2},"7":{"order":10,"lead":5}},
            "phase_germ":{"phase":"q^253=exp(253 i theta)","tau":"2 sin(theta)^2",
                          "A_tau_over_tau_squared_limit":6048},
            "checker_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "elapsed_seconds":round(time.monotonic()-start,3)}
    (HERE/"source_entry_verification.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({k:result[k] for k in ["status","checks","categories","source_y_support","braided_column_support","elapsed_seconds"]}))

if __name__=="__main__":
    main()

