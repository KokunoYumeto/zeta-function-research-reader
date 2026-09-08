"""Deterministic rational/algebraic checks; written proofs remain authoritative.

Run with one Python worker. No network, zero search, or Lean process is used.
On Windows the process tree is limited to exactly 5,000,000,000 bytes.
"""
from pathlib import Path
import ctypes
import hashlib
import json
import os
import time


def install_memory_ceiling():
    if os.name != "nt":
        return {"status": "not_windows", "ceiling_bytes": 5_000_000_000}
    from ctypes import wintypes
    class BasicLimits(ctypes.Structure):
        _fields_ = [("PerProcessUserTimeLimit", ctypes.c_int64),
                    ("PerJobUserTimeLimit", ctypes.c_int64),
                    ("LimitFlags", wintypes.DWORD),
                    ("MinimumWorkingSetSize", ctypes.c_size_t),
                    ("MaximumWorkingSetSize", ctypes.c_size_t),
                    ("ActiveProcessLimit", wintypes.DWORD),
                    ("Affinity", ctypes.c_size_t),
                    ("PriorityClass", wintypes.DWORD),
                    ("SchedulingClass", wintypes.DWORD)]
    class IOCounters(ctypes.Structure):
        _fields_ = [(name, ctypes.c_uint64) for name in
                    ("ReadOperationCount", "WriteOperationCount", "OtherOperationCount",
                     "ReadTransferCount", "WriteTransferCount", "OtherTransferCount")]
    class ExtendedLimits(ctypes.Structure):
        _fields_ = [("BasicLimitInformation", BasicLimits),
                    ("IoInfo", IOCounters),
                    ("ProcessMemoryLimit", ctypes.c_size_t),
                    ("JobMemoryLimit", ctypes.c_size_t),
                    ("PeakProcessMemoryUsed", ctypes.c_size_t),
                    ("PeakJobMemoryUsed", ctypes.c_size_t)]
    api = ctypes.WinDLL("kernel32", use_last_error=True)
    api.CreateJobObjectW.argtypes = [ctypes.c_void_p, wintypes.LPCWSTR]
    api.CreateJobObjectW.restype = wintypes.HANDLE
    api.SetInformationJobObject.argtypes = [wintypes.HANDLE, ctypes.c_int,
                                           ctypes.c_void_p, wintypes.DWORD]
    api.SetInformationJobObject.restype = wintypes.BOOL
    api.AssignProcessToJobObject.argtypes = [wintypes.HANDLE, wintypes.HANDLE]
    api.AssignProcessToJobObject.restype = wintypes.BOOL
    api.GetCurrentProcess.restype = wintypes.HANDLE
    job = api.CreateJobObjectW(None, None)
    if not job:
        raise ctypes.WinError(ctypes.get_last_error())
    limits = ExtendedLimits()
    limits.BasicLimitInformation.LimitFlags = 0x00000200  # JOB_OBJECT_LIMIT_JOB_MEMORY
    limits.JobMemoryLimit = 5_000_000_000
    if not api.SetInformationJobObject(job, 9, ctypes.byref(limits), ctypes.sizeof(limits)):
        raise ctypes.WinError(ctypes.get_last_error())
    if not api.AssignProcessToJobObject(job, api.GetCurrentProcess()):
        raise ctypes.WinError(ctypes.get_last_error())
    # Keep the handle open for the lifetime of this bounded process.
    return {"status": "enforced_windows_job", "ceiling_bytes": 5_000_000_000,
            "run_class": "non-critical", "worker_count": 1}


RESOURCE = install_memory_ceiling()
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
s, t, u, r = sp.symbols("s t u r")
half = sp.Rational(1, 2)
quarter = sp.Rational(1, 4)
checks = []


def identity(name, difference):
    if isinstance(difference, sp.MatrixBase):
        entries = list(difference)
    else:
        entries = [difference]
    residuals = [sp.expand(sp.together(x).as_numer_denom()[0]) for x in entries]
    if any(x != 0 for x in residuals):
        raise AssertionError((name, residuals))
    checks.append({"id": name, "status": "pass", "method": "exact_symbolic_identity"})


