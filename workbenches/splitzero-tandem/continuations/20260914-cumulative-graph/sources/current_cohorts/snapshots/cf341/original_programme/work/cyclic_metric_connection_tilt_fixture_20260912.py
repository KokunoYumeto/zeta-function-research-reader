"""Exact CM.3--5 and CM.9--12 calibration in original coordinates.

The original amplitude is a(t)=(t+1)exp(-t^2/2), without rescaling.
Only this task's work files are written. No arithmetic-density claim is made.
"""
from pathlib import Path
import hashlib
import json
import math
import sys

import sympy as sp

ROOT = Path(__file__).resolve().parent
BASE = Path(__file__).stem
# Pin the complete source actually read; replay does not require a private path.
SOURCE_SHA256 = "7f58291e609995d05f99249a19d8835d2e12c7c7c182b1890b9a4d158511bb3c"
t, t1, t2, u, y, theta = sp.symbols("t t1 t2 u y theta", real=True)
I = sp.I
sqrtpi = sp.sqrt(sp.pi)
Z = sqrtpi * sp.exp(theta**2 / 4)


def gaussian_coeff(power, tilt):
    """Coefficient after restoring the exact integral factor sqrt(pi)e^(tilt²/4)."""
    seq = [sp.Integer(1), tilt / 2]
    for n in range(1, power):
        seq.append(sp.expand(tilt * seq[-1] / 2 + sp.Rational(n, 2) * seq[-2]))
    return seq[power]


def integrate_original_gaussian(poly, variables, tilt=0):
    tilt = sp.sympify(tilt)
    value = sp.Integer(0)
    for exponents, coeff in sp.Poly(sp.expand(poly), *variables).terms():
        value += coeff * sp.prod(gaussian_coeff(n, tilt) for n in exponents)
    return sp.expand(value) * (sqrtpi * sp.exp(tilt**2/4))**len(variables)


def zero(expr):
    return sp.cancel(sp.expand(expr)) == 0


checks = []


def equal(name, left, right):
    difference = left - right
    ok = all(zero(x) for x in difference) if isinstance(difference, sp.MatrixBase) else zero(difference)
    checks.append({"name": name, "passed": ok})
    if not ok:
        raise RuntimeError(f"Exact check failed: {name}: {difference}")


p = t + 1
d = 1 - t - t**2
mu = [integrate_original_gaussian(t**j*p**2, (t,)) for j in range(5)]
nu = [integrate_original_gaussian(t**j*d**2, (t,)) for j in range(5)]
cross = [integrate_original_gaussian(t**j*p*d, (t,)) for j in range(5)]
equal("CM3 original mixed moments through degree 4", sp.Matrix(cross),
      sp.Matrix([0]+[-sp.Rational(j,2)*mu[j-1] for j in range(1,5)]))

P = (t1+1)*(t2+1)
R = ((1-t1-t1**2)*(t2+1)+(t1+1)*(1-t2-t2**2))/2
sum_t = t1+t2
M_direct = [integrate_original_gaussian(sum_t**j * P**2, (t1,t2)) for j in range(5)]
B_direct = [integrate_original_gaussian(sum_t**j * R**2, (t1,t2)) for j in range(5)]
M_formula = [sum(sp.binomial(j,r)*mu[r]*mu[j-r] for r in range(j+1)) for j in range(5)]
B_formula = []
for j in range(5):
    diagonal = sum(sp.binomial(j,r)*nu[r]*mu[j-r] for r in range(j+1))/2
    off_diagonal = sp.Integer(0) if j<2 else sp.Rational(j*(j-1),8)*M_formula[j-2]
    B_formula.append(diagonal + off_diagonal)
equal("CM4 original sum moments through degree 4", sp.Matrix(M_direct), sp.Matrix(M_formula))
equal("CM4 complete derivative moments including distinct-index cross terms", sp.Matrix(B_direct), sp.Matrix(B_formula))

