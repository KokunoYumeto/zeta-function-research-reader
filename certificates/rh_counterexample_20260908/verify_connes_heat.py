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
import sys


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

ROOT = Path(__file__).resolve().parents[2]
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

source = ROOT / "tex" / "satellites" / "25_connes_complete_heat_transport.tex"
receipt = {"schema_version": 1, "run_class": "non-critical", "resource": RESOURCE,
           "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           "sympy_version": sp.__version__, "workers": 1, "check_count": len(checks),
           "all_passed": True, "elapsed_seconds": round(time.monotonic()-started,4),
           "manuscript_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
           "checks": checks,
           "limits": ["No numerical zero search", "No proof of source topology identification",
                      "No Lean certification", "Symbolic replays supplement complete written proofs"]}
if "--write" in sys.argv:
    (Path(__file__).resolve().parent/"connes_heat_results.json").write_text(json.dumps(receipt,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"all_passed": True, "checks": len(checks), "resource": RESOURCE}))
