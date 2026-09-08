"""Exact checks of the retained S6 source data and marked real T4 -> T3 map.

One non-critical Python worker. No network, Lean, numerical zero search,
or proof of the source manuscript's global S6 claim is performed.
"""
from pathlib import Path
import ctypes
import hashlib
import json
import os


def install_memory_ceiling():
    if os.name != "nt":
        raise RuntimeError("The specified replay requires a Windows job ceiling")
    from ctypes import wintypes as W
    class Basic(ctypes.Structure):
        _fields_ = [("User", ctypes.c_int64), ("JobUser", ctypes.c_int64),
                    ("Flags", W.DWORD), ("MinWS", ctypes.c_size_t),
                    ("MaxWS", ctypes.c_size_t), ("Active", W.DWORD),
                    ("Affinity", ctypes.c_size_t), ("Priority", W.DWORD),
                    ("Scheduling", W.DWORD)]
    class IO(ctypes.Structure):
        _fields_ = [(name, ctypes.c_uint64) for name in
                    ("ReadOps", "WriteOps", "OtherOps", "ReadBytes", "WriteBytes", "OtherBytes")]
    class Extended(ctypes.Structure):
        _fields_ = [("Basic", Basic), ("IO", IO),
                    ("ProcessMemory", ctypes.c_size_t), ("JobMemory", ctypes.c_size_t),
                    ("PeakProcessMemory", ctypes.c_size_t), ("PeakJobMemory", ctypes.c_size_t)]
    api = ctypes.WinDLL("kernel32", use_last_error=True)
    api.CreateJobObjectW.argtypes = [ctypes.c_void_p, W.LPCWSTR]
    api.CreateJobObjectW.restype = W.HANDLE
    api.SetInformationJobObject.argtypes = [W.HANDLE, ctypes.c_int, ctypes.c_void_p, W.DWORD]
    api.SetInformationJobObject.restype = W.BOOL
    api.AssignProcessToJobObject.argtypes = [W.HANDLE, W.HANDLE]
    api.AssignProcessToJobObject.restype = W.BOOL
    api.GetCurrentProcess.restype = W.HANDLE
    job = api.CreateJobObjectW(None, None)
    if not job:
        raise ctypes.WinError(ctypes.get_last_error())
    limits = Extended()
    limits.Basic.Flags = 0x00000200
    limits.JobMemory = 5_000_000_000
    if not api.SetInformationJobObject(job, 9, ctypes.byref(limits), ctypes.sizeof(limits)):
        raise ctypes.WinError(ctypes.get_last_error())
    if not api.AssignProcessToJobObject(job, api.GetCurrentProcess()):
        raise ctypes.WinError(ctypes.get_last_error())
    return {"status": "enforced_windows_job", "ceiling_bytes": 5_000_000_000,
            "run_class": "non-critical", "worker_count": 1}


RESOURCE = install_memory_ceiling()
import sympy as S
ROOT = Path(__file__).resolve().parents[1]
rows = []


def exact(name, difference):
    entries = list(difference) if isinstance(difference, S.MatrixBase) else [difference]
    residuals = [S.expand(S.together(t).as_numer_denom()[0]) for t in entries]
    if any(t != 0 for t in residuals):
        raise AssertionError((name, residuals))
    rows.append({"id": name, "status": "pass", "entries": len(entries),
                 "method": "exact_symbolic_zero_residual"})


A1 = S.Matrix([[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]])
A2 = S.Matrix([[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]])
M0 = S.Matrix([[1,0,0,0],[0,1,0,0],[0,1,1,0],[-1,0,0,1]])
v1 = S.Matrix([1,2,-4,0]); v2 = S.Matrix([-1,-3,3,0])
e = [S.eye(4)[:,j] for j in range(4)]
P = S.eye(3).row_join(S.zeros(3,1)); inclusion = P.T
B1 = S.Matrix([[1,0,0],[6,0,1],[-6,-1,-1]])
B2 = S.Matrix([[1,0,0],[0,0,-1],[-6,1,0]])
B0 = S.Matrix([[1,0,0],[0,1,0],[0,1,1]])
c1 = S.Matrix([1,2,-4])/3; c2 = S.Matrix([-1,-3,3])/4
c0 = S.Matrix([0,0,1])

