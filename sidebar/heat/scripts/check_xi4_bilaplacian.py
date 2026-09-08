"""Exact Cartesian verification of the complete bilaplacian coefficients.

All differentiations precede substitution of the original gamma(z).
One non-critical Python worker; no network, Lean, or numerical zero scan.
The checked formulas and original sigma are self-contained in this script.
"""
from pathlib import Path
import ctypes
import hashlib
import json
import os
import time


def install_memory_ceiling():
    if os.name != "nt":
        raise RuntimeError("This replay requires the specified Windows job ceiling")
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
    limits.BasicLimitInformation.LimitFlags = 0x00000200
    limits.JobMemoryLimit = 5_000_000_000
    if not api.SetInformationJobObject(job, 9, ctypes.byref(limits), ctypes.sizeof(limits)):
        raise ctypes.WinError(ctypes.get_last_error())
    if not api.AssignProcessToJobObject(job, api.GetCurrentProcess()):
        raise ctypes.WinError(ctypes.get_last_error())
    # The handle remains open until this one process exits.
    return {"status": "enforced_windows_job", "ceiling_bytes": 5_000_000_000,
            "run_class": "non-critical", "worker_count": 1}


RESOURCE = install_memory_ceiling()
import sympy as S

ROOT = Path(__file__).resolve().parents[1]
started = time.monotonic()
x, y, w, s, tau = S.symbols("x y w s tau", real=True)
z = S.symbols("z", positive=True)
coordinates = (x, y, w)
Q = 1 + x*y
sigma = (Q**3*w + y**2*Q*(4 + 3*x*y))/2
gamma = {x: 1/z, y: -3*z/2, w: 13*z**2/2}
rows = []


def exact(name, difference):
    entries = list(difference) if isinstance(difference, S.MatrixBase) else [difference]
    residuals = [S.expand(S.together(term).as_numer_denom()[0]) for term in entries]
    if any(term != 0 for term in residuals):
        raise AssertionError((name, residuals))
    rows.append({"id": name, "entries": len(entries), "status": "pass",
                 "method": "exact_symbolic_zero_residual"})


def laplacian(f):
    return sum(S.diff(f, q, 2) for q in coordinates)


def on_gamma(f):
    return f.subs(gamma, simultaneous=True)


gradient = S.Matrix([S.diff(sigma, q) for q in coordinates])
hessian = S.hessian(sigma, coordinates)
N = gradient.dot(gradient)
L = laplacian(sigma)
gradL = S.Matrix([S.diff(L, q) for q in coordinates])
gradN = S.Matrix([S.diff(N, q) for q in coordinates])
hessian_square = sum(entry**2 for entry in hessian)
g_gradL = gradient.dot(gradL)
g_H_g = (gradient.T*hessian*gradient)[0]

exact("original_Q_on_gamma", on_gamma(Q) + S.Rational(1, 2))
exact("original_sigma_on_gamma", on_gamma(sigma) + z**2/8)
exact("original_time_map", 1-8*((1-z**2)/8)-z**2)
exact("original_cartesian_gradient", gradient-S.Matrix([
    3*y*Q**2*w/2+y**3*(7+6*x*y)/2,
    3*x*Q**2*w/2+(8*y+21*x*y**2+12*x**2*y**3)/2,
    Q**3/2]))
exact("original_cartesian_Laplacian", L-(3*w*Q*(x**2+y**2)
      +3*y**4+18*x**2*y**2+21*x*y+4))
exact("gradient_on_unchanged_gamma", on_gamma(gradient)-S.Matrix([
    -9*z**3/32, -3*z/16, -S.Rational(1, 16)]))
exact("full_hessian_on_unchanged_gamma", on_gamma(hessian)-S.Matrix([
    [-27*z**4/4, 3*z**2/16, -9*z/16],
    [3*z**2/16, S.Rational(13, 4), 3/(8*z)],
    [-9*z/16, 3/(8*z), 0]]))
exact("full_gradient_N_identity", gradN-2*hessian*gradient)
exact("full_Laplacian_N_identity", laplacian(N)-2*hessian_square-2*g_gradL)

