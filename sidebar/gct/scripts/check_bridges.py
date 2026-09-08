"""Exact replay of new conic, specialization, spectral and verifier maps."""
from pathlib import Path
import json, hashlib, itertools, datetime
import sympy as s

ROOT=Path(__file__).resolve().parents[1]
results=[]
def check(name, condition):
    ok=bool(condition)
    results.append({"name":name,"passed":ok})
    if not ok:
        raise AssertionError(name)
def zero(expr):
    return s.cancel(s.expand(expr))==0
def matrix_zero(M):
    return all(zero(v) for v in M)

a,q,p,r,t,lam=s.symbols('a q p r t lam')
sp=s.symbols('s')
C=q**10-q**4-q**(-4)+q**(-10)
def qinteger(n):
    return sum(q**(n-1-2*j) for j in range(n))
check("source_coefficient_quotient",
 zero(C*(q+1/q) - (qinteger(6)*(qinteger(7)-qinteger(3))-qinteger(3)*qinteger(8))))
check("source_coefficient_factor",zero(C-(q-1/q)**2*qinteger(7)*qinteger(3)))
check("conic_relation",zero((q+1/q)**2-(q-1/q)**2-4))
Ca=-a*(7-14*a+7*a**2-a**3)*(3-a)
check("coefficient_in_original_a",zero(C-Ca.subs(a,-(q-1/q)**2)))
check("source_second_jet",s.diff(C,q,2).subs(q,1)==168)
check("source_base_first_jet",s.diff(Ca,a).subs(a,0)==-21)
q0=(s.sqrt(14)+s.I*s.sqrt(2))/4
check("circle_character_unit",s.expand_complex(q0*s.conjugate(q0))==1)
check("circle_character_a",s.simplify(-(q0-1/q0)**2)==s.Rational(1,2))
check("circle_character_C",Ca.subs(a,s.Rational(1,2))==-s.Rational(65,32))
rq=q-1/q; pq=q+1/q
Dcoef=-q/(rq*pq)
check("heat_lift_r",zero(Dcoef*s.diff(rq,q)+1/rq))
check("heat_lift_p",zero(Dcoef*s.diff(pq,q)+1/pq))
check("heat_lift_a",zero(Dcoef*s.diff(-rq**2,q)-2))
check("heat_source_coefficient",zero(Dcoef*s.diff(C,q)-2*s.diff(Ca,a).subs(a,-rq**2)))
check("heat_source_x",zero(s.diff(-1/(2*r),r)*(-1/r)+1/(2*r**3)))
check("heat_source_y",zero(s.diff(3*r,r)*(-1/r)+3/r))
check("heat_source_w",zero(s.diff(26*r*r,r)*(-1/r)+52))
check("qinteger7_trace",zero(qinteger(7)-((q+1/q)**6-5*(q+1/q)**4+6*(q+1/q)**2-1)))

K=s.Matrix([[0,0,0,-1],[1,0,0,0],[0,1,0,2-2*sp],[0,0,1,0]])
I=s.eye(4)
Ki=-K**3+(2-2*sp)*K
R=K-Ki
P=K+Ki
check("quartic_relation",matrix_zero(K**4+(2*sp-2)*K**2+I))
check("quartic_inverse_both",matrix_zero(K*Ki-I) and matrix_zero(Ki*K-I))
check("root_coordinate_R_squared",matrix_zero(R**2+2*sp*I))
check("trace_coordinate_P_squared",matrix_zero(P**2-(4-2*sp)*I))
check("quartic_characteristic",zero(K.charpoly(lam).as_expr()-(lam**4+(2*sp-2)*lam**2+1)))
check("coefficient_operator",matrix_zero(K**10-K**4-Ki**4+Ki**10-Ca.subs(a,2*sp)*I))
T=s.Matrix([[1,0,0,2*sp-2],[0,2*sp-1,3-2*sp,0],[0,0,0,2],[0,1,-1,0]])
check("alternative_basis_unit_determinant",T.det()==4)
Rtwo=s.diag(s.Matrix([[0,-2*sp],[1,0]]),s.Matrix([[0,-2*sp],[1,0]]))
check("alternative_basis_two_sheet_matrix",matrix_zero(R*T-T*Rtwo))

u,v=s.symbols('u v')
special=s.diag(1,1,1,-a)
check("specialization_rank_generic",special.det()==-a)
check("specialization_rank_zero",special.subs(a,0).rank()==3)
check("Tor_connecting_sign",zero(a*(-1)-(-a)))
root=s.Matrix([[0,-a],[1,0]])
R1=s.kronecker_product(root,s.eye(2))
R2=s.kronecker_product(s.eye(2),root)
check("node_regular_representation_relations",
 matrix_zero(R1*R2-R2*R1) and matrix_zero(R1**2+a*I) and matrix_zero(R2**2+a*I))