S = 1 + I*sum_t
c = [sp.Integer(1), S, S**2]
dc = [sp.Integer(0), I, 2*I*S]
D = [R*c[j]+P*dc[j] for j in range(3)]
H0 = sp.Matrix(3,3,lambda i,j: integrate_original_gaussian(P**2*sp.conjugate(c[i])*c[j],(t1,t2)))
Hd = sp.Matrix(3,3,lambda i,j: integrate_original_gaussian(sp.conjugate(D[i])*D[j],(t1,t2)))
HB = sp.Matrix(3,3,lambda i,j: integrate_original_gaussian(R**2*sp.conjugate(c[i])*c[j],(t1,t2)))
HP = sp.Matrix(3,3,lambda i,j: integrate_original_gaussian(P**2*sp.conjugate(dc[i])*dc[j],(t1,t2)))
HC1 = sp.Matrix(3,3,lambda i,j: integrate_original_gaussian(P*R*sp.conjugate(c[i])*dc[j],(t1,t2)))
HC2 = sp.Matrix(3,3,lambda i,j: integrate_original_gaussian(P*R*sp.conjugate(dc[i])*c[j],(t1,t2)))
equal("CM5 complete derivative Gram from original differentiated amplitudes", Hd, HB+HP+HC1+HC2)
equal("CM5 separate cross matrices are adjoints", HC1.H, HC2)
equal("CM5 amplitude Gram Hermitian", H0.H, H0)
equal("CM5 derivative Gram Hermitian", Hd.H, Hd)

def sum_moment_functional(poly):
    return sum(coefficient*M_direct[exponents[0]] for exponents,coefficient in sp.Poly(sp.expand(poly),u).terms())

cu = [sp.Integer(1),1+I*u,(1+I*u)**2]
du = [x.diff(u) for x in cu]
HC1_by_parts = sp.Matrix(3,3,lambda i,j: -sum_moment_functional((sp.conjugate(cu[i])*du[j]).diff(u))/2)
HC2_by_parts = sp.Matrix(3,3,lambda i,j: -sum_moment_functional((sp.conjugate(du[i])*cu[j]).diff(u))/2)
equal("CM5 first m-prime cross term by original sum integration by parts", HC1, HC1_by_parts)
equal("CM5 second m-prime cross term by original sum integration by parts", HC2, HC2_by_parts)

Mt = integrate_original_gaussian(p**2,(t,),theta)
Nt = integrate_original_gaussian(d**2,(t,),theta)
Ct = integrate_original_gaussian(p*d,(t,),theta)
Et_direct = integrate_original_gaussian((d+theta*p/2)**2,(t,),theta)
Pt_mass = integrate_original_gaussian(P**2,(t1,t2),theta)
Bt_direct = integrate_original_gaussian(R**2,(t1,t2),theta)
product_cross = integrate_original_gaussian(P*R,(t1,t2),theta)
Et_product_direct = integrate_original_gaussian((R+theta*P/2)**2,(t1,t2),theta)
equal("CM9 original tilted product mass", Pt_mass, Mt**2)
equal("CM9 original one-factor tilted cross integral", Ct, -theta*Mt/2)
equal("CM9 original tilted product derivative energy", Bt_direct, Nt*Mt/2+theta**2*Mt**2/8)
equal("CM11 directly differentiated tilted amplitude", Et_direct, Nt-theta**2*Mt/4)
equal("CM11 original tilted product cross integral", product_cross, -theta*Mt**2/2)
equal("CM12 directly differentiated tilted product", Et_product_direct, Mt*(Nt-theta**2*Mt/4)/2)

# Independent fibre integration in original (u,y), whose Jacobian has absolute value 1.
b = 1+u/2
Q = b**2-y**2
Qprime = b-u*Q/2
Cfibre = sp.sqrt(sp.pi/2)


def fibre_gaussian(poly):
    result = 0
    for (power,), coefficient in sp.Poly(sp.expand(poly),y).terms():
        if power % 2:
            continue
        n = power//2
        result += coefficient*sp.Rational(math.factorial(2*n),math.factorial(n)*8**n)
    return sp.expand(result)