# SymPy differentiates the actual composite directly in the three original
# Cartesian coordinates. The formal h derivatives are never evaluated on a
# polynomial substitute for the arithmetic function.
h = S.Function("h")
h_derivatives = {j: S.diff(h(s), s, j).subs(s, sigma) for j in range(1, 5)}
full_coefficients = {
    4: N**2,
    3: 4*g_H_g+2*N*L,
    2: 2*hessian_square+4*g_gradL+L**2,
    1: laplacian(L),
}
exact("full_first_cartesian_chain_rule", laplacian(h(sigma))
      -N*h_derivatives[2]-L*h_derivatives[1])
exact("full_second_cartesian_chain_rule", laplacian(laplacian(h(sigma)))
      -sum(full_coefficients[j]*h_derivatives[j] for j in range(1, 5)))

N_gamma = (81*z**6+36*z**2+4)/1024
L_gamma = (13-27*z**4)/4
exact("N_gamma_all_terms", on_gamma(N)-N_gamma)
exact("L_gamma_all_terms", on_gamma(L)-L_gamma)
exact("Hessian_Frobenius_all_offdiagonal_copies", on_gamma(hessian_square)
      -(729*z**8/16+9*z**4/128+81*z**2/128+S.Rational(169, 16)+9/(32*z**2)))
exact("gradient_L_contraction_all_terms", on_gamma(g_gradL)
      -(9477*z**8/512-405*z**4/64+27*z**2/128+S.Rational(81, 32)+3/(32*z**2)))
exact("gradient_Hessian_gradient_all_terms", on_gamma(g_H_g)
      -(-2187*z**10/4096+81*z**6/4096-81*z**4/4096
        +117*z**2/1024+S.Rational(9, 1024)))

displayed_coefficients = {
    4: N_gamma**2,
    3: -6561*z**10/2048+243*z**6/2048-135*z**4/1024
       +351*z**2/512+S.Rational(31, 512),
    2: 26973*z**8/128-4419*z**4/64+135*z**2/64
       +S.Rational(669, 16)+15/(16*z**2),
    1: -111*z**2+36/z**2,
}
for j in range(1, 5):
    exact(f"C_{j}_from_original_Cartesian_derivatives",
          on_gamma(full_coefficients[j])-displayed_coefficients[j])

residue_weights = {j: S.limit(z**2*displayed_coefficients[j], z, 0, dir="+")
                   for j in range(1, 5)}
exact("all_four_residue_weights", S.Matrix([residue_weights[j] for j in range(1, 5)])
      -S.Matrix([36, S.Rational(15, 16), 0, 0]))
d1, d2, d3, d4 = S.symbols("h_prime_0 h_second_0 h_third_0 h_fourth_0")
jets = {1: d1, 2: d2, 3: d3, 4: d4}
exact("general_h_full_bilaplacian_residue", sum(residue_weights[j]*jets[j]
      for j in range(1, 5))-(15*d2/16+36*d1))
exact("general_h_full_first_diffusion_limit",
      S.limit(N_gamma, z, 0, dir="+")*d2+S.limit(L_gamma, z, 0, dir="+")*d1
      -(d2/256+13*d1/4))

# Exact data for the negative-Newman-time residue. The derivative delta
# contributes -1/336 to D(lambda), hence to the linear Fourier coefficient.
v = S.symbols("v", real=True)
T = S.symbols("T", positive=True)
k0, Cstar = S.symbols("k_0 C_star", real=True)
c0 = -S.Rational(59, 275184)
c1 = S.Rational(1, 1296)
c2 = S.Rational(3, 132496)
beta = S.Rational(1, 336)
d0 = S.Rational(127, 219024)
energy_first_moment = 3*c0-beta+S.Rational(9, 2)*c1+S.Rational(13, 2)*c2
multiplier = (c0*S.exp(3*S.I*v)-S.I*v*beta*S.exp(3*S.I*v)
              +c1*S.exp(S.Rational(9, 2)*S.I*v)
              +c2*S.exp(S.Rational(13, 2)*S.I*v))
exact("xi4_original_mass_and_multiplier_at_zero",
      S.Matrix([c0+c1+c2-d0, multiplier.subs(v, 0)-d0]))
exact("xi4_first_moment_with_derivative_delta",
      S.Matrix([energy_first_moment,
                S.diff(multiplier, v).subs(v, 0)-S.I*energy_first_moment]))
real_residue_multiplier = S.expand_complex(
    (-S.Rational(15, 16)*v**2+36*S.I*v)*multiplier).as_real_imag()[0]
