"""Independent exact MGF/Schur review of the GMT bounded calibration."""
from pathlib import Path
import hashlib
import json
import sympy as s

u, z, x = s.symbols('u z x', real=True)
I = s.I
checks = []


def check(name, value):
    passed = bool(value)
    checks.append({'name': name, 'passed': passed})
    if not passed:
        raise ValueError(name)


def equal(a, b):
    if isinstance(a, s.MatrixBase):
        return a.shape == b.shape and all(s.cancel(v-w) == 0 for v,w in zip(a,b))
    return s.cancel(a-b) == 0


def mgf_moments(beta, mass, maximum):
    polynomial = s.series(mass / s.cos(z)**beta, z, 0, maximum+1).removeO().expand()
    return [s.factorial(j) * polynomial.coeff(z,j) for j in range(maximum+1)]


def observation(p, moments):
    return s.expand(sum(coef*moments[index[0]] for index,coef in s.Poly(s.expand(p),u).terms()))


reference_one = mgf_moments(2,s.Rational(1,2),10)
arithmetic_one = [reference_one[j]+reference_one[j+2]/4 for j in range(9)]
arithmetic_sum = [sum(s.binomial(n,j)*arithmetic_one[j]*arithmetic_one[n-j] for j in range(n+1)) for n in range(9)]
reference_sum = mgf_moments(4,s.Rational(1,4),8)
check('GMT34_moments_by_MGF',arithmetic_sum == [s.Rational(9,16),0,s.Rational(9,2),0,117,0,5472,0,385272])
M = s.Matrix(4,4,lambda a,b: observation((1-I*u)**a*(1+I*u)**b,arithmetic_sum))
M0 = s.Matrix(4,4,lambda a,b: observation((1-I*u)**a*(1+I*u)**b,reference_sum))
check('GMT35_actual_matrix',equal(M,s.Matrix([[9,9,-63,-207],[9,81,81,-1863],[-63,81,2025,2025],[-207,-1863,2025,93393]])/16))
check('GMT35_reference_matrix',equal(M0,s.Matrix([[1,1,-3,-11],[1,5,5,-55],[-3,5,65,65],[-11,-55,65,1685]])/4))
B = s.Matrix([[-1,0],[-2,-1],[1,-2],[0,1]])
J = s.Matrix([[1,0,1,2],[0,1,2,5]])
E = s.eye(4)[:,:2]


def schur_lift(H):
    R = (E-B*(B.H*H*B).inv()*B.H*H*E).applyfunc(s.cancel)
    G = (E.H*H*E-E.H*H*B*(B.H*H*B).inv()*B.H*H*E).applyfunc(s.cancel)
    return G,R


