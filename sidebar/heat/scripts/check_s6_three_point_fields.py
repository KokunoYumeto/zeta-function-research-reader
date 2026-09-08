"""Exact independent checks of the original three-point fluid field.

One non-critical Python worker, 5,000,000,000-byte Windows job ceiling.
Sparse Fourier convolution checks convection before using product-to-sum.
Arbitrary Taylor jets check the complete compact-localization identity.
No Lean, numerical evolution, network access, or numerical zero search.
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
        _fields_ = [("BasicLimitInformation", BasicLimits), ("IoInfo", IOCounters),
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
    limits.BasicLimitInformation.LimitFlags = 0x00000200 | 0x00000008
    limits.BasicLimitInformation.ActiveProcessLimit = 1
    limits.JobMemoryLimit = 5_000_000_000
    if not api.SetInformationJobObject(job, 9, ctypes.byref(limits), ctypes.sizeof(limits)):
        raise ctypes.WinError(ctypes.get_last_error())
    if not api.AssignProcessToJobObject(job, api.GetCurrentProcess()):
        raise ctypes.WinError(ctypes.get_last_error())
    return {"status": "enforced_windows_job", "ceiling_bytes": 5_000_000_000,
            "run_class": "non-critical", "worker_count": 1,
            "active_process_limit": 1}


RESOURCE = install_memory_ceiling()
import sympy as S

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / "tex" / "s6_three_point_forcing.tex"
STARTED = time.monotonic()
PROOF_BEFORE = hashlib.sha256(PROOF.read_bytes()).hexdigest()
ROWS = []


def exact(name, residual):
    entries = list(residual) if isinstance(residual, S.MatrixBase) else (
        list(residual) if isinstance(residual, (list, tuple)) else [residual])
    differences = [S.expand(S.together(v).as_numer_denom()[0]) for v in entries]
    if any(v != 0 for v in differences):
        raise AssertionError((name, differences))
    ROWS.append({"id": name, "status": "pass", "entries": len(entries),
                 "method": "exact_symbolic_zero_residual"})


def assertion(name, condition, detail):
    if not condition:
        raise AssertionError((name, detail))
    ROWS.append({"id": name, "status": "pass", "method": "exact_finite_comparison",
                 "detail": detail})


def mat(values):
    return S.Matrix([S.Rational(v) for v in values])


labels = (1, 2, 0)
pairs = ((1, 2), (1, 0), (2, 0))
k = {1: mat([4, 0, 1]), 2: mat([3, 0, 1]), 0: mat([0, 1, 0])}
c = {1: mat([1, 2, -4])/3, 2: mat([-1, -3, 3])/4, 0: mat([0, 0, 1])}
a_symbols = S.symbols("a1 a2 a0", real=True)
ad_symbols = S.symbols("ad1 ad2 ad0", real=True)
a = dict(zip(labels, a_symbols))
ad = dict(zip(labels, ad_symbols))
nu = S.symbols("nu", positive=True)
expected_lengths = {1: (17, S.Rational(7, 3)), 2: (10, S.Rational(19, 16)), 0: (1, 1)}
for j in labels:
    exact(f"base_{j}_orthogonality_lengths", [k[j].dot(c[j]),
          k[j].dot(k[j])-expected_lengths[j][0], c[j].dot(c[j])-expected_lengths[j][1]])

W = S.Matrix.vstack(*(k[j].T for j in labels))
Winv = S.Matrix([[1, -1, 0], [0, 0, 1], [-3, 4, 0]])
G = S.Matrix([[17, 13, 0], [13, 10, 0], [0, 0, 1]])
metric = S.Matrix([[10, -13, 0], [-13, 17, 0], [0, 0, 1]])
exact("phase_inverse_both_orders", list(W*Winv-S.eye(3))+list(Winv*W-S.eye(3)))
exact("phase_determinant_original_orientation", W.det()+1)
exact("contravariant_metric_full_matrix", W*W.T-G)
exact("covariant_metric_full_matrix", Winv.T*Winv-metric)
exact("metric_inverse", metric*G-S.eye(3))
J = S.Matrix(3, 3, S.symbols("J0:9"))
v = S.Matrix(S.symbols("v0:3"))
qgrad = S.Matrix(S.symbols("qg0:3"))
H = S.Matrix([[S.Symbol(f"H{min(i,j)}{max(i,j)}") for j in range(3)] for i in range(3)])
exact("phase_convection_pushforward", (W*J*Winv)*(W*v)-W*(J*v))
exact("phase_divergence_pushforward", S.trace(W*J*Winv)-S.trace(J))
exact("phase_pressure_pushforward", W*(W.T*qgrad)-G*qgrad)
exact("phase_laplacian_mixed_coefficient", S.trace(W.T*H*W)-sum(G[i,j]*H[i,j] for i in range(3) for j in range(3)))

table = [
    (1, 2, 1, (7, 0, 2), (0, "1/12", "1/12"), ("-7/318", "1/12", "49/636"), "1/6", 53),
    (1, 2, -1, (1, 0, 0), ("1/6", "5/12", "-7/12"), (0, "5/12", "-7/12"), "1/6", 1),
    (1, 0, 1, (4, 1, 1), ("1/3", "2/3", "-2/3"), ("1/27", "16/27", "-20/27"), "4/3", 18),
    (1, 0, -1, (4, -1, 1), ("-1/3", "-2/3", 2), ("-17/27", "-16/27", "52/27"), "4/3", 18),
    (2, 0, 1, (3, 1, 1), ("-1/4", "-3/4", 0), ("7/44", "-27/44", "3/22"), "-3/2", 11),
    (2, 0, -1, (3, -1, 1), ("1/4", "3/4", "-3/2"), ("29/44", "27/44", "-15/11"), "-3/2", 11),
]
cross_rows = []
for i, j, sign, kt, bt, pt, dot, length in table:
    kk = k[i]+sign*k[j]
    bb = c[i].dot(k[j])*c[j]+sign*c[j].dot(k[i])*c[i]
    pp = bb-kk*kk.dot(bb)/kk.dot(kk)
    name = f"pair_{i}{j}_{'plus' if sign == 1 else 'minus'}"
    exact(name+"_original_frequency", kk-mat(kt))
    exact(name+"_unprojected_column", bb-mat(bt))
    exact(name+"_projection_pressure", list(pp-mat(pt))+[kk.dot(bb)-S.Rational(dot), kk.dot(kk)-length, kk.dot(pp)])
    assertion(name+"_nonzero_transverse", pp.dot(pp)>0, str(pp.dot(pp)))
    cross_rows.append((i, j, sign, kk, bb, pp))
exact("pair_12_plus_original_curl", cross_rows[0][3].cross(cross_rows[0][4])-mat(["-1/6", "-7/12", "7/12"]))


def key(vector):
    return tuple(int(v) for v in vector)


def negative(frequency):
    return tuple(-v for v in frequency)


base_keys = [key(k[j]) for j in labels]
cross_keys = [key(row[3]) for row in cross_rows]
assertion("all_nine_frequencies_distinct_up_to_sign",
          len(set(base_keys+cross_keys+[negative(v) for v in base_keys+cross_keys])) == 18,
          {"base": base_keys, "cross": cross_keys})


def add_coeff(target, frequency, value):
    target[frequency] = target.get(frequency, S.zeros(3, 1))+value


def add_sine(target, frequency, vector):
    add_coeff(target, frequency, vector/(2*S.I))
    add_coeff(target, negative(frequency), -vector/(2*S.I))


ufourier = {}
for j in labels:
    add_sine(ufourier, key(k[j]), a[j]*c[j])
# Direct ordered Fourier convolution, independent of the displayed B formula.
nfourier = {}
for p, up in ufourier.items():
    for q, uq in ufourier.items():
        out = tuple(p[d]+q[d] for d in range(3))
        add_coeff(nfourier, out, 2*S.pi*S.I*up.dot(mat(q))*uq)
expected_n = {}
pressure = {}
expected_f = {}
for i, j, sign, kk, bb, pp in cross_rows:
    frequency = key(kk)
    add_sine(expected_n, frequency, S.pi*a[i]*a[j]*bb)
    add_sine(expected_f, frequency, S.pi*a[i]*a[j]*pp)
    scalar = a[i]*a[j]*kk.dot(bb)/(4*kk.dot(kk))
    pressure[frequency] = scalar
    pressure[negative(frequency)] = scalar
for j in labels:
    add_sine(expected_f, key(k[j]), (ad[j]+4*S.pi**2*nu*k[j].dot(k[j])*a[j])*c[j])
all_keys = sorted(set(nfourier)|set(expected_n)|set(ufourier)|set(pressure))
for frequency in all_keys:
    nk = nfourier.get(frequency, S.zeros(3, 1))
    exact("fourier_convection_"+str(frequency), nk-expected_n.get(frequency, S.zeros(3, 1)))
    uk = ufourier.get(frequency, S.zeros(3, 1))
    utk = sum((uk.diff(a[j])*ad[j] for j in labels), S.zeros(3, 1))
    momentum = utk+4*S.pi**2*nu*sum(vv**2 for vv in frequency)*uk+nk
    momentum += 2*S.pi*S.I*mat(frequency)*pressure.get(frequency, S.S.Zero)
    exact("fourier_full_momentum_"+str(frequency), momentum-expected_f.get(frequency, S.zeros(3, 1)))
for j in labels:
    fpositive = expected_f[key(k[j])]
    # Pairing a real sine mode uses positive and negative Fourier coefficients.
    recovered = (2*S.I*fpositive).dot(c[j])/c[j].dot(c[j])
    exact(f"base_{j}_prescribed_force_ODE", recovered-ad[j]-4*S.pi**2*nu*k[j].dot(k[j])*a[j])

C = S.Matrix.hstack(*(c[j] for j in labels))
exact("polarization_determinant", C.det()+S.Rational(1, 12))
# Torus integration from actual Fourier coefficients rather than an assumed Gram matrix.
stress = sum((vec*ufourier.get(negative(freq), S.zeros(3, 1)).T
              for freq, vec in ufourier.items()), S.zeros(3))
expected_stress = C*S.diag(*(a[j]**2 for j in labels))*C.T/2
exact("full_quadratic_stress_from_fourier", stress-expected_stress)
exact("stress_cone_coordinate_inverse", C.inv()*stress*C.inv().T-S.diag(*(a[j]**2/2 for j in labels)))
exact("energy_original_polar_lengths", S.trace(stress)/2-(S.Rational(7,3)*a[1]**2+S.Rational(19,16)*a[2]**2+a[0]**2)/4)
r = S.symbols("r1 r2 r0", nonnegative=True)
cone_stress = C*S.diag(*r)*C.T
for mask in range(8):
    lifts = [(-1 if mask & (1 << j) else 1)*S.sqrt(2*r[j]) for j in range(3)]
    exact(f"stress_cone_right_inverse_sign_{mask}", C*S.diag(*(v*v for v in lifts))*C.T/2-cone_stress)

# Generic second-order spatial jets and first-order time jets suffice to test
# every term of the differential product identity, at an arbitrary point.
x = S.symbols("x1 x2 x3", real=True)
t = S.symbols("t", real=True)
origin = dict.fromkeys((*x, t), S.S.Zero)


def jet(name, time_derivative=False):
    f = S.Symbol(name)
    f += sum(S.Symbol(f"{name}_d{i}")*x[i] for i in range(3))
    f += sum(S.Symbol(f"{name}_dd{i}{i}")*x[i]**2/2 for i in range(3))
    f += sum(S.Symbol(f"{name}_dd{i}{j}")*x[i]*x[j] for i in range(3) for j in range(i+1,3))
    if time_derivative:
        f += S.Symbol(name+"_dt")*t
    return f


def grad(f):
    return S.Matrix([S.diff(f, z) for z in x])


def lap(f):
    if isinstance(f, S.MatrixBase):
        return f.applyfunc(lap)
    return sum(S.diff(f, z, 2) for z in x)


def at0(f):
    return f.subs(origin, simultaneous=True)


def curl(vv):
    return S.Matrix([S.diff(vv[2],x[1])-S.diff(vv[1],x[2]),
                     S.diff(vv[0],x[2])-S.diff(vv[2],x[0]),
                     S.diff(vv[1],x[0])-S.diff(vv[0],x[1])])


chi = jet("chi")
uu = S.Matrix([jet(f"u{i}", True) for i in range(3)])
dd = S.Matrix([jet(f"d{i}", True) for i in range(3)])
pp = jet("p")
N = uu.jacobian(x)*uu
ff = uu.diff(t)+N-nu*lap(uu)+grad(pp)
VV = chi*uu+dd
lhs = at0(VV.diff(t)+VV.jacobian(x)*VV-nu*lap(VV)+grad(chi*pp))
rhs = chi*ff+(chi**2-chi)*N+dd.diff(t)
rhs += (chi*uu.dot(grad(chi))+dd.dot(grad(chi)))*uu
rhs += chi*dd.jacobian(x)*uu+chi*uu.jacobian(x)*dd+dd.jacobian(x)*dd
rhs -= nu*(2*uu.jacobian(x)*grad(chi)+lap(chi)*uu+lap(dd))
rhs += pp*grad(chi)
exact("generic_cutoff_full_force_identity", lhs-at0(rhs))
AA = S.Matrix([jet(f"A{i}") for i in range(3)])
exact("generic_cutoff_vector_potential_product", at0(curl(chi*AA)-chi*curl(AA)-grad(chi).cross(AA)))
exact("generic_cutoff_divergence_of_curl", at0(sum(S.diff(curl(chi*AA)[i],x[i]) for i in range(3))))
for j in labels:
    exact(f"base_{j}_vector_potential_original_sign", -k[j].cross(k[j].cross(c[j]))/k[j].dot(k[j])-c[j])

PROOF_AFTER = hashlib.sha256(PROOF.read_bytes()).hexdigest()
assertion("proof_bytes_stable_during_replay", PROOF_BEFORE == PROOF_AFTER, PROOF_AFTER)
receipt = {"status": "pass", "check_count": len(ROWS), "checks": ROWS,
           "resource": RESOURCE, "sympy_version": S.__version__,
           "elapsed_seconds": time.monotonic()-STARTED,
           "proof_sha256": PROOF_AFTER,
           "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           "proof_scope": "Exact original vectors and all sparse Fourier modes; full pressure/force signs; metric and stress maps; arbitrary-jet localization product identity. Analytic smoothness and amplitude bounds are proved in TeX.",
           "Lean_run": False, "Navier_Stokes_counterexample": False}
out = ROOT / "checks" / "s6_three_point_fields_checks.json"
out.parent.mkdir(exist_ok=True)
out.write_text(json.dumps(receipt, indent=2)+"\n", encoding="utf-8")
print(json.dumps({"status": "pass", "check_count": len(ROWS),
                  "resource": RESOURCE, "elapsed_seconds": receipt["elapsed_seconds"],
                  "proof_sha256": PROOF_AFTER}, indent=2))