F = fibre_gaussian(Q**2)
G = fibre_gaussian(Qprime**2)
mixed_fibre = fibre_gaussian(Q*Qprime)
equal("original centred-coordinate Jacobian", sp.Matrix([[sp.Rational(1,2),1],[sp.Rational(1,2),-1]]).det(), -1)
equal("fibre product amplitude mass", F, b**4-b**2/2+sp.Rational(3,16))
equal("fibre mixed derivative is half density derivative", mixed_fibre, (F.diff(u)-u*F)/2)
normal_fibre = sp.cancel(G-mixed_fibre**2/F)
equal("full fibre normal energy", normal_fibre, b**2/(8*F))
fisher_plus_normal = sp.cancel((F.diff(u)+(theta-u)*F)**2/F+4*normal_fibre)
tilted_product_fibre = fibre_gaussian((Qprime+theta*Q/2)**2)
equal("CM12 Fisher plus complete relative energy pointwise", fisher_plus_normal, 4*tilted_product_fibre)

# Integrate C_fibre exp(-u²/2+theta*u) times a polynomial via u=sqrt(2)*t.
integrated_fibre_total = sp.sqrt(2)*Cfibre*integrate_original_gaussian(
    sp.expand(4*tilted_product_fibre).subs(u,sp.sqrt(2)*t),(t,),sp.sqrt(2)*theta)
equal("CM12 complete tilted information identity by direct fibre integration", integrated_fibre_total, 2*Mt*(Nt-theta**2*Mt/4))


def encode(value):
    if isinstance(value, sp.MatrixBase):
        return [[str(sp.expand(item)) for item in row] for row in value.tolist()]
    if isinstance(value,list):
        return [str(sp.expand(item)) for item in value]
    return str(value)


symbolic_tilt = {
    "M_over_Z": sp.cancel(Mt/Z), "N_over_Z": sp.cancel(Nt/Z),
    "one_factor_cross_over_Z": sp.cancel(Ct/Z),
    "tilted_one_factor_derivative_energy_over_Z": sp.cancel(Et_direct/Z),
    "original_product_mass_over_Z_squared": sp.cancel(Pt_mass/Z**2),
    "original_product_derivative_energy_over_Z_squared": sp.cancel(Bt_direct/Z**2),
    "product_cross_over_Z_squared": sp.cancel(product_cross/Z**2),
    "tilted_product_derivative_energy_over_Z_squared": sp.cancel(Et_product_direct/Z**2),
    "CM12_total_over_Z_squared": sp.cancel(integrated_fibre_total/Z**2),
}
result = {
    "title":"Cyclic metric-connection exact non-even Gaussian fixture",
    "scope":"Original amplitude (t+1)exp(-t²/2), k=2, real theta; verifies the identities in CM3-5 and CM9-12 without identifying this amplitude with the arithmetic packet amplitude.",
    "source_file":"cyclic_sum_metric_connection_20260912.tex",
    "source_sha256":SOURCE_SHA256,
    "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "python":sys.version.split()[0],"sympy":sp.__version__,"optimized_python":not __debug__,
    "original_mass":"3*sqrt(pi)/2","tilt_factor_Z":"sqrt(pi)*exp(theta**2/4)",
    "mu_0_through_4":encode(mu),"nu_0_through_4":encode(nu),"cross_0_through_4":encode(cross),
    "M_j_2_0_through_4":encode(M_direct),"B_j_2_0_through_4":encode(B_direct),
    "H0_in_1_S_S2":encode(H0),"Hderivative_in_1_S_S2":encode(Hd),
    "derivative_Gram_amplitude_derivative_part":encode(HB),"derivative_Gram_coefficient_derivative_part":encode(HP),
    "derivative_Gram_first_cross_term":encode(HC1),"derivative_Gram_second_cross_term":encode(HC2),
    "symbolic_real_tilt":{name:encode(value) for name,value in symbolic_tilt.items()},
    "at_theta_1":{name:encode(value.subs(theta,1)) for name,value in symbolic_tilt.items()},
    "fibre_mass_polynomial_F":str(F),"fibre_derivative_energy_polynomial_G":str(G),
    "fibre_normal_energy_after_original_C_exp_factor":str(normal_fibre),
    "fibre_normal_energy_at_u_0":"2*sqrt(pi/2)/11",
    "checks":checks,"check_count":len(checks),"passed":all(row['passed'] for row in checks),
}
suffix='_optimized.json' if not __debug__ else '.json'
dest=ROOT/(BASE+suffix)
dest.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'output':dest.name,'checks':len(checks),'passed':result['passed'],
                  'theta_1':result['at_theta_1'],'Hderivative':result['Hderivative_in_1_S_S2']},indent=2))
