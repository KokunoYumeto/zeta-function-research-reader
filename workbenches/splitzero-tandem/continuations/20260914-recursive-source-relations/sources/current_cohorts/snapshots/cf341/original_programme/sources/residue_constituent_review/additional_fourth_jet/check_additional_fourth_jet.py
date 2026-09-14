"""One new q=3, dim F=2 exact check of RCX28 and RCX30-32."""
from __future__ import annotations
import json
import platform
import sys
import sympy as s

CHECKS = []

def exact(value):
    return s.cancel(s.expand(value))

def mat_exact(matrix):
    return matrix.applyfunc(exact)

def zero(value):
    if isinstance(value, s.MatrixBase):
        return all(exact(v) == 0 for v in value)
    return exact(value) == 0

def check(name, value):
    if not bool(value):
        raise AssertionError(name)
    CHECKS.append(name)

def equality(name, lhs, rhs):
    check(name, zero(lhs-rhs))

def encoded(value):
    if isinstance(value, s.MatrixBase):
        return [[s.sstr(exact(value[i,j])) for j in range(value.cols)] for i in range(value.rows)]
    if isinstance(value, (tuple, list)):
        return [encoded(v) for v in value]
    if isinstance(value, dict):
        return {str(k): encoded(v) for k,v in value.items()}
    return s.sstr(exact(value))

def determinant_coefficients(matrices, variable):
    """Direct 2x2 scalar determinant, retaining its Taylor coefficients."""
    polynomial = sum((m*variable**n for n,m in enumerate(matrices)), s.zeros(2))
    determinant = s.Poly(s.expand(polynomial[0,0]*polynomial[1,1]-polynomial[0,1]*polynomial[1,0]), variable)
    return [exact(determinant.nth(n)) for n in range(5)]

def scalar_log_coefficients(determinant):
    """Solve d'=d ell' coefficientwise; ell_0=log(d_0) is retained separately."""
    result = [s.log(determinant[0])]
    for n in range(1,5):
        product = sum(k*result[k]*determinant[n-k] for k in range(1,n))
        result.append(exact((n*determinant[n]-product)/(n*determinant[0])))
    return result