exact("original_full_matrices_fix_fourth_circle",
      S.Matrix.hstack(A1*e[3]-e[3], A2*e[3]-e[3], M0*e[3]-e[3]))
exact("original_full_monodromy_product_and_orders",
      S.Matrix.hstack(A1*A2*M0-S.eye(4), A1**3-S.eye(4), A2**4-S.eye(4)))
exact("all_three_full_projection_intertwiners",
      S.Matrix.hstack(P*A1-B1*P, P*A2-B2*P, P*M0-B0*P))
exact("quotient_product_orders_and_volume",
      S.Matrix(list(B1*B2*B0-S.eye(3))+list(B1**3-S.eye(3))
               +list(B2**4-S.eye(3))+[B1.det()-1,B2.det()-1,B0.det()-1]))
exact("marked_projection_section_and_kernel",
      S.Matrix.hstack(P*inclusion-S.eye(3), P*e[3]))
defects = [S.Matrix([[0,0,0],[0,0,0],[0,0,0],r])
           for r in [[-2,1,0],[3,0,1],[-1,0,0]]]
exact("full_original_section_defects",
      S.Matrix.hstack(A1*inclusion-inclusion*B1-defects[0],
                      A2*inclusion-inclusion*B2-defects[1],
                      M0*inclusion-inclusion*B0-defects[2]))
l1,l2,l3 = S.symbols("l1 l2 l3")
exact("no_alternative_linear_cusp_equivariant_section_equation",
      S.Matrix([[l1,l2,l3]])*(B0-S.eye(3))-S.Matrix([[0,l3,0]]))
exact("original_twists_and_all_three_directions",
      S.Matrix(list(A1*v1-v1)+list(A2*v2-v2)+list(P*v1/3-c1)
               +list(P*v2/4-c2)+list(P*(M0-S.eye(4))*e[1]-c0)))

# This is the original two-dimensional cusp image lattice before its
# restriction by P, including the direction that P kills.
tor_inclusion = S.Matrix.hstack(e[2],e[3])
source_B0 = S.Matrix([[0,1],[-1,0]])
quotient_tor_inclusion = S.Matrix([0,0,1])
exact("original_cusp_B0_and_R2_T2_restriction_diagram",
      S.Matrix.hstack((M0-S.eye(4))[:,:2]-tor_inclusion*source_B0,
                      P.T*(P*tor_inclusion-quotient_tor_inclusion*S.Matrix([[1,0]]))))

directions = S.Matrix.hstack(c1,c2,c0)
direction_inverse = S.Matrix([[9,-3,0],[8,-4,0],[6,-1,1]])
exact("three_directions_determinant_and_explicit_inverse",
      S.Matrix([directions.det()+S.Rational(1,12)]
               +list(directions*direction_inverse-S.eye(3))
               +list(direction_inverse*directions-S.eye(3))))
K = S.Matrix([[4,0,1],[3,0,1],[0,1,0]])
pairing = S.Matrix([[0,-S.Rational(1,4),1],[-S.Rational(1,3),0,1],
                    [S.Rational(2,3),-S.Rational(3,4),0]])
exact("original_wave_basis_and_full_cross_pairings",
      S.Matrix([K.det()+1]+list(K*directions-pairing)))

affine_residuals = []
free_first_shifts = []
for label,B,c,m,original_v in [(1,B1,c1,3,v1),(2,B2,c2,4,v2)]:
    affine_residuals += list(B*c-c)
    for k in range(1,m+1):
        translation = sum((B**r*c for r in range(k)), S.zeros(3,1))
        affine_residuals += list(translation-k*c)
        affine_residuals += list(S.Matrix([[1,0,0]])*B**k-S.Matrix([[1,0,0]]))
        if k<m:
            assert translation[0].is_integer is False
            free_first_shifts.append({"point":label,"power":k,"first_shift":str(translation[0])})
    affine_residuals += list(m*c-P*original_v)
