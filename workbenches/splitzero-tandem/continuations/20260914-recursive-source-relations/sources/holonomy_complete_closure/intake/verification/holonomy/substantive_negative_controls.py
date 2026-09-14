"""Separate formula mutations for the new holonomy target only.

If a deliberately false equality unexpectedly passes, main returns zero.
There is no unconditional failure or startup-refusal guard.
"""
from __future__ import annotations
import argparse
import json
import sympy as s

def exact(x):
    return s.cancel(s.expand(x))

def matrix_exact(M):
    return M.applyfunc(exact)

def zero(x):
    return all(exact(v)==0 for v in x) if isinstance(x,s.MatrixBase) else exact(x)==0

def baseline_equal(a,b,label):
    if not zero(a-b):
        raise ArithmeticError('BASELINE_FAILED:'+label)

def encode(x):
    if isinstance(x,s.MatrixBase):
        return [[s.sstr(exact(x[i,j])) for j in range(x.cols)] for i in range(x.rows)]
    if isinstance(x,dict):
        return {k:encode(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)):
        return [encode(v) for v in x]
    return str(x)

def emit(name,evidence):
    print(json.dumps({'control':name,'evidence':encode(evidence)},indent=2),flush=True)

def mutation_equal(name,a,b):
    difference=a-b
    if not zero(difference):
        raise ArithmeticError('MUTATION_REJECTED:'+name+': '+str(difference))

def quotient(M,J):
    G=matrix_exact((J*M.inv()*J.H).inv())
    C=matrix_exact(M.inv()*J.H*G)
    return G,C

def erase_variance():
    name='erase-variance'
    eta=s.Rational(1,3)
    M=7*s.eye(2)
    J=s.Matrix([[1,0]])
    boundary=s.Matrix([0,1])
    phases=[7*s.Matrix([[1,sign*eta],[sign*eta,1]]) for sign in [1,-1]]
    G,C=quotient(M,J)
    records=[quotient(Mj,J) for Mj in phases]
    mean_quotient=matrix_exact(sum((Gj for Gj,Cj in records),s.zeros(1))/2)
    variance=matrix_exact(sum(((C-Cj).H*Mj*(C-Cj) for Mj,(Gj,Cj) in zip(phases,records)),s.zeros(1))/2)
    baseline_equal(sum(phases,s.zeros(2))/2,M,'literal phase source mean')
    baseline_equal(G,mean_quotient+variance,'complete quotient-mean variance identity')
    for Mj,(Gj,Cj) in zip(phases,records):
        X=(boundary.H*Mj*boundary).inv()*boundary.H*Mj*C
        baseline_equal(C-Cj,boundary*X,'actual original boundary-column difference')
    emit(name,{'eta':eta,'M':M,'J':J,'boundary':boundary,'phase_source_grams':phases,
               'canonical_lift':C,'phase_lifts':[Cj for Gj,Cj in records],
               'G':G,'mean_phase_quotient':mean_quotient,'variance':variance,
               'mutated_rhs_with_variance_erased':mean_quotient,'exact_residual':G-mean_quotient})
    mutation_equal(name,G,mean_quotient)

def support_is_absence():
    name='support-is-absence'
    tau=('absent',)
    source=('ell',s.Integer(7))
    source_zero=('ell',s.Integer(0))
    linear_map=s.zeros(1)
    def supported_lift(x):
        if x==tau:
            return tau
        return (x[0],(linear_map*s.Matrix([x[1]]))[0])
    def mutated_lift(x):
        image=supported_lift(x)
        if image!=tau and image[1]==0:
            return tau
        return image
    expected=supported_lift(source)
    actual=mutated_lift(source)
    if supported_lift(tau)!=tau or expected!=source_zero:
        raise ArithmeticError('BASELINE_FAILED:actual supported lift')
    emit(name,{'coefficient_linear_map':linear_map,'source_element':source,
               'external_absence':tau,'correct_supported_image':expected,
               'correct_supported_zero_image':supported_lift(source_zero),
               'correct_absence_image':supported_lift(tau),'mutated_image':actual,
               'mutation':'collapse a computed supported coefficient zero to external absence'})
    if actual!=expected:
        raise ArithmeticError('MUTATION_REJECTED:'+name+': computed supported zero was replaced by external absence')

def omit_fourier_factor():
    name='omit-fourier-factor'
    m=s.Integer(2)
    character_matrix=s.Matrix([[1,1],[1,-1]])
    correct=character_matrix/s.sqrt(m)
    vector=s.Matrix([s.Rational(1,3),s.Rational(2,3)+s.I/7])
    baseline_equal(correct.H*correct,s.eye(2),'Fourier isometry with retained sqrt(m)')
    baseline_equal(correct.H*(correct*vector),vector,'Fourier inverse with retained sqrt(m)')
    mutated=character_matrix
    actual=matrix_exact(mutated.H*mutated)
    emit(name,{'cover_degree':m,'character_matrix':character_matrix,'correct_fourier_matrix':correct,
               'source_vector':vector,'correct_roundtrip':matrix_exact(correct.H*(correct*vector)),
               'mutated_unscaled_matrix':mutated,'mutated_gram':actual,
               'expected_gram':s.eye(2),'exact_residual':actual-s.eye(2)})
    mutation_equal(name,actual,s.eye(2))

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--negative',required=True,choices=['erase-variance','support-is-absence','omit-fourier-factor'])
    args=parser.parse_args()
    controls={'erase-variance':erase_variance,'support-is-absence':support_is_absence,'omit-fourier-factor':omit_fourier_factor}
    controls[args.negative]()
    return 0

if __name__=='__main__':
    raise SystemExit(main())