check("node_special_top_layer_nonzero",any(v!=0 for v in (R1*R2).subs(a,0)))
for prime in [3,5,7,11]:
    count=sum((i*i-j*j)%prime==0 for i in range(prime) for j in range(prime))
    punctured=sum((i*i-j*j)%prime==0 and i*j%prime!=0 for i in range(prime) for j in range(prime))
    check(f"node_count_F{prime}",count==2*prime-1)
    check(f"punctured_node_count_F{prime}",punctured==2*(prime-1))

for d in [1,2,3]:
    variables=s.symbols(f'a0:{d*d}')
    A=s.Matrix(d,d,variables)
    M=s.BlockMatrix([[s.zeros(d),-2*A],[s.eye(d),s.zeros(d)]]).as_explicit()
    check(f"characteristic_pullback_d{d}",zero(M.charpoly(lam).as_expr()-(lam**2*s.eye(d)+2*A).det()))

# Exhaustive small Boolean witnesses; literal tuples use (index,positive).
for n in [1,2]:
    literals=list(itertools.product(range(n),[False,True]))
    clauses=list(itertools.product(literals,repeat=3))
    formulas=((cl,) for cl in clauses) if n==2 else itertools.product(clauses,repeat=2)
    for number,formula in enumerate(formulas):
        direct=0; arithmetic=0
        for bits in itertools.product([0,1],repeat=n):
            direct+=all(any(bool(bits[i])==positive for i,positive in cl) for cl in formula)
            truth=1
            for cl in formula:
                complement=1
                for i,positive in cl:
                    literal=bits[i] if positive else 1-bits[i]
                    complement*=1-literal
                truth*=1-complement
            arithmetic+=truth
        check(f"Boolean_arithmetization_n{n}_{number}",direct==arithmetic)
        check(f"Boolean_modulus_n{n}_{number}",arithmetic%(2**(n+1))==direct)

# Full material drift and original Euclidean diffusion from the new parent source.
x,y,w,b,c=s.symbols('x y w b c')
vv=1+x*y
F1=vv**3*w+y*y*vv*(4+3*x*y)
F2=y+3*x*vv**2*w+3*x*y*y*(4+3*x*y)
F3=2*x-3*x*x*y-x**3*w
s_original=F1/2
gradient=s.Matrix([s.diff(s_original,z) for z in (x,y,w)])
display_gradient=s.Matrix([(3*y*vv**2*w+y**3*(1+6*vv))/2,
 (3*x*vv**2*w+2*y*(vv+3*vv**2)+x*y*y*(1+6*vv))/2,vv**3/2])
check('material_gradient_full',matrix_zero(gradient-display_gradient))
laplace=sum(s.diff(s_original,z,2) for z in (x,y,w))
display_laplace=3*w*vv*(x*x+y*y)+18*x*x*y*y+21*x*y+3*y**4+4
check('material_Laplacian_full',zero(laplace-display_laplace))
JF=s.Matrix([F1,F2,F3]).jacobian([x,y,w])
U=s.expand(-s.Rational(1,2)*JF.adjugate()*s.Matrix([2,6*F3,0]))
check('material_full_target_drift',matrix_zero(JF*U-s.Matrix([2,6*F3,0])))
check('material_Us',zero((gradient.T*U)[0]-1))
PP=c*r**3-2*r*r+b*r-4*sp
Pr=s.diff(PP,r)
check('material_full_root_lift',zero(s.diff(PP,sp)+6*c*s.diff(PP,b)+(4-6*c*r)))
for index,point,want_A,want_B in [(1,{x:1,y:-s.Rational(3,2),w:s.Rational(13,2)},s.Rational(121,1024),-s.Rational(7,2)),
 (0,{x:0,y:0,w:-s.Rational(1,4)},s.Rational(1,4),4)]:
    check(f'material_same_F_fibre_{index}',[f.subs(point) for f in [F1,F2,F3]]==[-s.Rational(1,4),0,0])
    check(f'material_diffusion_A_{index}',sum(g.subs(point)**2 for g in gradient)==want_A)
    check(f'material_diffusion_B_{index}',laplace.subs(point)==want_B)

receipt={"schema_version":1,"timestamp_utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),
 "arithmetic":"exact symbolic rational/polynomial plus exhaustive finite sets",
 "sympy_version":s.__version__,"Lean_used":False,"checks":results,
 "all_passed":all(x['passed'] for x in results),
 "source_hashes":{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()
  for p in [Path(__file__),ROOT/'tex/specialization_spectral.tex',ROOT/'tex/conic_arithmetic_bridge.tex',ROOT/'tex/boolean_reduction.tex',ROOT/'tex/material_generator_interface.tex']}}
(ROOT/'checks/root_bridges.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
print(json.dumps({"passed":len(results),"all_passed":receipt['all_passed']}))