exact("finite_affine_orders_and_every_nonidentity_freeness_witness",
      S.Matrix(affine_residuals))

base_translation = S.Matrix(S.symbols("b1 b2 b3"))
marked_point = S.Matrix(S.symbols("y1 y2 y3"))
conjugacy = []
for B,c in [(B1,c1),(B2,c2)]:
    next_translation = B*base_translation-c
    conjugacy += list(B*(marked_point-base_translation)+c+next_translation-B*marked_point)
exact("full_logarithmic_overlap_affine_conjugacy",S.Matrix(conjugacy))
exact("uncorrected_three_affine_maps_marking_defect",
      c1+B1*c2-S.Matrix([S.Rational(1,12),-S.Rational(1,12),S.Rational(1,6)]))

# Verify the full real period formula for J=Pi^{-1} i Pi. No period
# coefficient is replaced by a special constant, and the determinant E
# remains the original 6*mu_I^2-tau_I*beta_I on its nonzero domain.
mr,mi,tr,ti,br,bi = S.symbols("mu_R mu_I tau_R tau_I beta_R beta_I",real=True)
real_period = S.Matrix([[6*mr,tr,1,0],[6*mi,ti,0,0],
                        [br,mr,0,1],[bi,mi,0,0]])
i_operator = S.diag(S.Matrix([[0,-1],[1,0]]),S.Matrix([[0,-1],[1,0]]))
detE = 6*mi**2-ti*bi
columns = []
for index in range(4):
    re_p,im_p,re_q,im_q = real_period[:,index]
    a_prime = (mi*re_p-ti*re_q)/detE
    b_prime = (-bi*re_p+6*mi*re_q)/detE
    c_prime = -im_p-6*mr*a_prime-tr*b_prime
    d_prime = -im_q-br*a_prime-mr*b_prime
    columns.append(S.Matrix([a_prime,b_prime,c_prime,d_prime]))
J = S.Matrix.hstack(*columns)
exact("complete_original_real_period_complex_structure_formula",
      real_period*J-i_operator*real_period)

exact("individual_wave_covector_transforms_retained",
      S.Matrix.vstack(K[0,:]*B1-S.Matrix([[-2,-1,-1]]),
                      K[1,:]*B2-S.Matrix([[-3,1,0]]),K[2,:]*B0-K[2,:]))
orbit_residuals = []
wave_orbits = {}
for label,k,B,c,m in [(1,K[0,:],B1,c1,3),(2,K[1,:],B2,c2,4)]:
    orbit = [k*B**r for r in range(m)]
    wave_orbits[str(label)] = [list(map(str,row)) for row in orbit]
    orbit_residuals += list(k*B**m-k)
    for row in orbit:
        orbit_residuals += list(row*c)
exact("finite_orbit_sum_field_equivariance_frequency_identities",S.Matrix(orbit_residuals))

proof = ROOT/'tex/s6_three_point_quotient.tex'
receipt = {"schema_version":1,"status":"pass","all_passed":True,
           "check_count":len(rows),"checks":rows,"resource":RESOURCE,
           "workers":1,"run_class":"non-critical","sympy_version":S.__version__,
           "checker_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           "proof":{"path":"tex/s6_three_point_quotient.tex",
                    "sha256":hashlib.sha256(proof.read_bytes()).hexdigest()},
           "finite_freeness_first_coordinate_witnesses":free_first_shifts,
           "finite_wave_covector_orbits":wave_orbits,
           "scope":"Exact source-data and marked real fibre-quotient identities supplement the complete written proof. No certification of the original global S6 claim, no global smooth quotient at the singular cusp, and no NS endpoint are asserted."}
target=ROOT/'checks/s6_three_point_forcing_checks.json'
target.write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({"status":"pass","check_count":len(rows),"resource":RESOURCE,
                  "receipt_sha256":hashlib.sha256(target.read_bytes()).hexdigest(),
                  "proof_sha256":receipt['proof']['sha256']}))