G,R = schur_lift(M)
G0,R0 = schur_lift(M0)
check('GMT37_G3',equal(G,s.Matrix([[s.Rational(81,244),s.Rational(81,244)],[s.Rational(81,244),s.Rational(175041,80764)]])))
check('GMT37_R3',equal(R,s.Matrix([[s.Rational(117,122),s.Rational(-801,40382)],[s.Rational(-5,61),s.Rational(18963,20191)],[s.Rational(5,122),s.Rational(-907,40382)],[0,s.Rational(7,331)]])))
check('GMT37_G3_reference',equal(G0,s.Matrix([[s.Rational(5,38),s.Rational(5,38)],[s.Rational(5,38),s.Rational(2255,4142)]])))
check('literal_boundary_kernel',equal(J*B,s.zeros(2)))
check('literal_right_inverse',equal(J*R,s.eye(2)))
check('literal_boundary_orthogonality',equal(B.H*M*R,s.zeros(2)))
W = (M[2:,2:]-M[2:,:2]*M[:2,:2].inv()*M[:2,2:]).applyfunc(s.cancel)
FD = (J[:,2:]-J[:,:2]*M[:2,:2].inv()*M[:2,2:]).applyfunc(s.cancel)
ZD = (FD.H*M[:2,:2]*FD).applyfunc(s.cancel)
check('GMT38_W',equal(W,s.Matrix([[81,243],[243,3159]])))
check('GMT38_FD',equal(FD,s.Matrix([[10,2],[0,28]])))
check('GMT38_ZD',equal(ZD,s.Matrix([[225,675],[675,16137]])/4))
actual_ratio = s.cancel(M[:2,:2].det()/G.det())
reference_ratio = s.cancel(M0[:2,:2].det()/G0.det())
check('GMT39_actual_ratio',actual_ratio == s.Rational(20191,4860))
check('GMT39_reference_ratio',reference_ratio == s.Rational(2071,450))
check('GMT39_relative_ratio',s.cancel(actual_ratio/reference_ratio) == s.Rational(100955,111834))
check('GMT39_a3',s.cancel(W.det()/W[0,0]**2) == 30)
check('GMT25_denominator_exponent_matters',s.cancel(W.det()/W[0,0]) != 30)
delta = M-M0
Ht = M0+x*delta
Gt,Rt = schur_lift(Ht)
At = B.H*Ht*B
Ct = B.H*delta*Rt
check('GMT20_symbolic_R_derivative',equal(Rt.diff(x),-B*At.inv()*Ct))
check('GMT20_symbolic_G_derivative',equal(Gt.diff(x),Rt.H*delta*Rt))
check('GMT20_symbolic_G_second_derivative',equal(Gt.diff(x,2),-2*Ct.H*At.inv()*Ct))
coupling = B.H*delta*R0
check('nonzero_boundary_coupling',not equal(coupling,s.zeros(2)))
check('t0_loss_still_zero',equal((x*x*coupling.H*At.inv()*coupling).subs(x,0),s.zeros(2)))
Astar = s.Rational(4515,4)
epsstar = s.factorial(8)/s.Integer(2)**92
entry_error = 8192*Astar*epsstar
check('GMT40_one_factor_sixth_moment',arithmetic_one[6] == 1128)
check('GMT41_strict_entry_bound',entry_error < s.Rational(1,40000))
check('GMT41_strict_operator_bound',4*entry_error < s.Rational(1,10000))
low = M-s.eye(4)/10000
high = M+s.eye(4)/10000
minors = [low[:j,:j].det() for j in range(1,5)]
check('GMT41_exact_lower_principal_minors',minors == [s.Rational(703,1250),s.Rational(253068751,100000000),s.Rational(102481960035937,500000000000),s.Rational(4980299350501627807501,10000000000000000)])
check('GMT41_all_lower_principal_minors_positive',all(v>0 for v in minors))
Glow,_ = schur_lift(low)
Ghigh,_ = schur_lift(high)
lower = s.cancel(low[:2,:2].det()/Ghigh.det())
upper = s.cancel(high[:2,:2].det()/Glow.det())
check('GMT42_exact_lower',lower == s.Rational(20694424798404596925036,4984219548001747192501))
check('GMT42_exact_upper',upper == s.Rational(20703435010591353075036,4980299350501627807501))
check('GMT42_reference_comparison',1 < lower < actual_ratio < upper < reference_ratio)
Htest = M+s.eye(4)/20000
Gtest,Rtest = schur_lift(Htest)
Alow = B.H*low*B
Ainv = (B.H*Htest*B).inv()
sigma = abs(B).T*(s.eye(4)/20000)*abs(R)
Kentry = s.Matrix(2,2,lambda a,b:(Alow.inv()[a,a]+Alow.inv()[b,b])/2)
Rerror = abs(B)*Kentry*sigma
tau = sigma.T*abs(Alow.inv())*sigma
Dq = s.diag(*[sum(tau[i,j] for j in range(2)) for i in range(2)])
SE = B.H*(Htest-M)*R
Rdiff = (Rtest-R).applyfunc(s.cancel)
loss = (R.H*Htest*R-Gtest).applyfunc(s.cancel)
check('GMT29a_inverse_entry_majorants',all(abs(Ainv[a,b]) <= Kentry[a,b] for a in range(2) for b in range(2)))
check('GMT29a_exact_original_lift_difference',equal(Rdiff,-B*Ainv*SE))
check('GMT29a_original_lift_coefficient_bounds',all(abs(Rdiff[a,b]) <= Rerror[a,b] for a in range(4) for b in range(2)))
check('GMT29a_quadratic_loss_identity',equal(loss,Rdiff.H*Htest*Rdiff))
check('GMT29b_boundary_inverse_loss_identity',equal(loss,SE.H*Ainv*SE))
check('GMT29b_loss_upper_strict_Sylvester',all((Dq-loss)[:j,:j].det()>0 for j in range(1,3)))
check('GMT29a_preserved_original_quotient',equal(J*Rdiff,s.zeros(2)))
payload = {'schema':'gmt-independent-mgf-schur-review-v1','status':'passed','sympy':s.__version__,
           'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           'check_count':len(checks),'checks':checks,
           'one_factor_reference_moments_0_to_10':[str(v) for v in reference_one],
           'one_factor_arithmetic_moments_0_to_8':[str(v) for v in arithmetic_one],
           'strict_entry_error':str(entry_error),'lower_principal_minors':[str(v) for v in minors],
           'bounded_ratio_lower':str(lower),'bounded_ratio_upper':str(upper),
           'analytic_capped_measure_integrated':False,
           'scope':'Independent MGF-generated exact calibration and symbolic resolvent derivatives; the capped ratio follows from the written tail and strict-envelope proofs.'}
out = Path(__file__).with_name('gamma_finite_metric_transfer_independent_check_result_20260913.json')
out.write_text(json.dumps(payload,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'passed','checks':len(checks),'output':out.name}))