def main():
    t,w,x = s.symbols('t w x')
    u = s.Rational(3,2)
    A = s.Matrix([[0,0,0],[1,0,-2],[0,1,0]])
    e = s.Matrix([1,0,0])
    ell = s.Matrix([[0,0,1]])
    R = e*ell
    inclusion = s.Matrix([[0,0],[1,0],[0,1]])
    quotient = s.Matrix([[1,0,0]])
    B = s.Matrix([[1,(1+s.I)/2,(2-s.I)/3],[0,1,(1+2*s.I)/3],[0,0,1]])
    H0 = mat_exact(B.H*B)
    HF = mat_exact(inclusion.H*H0*inclusion)
    AF = s.Matrix([[0,-2],[1,0]])
    equality('monic polynomial S^3+2S retained', A.charpoly(t).as_expr(), t**3+2*t)
    equality('actual constituent invariance', A*inclusion, inclusion*AF)
    equality('quotient annihilates constituent', quotient*inclusion, s.zeros(1,2))
    equality('initial matrix invertible with determinant one', B.det(), 1)
    check('positive Hermitian H0 by B*B and nonzero determinant', H0 == H0.H and B.det() != 0)
    check('proper constituent dimension exactly two in dimension three', inclusion.rank() == 2 and quotient.rank() == 1)
    check('H0 has a nonreal off-diagonal entry', s.im(H0[0,1]) != 0)
    check('H0 is nonscalar', not zero(H0-H0[0,0]*s.eye(3)))
    check('HF determinant is positive', exact(HF.det()).is_positive is True)

    # Actual solution of Pi'=-Pi(A+tR)/u: multiplication stays on the right.
    period = [B]
    for n in range(4):
        previous = period[n-1] if n else s.zeros(3)
        period.append(mat_exact(-(period[n]*A+previous*R)/(u*(n+1))))
    At = A+t*R
    Q = [s.eye(3)]
    for n in range(4):
        Q.append(mat_exact(Q[n].diff(t)-At*Q[n]/u))
    for n in range(5):
        equality('actual Taylor coefficient equals B Q_'+str(n)+'(0)/'+str(s.factorial(n)),
                 s.factorial(n)*period[n], B*Q[n].subs(t,0))
    equality('ordered Q3 identity as a polynomial in t', Q[3], -At**3/u**3+(R*At+2*At*R)/u**2)
    wrong_Q3 = -At**3/u**3+(2*R*At+At*R)/u**2
    order_residual = mat_exact((wrong_Q3-Q[3]).subs(t,0))
    check('Q3 ordering is substantive on this fixture', not zero(order_residual))

    D = [mat_exact(HF.inv()*inclusion.H*H0*Q[n].subs(t,0)*inclusion) for n in range(1,5)]
    D1,D2,D3,D4 = D
    commutator = mat_exact(D1*D2-D2*D1)
    check('D1 and D2 do not commute', not zero(commutator))
    phi4_formula = exact(s.trace(D4-4*D1*D3-3*D2**2+12*D1**2*D2-6*D1**4))

    # Independent scalar determinant logarithms from actual period coefficients.
    Y = [mat_exact(p*inclusion) for p in period]
    pure_matrices = [mat_exact(Y[0].H*y) for y in Y]
    real_matrices = [mat_exact(sum((Y[i].H*Y[n-i] for i in range(n+1)), s.zeros(2))) for n in range(5)]
    pure_det = determinant_coefficients(pure_matrices, t)
    real_det = determinant_coefficients(real_matrices, x)
    pure_log = scalar_log_coefficients(pure_det)
    real_log = scalar_log_coefficients(real_det)
    pure_derivatives = [exact(s.factorial(n)*pure_log[n]) for n in range(1,5)]
    real_derivatives = [exact(s.factorial(n)*real_log[n]) for n in range(1,5)]
    equality('RCX32 matches actual pure fourth derivative', phi4_formula, pure_derivatives[3])
    check('pure fourth jet has nonzero real part', s.re(pure_derivatives[3]) != 0)
    check('pure fourth jet has nonzero imaginary part', s.im(pure_derivatives[3]) != 0)

    L = ell*inclusion
    source_projector = inclusion*HF.inv()*inclusion.H*H0
    quotient_cost = exact((e.H*H0*(s.eye(3)-source_projector)*e)[0])
    dual_cost = exact((L*HF.inv()*L.H)[0])
    cost = exact(quotient_cost*dual_cost)
    mixed_derivative = exact(cost/(s.conjugate(u)*u))
    equality('RCX29 pure first derivative', pure_derivatives[0], -s.trace(AF)/u)
    equality('RCX29 pure second derivative', pure_derivatives[1], -(L*HF.inv()*inclusion.H*H0*e)[0]/u)
    equality('RCX28 real second derivative with pure jet retained', real_derivatives[1], 2*s.re(pure_derivatives[1]))
    equality('RCX28 real fourth derivative with all six mixed contributions',
             real_derivatives[3], 2*s.re(phi4_formula)+6*mixed_derivative)
    check('quotient cost and dual cost are both strictly positive', quotient_cost.is_positive is True and dual_cost.is_positive is True)
    check('mixed term alone is not the real fourth derivative', not zero(real_derivatives[3]-6*mixed_derivative))

    # A second route: actual bivariate Gram, exact scalar determinant and log.
    gram_bivariate = sum((Y[i].H*Y[j]*w**i*t**j for i in range(5) for j in range(5) if i+j<=4), s.zeros(2))
    determinant_bivariate = s.expand(gram_bivariate[0,0]*gram_bivariate[1,1]-gram_bivariate[0,1]*gram_bivariate[1,0])
    def trunc(poly):
        return s.Add(*(exact(c)*t**a*w**b for (a,b),c in s.Poly(s.expand(poly),t,w).terms() if a+b<=4))
    determinant_bivariate = trunc(determinant_bivariate)
    constant = exact(determinant_bivariate.subs({t:0,w:0}))
    Z = trunc(determinant_bivariate/constant-1)
    power = s.Integer(1)
    log_bivariate = s.Integer(0)
    for n in range(1,5):
        power = trunc(power*Z)
        log_bivariate += (-1)**(n+1)*power/s.Integer(n)
    log_bivariate = trunc(log_bivariate)
    coefficients = s.Poly(log_bivariate,t,w)
    bivariate_coefficients = {(a,b): exact(coefficients.coeff_monomial(t**a*w**b)) for total in range(1,5) for a in range(total+1) for b in [total-a]}
    for n in range(1,5):
        equality('bivariate pure t^'+str(n)+' retained', bivariate_coefficients[n,0], pure_log[n])
        equality('bivariate pure w^'+str(n)+' is the conjugate', bivariate_coefficients[0,n], s.conjugate(pure_log[n]))
    for a,b in [(1,1),(2,1),(1,2),(3,1),(1,3)]:
        equality('RCX26 vanishing mixed coefficient '+str((a,b)), bivariate_coefficients[a,b], 0)
    equality('RCX26 factor 2!2! in nonscalar constituent Gram', 4*bivariate_coefficients[2,2], mixed_derivative)
    equality('real x^4 coefficient is the sum of all bidegree-four coefficients', real_log[4], sum(bivariate_coefficients[a,4-a] for a in range(5)))

    output = {
        'status': 'PASS', 'scope': 'One new exact q=3, dim(F)=2 nonscalar fixture of RCX28/30/31/32; no predecessor replay',
        'python': platform.python_version(), 'python_executable': sys.executable,
        'optimization_level': sys.flags.optimize, 'sympy': s.__version__, 'sympy_file': s.__file__,
        'exact_check_count': len(CHECKS), 'checks': CHECKS,
        'input': encoded({'A':A,'R':R,'inclusion':inclusion,'quotient':quotient,'AF':AF,'B':B,'H0':H0,'HF':HF,'u':u}),
        'actual_period_Taylor_coefficients_0_through_4': encoded(period),
        'Q_polynomials_0_through_4': encoded(Q), 'D_matrices_1_through_4': encoded(D),
        'noncommutativity_witnesses': encoded({'D1_D2_minus_D2_D1':commutator,'reversed_Q3_order_minus_correct_Q3_at_zero':order_residual}),
        'pure_determinant_coefficients_0_through_4': encoded(pure_det),
        'real_determinant_coefficients_0_through_4': encoded(real_det),
        'log_constant': s.sstr(s.log(constant)),
        'pure_log_coefficients_1_through_4': encoded(pure_log[1:]),
        'real_log_coefficients_1_through_4': encoded(real_log[1:]),
        'pure_derivatives_1_through_4': encoded(pure_derivatives),
        'real_derivatives_1_through_4': encoded(real_derivatives),
        'bivariate_log_coefficients_total_degree_1_through_4': encoded(bivariate_coefficients),
        'comparison': encoded({'phi4_RCX32':phi4_formula,'phi4_actual':pure_derivatives[3],
                              'quotient_cost':quotient_cost,'dual_cost':dual_cost,'c_F_H0':cost,
                              'mixed_fourth_derivative':mixed_derivative,'mixed_x2w2_coefficient':bivariate_coefficients[2,2],
                              'twice_real_pure_fourth':2*s.re(phi4_formula),'six_times_mixed':6*mixed_derivative,
                              'real_fourth_actual':real_derivatives[3],
                              'real_fourth_RCX28':2*s.re(phi4_formula)+6*mixed_derivative,
                              'real_fourth_residual':real_derivatives[3]-2*s.re(phi4_formula)-6*mixed_derivative}),
    }
    print(json.dumps(output, indent=2, ensure_ascii=False))

if __name__ == '__main__':
    main()
