#!/usr/bin/env python3
"""Exact finite conormal and Weyl-correction calibration.

All quotient coordinates use the original monic h and unscaled tensor power
bases. The first thickening is computed by complete monic h-adic division,
retaining h-degree zero and one and quotienting precisely I². Polynomial
units are explicitly declared calibration data, not actual theta values.
No Python assertions, floating point, numerical quadrature, or Lean runs.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from functools import lru_cache
import hashlib
from itertools import product
import json
from pathlib import Path
import sys

import sympy as sp

ROOT=Path(__file__).resolve().parents[1]
s=sp.Symbol("s")
RECORDS=[]


def same(a,b):
    if isinstance(a,sp.MatrixBase) or isinstance(b,sp.MatrixBase):
        return a.shape==b.shape and all(sp.cancel(v)==0 for v in a-b)
    return sp.cancel(sp.expand(a-b))==0


def record(name,ok,kind="exact",**evidence):
    passed=bool(ok)
    RECORDS.append(dict(name=name,kind=kind,passed=passed,**evidence))
    if not passed: raise ArithmeticError(name)


def eq(name,a,b,**evidence): record(name,same(a,b),**evidence)
def reject(name,a,b): record(name,not same(a,b),kind="negative_control")


def tensor(matrices):
    if len(matrices)==1:return matrices[0]
    return sp.kronecker_product(*matrices)


def vector(p,d):
    pp=sp.Poly(sp.expand(p),s)
    return sp.Matrix([pp.nth(j) for j in range(d)])


class Thickening:
    def __init__(self,h,k):
        self.h=sp.expand(h);self.k=k;self.d=int(sp.degree(h,s));self.n=self.d**k
        self.variables=sp.symbols(f"s0:{k}")
        self.powers=list(product(range(self.d),repeat=k))
        self.basis=[sp.prod(v**a for v,a in zip(self.variables,p)) for p in self.powers]
        self.hs=[self.h.subs(s,v) for v in self.variables]
        self.basis2=self.basis+[sp.expand(hi*b) for hi in self.hs for b in self.basis]
        self.dimension2=(k+1)*self.n
    @lru_cache(None)
    def h_adic(self,power):
        dividend=s**power; result=[]
        while dividend!=0:
            quotient,remainder=sp.div(sp.Poly(dividend,s),sp.Poly(self.h,s))
            result.append(vector(remainder.as_expr(),self.d))
            dividend=quotient.as_expr()
        return result
    @lru_cache(None)
    def monomial2(self,powers):
        digits=[self.h_adic(a) for a in powers]
        zeroth=[v[0] if v else sp.zeros(self.d,1) for v in digits]
        blocks=[tensor(zeroth)]
        for i in range(self.k):
            first=zeroth.copy()
            first[i]=digits[i][1] if len(digits[i])>1 else sp.zeros(self.d,1)
            blocks.append(tensor(first))
        return sp.Matrix.vstack(*blocks)
    def vec2(self,p):
        pp=sp.Poly(sp.expand(p),*self.variables)
        return sum((c*self.monomial2(tuple(a)) for a,c in pp.terms()),sp.zeros(self.dimension2,1))
    def vec(self,p): return self.vec2(p)[:self.n,:]
    def poly(self,v): return sp.expand(sum(v[i]*b for i,b in enumerate(self.basis)))
    def derivative(self,p): return sp.expand(sum(sp.diff(p,v) for v in self.variables)/self.k)
    def mult(self,p): return sp.Matrix.hstack(*[self.vec(p*b) for b in self.basis])
    def mult2(self,p): return sp.Matrix.hstack(*[self.vec2(p*b) for b in self.basis2])


def run_fixture(name,h,k):
    pfx=f"{name}:k{k}:"
    Q=Thickening(h,k);d,n,m=Q.d,Q.n,Q.dimension2
    rdistinct=int(sp.degree(sp.Poly(h,s).sqf_part().as_expr(),s))
    for i,b in enumerate(Q.basis2):
        target=sp.zeros(m,1);target[i]=1
        eq(pfx+f"complete_h_adic_basis_{i}",Q.vec2(b),target)
    pi=sp.eye(n).row_join(sp.zeros(n,k*n))
    j=sp.eye(n).col_join(sp.zeros(k*n,n))
    conormal=sp.zeros(n,k*n).col_join(sp.eye(k*n))
    derivative=sp.Matrix.hstack(*[Q.vec(Q.derivative(b)) for b in Q.basis2])
    D0=derivative*j
    original_sum=sum(Q.variables)
    Z=Q.mult(original_sum);Zhat=Q.mult2(original_sum)
    centered_sum=original_sum-sp.Rational(k,2)
    Zc=Q.mult(centered_sum);Zhatc=Q.mult2(centered_sum)
    eq(pfx+"original_centered_sum_E",Zc,Z-sp.Rational(k,2)*sp.eye(n))
    eq(pfx+"original_centered_sum_E2",Zhatc,Zhat-sp.Rational(k,2)*sp.eye(m))
    reject(pfx+"reject_omitted_original_center",Zc,Z)
    eq(pfx+"canonical_section",pi*j,sp.eye(n))
    eq(pfx+"conormal_kernel",pi*conormal,sp.zeros(n,k*n))
    eq(pfx+"thickened_sum_projection",pi*Zhat,Z*pi)
    eq(pfx+"derivation_sum_one",derivative*Q.vec2(original_sum),Q.vec(1))
    eq(pfx+"derivation_intertwiner",derivative*Zhat-Z*derivative,pi)
    eq(pfx+"centered_derivation_intertwiner",Zc*derivative-derivative*Zhatc,-pi)
    reject(pfx+"reject_reversed_derivation_sign",Zc*derivative-derivative*Zhatc,pi)

    ell0=sp.zeros(d);ell0[0,d-1]=1
    hprime=sp.diff(h,s)
    hp0=sp.Matrix.hstack(*[vector(sp.rem(sp.Poly(hprime*s**a,s),sp.Poly(h,s)).as_expr(),d) for a in range(d)])
    Ls=[];Hs=[];Ps=[]
    for i in range(k):
        L=tensor([ell0 if q==i else sp.eye(d) for q in range(k)])
        hp=tensor([hp0 if q==i else sp.eye(d) for q in range(k)])
        Li=sp.Matrix.hstack(*[Q.vec(sp.Poly(b,Q.variables[i]).nth(d-1)) for b in Q.basis])
        eq(pfx+f"literal_top_coefficient_map_{i}",L,Li)
        eq(pfx+f"original_hprime_multiplication_{i}",hp,Q.mult(sp.diff(Q.hs[i],Q.variables[i])))
        P=hp*L/d
        eq(pfx+f"projector_idempotent_{i}",P*P,P)
        eq(pfx+f"projector_rank_{i}",P.rank(),d**(k-1))
        eq(pfx+f"projector_actual_top_identity_{i}",L*hp*L,d*L)
        if d>1 and not same(P,P.T):
            reject(pfx+f"retain_nonorthogonal_projector_{i}",P,P.T)
        Ls.append(L);Hs.append(hp);Ps.append(P)
    Lstack=sp.Matrix.vstack(*Ls)
    Crow=sp.Matrix.hstack(*Hs)/k
    J=sum((hp*L for hp,L in zip(Hs,Ls)),sp.zeros(n))/k
    eq(pfx+"full_remainder_lift_defect",Zhat*j-j*Z,conormal*Lstack)
    eq(pfx+"centered_remainder_lift_defect",Zhatc*j-j*Zc,conormal*Lstack)
    eq(pfx+"full_conormal_derivative_row",derivative*conormal,Crow)
    eq(pfx+"commutator_original_coordinates",Z*D0-D0*Z,-sp.eye(n)+J)
    eq(pfx+"commutator_original_centered_coordinates",Zc*D0-D0*Zc,-sp.eye(n)+J)
    eq(pfx+"projector_correction",J,sp.Rational(d,k)*sum(Ps,sp.zeros(n)))
    reject(pfx+"reject_missing_finite_correction",Z*D0-D0*Z,-sp.eye(n))
    if k>1: reject(pfx+"reject_missing_one_over_k",J,sum((hp*L for hp,L in zip(Hs,Ls)),sp.zeros(n)))
    for i in range(k):
        for q in range(k):
            eq(pfx+f"commuting_projectors_{i}_{q}",Ps[i]*Ps[q],Ps[q]*Ps[i])
    joints=[]
    for mask in product((0,1),repeat=k):
        joint=sp.eye(n)
        for b,P in zip(mask,Ps):joint=joint*(P if b else sp.eye(n)-P)
        count=sum(mask);expected_rank=(d-1)**(k-count)
        eq(pfx+f"joint_rank_{mask}",joint.rank(),expected_rank)
        eq(pfx+f"joint_eigenvalue_{mask}",J*joint,sp.Rational(d*count,k)*joint)
        eq(pfx+f"joint_idempotent_{mask}",joint*joint,joint)
        joints.append(joint)
    eq(pfx+"complete_joint_decomposition",sum(joints,sp.zeros(n)),sp.eye(n))
    cp=J.charpoly()
    expected=sp.prod((cp.gen-sp.Rational(d*q,k))**(sp.binomial(k,q)*(d-1)**(k-q)) for q in range(k+1))
    eq(pfx+"complete_correction_characteristic_polynomial",cp.as_expr(),expected)
    eq(pfx+"correction_trace",sp.trace(J),n)
    eq(pfx+"correction_rank",J.rank(),n-(d-1)**k)
    eq(pfx+"full_conormal_row_rank",Crow.rank(),n-(d-rdistinct)**k)
    eq(pfx+"exact_row_factorization",Crow*Lstack,J)
    eq(pfx+"row_injective_on_coefficient_image",Lstack.rank(),J.rank())
    eq(pfx+"full_row_contains_correction_image",Crow.row_join(J).rank(),Crow.rank())
    eq(pfx+"rank_gap",Crow.rank()-J.rank(),(d-1)**k-(d-rdistinct)**k)
    if rdistinct>1: reject(pfx+"reject_equal_row_and_correction_ranks",Crow.rank(),J.rank())
    for i in range(k):
        for q in range(i,k):
            for a,b in enumerate(Q.basis):
                square=Q.hs[i]*Q.hs[q]*b
                eq(pfx+f"exact_I_squared_quotient_{i}_{q}_{a}",Q.vec2(square),sp.zeros(m,1))
                eq(pfx+f"derivative_maps_I_squared_to_I_{i}_{q}_{a}",Q.vec(Q.derivative(square)),sp.zeros(n,1))

    # The target is E[epsilon]/epsilon², with its full original E multiplication.
    Phi=pi.col_join(derivative)
    target_one=Q.vec(1).col_join(sp.zeros(n,1))
    eq(pfx+"dual_number_map_unit",Phi*Q.vec2(1),target_one)
    for i,variable in enumerate(Q.variables):
        a=Q.mult(variable)
        target_action=sp.BlockMatrix([[a,sp.zeros(n)],[sp.eye(n)/k,a]]).as_explicit()
        eq(pfx+f"dual_number_map_generator_multiplicativity_{i}",Phi*Q.mult2(variable),target_action*Phi)
    eq(pfx+"dual_number_image_dimension",Phi.rank(),n+Crow.rank())
    eq(pfx+"dual_number_kernel_dimension",len(Phi.nullspace()),k*n-Crow.rank())
    kernel=sp.Matrix.hstack(*Phi.nullspace()) if Phi.nullspace() else sp.zeros(m,0)
    eq(pfx+"dual_number_kernel_in_conormal",pi*kernel,sp.zeros(n,kernel.cols))
    image_description=pi.col_join(derivative-D0*pi)
    eq(pfx+"dual_number_image_graph_plus_row",image_description,
       sp.BlockMatrix([[sp.eye(n),sp.zeros(n,k*n)],[sp.zeros(n),Crow]]).as_explicit())
    record(pfx+"dual_number_surjectivity_criterion",(Phi.rank()==2*n)==(rdistinct==d))
    record(pfx+"dual_number_isomorphism_criterion",(Phi.rows==Phi.cols and Phi.det()!=0) if (k==1 and rdistinct==d) else Phi.rank()<Phi.cols or Phi.rank()<Phi.rows)

    # Retain a polynomial unit and its entire first conormal class.
    U_base_poly=sp.prod(variable+5 for variable in Q.variables)
    U_conormal_poly=sum((i+1)*hi for i,hi in enumerate(Q.hs))
    U_poly=U_base_poly+U_conormal_poly
    U=Q.mult(U_poly);Uhat=Q.mult2(U_poly)
    Uhat_base=Q.mult2(U_base_poly)
    eq(pfx+"conormal_unit_term_vanishes_only_in_E",U,Q.mult(U_base_poly))
    reject(pfx+"retain_full_unit_first_conormal_class",Uhat,Uhat_base)
    record(pfx+"original_unit_in_E",U.det()!=0)
    record(pfx+"original_unit_in_E2",Uhat.det()!=0)
    unit_j=Uhat*j*U.inv()
    beta_vector=U.inv()*derivative*Q.vec2(U_poly)
    beta=Q.mult(Q.poly(beta_vector))
    DU=derivative*unit_j
    DU_base=derivative*Uhat_base*j*U.inv()
    eq(pfx+"unit_conormal_derivative_difference",DU-DU_base,
       Q.mult(Q.derivative(U_conormal_poly))*U.inv())
    reject(pfx+"reject_deleted_unit_conormal_term",DU,DU_base)
    JU=U*J*U.inv()
    eq(pfx+"transported_section_full_projection",pi*unit_j,sp.eye(n))
    eq(pfx+"transported_derivative_beta_term",DU,beta+U*D0*U.inv())
    reject(pfx+"reject_omitted_unit_connection",DU,U*D0*U.inv())
    eq(pfx+"transported_correction",Z*DU-DU*Z,-sp.eye(n)+JU)
    eq(pfx+"centered_transported_correction",Zc*DU-DU*Zc,-sp.eye(n)+JU)
    eq(pfx+"centered_transported_lift_defect",Zhatc*unit_j-unit_j*Zc,Uhat*(Zhatc*j-j*Zc)*U.inv())
    eq(pfx+"transported_correction_trace",sp.trace(JU),n)
    eq(pfx+"transported_correction_rank",JU.rank(),J.rank())
    eq(pfx+"transported_beta_commutes_sum",Z*beta,beta*Z)
    eq(pfx+"unit_conormal_transport",Uhat*conormal,conormal*sp.diag(*([U]*k)))
    if d>1: reject(pfx+"reject_untransported_projector",JU,J)
    if k==1:
        g=h*U_poly.subs(Q.variables[0],s)
        gprime=Q.mult(sp.diff(g,s).subs(s,Q.variables[0]))
        eq(pfx+"one_factor_original_gprime_correction",JU,gprime*Ls[0]*U.inv())
        eq(pfx+"one_factor_gprime_full_residue",gprime,U*Hs[0])
    return dict(name=name,h=str(sp.expand(h)),k=k,degree=d,distinct_roots=rdistinct,
                E_dimension=n,E2_dimension=m,original_sum=str(original_sum),
                original_centered_sum=str(centered_sum),
                monomial_basis=list(map(str,Q.basis)),
                correction_rank=J.rank(),full_conormal_row_rank=Crow.rank(),
                Phi_rank=Phi.rank(),unit_polynomial=str(U_poly))


def local_conormal_coefficients():
    w=sp.Symbol("w")
    for m in range(1,5):
        local_h=w**m*(2+3*w+w**2)
        derivative=sp.diff(local_h,w)
        for j in range(m):
            output=sp.rem(derivative*w**j,w**m,w)
            expected=2*m*w**(m-1) if j==0 else 0
            eq(f"local_hprime_m{m}:input_power{j}",output,expected)
        if m>1:
            reject(f"local_hprime_m{m}:reject_top_coefficient_extraction",sp.rem(derivative*w**(m-1),w**m,w),2*m*w**(m-1))


def declared_metric_counterexample():
    # Actual coordinates for h=s², k=2, and an explicitly declared positive
    # calibration metric. No assertion identifies G with a theta metric.
    P1=sp.diag(0,0,1,1);P2=sp.diag(0,1,0,1);J=P1+P2
    G=sp.Matrix([[1,0,0,0],[0,2,1,0],[0,1,2,0],[0,0,0,1]])
    for size in range(1,5):
        record(f"metric_witness:positive_principal_minor_{size}",G[:size,:size].det()>0)
    eq("metric_witness:Hermitian_correction",J.T*G,G*J)
    reject("metric_witness:Hermitian_sum_does_not_force_P1",P1.T*G,G*P1)
    reject("metric_witness:Hermitian_sum_does_not_force_P2",P2.T*G,G*P2)


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--output",type=Path,required=True)
    parser.add_argument("--self-test-failure",action="store_true")
    args=parser.parse_args();models=[];error=None
    try:
        local_conormal_coefficients()
        declared_metric_counterexample()
        for k in (1,2,3):models.append(run_fixture("degree_one",s-2,k))
        for k in (1,2,3):models.append(run_fixture("double_root",(s-sp.Rational(1,3))**2,k))
        for k in (1,2):models.append(run_fixture("mixed_repeated",(s-1)**2*(s+2),k))
        models.append(run_fixture("squarefree",(s-1)*(s+2),2))
        if args.self_test_failure:
            record("intentional_false_identity",sp.Rational(1,2)==1,kind="harness_negative_control")
    except Exception as exc:
        error=f"{type(exc).__name__}: {exc}"
    source=ROOT/"tex/conormal_finite_weyl.tex"
    pr=ROOT/"sources/web_sum_connection_delivery/Tau_Sum_Connection_Control/NOTE.tex"
    output=dict(created_utc=datetime.now(timezone.utc).isoformat(),
       scope="Exact finite original polynomial quotients, first conormal thickening, canonical remainder commutator, nonorthogonal projectors, unit transport and dual-number algebra map; no arithmetic theta-unit values, analytic estimate, RH proof or Lean execution.",
       python_version=sys.version,optimization_level=sys.flags.optimize,sympy_version=sp.__version__,
       checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
       source_sha256=hashlib.sha256(source.read_bytes()).hexdigest() if source.exists() else None,
       pr20_source_sha256=hashlib.sha256(pr.read_bytes()).hexdigest(),
       total=len(RECORDS),passed=sum(q["passed"] for q in RECORDS),
       exact_checks=sum(q["kind"]=="exact" for q in RECORDS),negative_controls=sum(q["kind"]=="negative_control" for q in RECORDS),
       all_passed=error is None and all(q["passed"] for q in RECORDS),error=error,models=models,records=RECORDS)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(output,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({k:output[k] for k in ("total","passed","exact_checks","negative_controls","all_passed","error")},sort_keys=True))
    return 0 if output["all_passed"] else 1


if __name__=="__main__":raise SystemExit(main())