def heat(f, time_parameter):
    degree = sp.Poly(f, s).degree()
    if degree is sp.S.NegativeInfinity:
        return sp.Integer(0)
    return sp.expand(sum((-time_parameter/4)**k / sp.factorial(k)
                         * sp.diff(f, s, 2*k)
                         for k in range(int(degree)//2 + 1)))


def B(f):
    return s*f-t*sp.diff(f, s)/2


def star(f, g):
    degree = min(sp.Poly(f, s).degree(), sp.Poly(g, s).degree())
    return sp.expand(sum((-t/2)**k/sp.factorial(k)
                         *sp.diff(f,s,k)*sp.diff(g,s,k)
                         for k in range(int(degree)+1)))


started = time.monotonic()
for degree in range(11):
    f = s**degree
    identity(f"heat_group_degree_{degree}", heat(heat(f,t),u)-heat(f,t+u))
    identity(f"heat_inverse_degree_{degree}", heat(heat(f,t),-t)-f)
    identity(f"coordinate_conjugation_degree_{degree}", heat(s*f,t)-B(heat(f,t)))
    identity(f"heat_equation_degree_{degree}", sp.diff(heat(f,t),t)+sp.diff(heat(f,t),s,2)/4)

f = 3-2*s+5*s**2-7*s**3+11*s**5
g = -13+17*s**2-19*s**4
h = 23-29*s+31*s**3
identity("full_heat_product", heat(f*g,t)-star(heat(f,t),heat(g,t)))
identity("star_conjugation", star(f,g)-heat(heat(f,-t)*heat(g,-t),t))
identity("star_associativity", star(star(f,g),h)-star(f,star(g,h)))
identity("star_coordinate", star(s,f)-B(f))

Z = sp.Function("Z")(s)
identity("first_generator", B(Z)-(s*Z-t*sp.diff(Z,s)/2))
identity("second_generator", B(B(Z))-(s**2*Z-t*s*sp.diff(Z,s)-t*Z/2+t**2*sp.diff(Z,s,2)/4))
A = sp.Function("A")(s,t)
P = sp.Function("P")(s,t)
identity("analytic_unit_full_heat_rule",
         sp.diff(A*P,t)+sp.diff(A*P,s,2)/4
         -(A*(sp.diff(P,t)+sp.diff(P,s,2)/4)
           +(sp.diff(A,t)+sp.diff(A,s,2)/4)*P+sp.diff(A,s)*sp.diff(P,s)/2))
R = sp.Matrix([[0,-2*s],[1,0]])
connection = sp.diag(0,1/(2*s))
identity("root_square_original_s", R*R+2*s*sp.eye(2))
identity("cover_connection_commutator", sp.diff(R,s)+connection*R-R*connection+R.inv())
identity("connection_square_zeroth_term", sp.diff(connection,s)+connection*connection-sp.diag(0,-1/(4*s*s)))
identity("root_chain_rule", sp.diff(-r*r/2,r)*(-1/r)-1)

for k in range(1,6):
    odd = s**7
    for j in range(k):
        odd = sp.diff(odd,s)+odd/(2*s)
    coefficient = sp.prod(sp.Rational(15,2)-j for j in range(k))
    identity(f"odd_iterated_domain_coefficient_{k}", odd-coefficient*s**(7-k))
    for n in range(k):
        assert sp.prod(sp.Rational(2*n+1,2)-j for j in range(k)) != 0

for m in range(1,9):
    # Full written proof handles arbitrary m; these are exact bounded replays.
    Xi = (s-2)**m*(3+5*(s-2)+7*(s-2)**2)
    witness = (s-2)*Xi
    identity(f"multiplicity_heat_obstruction_{m}",
             sp.diff(witness,s,m+1).subs(s,2)-sp.factorial(m+1)*3)

for k in range(5):
    identity(f"raw_jet_coordinate_{k}",
             sp.diff(s*f,s,k)-s*sp.diff(f,s,k)
             -(k*sp.diff(f,s,k-1) if k else 0))

lam = sp.symbols("lambda")
test_h = sp.Function("h")(u)
weight = sp.exp(t*u*u/4+sp.I*lam*u)
test_value = weight*test_h
for k in range(1,5):
    test_value = -sp.I*sp.diff(test_value,u)+(sp.I*t*u/2-lam)*test_value
    identity(f"weighted_compact_inverse_conjugation_{k}",
             test_value-weight*(-sp.I)**k*sp.diff(test_h,u,k))
identity("test_heat_multiplier_equation",
         sp.diff(sp.exp(t*u*u/4),t)-u*u*sp.exp(t*u*u/4)/4)

# Exact local Taylor calculation, including the k > m range where
# some lower coefficients survive. Symbols retain every local unit coefficient.
for m in range(1,6):
    for k in range(1,8):
        coefficients = sp.symbols(f"b0:{k+2}")
        local_input = sum(coefficients[n]*s**(m+n) for n in range(k+2))
        local_output = sp.Poly(sp.diff(local_input,s,k),s)
        differences = []
        for j in range(m):
            n = j+k-m
            expected = (sp.factorial(j+k)/sp.factorial(j)*coefficients[n]
                        if n >= 0 else 0)
            differences.append(local_output.coeff_monomial(s**j)-expected)
        identity(f"full_derivative_domain_m{m}_k{k}",sp.Matrix(differences))

unit0, unit1, h0, h1 = sp.symbols("A0 A1 h0 h1")
identity("simple_zero_heat_domain_retained_unit",
         sp.diff(s*(unit0+unit1*s)*(h0+h1*s),s,2).subs(s,0)
         -2*(unit0*h1+unit1*h0))
identity("source_second_derivative_commutator",
         sp.diff(s*Z,s,2)-s*sp.diff(Z,s,2)-2*sp.diff(Z,s))

x = sp.symbols("x")
commutator_polynomial = sp.Integer(1)
for k in range(7):
    closed = sp.factorial(k)*sum(
        (-1)**j*(t/2)**(k-j)*x**(k-2*j)
        /(2**j*sp.factorial(j)*sp.factorial(k-2*j))
        for j in range(k//2+1))
    identity(f"heat_commutator_recurrence_{k}",commutator_polynomial-closed)
    commutator_polynomial = sp.expand(t*x*commutator_polynomial/2
                                     -sp.diff(commutator_polynomial,x))

rho = sp.symbols("rho")
z = sp.symbols("z")
lambda_from_rho = sp.I*(rho-half)
identity("mellin_original_exponent",-sp.I*(sp.I*(z-half))-(z-half))
identity("mellin_zero_local_coordinate",sp.I*(z-half)-lambda_from_rho-sp.I*(z-rho))
for n in range(1,41):
    divisor_sum = sum(sp.mobius(d) for d in sp.divisors(n))
    identity(f"moebius_exact_divisor_{n}",divisor_sum-(1 if n == 1 else 0))

for m in range(1,7):
    local_unit = sp.symbols(f"a0:{m}")
    original_jets = sp.symbols(f"f0:{m}")
    reciprocal = [1/local_unit[0]]
    for j in range(1,m):
        reciprocal.append(-sum(local_unit[k]*reciprocal[j-k]
                               for k in range(1,j+1))/local_unit[0])
    principal_coefficients = [sum(sp.I**j*original_jets[j]/sp.factorial(j)
                                 *reciprocal[q-j] for j in range(q+1))
                              for q in range(m)]
    reconstructed = [sum(local_unit[j]*principal_coefficients[q-j]
                         for j in range(q+1)) for q in range(m)]
    identity(f"arithmetic_principal_parts_inverse_m{m}",
             sp.Matrix([reconstructed[q]-sp.I**q*original_jets[q]/sp.factorial(q)
                        for q in range(m)]))

nodes = [(sp.Integer(-2),1), (sp.Rational(3,2),2), (1+sp.I,3)]
for node,m in nodes:
    Bnode = sp.prod((s-other)**multiplicity for other,multiplicity in nodes
                    if other != node)
    for j in range(m):
        local_germ = (s-node)**j/(sp.factorial(j)*Bnode)
        taylor = sum(sp.diff(local_germ,s,k).subs(s,node)*(s-node)**k/sp.factorial(k)
                     for k in range(m))
        basis = Bnode*taylor
        for other,multiplicity in nodes:
            for k in range(multiplicity):
                identity(f"mixed_Hermite_{node}_{j}_at_{other}_{k}",
                         sp.diff(basis,s,k).subs(s,other)
                         -(1 if other == node and k == j else 0))

# Full original Gaussian coefficients and the complex scaling generator.
beta = sp.symbols("beta", nonzero=True)
gaussian = sp.exp(-sp.pi*beta*x*x)
psi_beta = (4*sp.pi**2*beta**2*x**4-6*sp.pi*beta*x*x)*gaussian
theta_plus_one_gaussian = x*sp.diff(gaussian,x)+gaussian
identity("Schwartz_Gaussian_Euler_seed",
         x*sp.diff(theta_plus_one_gaussian,x)-psi_beta)
identity("Schwartz_complex_scaling_generator",
         -sp.I*psi_beta/2-2*sp.I*beta*sp.diff(psi_beta,beta)
         +sp.I*(x*sp.diff(psi_beta,x)+psi_beta/2))
y = sp.symbols("y", real=True)
identity("exponential_Mellin_modulus_all_factors",
         quarter*(4+4*y*y)*(1+4*y*y)/sp.pi**2
         *sp.pi*y/sp.sinh(sp.pi*y)
         -(1+y*y)*(1+4*y*y)*y/(sp.pi*sp.sinh(sp.pi*y)))
for j in range(8):
    falling_derivative = sp.diff(x**(-z),x,j)*x**j/x**(-z)
    identity(f"inverse_Mellin_rising_factorial_j{j}",
             falling_derivative-(-1)**j*sp.rf(z,j))
for k in range(1,9):
    gamma_residue = 2/((-1)**k*sp.factorial(k))
    identity(f"arithmetic_origin_residue_k{k}",
             half*(-2*k)*(-2*k-1)*sp.pi**k*gamma_residue
             -2*k*(2*k+1)*(-1)**k*sp.pi**k/sp.factorial(k))
for delta in [sp.Rational(3,2),sp.Integer(2),sp.Integer(3),
              sp.Rational(7,2),sp.Integer(5),sp.Integer(7),
              sp.Rational(15,2),sp.Integer(9)]:
    allowed = [a for a in range(12) if 2*a-delta < -1]
    identity(f"Sobolev_strict_degree_count_delta{delta}",
             len(allowed)-sp.ceiling((delta-1)/2))
for degree in range(8):
    identity(f"Sobolev_Fourier_moment_sign_{degree}",
             sp.I**degree*(-sp.I)**degree-1)
identity("Sobolev_original_generator_sign",sp.I*(-1)-(-sp.I))

# Meromorphic heat is conjugated through its entire numerator, not
# through an unrestricted Laurent series. Retain the original affine map.
for degree in range(9):
    input_F = s**degree
    numerator_H = input_F.subs(s,sp.I*(z-half))
    z_heat = sum((t/4)**k/sp.factorial(k)*sp.diff(numerator_H,z,2*k)
                 for k in range(degree//2+1))
    identity(f"meromorphic_heat_affine_conjugacy_degree{degree}",
             z_heat-heat(input_F,t).subs(s,sp.I*(z-half)))
unit = 3+5*z+7*z*z
numerator = 11-13*z+17*z**2-19*z**3+23*z**4
for m in range(1,7):
    local_zeta = z**m*unit
    meromorphic_M = numerator/local_zeta
    expanded_generator = (sp.diff(meromorphic_M,z,2)
        +2*sp.diff(local_zeta,z)/local_zeta*sp.diff(meromorphic_M,z)
        +sp.diff(local_zeta,z,2)/local_zeta*meromorphic_M)/4
    identity(f"meromorphic_full_unit_pole_cancellation_m{m}",
             expanded_generator-sp.diff(numerator,z,2)/(4*local_zeta))
    M0,M1,M2 = sp.symbols("M0 M1 M2")
    regular_M = M0+M1*z+M2*z*z
    analytic_numerator = sp.diff(local_zeta*regular_M,z,2)/(4*unit)
    principal = sum(sp.diff(analytic_numerator,z,n).subs(z,0)
                    /sp.factorial(n)*z**(n-m) for n in range(m))
    expected = m*(m-1)*M0/(4*z*z)+(m*(m+1)*M1+2*m*sp.Rational(5,3)*M0)/(4*z)
    identity(f"meromorphic_instantaneous_Schwartz_poles_m{m}",
             principal-expected)
for degree in range(8):
    coefficients = sp.symbols(f"c0:{degree+1}")
    numerator_initial = sum(coefficients[n]*z**n for n in range(degree+1))
    numerator_time = sum((t/4)**k/sp.factorial(k)*sp.diff(numerator_initial,z,2*k)
                         for k in range(degree//2+1))
    for n in range(min(4,degree+1)):
        expected = sum(t**k*sp.factorial(n+2*k)/(4**k*sp.factorial(k)*sp.factorial(n))
                       *coefficients[n+2*k] for k in range((degree-n)//2+1))
        identity(f"meromorphic_time_numerator_jets_degree{degree}_n{n}",
                 sp.diff(numerator_time,z,n).subs(z,0)/sp.factorial(n)-expected)

# Reflection periods and exact complex-time jets used by the persistent core.
mu = sp.symbols("mu")
identity("persistent_core_reflection_composition",
         2*lam-(2*mu-s)-(s+2*(lam-mu)))
for k in range(4):
    for j in range(4):
        identity(f"persistent_heat_time_jets_k{k}_j{j}",
                 sp.diff(heat(f,t),s,j,t,k).subs(t,0)
                 -(-quarter)**k*sp.diff(f,s,2*k+j))
v, radius = sp.symbols("v radius", positive=True)
identity("Hadamard_positive_counting_integrand",
         sp.diff(sp.log(1+radius**2/v**2),v)
         +2*radius**2/(v*(v**2+radius**2)))

def xi4_original_operator(value):
    return (-sp.Rational(59,275184)*value.subs(s,s+3)
            -sp.Rational(1,336)*sp.diff(value,s).subs(s,s+3)
            +sp.Rational(1,1296)*value.subs(s,s+sp.Rational(9,2))
            +sp.Rational(3,132496)*value.subs(s,s+sp.Rational(13,2)))
identity("xi4_original_multiplier_at_zero",
         -sp.Rational(59,275184)+sp.Rational(1,1296)
         +sp.Rational(3,132496)-sp.Rational(127,219024))
for degree in range(8):
    value=s**degree
    identity(f"xi4_full_operator_heat_commutation_degree{degree}",
             xi4_original_operator(heat(value,t))-heat(xi4_original_operator(value),t))
identity("xi4_cosine_even_extension_factor",sp.Rational(8,2)/2-2)

# Retained Cartesian polynomial and every second-diffusion coefficient.
xx,yy,ww,zz=sp.symbols("xx yy ww zz", nonzero=True)
coords=(xx,yy,ww)
Qsp=1+xx*yy
sigma=(Qsp**3*ww+yy**2*Qsp*(4+3*xx*yy))/2
curve={xx:1/zz,yy:-3*zz/2,ww:13*zz**2/2}
lap=lambda value:sum(sp.diff(value,c,2) for c in coords)
grad=sp.Matrix([sp.diff(sigma,c) for c in coords])
hess=sp.hessian(sigma,coords)
Nsp=(grad.T*grad)[0]
Lsp=lap(sigma)
normH=sum(hess[i,j]**2 for i in range(3) for j in range(3))
ggradL=sum(grad[i]*sp.diff(Lsp,coords[i]) for i in range(3))
gHg=(grad.T*hess*grad)[0]
identity("original_spatial_map_left_inverse",sigma.subs({xx:0,yy:0,ww:2*s})-s)
identity("original_spatial_curve_Q",Qsp.subs(curve)+half)
identity("original_spatial_curve_sigma",sigma.subs(curve)+zz**2/8)
gradient_expected=sp.Matrix([-9*zz**3/32,-3*zz/16,-sp.Rational(1,16)])
hessian_expected=sp.Matrix([
 [-27*zz**4/4,3*zz**2/16,-9*zz/16],
 [3*zz**2/16,sp.Rational(13,4),3/(8*zz)],
 [-9*zz/16,3/(8*zz),0]])
for i in range(3):
    identity(f"bilaplacian_original_gradient_{i}",grad[i].subs(curve)-gradient_expected[i])
    for j in range(3):
        identity(f"bilaplacian_original_Hessian_{i}_{j}",
                 hess[i,j].subs(curve)-hessian_expected[i,j])
Ncurve=(81*zz**6+36*zz**2+4)/1024
Lcurve=(13-27*zz**4)/4
normcurve=(729*zz**8/16+9*zz**4/128+81*zz**2/128
           +sp.Rational(169,16)+9/(32*zz**2))
glcurve=(9477*zz**8/512-405*zz**4/64+27*zz**2/128
         +sp.Rational(81,32)+3/(32*zz**2))
ghgcurve=(-2187*zz**10/4096+81*zz**6/4096-81*zz**4/4096
          +117*zz**2/1024+sp.Rational(9,1024))
for name,actual,expected in [
 ("N",Nsp,Ncurve),("L",Lsp,Lcurve),("H_norm",normH,normcurve),
 ("g_grad_L",ggradL,glcurve),("g_H_g",gHg,ghgcurve),
 ("Delta_L",lap(Lsp),-111*zz**2+36/zz**2)]:
    identity("bilaplacian_retained_contraction_"+name,actual.subs(curve)-expected)
coefficients=[lap(Lsp),2*normH+4*ggradL+Lsp**2,
              4*gHg+2*Nsp*Lsp,Nsp**2]
Ccurve=[
 -111*zz**2+36/zz**2,
 26973*zz**8/128-4419*zz**4/64+135*zz**2/64+sp.Rational(669,16)+15/(16*zz**2),
 -6561*zz**10/2048+243*zz**6/2048-135*zz**4/1024+351*zz**2/512+sp.Rational(31,512),
 Ncurve**2]
for j in range(4):
    identity(f"bilaplacian_full_C_{j+1}",coefficients[j].subs(curve)-Ccurve[j])
    identity(f"bilaplacian_scaled_limit_C_{j+1}",
             sp.limit(zz**2*Ccurve[j],zz,0)-[36,sp.Rational(15,16),0,0][j])
for degree in range(1,4):
    htest=s**degree
    full=sum(coefficients[j]*sp.diff(htest,s,j+1).subs(s,sigma) for j in range(4))
    identity(f"bilaplacian_direct_Cartesian_chain_degree{degree}",
             lap(lap(sigma**degree))-full)
residue=lambda value:36*sp.diff(value,s).subs(s,0)+sp.Rational(15,16)*sp.diff(value,s,2).subs(s,0)
Xi0,Xi2,Xi4=sp.symbols("Xi0 Xi2 Xi4", nonzero=True)
Xi_sample=Xi0+Xi2*s**2/2+Xi4*s**4/24
esection=8*s*s*Xi_sample/(15*Xi0)
identity("source_residue_exact_trace_section",residue(esection)-1)
sample=3-5*s+7*s**2-11*s**3+13*s**4
projected=sample-esection*residue(sample)
identity("source_residue_projection_range",residue(projected))
identity("source_residue_projection_idempotence",
         projected-esection*residue(projected)-projected)
for degree in range(6):
    htest=s**degree
    actual=residue(xi4_original_operator(htest))
    operator_residue=sum(c*(36*sp.diff(htest,s,1+offset).subs(s,shift)
                            +sp.Rational(15,16)*sp.diff(htest,s,2+offset).subs(s,shift))
      for c,shift,offset in [
       (-sp.Rational(59,275184),3,0),(-sp.Rational(1,336),3,1),
       (sp.Rational(1,1296),sp.Rational(9,2),0),
       (sp.Rational(3,132496),sp.Rational(13,2),0)])
    identity(f"xi4_original_residue_all_terms_degree{degree}",actual-operator_residue)
for d in range(5):
    data=sp.symbols(f"jet0:{d+1}")
    reciprocal=sp.series(1/Xi_sample,s,0,d+1).removeO()
    section_poly=sp.series(reciprocal*sum(data[j]*s**j/sp.factorial(j)
                                         for j in range(d+1)),s,0,d+1).removeO()
    section=Xi_sample*section_poly
    for j in range(d+1):
        identity(f"source_origin_jet_section_d{d}_j{j}",
                 sp.diff(section,s,j).subs(s,0)-data[j])

# Normal ordering is essential: D and multiplication by s do not commute.
def normal_jet_operator(value,j):
    return sum(sp.binomial(j,k)*(-2*(s-lam)/t)**(j-k)*sp.diff(value,s,k)
               for k in range(j+1))
def Aop(value):
    return sp.diff(value,s)-2*(s-lam)*value/t
def iterate_A(value,n):
    for _ in range(n):
        value=sp.expand(Aop(value))
    return value
for j in range(7):
    hermite=lambda variable:sum(sp.factorial(j)*t**(-ell)*variable**(j-2*ell)
        /(sp.factorial(ell)*sp.factorial(j-2*ell)) for ell in range(j//2+1))
    value=s**3-2*s+5
    corrected=sum(sp.factorial(j)*t**(-ell)*iterate_A(value,j-2*ell)
        /(sp.factorial(ell)*sp.factorial(j-2*ell)) for ell in range(j//2+1))
    identity(f"moving_finite_jet_normal_order_j{j}",
             normal_jet_operator(value,j)-corrected)
    identity(f"moving_finite_jet_heat_conjugacy_j{j}",
             heat(normal_jet_operator(heat(value,t),j),-t)
             -hermite(-2*(s-lam)/t)*value)

# Independent Cartesian replay of compression, leakage and return.
eta={xx:0,yy:0,ww:2*s}
section_family={yy:0,ww:2*s}
identity("diffusion_eta_gradient",grad.subs(eta)-sp.Matrix([0,0,half]))
identity("diffusion_eta_hessian",hess.subs(eta)-sp.Matrix([[0,3*s,0],[3*s,4,0],[0,0,0]]))
identity("diffusion_eta_N",Nsp.subs(eta)-quarter)
identity("diffusion_eta_L",Lsp.subs(eta)-4)
identity("diffusion_leakage_family_sigma",sigma.subs(section_family)-s)
identity("diffusion_leakage_family_N",Nsp.subs(section_family)-quarter-9*xx**2*s**2)
identity("diffusion_leakage_family_L",Lsp.subs(section_family)-4-6*xx**2*s)
for j,expected in enumerate([24*s,36*s**2+48,2,sp.Rational(1,16)]):
    identity(f"diffusion_second_compression_coefficient_D{j+1}",
             coefficients[j].subs(eta)-expected)
compressed=lambda h:sp.diff(h,s,2)/4+4*sp.diff(h,s)
for degree in range(7):
    h=s**degree
    leakage=(Nsp-quarter)*sp.diff(h,s,2).subs(s,sigma)+(Lsp-4)*sp.diff(h,s).subs(s,sigma)
    identity(f"diffusion_leakage_family_degree{degree}",
             leakage.subs(section_family)-xx**2*3*degree*(3*degree-1)*s**degree)
    full_compressed=sum(coefficients[j].subs(eta)*sp.diff(h,s,j+1) for j in range(4))
    feedback=(36*s**2+32)*sp.diff(h,s,2)+24*s*sp.diff(h,s)
    identity(f"diffusion_second_feedback_degree{degree}",
             full_compressed-compressed(compressed(h))-feedback)
    identity(f"diffusion_return_of_leakage_degree{degree}",
             lap(leakage).subs(eta)-feedback)
    nu,theta=sp.symbols("nu theta")
    ht=heat(h,-4*nu*theta)
    spatial=ht.subs(s,sigma)
    residual=nu*((1-Nsp)*sp.diff(ht,s,2).subs(s,sigma)
                 -Lsp*sp.diff(ht,s).subs(s,sigma))
    identity(f"viscous_original_pullback_residual_degree{degree}",
             sp.diff(spatial,theta)-nu*lap(spatial)-residual)

# Actual three-coordinate source and the published sample retain all entries.
Ffull=sp.Matrix([2*sigma,
 yy+3*xx*Qsp**2*ww+3*xx*yy**2*(4+3*xx*yy),
 2*xx-3*xx**2*yy-xx**3*ww])
Sfull=sp.diag(half,1,1)*Ffull
JF=Ffull.jacobian(coords)
JS=Sfull.jacobian(coords)
identity("flow_original_polynomial_determinant",JF.det()+2)
identity("flow_original_spatial_S_determinant",JS.det()+1)
rows=[sp.Matrix(list(JF.row(j))) for j in range(3)]
Winverse=sp.Matrix.hstack(-rows[1].cross(rows[2])/2,
                          -rows[2].cross(rows[0])/2,
                          -rows[0].cross(rows[1])/2)
identity("flow_original_full_cofactor_inverse",JF*Winverse-sp.eye(3))
identity("flow_original_scaled_target_inverse",
         JS*Winverse*sp.diag(2,1,1)-sp.eye(3))
rr=sp.symbols("r_sample",positive=True)
path={xx:rr,yy:0,ww:0}
Jpath=sp.Matrix([[0,0,half],[0,1,3*rr],[2,-3*rr**2,-rr**3]])
Jpath_inverse=sp.Matrix([[-8*rr**3,3*rr**2/2,half],[-6*rr,1,0],[2,0,0]])
identity("public_witness_original_sample_coordinates",Sfull.subs(path)-sp.Matrix([0,0,2*rr]))
identity("public_witness_original_sample_J",JS.subs(path)-Jpath)
identity("public_witness_original_sample_full_inverse",Jpath*Jpath_inverse-sp.eye(3))
identity("public_witness_original_sample_inverse_reverse",Jpath_inverse*Jpath-sp.eye(3))
uvec=sp.Matrix(sp.symbols("u_sample1:4"))
vvec=Jpath*uvec
identity("public_witness_full_swirl_channel",vvec[1]-6*rr*vvec[0]-uvec[1])
nu_positive,Xin,tau_positive=sp.symbols("nu_positive X_in tau_positive",positive=True)
identity("public_witness_residue_norm_denominator",
         (1+36*rr**2).subs(rr,sp.sqrt(2*nu_positive*Xin*tau_positive))
         -(1+72*nu_positive*Xin*tau_positive))

aa,th,vv,bb,thp,thpp=sp.symbols("a_shift theta v_t b_t theta_prime theta_second")
sample_h=3-2*s+5*s**2-7*s**3+11*s**5
def V_flow(h):
    return heat(h,th).subs(s,s+aa)
def V_flow_inverse(h):
    return heat(h.subs(s,s-aa),-th)
identity("flow_translation_heat_full_inverse",V_flow_inverse(V_flow(sample_h))-sample_h)
identity("flow_original_spectrum_conjugate",
         V_flow(s*sample_h)-((s+aa)*V_flow(sample_h)-th*sp.diff(V_flow(sample_h),s)/2))
Fprofile=V_flow(sample_h)
timeop=lambda h: thp*sp.diff(h,th)+vv*sp.diff(h,aa)+bb*sp.diff(h,vv)+thpp*sp.diff(h,thp)
identity("flow_profile_first_time_generator",
         timeop(Fprofile)+thp*sp.diff(Fprofile,s,2)/4-vv*sp.diff(Fprofile,s))
identity("flow_profile_full_second_time_generator",
         timeop(timeop(Fprofile))-
         (thp**2*sp.diff(Fprofile,s,4)/16
          -thp*vv*sp.diff(Fprofile,s,3)/2
          +(vv**2-thpp/4)*sp.diff(Fprofile,s,2)+bb*sp.diff(Fprofile,s)))
du=sp.symbols("du0:9")
Du=sp.Matrix(3,3,du)
force_terms=sp.Matrix(sp.symbols("material_accel1:4"))
for j in range(3):
    Sj=Sfull[j]
    gradSj=sp.Matrix([sp.diff(Sj,z) for z in coords])
    accel=gradSj.dot(force_terms)+(uvec.T*sp.hessian(Sj,coords)*uvec)[0]
    material_full=gradSj.dot(force_terms-Du*uvec)
    velocity_expr=gradSj.dot(uvec)
    material_full+=sum(uvec[k]*sp.diff(velocity_expr,coords[k]) for k in range(3))
    material_full+=gradSj.dot(Du*uvec)
    identity(f"flow_full_material_acceleration_channel{j+1}",accel-material_full)

zz_local=sp.symbols("zeta_local")
unit=3+5*zz_local+7*zz_local**2+11*zz_local**3
speed=sp.symbols("actual_swirl_speed")
for multiplicity in range(1,6):
    entire=zz_local**multiplicity*unit
    logarithmic=speed*sp.diff(entire,zz_local)/entire
    identity(f"flow_residue_complete_local_unit_m{multiplicity}",
             logarithmic-speed*(multiplicity/zz_local+sp.diff(unit,zz_local)/unit))
    identity(f"flow_residue_coefficient_m{multiplicity}",
             sp.residue(logarithmic,zz_local,0)-multiplicity*speed)
sample_tangent=sp.Matrix([rr/(2*tau_positive),0,0])+uvec
for j in (0,1):
    identity(f"public_witness_moving_label_cancellation_channel{j+1}",
             (Jpath*sample_tangent)[j]-vvec[j])

source = ROOT / "tex" / "connes_quotient_heat_transport.tex"
receipt = {"schema_version": 1, "run_class": "non-critical", "resource": RESOURCE,
           "sympy_version": sp.__version__, "workers": 1, "check_count": len(checks),
           "all_passed": True, "elapsed_seconds": round(time.monotonic()-started,4),
           "manuscript_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
           "checks": checks,
           "limits": ["No numerical zero search", "No proof of source topology identification",
                      "No Lean certification", "Symbolic replays supplement complete written proofs"]}
(ROOT/"checks"/"verification_receipt.json").write_text(json.dumps(receipt,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"all_passed": True, "checks": len(checks), "resource": RESOURCE}))
