"""Exact original-measure Gram/quotient replay of TC1--13 and its P/Q link.

The positive Gaussian measure has its literal mass mu and variance sigma^2.
The quotient roots are declared calibration coefficients, not arithmetic zeros.
No Lean or numerical quadrature is used. Fault modes deliberately corrupt one
sign/factor comparison while running the complete same collection of checks.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import platform
import sys
import sympy as sp

MU, SIGMA = sp.symbols('mu sigma', positive=True)
S, U, THETA = sp.symbols('S u theta', real=True)
C = sp.Rational(1, 2)
X = S - C
CHI = X**2 - SIGMA**2
I = sp.I
CHECKS = []
FAULT = 'none'


def exact(value):
    if isinstance(value, sp.MatrixBase):
        return value.applyfunc(lambda x: sp.cancel(sp.expand(x)))
    return sp.cancel(sp.expand(value))


def equal(name, actual, expected):
    residual = exact(actual - expected)
    passed = all(x == 0 for x in residual) if isinstance(residual, sp.MatrixBase) else residual == 0
    CHECKS.append({'name': name, 'passed': bool(passed), 'residual': encode(residual)})


def different(name, actual, wrong):
    residual = exact(actual - wrong)
    passed = any(x != 0 for x in residual) if isinstance(residual, sp.MatrixBase) else residual != 0
    CHECKS.append({'name': name, 'passed': bool(passed), 'nonzero_residual': encode(residual)})


def encode(value):
    if isinstance(value, sp.MatrixBase):
        return [[str(exact(value[r, c])) for c in range(value.cols)] for r in range(value.rows)]
    if isinstance(value, list):
        return [encode(item) for item in value]
    return str(exact(value))


def moment(j):
    if j % 2:
        return sp.Integer(0)
    return MU * sp.factorial(j) * SIGMA**j / (2**(j//2) * sp.factorial(j//2))


TILTED = [MU * sp.exp(SIGMA**2 * THETA**2 / 2)]
for _ in range(10):
    TILTED.append(sp.diff(TILTED[-1], THETA))


def integrate_u(polynomial, tilted=False, derivative_at_zero=False):
    values = TILTED if tilted else None
    answer = 0
    for (j,), coefficient in sp.Poly(sp.expand(polynomial), U).terms():
        answer += coefficient * (values[j] if tilted else moment(j + int(derivative_at_zero)))
    return exact(answer)


def inner(left, right, **kwargs):
    left_line = left.subs(S, C + I*U)
    right_line = right.subs(S, C + I*U)
    return integrate_u(sp.conjugate(left_line)*right_line, **kwargs)


def gram(polynomials, **kwargs):
    return sp.Matrix(len(polynomials), len(polynomials),
                     lambda r, c: inner(polynomials[r], polynomials[c], **kwargs))


def quotient_column(polynomial):
    remainder = sp.Poly(sp.rem(sp.expand(polynomial), sp.expand(CHI), S), S)
    return sp.Matrix([remainder.nth(j) for j in range(2)])


def coefficient_column(polynomial, count):
    p = sp.Poly(sp.expand(polynomial), S)
    return sp.Matrix([p.nth(j) for j in range(count)])


def main():
    global FAULT
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--fault', choices=['none', 'wrong-phase-sign', 'wrong-boundary-factor', 'wrong-toda-loss-sign'], default='none')
    args = parser.parse_args()
    FAULT = args.fault
    equal('TC1/c-original', C, sp.Rational(1,2))
    equal('TC1/literal-mass', moment(0), MU)
    for j in range(1, 5):
        equal(f'TC3/Gaussian-moment-recurrence-{2*j}', moment(2*j), (2*j-1)*SIGMA**2*moment(2*j-2))
        equal(f'TC3/Gaussian-odd-moment-{2*j-1}', moment(2*j-1), sp.Integer(0))

    # Derive all maps from literal reduction in the original (1,S) basis.
    L = sp.Matrix.hstack(quotient_column(sp.Integer(1)), quotient_column(X))
    AS = sp.Matrix.hstack(quotient_column(S), quotient_column(S**2))
    AX = exact(L.inv()*AS*L)
    equal('TC2/original-coefficient-transform', L, sp.Matrix([[1,-C],[0,1]]))
    equal('TC2/original-S-action', AS, sp.Matrix([[0,SIGMA**2-C**2],[1,2*C]]))
    equal('TC2/S-action-in-x-basis', AX, sp.Matrix([[C,SIGMA**2],[1,C]]))
    equal('TC2/intertwiner', AS*L, L*AX)
    equal('TC2/determinant-one', L.det(), sp.Integer(1))
    equal('TC2/x-action-polynomial', (AX-C*sp.eye(2))**2, SIGMA**2*sp.eye(2))

    # Gram--Schmidt starts from original S powers and the integral above.
    polynomials, norms = [], []
    for j in range(4):
        p = S**j
        for old, norm in zip(polynomials, norms):
            p -= old * inner(old, p) / norm
        p = exact(p)
        polynomials.append(p)
        norms.append(inner(p, p))
    claimed = [sp.Integer(1), X, X**2+SIGMA**2, X**3+3*SIGMA**2*X]
    claimed_norms = [MU, MU*SIGMA**2, 2*MU*SIGMA**4, 6*MU*SIGMA**6]
    for j in range(4):
        equal(f'TC3/derived-monic-polynomial-{j}', polynomials[j], claimed[j])
        equal(f'TC3/derived-full-norm-{j}', norms[j], claimed_norms[j])
        equal(f'TC3/leading-coefficient-{j}', sp.Poly(polynomials[j],S).LC(), sp.Integer(1))
        for ell in range(j):
            equal(f'TC3/direct-orthogonality-{ell}-{j}', inner(polynomials[ell],polynomials[j]), sp.Integer(0))
    phase2 = U**2-SIGMA**2 if FAULT == 'wrong-phase-sign' else -(U**2-SIGMA**2)
    equal('TC3/literal-p2-vertical-phase', polynomials[2].subs(S,C+I*U), phase2)
    equal('TC3/literal-p3-vertical-phase', polynomials[3].subs(S,C+I*U), -I*(U**3-3*SIGMA**2*U))
    bx = [exact(L.inv()*quotient_column(p)) for p in polynomials]
    expected_b = [sp.Matrix([1,0]), sp.Matrix([0,1]), sp.Matrix([2*SIGMA**2,0]), sp.Matrix([0,4*SIGMA**2])]
    for j in range(4):
        equal(f'TC4/original-reduction-column-{j}', bx[j], expected_b[j])

    expected_g = {1: sp.diag(MU,MU*SIGMA**2), 2: sp.diag(MU/3,MU*SIGMA**2),
                  3: sp.diag(MU/3,3*MU*SIGMA**2/11)}
    degrees = {}
    metrics, original_metrics, kernels, volumes, operators = {}, {}, {}, {}, {}
    for N in (1,2,3):
        source_basis = [S**j for j in range(N+1)]
        H = gram(source_basis)
        B = sp.Matrix.hstack(*(quotient_column(p) for p in source_basis))
        KS = exact(B*H.inv()*B.H)
        GS = exact(KS.inv())
        GX = exact(L.H*GS*L)
        KX = exact(GX.inv())
        right_inverse = exact(H.inv()*B.H*GS)
        equal(f'TC5/N{N}/actual-right-inverse', B*right_inverse, sp.eye(2))
        equal(f'TC5/N{N}/original-minimum-Gram', right_inverse.H*H*right_inverse, GS)
        equal(f'TC5/N{N}/original-coefficient-adjoint', H*right_inverse, B.H*GS)
        equal(f'TC5/N{N}/full-x-metric', GX, expected_g[N])
        equal(f'TC5/N{N}/kernel-coordinate-transport', KS, L*KX*L.H)
        equal(f'TC5/N{N}/Gram-coordinate-transport', GS, L.inv().H*GX*L.inv())
        orthogonal_K = sum((bx[j]*bx[j].H/norms[j] for j in range(N+1)), sp.zeros(2))
        equal(f'TC5/N{N}/two-independent-kernel-constructions', KX, orthogonal_K)
        V = exact(GS.det())
        equal(f'TC5/N{N}/determinant-coordinate-invariance', V, GX.det())
        equal(f'TC5/N{N}/claimed-volume', V, MU**2*SIGMA**2/{1:1,2:3,3:11}[N])
        equal(f'TC6/N{N}/source-Hankel-determinant', H.det(), sp.prod(norms[:N+1]))
        relation_basis = [CHI*S**j for j in range(N-1)]
        relation_gram = gram(relation_basis)
        relation_det = relation_gram.det()  # SymPy retains det of the 0-by-0 matrix as 1.
        if relation_basis:
            relation_coefficients = sp.Matrix.hstack(*(coefficient_column(p,N+1) for p in relation_basis))
            equal(f'TC6/N{N}/literal-relation-kernel', B*relation_coefficients, sp.zeros(2,N-1))
            equal(f'TC6/N{N}/minimum-orthogonal-to-full-kernel', relation_coefficients.H*H*right_inverse, sp.zeros(N-1,2))
        equal(f'TC6/N{N}/source-relation-volume-ratio', H.det()/relation_det, V)
        operator = exact(AX+GX.inv()*AX.H*GX-2*C*sp.eye(2))
        equal(f'TC7/N{N}/original-metric-self-adjointness', GX*operator, operator.H*GX)
        metrics[N], kernels[N], volumes[N], operators[N] = GX, KX, V, operator
        original_metrics[N] = GS
        degrees[N] = {'original_source_Gram':encode(H), 'original_quotient_matrix':encode(B),
                      'original_minimum_coefficient_matrix':encode(right_inverse),
                      'K_S':encode(KS), 'G_S':encode(GS), 'K_x':encode(KX), 'G_x':encode(GX),
                      'volume':encode(V), 'source_determinant':encode(H.det()),
                      'original_relation_Gram':encode(relation_gram), 'relation_determinant':encode(relation_det),
                      'actual_defect_operator':encode(operator)}
        # Exact tilted parity transport, retaining original S powers.
        n = N+1
        real_H = sp.Matrix(n,n,lambda r,s: TILTED[r+s])
        parity = sp.diag(*[(-1)**j for j in range(n)])
        equal(f'TC-phase/N{N}/u-Hankel-parity-congruence', real_H.subs(THETA,-THETA), parity*real_H*parity)
        transform = sp.Matrix(n,n,lambda r,j: sp.binomial(j,r)*C**(j-r)*I**r if r<=j else 0)
        equal(f'TC-phase/N{N}/S-u-determinant-modulus', transform.det()*sp.conjugate(transform.det()), sp.Integer(1))
        for j in range(n):
            equal(f'TC-phase/N{N}/literal-S-u-column-{j}', sum(transform[r,j]*U**r for r in range(n)), (C+I*U)**j)
        equal(f'TC-phase/N{N}/S-u-full-Gram-congruence', gram(source_basis,tilted=True), transform.H*real_H*transform)
        relation_n = N-1
        real_B = sp.Matrix(relation_n,relation_n,lambda r,s: TILTED[r+s+4]+2*SIGMA**2*TILTED[r+s+2]+SIGMA**4*TILTED[r+s])
        relation_parity = sp.diag(*[(-1)**j for j in range(relation_n)])
        equal(f'TC-phase/N{N}/relation-Hankel-parity', real_B.subs(THETA,-THETA), relation_parity*real_B*relation_parity)
        source_log_derivative = sp.trace(H.inv()*gram(source_basis,derivative_at_zero=True))
        relation_log_derivative = sp.trace(relation_gram.inv()*gram(relation_basis,derivative_at_zero=True)) if relation_n else sp.Integer(0)
        equal(f'TC-phase/N{N}/source-log-derivative-zero', source_log_derivative, sp.Integer(0))
        equal(f'TC-phase/N{N}/relation-log-derivative-zero', relation_log_derivative, sp.Integer(0))
        equal(f'TC-phase/N{N}/volume-log-derivative-zero', source_log_derivative-relation_log_derivative, sp.Integer(0))
        degrees[N]['tilted_source_basis_transform_S_to_u'] = encode(transform)
        degrees[N]['volume_log_derivative_at_zero'] = encode(source_log_derivative-relation_log_derivative)

    equal('TC6/vertical-relation-sign', CHI.subs(S,C+I*U), -(U**2+SIGMA**2))
    relation_centered_gram = gram([CHI,CHI*X])
    equal('TC6/complete-centered-relation-Gram', relation_centered_gram, sp.diag(6*MU*SIGMA**4,22*MU*SIGMA**6))
    relation_shift = sp.Matrix([[1,C],[0,1]])
    equal('TC6/original-relation-basis-transform', gram([CHI,CHI*S]), relation_shift.H*relation_centered_gram*relation_shift)
    equal('TC7/H1', operators[1], sp.Matrix([[0,2*SIGMA**2],[2,0]]))
    equal('TC7/H2', operators[2], sp.Matrix([[0,4*SIGMA**2],[sp.Rational(4,3),0]]))
    epsilon = {}
    for N in (1,2):
        epsilon[N] = exact(sp.trace(operators[N]**2)/2)
        equal(f'TC7/N{N}/squared-operator', operators[N]**2, epsilon[N]*sp.eye(2))
        boundary = (bx[N+1]*bx[N].H+bx[N]*bx[N+1].H)/norms[N]
        factor = sp.Rational(1,2) if FAULT == 'wrong-boundary-factor' and N == 2 else sp.Integer(1)
        equal(f'TC7/N{N}/rank-two-kernel-identity', AX*kernels[N]+kernels[N]*AX.H-2*C*kernels[N], factor*boundary)
        cross = exact((bx[N].H*metrics[N]*bx[N+1])[0]/norms[N])
        equal(f'TC-phase/N{N}/original-imaginary-cross-zero', cross, sp.Integer(0))
    equal('TC7/epsilon1-square', epsilon[1], 4*SIGMA**2)
    equal('TC7/epsilon2-square', epsilon[2], sp.Rational(16,3)*SIGMA**2)
    equal('TC-phase/spectral-phase-zero', sp.trace((AX-C*sp.eye(2))/I), sp.Integer(0))

    delta2, delta3 = exact(volumes[2]/volumes[1]), exact(volumes[3]/volumes[2])
    a3 = exact(norms[3]/norms[2])
    R2 = exact(volumes[1]/volumes[3])
    equal('TC8/delta2', delta2, sp.Rational(1,3))
    equal('TC8/delta3', delta3, sp.Rational(3,11))
    equal('TC8/a3', a3, 3*SIGMA**2)
    equal('TC8/R2', R2, sp.Integer(11))
    equal('TC8/R2-from-two-deltas', R2, 1/(delta2*delta3))
    exact_toda = exact(a3*(1-delta2)*(1/delta3-1))
    upper_toda = exact(a3*(R2-1)**2/(4*R2))
    exp_t = sp.sqrt(delta2/delta3)
    cosh_s = (sp.sqrt(R2)+1/sp.sqrt(R2))/2
    loss = exact(a3*(exp_t-cosh_s)**2)
    equal('TC9/actual-operator-equals-exact-Toda', epsilon[2], exact_toda)
    equal('TC9/upper-expression', upper_toda, sp.Rational(75,11)*SIGMA**2)
    equal('TC10/exp-t', exp_t, sp.sqrt(11)/3)
    equal('TC10/cosh-s', cosh_s, 6/sp.sqrt(11))
    equal('TC10/full-imbalance-square', loss, sp.Rational(49,33)*SIGMA**2)
    retained = upper_toda+loss if FAULT == 'wrong-toda-loss-sign' else upper_toda-loss
    equal('TC10/upper-minus-retained-square', epsilon[2], retained)

    # Exact link to E35--36 and the full P/Q coupling maps in original metric.
    vp, vm = sp.Matrix([SIGMA,1]), sp.Matrix([-SIGMA,1])
    equal('E-link/positive-eigenvector', AX*vp, (C+SIGMA)*vp)
    equal('E-link/negative-eigenvector', AX*vm, (C-SIGMA)*vm)
    P = exact(vp*(vp.H*metrics[2])/((vp.H*metrics[2]*vp)[0]))
    Q = exact((AX-(C-SIGMA)*sp.eye(2))/(2*SIGMA))
    w = sp.Matrix([-3*SIGMA,1])
    equal('TC12/P-explicit-matrix', P, sp.Matrix([[sp.Rational(1,4),3*SIGMA/4],[1/(4*SIGMA),sp.Rational(3,4)]]))
    equal('TC12/Q-explicit-matrix', Q, sp.Matrix([[sp.Rational(1,2),SIGMA/2],[1/(2*SIGMA),sp.Rational(1,2)]]))
    equal('E-link/N1-eigenvector-orthogonality', (vp.H*metrics[1]*vm)[0], sp.Integer(0))
    equal('E-link/N2-eigenvector-inner-product', (vp.H*metrics[2]*vm)[0], 2*MU*SIGMA**2/3)
    equal('TC12/orthogonal-kernel-vector', P*w, sp.zeros(2,1))
    equal('TC12/original-orthogonality-of-kernel', (vp.H*metrics[2]*w)[0], sp.Integer(0))
    equal('TC12/other-spectral-vector-orthogonal-projection', P*vm, vp/2)
    equal('E-link/orthogonal-projector-square', P*P, P)
    equal('E-link/orthogonal-projector-adjoint', P.H*metrics[2], metrics[2]*P)
    equal('E-link/spectral-projector-positive-image', Q*vp, vp)
    equal('E-link/spectral-projector-negative-kernel', Q*vm, sp.zeros(2,1))
    equal('E-link/spectral-projector-square', Q*Q, Q)
    D = Q-P
    D_adjoint = exact(metrics[2].inv()*D.H*metrics[2])
    hs2 = exact(sp.trace(D_adjoint*D))
    product = exact(D_adjoint*D)
    equal('TC13/adjoint-product-first-diagonal', product[0,0], sp.Rational(1,4))
    equal('TC13/adjoint-product-second-diagonal', product[1,1], sp.Rational(1,12))
    equal('TC13/adjoint-product-full-matrix', product, (sp.eye(2)-P)/3)
    equal('TC13/reverse-adjoint-product-full-matrix', D*D_adjoint, P/3)
    equal('E-link/projector-Hilbert-Schmidt-square', hs2, sp.Rational(1,3))
    equal('E-link/exact-spectral-gap-square', epsilon[2]-4*SIGMA**2, (2*SIGMA)**2*hs2)
    PS, QS, DS = exact(L*P*L.inv()), exact(L*Q*L.inv()), exact(L*D*L.inv())
    GS = original_metrics[2]
    equal('TC12/original-S-projector-adjoint', PS.H*GS, GS*PS)
    equal('TC12/original-S-spectral-projector-action', QS*AS, AS*QS)
    equal('TC13/original-S-Hilbert-Schmidt-invariance', sp.trace(GS.inv()*DS.H*GS*DS), hs2)

    # These explicit nonzero residuals identify what the injected controls test.
    different('sensitivity/p2-vertical-sign', polynomials[2].subs(S,C+I*U), U**2-SIGMA**2)
    different('sensitivity/rank-two-factor', AX*kernels[2]+kernels[2]*AX.H-2*C*kernels[2],
              (bx[3]*bx[2].H+bx[2]*bx[3].H)/(2*norms[2]))
    different('sensitivity/Toda-loss-sign', epsilon[2], upper_toda+loss)
    failures = [row['name'] for row in CHECKS if not row['passed']]
    proof = Path(__file__).with_name('toda_exterior_equality_calibration_20260913.tex')
    payload = {
        'schema':'toda-exterior-equality-exact-calibration-v1',
        'status':'failed' if failures else 'passed',
        'scope':'Symbolic Gaussian calibration from original monomial source Grams, literal polynomial reduction and multiplication matrices. Full positive mass mu, variance sigma^2, c=1/2 and vertical phases are retained. No arithmetic zero data, numerical quadrature, asymptotic estimate or Lean is used.',
        'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'source_sha256':hashlib.sha256(proof.read_bytes()).hexdigest(),
        'source_file':proof.name, 'python':platform.python_version(), 'sympy':sp.__version__,
        'optimized_python':not __debug__, 'fault_mode':FAULT,
        'checks':CHECKS, 'check_count':len(CHECKS), 'failure_count':len(failures), 'failed_checks':failures,
        'parameters':{'mu':'positive real, retained mass','sigma':'positive real, retained standard deviation','c':str(C),'k':1},
        'original_measure':'mu/(sqrt(2*pi)*sigma)*exp(-u^2/(2*sigma^2)) du',
        'original_quotient_polynomial':encode(CHI), 'L_coordinate':encode(L), 'A_S':encode(AS), 'A_x':encode(AX),
        'derived_source_polynomials':encode(polynomials), 'derived_full_norms':encode(norms),
        'derived_quotient_columns_x':encode(bx), 'degrees':degrees,
        'TC6_relation_Gram_in_chi_chix':encode(relation_centered_gram),
        'Toda':{'delta2':encode(delta2),'delta3':encode(delta3),'a3':encode(a3),'R2':encode(R2),
                'exact_radius_squared':encode(epsilon[2]),'upper_expression':encode(upper_toda),'imbalance_square':encode(loss)},
        'projectors_N2':{'P':encode(P),'Q':encode(Q),'Q_minus_P':encode(D),'adjoint_in_original_G2':encode(D_adjoint),
                         'full_adjoint_product':encode(product),'HS_squared':encode(hs2),
                         'P_original_S_basis':encode(PS),'Q_original_S_basis':encode(QS),'difference_original_S_basis':encode(DS)},
    }
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(payload,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':payload['status'],'check_count':len(CHECKS),'failure_count':len(failures),
                      'fault_mode':FAULT,'output':str(args.output)}),flush=True)
    return 1 if failures else 0


if __name__ == '__main__':
    raise SystemExit(main())