exact("xi4_full_real_quadratic_residue_coefficient",
      S.diff(real_residue_multiplier, v, 2).subs(v, 0)/2
      +S.Rational(15, 16)*d0)

# Differentiate the unchanged Gaussian parameter T/4. The four entries
# retain both moments, the full original Fourier factor 4, and the error
# factor 96; they do not replace the actual kernel by a constant.
gaussian_zero_moment = 2*S.sqrt(S.pi)/S.sqrt(T)
gaussian_second_moment = -4*S.diff(gaussian_zero_moment, T)
gaussian_fourth_moment = 16*S.diff(gaussian_zero_moment, T, 2)
exact("xi4_original_Gaussian_moments_leading_and_error_factors", S.Matrix([
    gaussian_second_moment-4*S.sqrt(S.pi)*T**(-S.Rational(3, 2)),
    gaussian_fourth_moment-24*S.sqrt(S.pi)*T**(-S.Rational(5, 2)),
    -4*S.Rational(15, 16)*d0*k0*gaussian_second_moment
        +15*d0*k0*S.sqrt(S.pi)*T**(-S.Rational(3, 2)),
    4*Cstar*gaussian_fourth_moment-96*Cstar*S.sqrt(S.pi)*T**(-S.Rational(5, 2)),
]))

section_value = S.symbols("section_value")
Xi = S.Function("Xi")
residue_section = 8*section_value*s**2*Xi(s)/(15*Xi(0))
section_first_jet = S.diff(residue_section, s).subs(s, 0)
section_second_jet = S.diff(residue_section, s, 2).subs(s, 0)
exact("xi4_residue_right_inverse_retaining_original_Xi", S.Matrix([
    section_first_jet, section_second_jet-16*section_value/15,
    36*section_first_jet+S.Rational(15, 16)*section_second_jet-section_value,
]))

receipt = {
    "schema_version": 1, "status": "pass", "all_passed": True,
    "check_count": len(rows), "checks": rows,
    "run_class": "non-critical", "resource": RESOURCE,
    "sympy_version": S.__version__, "workers": 1,
    "elapsed_seconds": round(time.monotonic()-started, 4),
    "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "formula_source": {
        "repository": "navier_stokes_research_2026-09-08",
        "path": "tex/arithmetic_bilaplacian.tex",
        "sha256_at_complete_read": "3df68fab19b3ffa7b5e9f85f9722f9e6b2ed47910591654604ae83ce20363111",
        "read_scope": "complete fragment; no source edit",
    },
    "retained_objects": {
        "coordinates": ["x", "y", "w"], "Euclidean_Laplacian": "d_x^2+d_y^2+d_w^2",
        "Q": str(Q), "sigma": str(sigma),
        "gamma": [str(gamma[q]) for q in coordinates], "domain": "real z > 0",
        "time_map": "tau=(1-z^2)/8; z=sqrt(1-8*tau), tau<1/8",
        "C_j": {str(j): str(displayed_coefficients[j]) for j in range(1, 5)},
        "general_h_residue": "lim_{z down to 0} z^2 Delta^2(h compose sigma)(gamma(z)) = 15 h''(0)/16 + 36 h'(0)",
        "original_fourier_multiplier": str(multiplier),
        "xi4_mass": str(d0), "xi4_first_energy_moment": str(energy_first_moment),
        "negative_time_leading_term": "-15*(127/219024)*k(0)*sqrt(pi)*T^(-3/2)",
        "negative_time_remainder_bound": "96*C_star*sqrt(pi)*T^(-5/2)",
        "residue_right_inverse": "E(a)(s)=8*a*s^2*Xi(s)/(15*Xi(0)), Xi(0) != 0",
    },
    "scope": "Exact symbolic identities supplement the complete written proofs. The general-h limit uses continuity of its first four derivatives at zero; no parity is assumed and the first-derivative contribution is retained. The negative-time asymptotic checks verify its exact moments, quadratic coefficient, Gaussian constants and residue section; the global analytic remainder proof remains in tex/xi4_bilaplacian.tex. No NS endpoint or RH counterexample is asserted.",
}
target = ROOT / "checks" / "xi4_bilaplacian_checks.json"
target.write_text(json.dumps(receipt, indent=2)+"\n", encoding="utf-8")
print(json.dumps({"status": "pass", "check_count": len(rows), "resource": RESOURCE,
                  "receipt_sha256": hashlib.sha256(target.read_bytes()).hexdigest()}))
