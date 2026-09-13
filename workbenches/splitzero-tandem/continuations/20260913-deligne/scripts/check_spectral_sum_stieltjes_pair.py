#!/usr/bin/env python3
"""Exact symmetric-square parity and coupled Gaussian norm calibrations.

Original symmetric tensors use unscaled orbit sums, with diagonal tensors
occurring once. Quotient algebras retain full polynomial powers. The norm
pushforward is the exact model w(t)=exp(-t^2/2), whose two-variable mass is
2*pi. It is not the arithmetic theta density. In the separate constrained
minimum fixtures the residue unit is an independently prescribed even unit.
No Python assert, numerical quadrature, or Lean execution is used.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from functools import lru_cache
import hashlib
import json
from pathlib import Path
import sys

import sympy as sp

ROOT=Path(__file__).resolve().parents[1]
s,y,x,delta,Z,r=sp.symbols("s y x delta Z r")
s1,s2,t1,t2=sp.symbols("s1 s2 t1 t2",real=True)
HALF=sp.Rational(1,2)
RECORDS=[]


def same(a,b):
    if isinstance(a,sp.MatrixBase) or isinstance(b,sp.MatrixBase):
        return a.shape==b.shape and all(sp.cancel(v)==0 for v in a-b)
    return sp.cancel(sp.expand(a-b))==0


def record(name,passed,kind="exact",**evidence):
    ok=bool(passed)
    RECORDS.append(dict(name=name,kind=kind,passed=ok,**evidence))
    if not ok:
        raise ArithmeticError(name)


def eq(name,a,b,**evidence): record(name,same(a,b),**evidence)
def reject(name,a,b): record(name,not same(a,b),kind="negative_control")


def remainder(p,h,var):
    return sp.rem(sp.Poly(p,var),sp.Poly(h,var)).as_expr().expand()


def coeffvec(p,var,d):
    pp=sp.Poly(sp.expand(p),var)
    return sp.Matrix([pp.nth(j) for j in range(d)])


def mult(p,h,var):
    d=int(sp.degree(h,var))
    return sp.Matrix.hstack(*[coeffvec(remainder(p*var**j,h,var),var,d) for j in range(d)])


def matrix_polynomial(p,a,var):
    return sum((c*a**j for (j,),c in sp.Poly(p,var).terms()),sp.zeros(a.rows))


class Quotient:
    """Explicit Groebner remainder basis; not a radical quotient."""
    def __init__(self,generators):
        self.groebner=sp.groebner(generators,x,delta,order="lex")
        if not self.groebner.is_zero_dimensional:
            raise ArithmeticError("Fixture ideal was not zero-dimensional")
        leads=[p.LM(order=self.groebner.order).exponents for p in self.groebner.polys]
        bx=min(a for a,b in leads if b==0)
        bd=min(b for a,b in leads if a==0)
        self.powers=sorted([(a,b) for a in range(bx) for b in range(bd)
                            if not any(a>=u and b>=v for u,v in leads)],key=lambda ab:(sum(ab),ab))
        self.basis=[x**a*delta**b for a,b in self.powers]
        self.dim=len(self.basis)
    def rem(self,p): return self.groebner.reduce(sp.expand(p))[1].expand()
    def vec(self,p):
        pp=sp.Poly(self.rem(p),x,delta)
        return sp.Matrix([pp.coeff_monomial(m) for m in self.basis])
    def multiplication(self,p): return sp.Matrix.hstack(*[self.vec(p*m) for m in self.basis])


def original_symmetric(h):
    d=int(sp.degree(h,s)); A=mult(s,h,s)
    orbit=[(i,j) for i in range(d) for j in range(i,d)]
    O=sp.zeros(d*d,len(orbit)); L=sp.zeros(len(orbit),d*d)
    for k,(i,j) in enumerate(orbit):
        O[i*d+j,k]=1
        if i!=j: O[j*d+i,k]=1
        L[k,i*d+j]=1
    S=L*(sp.kronecker_product(A,sp.eye(d))+sp.kronecker_product(sp.eye(d),A))*O
    difference=sp.kronecker_product(A,sp.eye(d))-sp.kronecker_product(sp.eye(d),A)
    Delta=L*difference**2*O
    reflection=sp.Matrix.hstack(*[coeffvec(remainder((1-s)**j,h,s),s,d) for j in range(d)])
    C=L*sp.kronecker_product(reflection,reflection)*O
    unit=sp.zeros(len(orbit),1); unit[orbit.index((0,0)),0]=1
    return dict(d=d,A=A,orbit=orbit,O=O,L=L,S=S,Delta=Delta,C=C,unit=unit)


def derive_parity_relations(h):
    p=sp.Poly(sp.expand(h.subs(s,(1+Z+r)/2)),Z,r)
    H0=sp.S.Zero; H1=sp.S.Zero; A0=sp.S.Zero; A1=sp.S.Zero
    for (a,b),c in p.terms():
        if b%2==0:
            if a%2: raise ArithmeticError("H0 is not even in Z")
            H0+=c*Z**a*delta**(b//2)
            A0+=c*(-x)**(a//2)*delta**(b//2)
        else:
            if not a%2: raise ArithmeticError("H1 is not odd in Z")
            H1+=c*Z**a*delta**((b-1)//2)
            A1+=c*(-x)**((a-1)//2)*delta**((b-1)//2)
    return tuple(map(sp.expand,(H0,H1,A0,A1)))


def algebra_model(name,H,minimum=False):
    prefix=name+":"
    D=int(sp.degree(H,y)); h=sp.expand((-1)**D*H.subs(y,-(s-HALF)**2))
    dat=original_symmetric(h); d=dat["d"]; n=d*(d+1)//2
    S,Delta,C,c=dat["S"],dat["Delta"],dat["C"],dat["unit"]
    ZM=S-sp.eye(n); XM=-ZM**2
    eq(prefix+"unscaled_orbit_left_inverse",dat["L"]*dat["O"],sp.eye(n))
    orbit_norm=dat["O"].T*dat["O"]
    eq(prefix+"unscaled_orbit_tensor_Gram",orbit_norm,sp.diag(*[1 if i==j else 2 for i,j in dat["orbit"]]))
    eq(prefix+"reflection_involution",C*C,sp.eye(n))
    eq(prefix+"reflection_sum_orientation",C*ZM,-ZM*C)
    eq(prefix+"reflection_relative_coordinate",C*Delta,Delta*C)
    eq(prefix+"commuting_base_relative",XM*Delta,Delta*XM)
    H0,H1,A0,A1=derive_parity_relations(h)
    eq(prefix+"source_even_odd_relations",h.subs(s,(1+Z+r)/2),H0.subs(delta,r**2)+r*H1.subs(delta,r**2))
    eq(prefix+"H0_parity",H0,A0.subs(x,-Z**2))
    eq(prefix+"H1_parity",H1,Z*A1.subs(x,-Z**2))
    eq(prefix+"exact_zero_base_polynomial",A0.subs(x,0),(-1)**D*H.subs(y,-delta/4))
    if D%2: reject(prefix+"reject_zero_base_sign",A0.subs(x,0),H.subs(y,-delta/4))
    Be=Quotient([A0,x*delta*A1]); Bo=Quotient([A0,delta*A1])
    eq(prefix+"even_dimension",Be.dim,D*(D+1))
    eq(prefix+"odd_dimension",Bo.dim,D**2)
    eq(prefix+"original_even_eigenspace",len((C-sp.eye(n)).nullspace()),Be.dim)
    eq(prefix+"original_odd_eigenspace",len((C+sp.eye(n)).nullspace()),Bo.dim)
    def eval_matrix(poly):
        return sum((v*XM**a*Delta**b for (a,b),v in sp.Poly(poly,x,delta).terms()),sp.zeros(n))
    eq(prefix+"original_A0_relation",eval_matrix(A0),sp.zeros(n))
    eq(prefix+"original_odd_relation",ZM*eval_matrix(delta*A1),sp.zeros(n))
    eq(prefix+"original_even_relation",eval_matrix(x*delta*A1),sp.zeros(n))
    reject(prefix+"reject_deleted_x_relation",eval_matrix(delta*A1),sp.zeros(n))
    even=sp.Matrix.hstack(*[eval_matrix(p)*c for p in Be.basis])
    odd=sp.Matrix.hstack(*[ZM*eval_matrix(p)*c for p in Bo.basis])
    P=even.row_join(odd)
    record(prefix+"complete_parity_isomorphism",P.det()!=0,determinant=str(P.det()))
    eq(prefix+"retained_reflection_eigenbasis",C*P,P*sp.diag(sp.eye(Be.dim),-sp.eye(Bo.dim)))
    # SSP.20--22: the source's actual three groups of literal orbit sums.
    single_pair_basis=[(-(s-HALF)**2)**j for j in range(D)]+[(s-HALF)*(-(s-HALF)**2)**j for j in range(D)]
    single_inverse=sp.Matrix.hstack(*[coeffvec(p,s,d) for p in single_pair_basis])
    single=single_inverse.inv()
    group_orbits=([(i,j) for i in range(D) for j in range(i,D)]+
                  [(D+i,D+j) for i in range(D) for j in range(i,D)]+
                  [(i,D+j) for i in range(D) for j in range(D)])
    newO=sp.zeros(d*d,n)
    for k,(i,j) in enumerate(group_orbits):
        newO[i*d+j,k]=1
        if i!=j: newO[j*d+i,k]=1
    newD=newO.T*newO
    newL=newD.inv()*newO.T
    oldL=(dat["O"].T*dat["O"]).inv()*dat["O"].T
    Ts=newL*sp.kronecker_product(single,single)*dat["O"]
    Tsi=oldL*sp.kronecker_product(single_inverse,single_inverse)*newO
    eq(prefix+"literal_symmetric_coordinate_inverse",Ts*Tsi,sp.eye(n))
    eq(prefix+"literal_symmetric_coordinate_det_square",Ts.det()**2,1,determinant=str(Ts.det()))
    eq(prefix+"literal_reflection_grouping",Ts*C*Tsi,sp.diag(sp.eye(Be.dim),-sp.eye(Bo.dim)))
    orbit_to_remainder=P.inv()*Tsi
    Qe=orbit_to_remainder[:Be.dim,:Be.dim]
    Qo=orbit_to_remainder[Be.dim:,Be.dim:]
    eq(prefix+"literal_to_quotient_full_coordinate_map",orbit_to_remainder,sp.diag(Qe,Qo))
    alpha=sp.Matrix.hstack(*[Be.vec(x*p) for p in Bo.basis])
    beta=sp.Matrix.hstack(*[Bo.vec(p) for p in Be.basis])
    Xe,Xo=Be.multiplication(x),Bo.multiplication(x)
    De,Do=Be.multiplication(delta),Bo.multiplication(delta)
    eq(prefix+"alpha_injective",alpha.rank(),Bo.dim)
    eq(prefix+"beta_surjective",beta.rank(),Bo.dim)
    eq(prefix+"alpha_beta_even_x",alpha*beta,Xe)
    eq(prefix+"beta_alpha_odd_x",beta*alpha,Xo)
    eq(prefix+"alpha_delta_intertwiner",De*alpha,alpha*Do)
    eq(prefix+"beta_delta_intertwiner",Do*beta,beta*De)
    eq(prefix+"original_even_x",XM*even,even*Xe)
    eq(prefix+"original_odd_x",XM*odd,odd*Xo)
    eq(prefix+"original_even_delta",Delta*even,even*De)
    eq(prefix+"original_odd_delta",Delta*odd,odd*Do)
    block=sp.BlockMatrix([[sp.eye(Be.dim),-alpha],[beta,sp.eye(Bo.dim)]]).as_explicit()
    eq(prefix+"original_sum_block",S*P,P*block)
    alpha_literal=Qe.inv()*alpha*Qo; beta_literal=Qo.inv()*beta*Qe
    eq(prefix+"literal_original_sum_block",Ts*S*Tsi,
       sp.BlockMatrix([[sp.eye(Be.dim),-alpha_literal],[beta_literal,sp.eye(Bo.dim)]]).as_explicit())
    reject(prefix+"reject_sum_alpha_sign",S*P,P*sp.BlockMatrix([[sp.eye(Be.dim),alpha],[beta,sp.eye(Bo.dim)]]).as_explicit())
    reject(prefix+"reject_missing_sum_one",S*P,P*(block-sp.eye(n)))
    g0=sp.expand(A0.subs(x,0))
    projection=sp.Matrix.hstack(*[coeffvec(remainder(p.subs(x,0),g0,delta),delta,D) for p in Be.basis])
    eq(prefix+"cokernel_projection_surjective",projection.rank(),D)
    eq(prefix+"cokernel_kills_alpha",projection*alpha,sp.zeros(D,Bo.dim))
    eq(prefix+"cokernel_exact_dimension",Be.dim-projection.rank(),alpha.rank())
    injection=sp.Matrix.hstack(*[Be.vec(delta**j*delta*A1) for j in range(D)])
    eq(prefix+"beta_kernel_explicit_injection",injection.rank(),D)
    eq(prefix+"beta_kernel_injection_zero",beta*injection,sp.zeros(Bo.dim,D))
    eq(prefix+"beta_kernel_dimension",len(beta.nullspace()),D)
    eq(prefix+"kernel_relative_action",De*injection,injection*mult(delta,g0,delta))
    eq(prefix+"cokernel_relative_action",projection*De,mult(delta,g0,delta)*projection)
    eq(prefix+"sum_zero_kernel_dimension",len(ZM.nullspace()),D)
    eq(prefix+"sum_zero_rank",ZM.rank(),2*D**2)
    eq(prefix+"kernel_annihilated_by_x",Xe*injection,sp.zeros(Be.dim,D))
    ctwist=sp.expand((-1)**(D+1)*delta*sp.diff(H,y).subs(y,-delta/4)/2)
    eq(prefix+"kernel_product_twist_constant",delta*A1.subs(x,0),ctwist)
    for a in range(D):
        for b in range(D):
            eq(prefix+f"kernel_inherited_product_{a}_{b}",
               Be.vec(delta**(a+b)*(delta*A1)**2),Be.vec(delta**(a+b)*ctwist*delta*A1))
    original_kernel=even*injection
    original_cokernel=projection*P.inv()[:Be.dim,:]
    eq(prefix+"original_sum_kernel_injection",ZM*original_kernel,sp.zeros(n,D))
    eq(prefix+"original_sum_cokernel_projection",original_cokernel*ZM,sp.zeros(D,n))
    eq(prefix+"original_sum_kernel_rank",original_kernel.rank(),D)
    eq(prefix+"original_sum_cokernel_rank",original_cokernel.rank(),D)
    rhoH=sp.Matrix.hstack(*[coeffvec(remainder(p.subs({x:0,delta:-4*y}),H,y),y,D) for p in Be.basis])
    iotaH=sp.Matrix.hstack(*[Be.vec(delta*A1*(-delta/4)**j) for j in range(D)])
    eq(prefix+"original_H_cokernel_rank",rhoH.rank(),D)
    eq(prefix+"original_H_kernel_rank",iotaH.rank(),D)
    eq(prefix+"original_H_cokernel_action",rhoH*De,-4*mult(y,H,y)*rhoH)
    eq(prefix+"original_H_kernel_action",De*iotaH,-4*iotaH*mult(y,H,y))
    cH=2*(-1)**D*y*sp.diff(H,y)
    for a in range(D):
        for b in range(D):
            eq(prefix+f"original_H_inherited_product_{a}_{b}",
               Be.vec((delta*A1)**2*(-delta/4)**(a+b)),
               Be.vec(delta*A1*cH.subs(y,-delta/4)*(-delta/4)**(a+b)))
    vv=1-(-(s-HALF)**2)/2
    Uone=mult(vv,h,s)
    U2=dat["L"]*sp.kronecker_product(Uone,Uone)*dat["O"]
    UU=P.inv()*U2*P
    Ue,Uo=UU[:Be.dim,:Be.dim],UU[Be.dim:,Be.dim:]
    eq(prefix+"full_even_unit_blocks",UU,sp.diag(Ue,Uo))
    eq(prefix+"full_unit_alpha",Ue*alpha,alpha*Uo)
    eq(prefix+"full_unit_beta",beta*Ue,Uo*beta)
    defect_unit=mult((1-y/2)**2,H,y)
    eq(prefix+"full_squared_defect_unit_cokernel",rhoH*Ue,defect_unit*rhoH)
    eq(prefix+"full_squared_defect_unit_kernel",Ue*iotaH,iotaH*defect_unit)
    eq(prefix+"unit_symmetric_determinant",U2.det(),Uone.det()**(d+1))
    eq(prefix+"unit_exact_sequence_determinant",Ue.det(),Uo.det()*defect_unit.det())
    # Check both source theta-primitive polynomial identities with all signs.
    aa=1+x+2*delta; bb=1-x+3*delta**2
    hp=h.subs(s,(1+Z+r)/2); hm=h.subs(s,(1+Z-r)/2)
    at=aa.subs({x:-Z**2,delta:r**2}); bt=bb.subs({x:-Z**2,delta:r**2})
    even_relation=(A0*aa+x*delta*A1*bb).subs({x:-Z**2,delta:r**2})
    odd_relation=(Z*(A0*aa+delta*A1*bb)).subs({x:-Z**2,delta:r**2})
    eq(prefix+"original_even_primitive_identity",even_relation,hp*(at-r*Z*bt)/2+hm*(at+r*Z*bt)/2)
    eq(prefix+"original_odd_primitive_identity",odd_relation,hp*(Z*at+r*bt)/2+hm*(Z*at-r*bt)/2)
    sqh=sp.Poly(h,s).sqf_part().as_expr()
    if int(sp.degree(sqh,s))<d:
        reject(prefix+"reject_original_nilpotent_deletion",matrix_polynomial(sqh,dat["A"],s),sp.zeros(d))
        smaller=int(sp.degree(sqh,s))
        reject(prefix+"reject_symmetric_radical_dimension",n,smaller*(smaller+1)//2)
        # The full central nilpotent ladder is retained in the original sum matrix.
        cp=ZM.charpoly()
        sqsum=sp.Poly(cp.as_expr(),cp.gen).sqf_part().as_expr()
        reject(prefix+"reject_sum_nilpotent_deletion",matrix_polynomial(sqsum,ZM,cp.gen),sp.zeros(n))
    if minimum:
        check_minimum(prefix,dat,h,H,P,Be,Bo,alpha,beta,Tsi,Qe,Qo,alpha_literal,beta_literal)
    return dict(name=name,H=str(H),h=str(h),A0=str(A0),A1=str(A1),
                even_dimension=Be.dim,odd_dimension=Bo.dim,
                even_basis=list(map(str,Be.basis)),odd_basis=list(map(str,Bo.basis)),
                original_unscaled_orbits=dat["orbit"],parity_embedding_determinant=str(P.det()))


@lru_cache(None)
def gm(j):
    return sp.S.Zero if j%2 else (sp.S.One if j==0 else sp.factorial2(j-1))


@lru_cache(None)
def mu(i,j):
    t=sp.Symbol("t",real=True)
    p=sp.Poly(sp.expand((HALF-sp.I*t)**i*(HALF+sp.I*t)**j),t)
    return sp.expand(sum(c*gm(k) for (k,),c in p.terms()))


def orbit_terms(i,j): return [(i,j)] if i==j else [(i,j),(j,i)]


def check_minimum(prefix,dat,h,H,P,Be,Bo,alpha,beta,Tsi,Qe,Qo,alpha_literal,beta_literal):
    d=dat["d"]; n=P.rows; D=d//2
    source_degree=2*(d-1)
    source=[(i,j) for i in range(source_degree+1) for j in range(i,source_degree+1) if i+j<=source_degree]
    M=sp.Matrix(len(source),len(source),lambda a,b:2*sp.pi*sum(mu(i,k)*mu(j,l)
          for i,j in orbit_terms(*source[a]) for k,l in orbit_terms(*source[b])))
    powers=[coeffvec(remainder(s**j,h,s),s,d) for j in range(source_degree+1)]
    Jraw=sp.Matrix.hstack(*[dat["L"]*sum((sp.kronecker_product(powers[i],powers[j]) for i,j in orbit_terms(*ij)),sp.zeros(d*d,1)) for ij in source])
    # This unit is a finite algebra input; it does not define the Gaussian density.
    vv=1-(-(s-HALF)**2)/2
    U=mult(vv,h,s)
    U2=dat["L"]*sp.kronecker_product(U,U)*dat["O"]
    record(prefix+"finite_unit_invertible",U2.det()!=0)
    eq(prefix+"finite_unit_reflection",U2*dat["C"],dat["C"]*U2)
    J=U2*Jraw
    K=J*M.inv()*J.conjugate().T; G=K.inv()
    rep=M.inv()*J.conjugate().T*G
    eq(prefix+"minimum_full_source_jet",J*rep,sp.eye(n))
    eq(prefix+"minimum_original_Gram",rep.conjugate().T*M*rep,G)
    for j,kvec in enumerate(J.nullspace()):
        eq(prefix+f"minimum_relation_orthogonality_{j}",kvec.conjugate().T*M*rep,sp.zeros(1,n))
    GG=P.conjugate().T*G*P
    Ge,Go=GG[:Be.dim,:Be.dim],GG[Be.dim:,Be.dim:]
    eq(prefix+"minimum_even_odd_orthogonality",GG,sp.diag(Ge,Go))
    eq(prefix+"minimum_metric_determinant",GG.det(),sp.conjugate(P.det())*P.det()*G.det())
    eq(prefix+"minimum_kernel_determinant",K.det(),P.det()*sp.conjugate(P.det())/(Ge.det()*Go.det()))
    SS=dat["S"]; W=SS.conjugate().T*G+G*SS-2*G
    off=beta.conjugate().T*Go-Ge*alpha
    expected=sp.BlockMatrix([[sp.zeros(Be.dim),off],[off.conjugate().T,sp.zeros(Bo.dim)]]).as_explicit()
    eq(prefix+"minimum_original_weight_block",P.conjugate().T*W*P,expected)
    Gliteral=Tsi.conjugate().T*G*Tsi
    Gel=Qe.conjugate().T*Ge*Qe; Gol=Qo.conjugate().T*Go*Qo
    eq(prefix+"literal_minimum_metric",Gliteral,sp.diag(Gel,Gol))
    eq(prefix+"literal_minimum_determinant",G.det(),Gel.det()*Gol.det())
    offliteral=beta_literal.conjugate().T*Gol-Gel*alpha_literal
    eq(prefix+"literal_original_weight",Tsi.conjugate().T*W*Tsi,
       sp.BlockMatrix([[sp.zeros(Be.dim),offliteral],[offliteral.conjugate().T,sp.zeros(Bo.dim)]]).as_explicit())
    reject(prefix+"reject_beta_adjoint_omission",beta.conjugate().T*Go,sp.zeros(Be.dim,Bo.dim))
    reject(prefix+"reject_original_weight_one",SS.conjugate().T*G+G*SS-G,W)
    eq(prefix+"minimum_weight_rank",W.rank(),2*off.rank())
    record(prefix+"minimum_weight_zero_multiplicity",len(W.nullspace())>=D)
    smaller=Go.inv()*off.conjugate().T*Ge.inv()*off
    cp=(G.inv()*W).charpoly(); cp2=smaller.charpoly()
    eq(prefix+"minimum_full_relative_characteristic",cp.as_expr(),cp.gen**D*cp2.as_expr().subs(cp2.gen,cp.gen**2))
    reject(prefix+"reject_dividing_orbit_sums_by_two",dat["O"].T*dat["O"],sp.eye(n))


def coupled_gaussian_norms():
    def variance_two(j): return 2**j*gm(2*j)
    relative=sp.Matrix(3,3,lambda a,c:(-1)**(a+c)*variance_two(a+c))
    eq("Gaussian:relative_weight_C",relative,sp.Matrix([[1,-2,12],[-2,12,-120],[12,-120,1680]]))
    for a in range(4):
        for c in range(4):
            l=a+c
            # Exact v integration in 1/2 exp(-(u²+v²)/4), including its Jacobian.
            integrated=(-1)**l*sp.Rational(1,2)*2**(2*l+1)*sp.gamma(sp.Rational(2*l+1,2))
            eq(f"Gaussian:conditional_matrix_entry_{a}_{c}",integrated,sp.sqrt(sp.pi)*(-1)**l*variance_two(l))
    triangular=sp.Matrix([[1,2,12],[0,1,12],[0,0,1]])
    eq("Gaussian:unscaled_relative_diagonalization",triangular.T*relative*triangular,sp.diag(1,8,384))
    for j in range(8):
        pushed=sp.sqrt(sp.pi)*4**(sp.Rational(1,2)+j)*sp.gamma(sp.Rational(1,2)+j)
        eq(f"Gaussian:half_line_Jacobian_moment_{j}",pushed,2*sp.pi*variance_two(j))
        reject(f"Gaussian:reject_extra_half_Jacobian_{j}",pushed/2,2*sp.pi*variance_two(j))
    for Mdegree in (0,1,2,3,4,5,6):
        original=[(i,j) for i in range(Mdegree+1) for j in range(i,Mdegree+1) if i+j<=Mdegree]
        new=[(par,a,b) for par in (0,1) for a in range(Mdegree//2+1) for b in range(Mdegree//2+1) if 2*a+2*b+par<=Mdegree]
        eq(f"Gaussian:M{Mdegree}:full_degree_count",len(new),len(original))
        polys=[sp.expand((s1+s2-1)**par*((s1-s2)**2)**a*(-(s1+s2-1)**2)**b) for par,a,b in new]
        T=sp.Matrix([[sp.Poly(p,s1,s2).coeff_monomial(s1**i*s2**j) for p in polys] for i,j in original])
        record(f"Gaussian:M{Mdegree}:full_filtered_coordinate_map",T.det()!=0,determinant=str(T.det()))
        for col,p in enumerate(polys):
            rebuilt=sum(T[j,col]*sum((s1**a*s2**b for a,b in orbit_terms(*ij)),sp.S.Zero) for j,ij in enumerate(original))
            eq(f"Gaussian:M{Mdegree}:unscaled_reconstruction_{col}",rebuilt,p)
        original_gram=sp.Matrix(len(original),len(original),lambda a,b:2*sp.pi*sum(mu(i,k)*mu(j,l)
              for i,j in orbit_terms(*original[a]) for k,l in orbit_terms(*original[b])))
        def projected(i,j):
            p,a,b=new[i];q,c,e=new[j]
            if p!=q: return sp.S.Zero
            return 2*sp.pi*(-1)**(a+c)*variance_two(a+c)*variance_two(b+e+p)
        pushed_gram=sp.Matrix(len(new),len(new),projected)
        eq(f"Gaussian:M{Mdegree}:direct_vs_matrix_parity_norm",T.conjugate().T*original_gram*T,pushed_gram)
        if Mdegree>=1:
            reject(f"Gaussian:M{Mdegree}:reject_missing_parity_x",pushed_gram,
                   sp.Matrix(len(new),len(new),lambda i,j:0 if new[i][0]!=new[j][0] else
                   2*sp.pi*(-1)**(new[i][1]+new[j][1])*variance_two(new[i][1]+new[j][1])*variance_two(new[i][2]+new[j][2])))
        if Mdegree>=2:
            reject(f"Gaussian:M{Mdegree}:reject_scalar_only_observation",relative[:2,:2],sp.diag(1,0))
    original_mass=(2**HALF*sp.gamma(HALF))**2
    pushed_mass=sp.sqrt(sp.pi)*4**HALF*sp.gamma(HALF)
    eq("Gaussian:full_two_variable_mass",original_mass,pushed_mass)


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--output",type=Path,required=True)
    ap.add_argument("--self-test-failure",action="store_true")
    args=ap.parse_args(); models=[];error=None
    try:
        coupled_gaussian_norms()
        models.append(algebra_model("simple_positive",y-1,minimum=True))
        models.append(algebra_model("central_length_two",y))
        models.append(algebra_model("simple_mixed",(y+1)*(y-sp.Rational(1,4)),minimum=True))
        models.append(algebra_model("repeated_off_line",(y+1)**2,minimum=True))
        models.append(algebra_model("central_length_four",y**2))
        models.append(algebra_model("repeated_and_positive",(y+1)**2*(y-sp.Rational(1,4))))
        if args.self_test_failure:
            record("intentional_false_identity",sp.Rational(1,2)==1,kind="harness_negative_control")
    except Exception as exc:
        error=f"{type(exc).__name__}: {exc}"
    source=ROOT/"tex"/"spectral_sum_stieltjes_pair.tex"
    pr=ROOT/"sources/web_pr17_spectral_sum/workbenches/tau-spectral-sum/RESEARCH_NOTE.md"
    output=dict(created_utc=datetime.now(timezone.utc).isoformat(),
          scope="Full finite symmetric-square quotient and original unscaled orbit coordinates; exact coupled Gaussian norm pushforward with mass2*pi. No arithmetic theta-moment enclosure, RH proof, or Lean execution.",
          model_coupling_scope="The matrix-weight/half-line norm uses one coherent declared Gaussian density in every coordinate. The separate constrained-minimum fixtures prescribe their even residue unit independently of that Gaussian density and do not test the actual analytic theta-unit coupling.",
          python_version=sys.version,optimization_level=sys.flags.optimize,sympy_version=sp.__version__,
          checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
          source_sha256=hashlib.sha256(source.read_bytes()).hexdigest() if source.exists() else None,
          pr17_source_sha256=hashlib.sha256(pr.read_bytes()).hexdigest(),
          total=len(RECORDS),passed=sum(q["passed"] for q in RECORDS),
          exact_checks=sum(q["kind"]=="exact" for q in RECORDS),
          negative_controls=sum(q["kind"]=="negative_control" for q in RECORDS),
          all_passed=error is None and all(q["passed"] for q in RECORDS),error=error,models=models,records=RECORDS)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(output,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({k:output[k] for k in ("total","passed","exact_checks","negative_controls","all_passed","error")},sort_keys=True))
    return 0 if output["all_passed"] else 1


if __name__=="__main__":
    raise SystemExit(main())
