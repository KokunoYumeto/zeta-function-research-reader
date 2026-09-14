"""Exact finite matrix checks for the two-actual-metric commutator transfer.

The written proof establishes the general norm bound; fixtures do not.
All inherited sealed artifacts are checked unchanged. No Lean or remote work.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import unittest

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parent
SC = ROOT.parent / "constituent_curvature"
QUOT = ROOT.parent / "quotient_compensation_review"
NOTE_SHA = "055d9ab41d454ff8b196d83e061df3e37c9bd50cbd87636e207f3bc7c7f2bfe2"
SEALS = [(SC, "946124f26860a285691780949bcb6967c280c8bb18956f0e86c1accfd93d77da", 28),
         (QUOT, "2d3c57653a9fd5806f21fa9d8dfbfdffe13446487de3fce7040ff827e72ba87b", 20)]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(ok, message):
    if not ok:
        raise AssertionError(message)


def verify_inherited():
    for folder, receipt_hash, count in SEALS:
        receipt = folder / "REVIEW_RECEIPT.json"
        require(digest(receipt) == receipt_hash, "inherited receipt unchanged")
        rows = json.loads(receipt.read_text(encoding="utf-8"))["artifacts"]
        require(len(rows) == count, "inherited artifact count")
        for row in rows:
            file = folder / row["path"]
            require(file.stat().st_size == row["bytes"] and digest(file) == row["sha256"], "inherited artifact unchanged: " + row["path"])


verify_inherited()
spec = importlib.util.spec_from_file_location("sealed_sc_matrix_helpers", SC / "check_constituent_curvature.py")
sc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sc)
s, equal, simp = sc.s, sc.equal, sc.simp
MUTATION = None


def clean(matrix):
    return matrix.applyfunc(simp)


def comm(a, b):
    return clean(a * b - b * a)


def adj(a, g):
    return clean(g.inv() * a.H * g)


def setup(name, v, diagonal, a, t, k, eta):
    n = a.rows
    e0, ell = s.eye(n)[:, 0], s.eye(n)[n - 1, :]
    rankone = e0 * ell
    generator = a + t * rankone - s.Rational(k, 2) * s.eye(n)
    g = clean(7 * v.H * v)
    root = clean(v.inv() * diagonal * v)
    comparison = clean(root**2)
    h = clean(g * comparison)
    b = comparison - s.eye(n)
    td = adj(generator, g)
    xg = clean(td + generator)
    xh = clean(comparison.inv() * td * comparison + generator)
    yh = clean(root * xh * root.inv())
    z = clean(comm(root, generator) * root.inv())
    return dict(name=name, n=n, v=v, diagonal=diagonal, a=a, t=t, k=k,
                e0=e0, ell=ell, rankone=rankone, tgen=generator, g=g, h=h,
                root=root, comparison=comparison, b=b, td=td,
                xg=xg, xh=xh, yh=yh, z=z, eta=eta,
                alpha=1-eta, beta=1+eta)


def fixtures():
    # Actual increasing-power companion algebra with two retained double roots.
    polynomial = (sc.S - 1)**2 * (sc.S + 2)**2
    a = sc.mul_matrix(sc.S, polynomial)
    p, jordan = a.jordan_form()
    diagonal = s.diag(s.Rational(3, 4), s.Rational(3, 4), s.Rational(5, 4), s.Rational(5, 4))
    equal(comm(diagonal, jordan), s.zeros(4), "retained primary blocks commute")
    w = s.diag(s.Matrix([[2, 1+s.I], [0, 3]]), s.Matrix([[1, 1-s.I], [0, 2]]))
    v = clean(w * p.inv())
    rows = [setup("repeated_companion_nonscalar_commuting", v, diagonal, a, 0, 3, s.Rational(9, 16)),
            setup("repeated_companion_rankone_noncommuting", v, diagonal, a, 1+2*s.I, 3, s.Rational(9, 16))]
    # Separate exact two-dimensional control fixture, not a claimed arithmetic packet.
    v2 = s.Matrix([[2, 1+s.I], [0, 3]])
    t0 = s.Matrix([[0, 1], [1, 0]])
    a2 = clean(v2.inv() * t0 * v2)
    rows.append(setup("two_dimensional_sharp_cross_term", v2,
                      s.diag(s.Rational(3, 4), s.Rational(5, 4)), a2, 0, 0, s.Rational(9, 16)))
    rows.append(setup("nonidentity_scalar_rescaling", v2,
                      s.Rational(6, 5)*s.eye(2), a2, 1+s.I, 2, s.Rational(11, 25)))
    return rows


FIXTURES = fixtures()


def norm2(matrix):
    require(matrix.shape == (2, 2), "explicit two-dimensional norm only")
    square = matrix.H * matrix
    tr, det = simp(s.trace(square)), simp(square.det())
    return simp(s.sqrt((tr + s.sqrt(tr**2 - 4*det))/2))


def original_norm2(matrix, f):
    # The exact isometry includes the original mass sqrt(7), not a changed Gram.
    observation = s.sqrt(7) * f["v"]
    equal(observation.H * observation, f["g"], "original source mass in norm observation")
    return norm2(clean(observation * matrix * observation.inv()))


class MetricTransferTests(unittest.TestCase):
    def test_01_pins_and_untouched_previous_seals(self):
        require(digest(ROOT / "ACTUAL_METRIC_COMMUTATOR_TRANSFER_CAPTURE.md") == NOTE_SHA, "captured complete note")
        verify_inherited()

    def test_02_actual_positive_metrics_and_square_root(self):
        for f in FIXTURES:
            sc.positive_gram(f["g"], "original nonidentity G")
            sc.positive_gram(f["h"], "actual H=GC")
            equal(f["g"].inv()*f["h"], f["comparison"], "actual metric comparison")
            equal(adj(f["root"], f["g"]), f["root"], "G-self-adjoint root")
            equal(f["root"]**2, f["comparison"], "literal square root")
            for eigenvalue in f["diagonal"].diagonal():
                require(eigenvalue > 0, "positive exact root eigenvalue")
                require(eigenvalue**2 >= f["alpha"] and eigenvalue**2 <= f["beta"], "admitted alpha/beta bounds")
            require(f["alpha"] > 0, "positive admitted allowance")

    def test_03_exact_adjoint_and_unconjugated_difference(self):
        for f in FIXTURES:
            equal(f["xh"], adj(f["tgen"], f["h"])+f["tgen"], "original H-adjoint control")
            equal(adj(f["xh"], f["h"]), f["xh"], "H-self-adjoint control")
            equal(f["comparison"]*f["xh"], f["xg"]+f["td"]*f["b"]+f["b"]*f["tgen"], "full retained CX_H identity")
            delta = comm(f["b"], f["td"]) if MUTATION == "reverse_adjoint_commutator" else comm(f["td"], f["b"])
            equal(f["xh"]-f["xg"], f["comparison"].inv()*delta, "exact adjoint commutator order")

    def test_04_isometry_and_full_Hermitian_error(self):
        for f in FIXTURES:
            root, g = f["root"], f["g"]
            equal(root.H*g*root, f["h"], "explicit H-to-G isometry")
            equal(f["yh"], root.inv()*f["td"]*root+root*f["tgen"]*root.inv(), "conjugated control factor order")
            zd = adj(f["z"], g)
            equal(zd, root.inv()*comm(f["td"], root), "Z adjoint sign and order")
            target = f["z"]-zd if MUTATION == "erase_Hermitian_cross_term" else f["z"]+zd
            equal(f["yh"]-f["xg"], target, "retained full Hermitian error")
            equal(adj(f["yh"], g), f["yh"], "transported control G-self-adjoint")

    def test_05_Sylvester_and_exact_integral_entries(self):
        for f in FIXTURES:
            root, tgen = f["root"], f["tgen"]
            y, rhs = comm(root, tgen), comm(f["b"], tgen)
            equal(root*y+y*root, rhs, "exact Sylvester equation")
            v, diagonal = f["v"], f["diagonal"]
            entries = clean(v*rhs*v.inv())
            # Integral of each original exp(-(s_i+s_j)r) entry, not numerical quadrature.
            solved = s.zeros(f["n"])
            for i in range(f["n"]):
                for j in range(f["n"]):
                    denominator = diagonal[i,i] + (2 if MUTATION == "wrong_Sylvester_denominator" else 1)*diagonal[j,j]
                    solved[i,j] = entries[i,j]/denominator
            equal(v.inv()*solved*v, y, "exact positive-sum Sylvester integral")

    def test_06_exact_norm_witness_and_sharper_cross_term(self):
        f = FIXTURES[2]
        eg, eh = original_norm2(f["xg"], f), original_norm2(f["yh"], f)
        hermitian_error = original_norm2(f["z"]+adj(f["z"], f["g"]), f)
        zbound = 2*original_norm2(f["z"], f)
        commnorm = original_norm2(comm(f["b"], f["tgen"]), f)
        equal(eg, 2, "exact original G radius")
        equal(eh, s.Rational(34,15), "exact H radius through displayed isometry")
        equal(hermitian_error, s.Rational(4,15), "exact Hermitian error")
        equal(zbound, s.Rational(4,3), "unretained-cross-term allowance")
        equal(commnorm, 1, "actual commutator norm")
        equal(s.Abs(eh-eg), hermitian_error, "reverse triangle equality fixture")
        require(hermitian_error < zbound, "retaining Hermitian cross term strictly sharper")
        require(s.Abs(eh-eg) <= commnorm/f["alpha"], "one exact finite example of stated general allowance")
        equal(original_norm2(comm(f["root"], f["tgen"]), f), s.Rational(1,2), "exact square-root commutator norm")
        equal(original_norm2(f["root"].inv(), f), s.Rational(4,3), "exact inverse-root norm")

    def test_07_coordinate_covariance_with_original_unit(self):
        for f in FIXTURES:
            n = f["n"]
            u = s.eye(n)
            for j in range(n):
                u[j,j] = j+2+s.I
                if j+1<n:
                    u[j,j+1] = 1-s.I
            inv = u.inv()
            g, h, tgen = u.H*f["g"]*u, u.H*f["h"]*u, inv*f["tgen"]*u
            c, b, root = inv*f["comparison"]*u, inv*f["b"]*u, inv*f["root"]*u
            equal(g.inv()*h, c, "coordinate covariance of actual comparison")
            equal(root**2, c, "coordinate covariance of actual root")
            equal(adj(root,g), root, "new-coordinate positive self-adjoint root")
            equal(adj(tgen,g), inv*f["td"]*u, "coordinate covariance of original adjoint")
            equal(comm(b,tgen), inv*comm(f["b"],f["tgen"])*u, "commutator covariance")
            equal((f["v"]*u)*tgen*(f["v"]*u).inv(), f["v"]*f["tgen"]*f["v"].inv(), "identical norm observation under coordinate change")
            equal((inv*f["e0"])*(f["ell"]*u), inv*f["rankone"]*u, "unit and top row both transported")

    def test_08_nonscalar_and_scalar_zero_error_cases(self):
        for f in (FIXTURES[0], FIXTURES[3]):
            equal(comm(f["b"],f["tgen"]),s.zeros(f["n"]),"actual commuting comparison")
            equal(f["xh"],f["xg"],"unconjugated zero error")
            equal(f["yh"],f["xg"],"transported zero error and equal radii")
            require(f["h"] != f["g"], "zero error does not identify metrics")
        require(len(set(FIXTURES[0]["diagonal"].diagonal())) > 1, "genuinely nonscalar commuting root")
        require(comm(FIXTURES[1]["b"],FIXTURES[1]["tgen"]) != s.zeros(4), "retained rank-one parameter makes noncommuting example")

    def test_09_rankone_term_and_source_mass_retained(self):
        for f in FIXTURES:
            n=f["n"]
            x=s.Matrix([j+1+s.I*(j+2) for j in range(n)])
            br=f["b"]*f["e0"]*f["ell"]-f["e0"]*f["ell"]*f["b"]
            equal(comm(f["b"],f["rankone"]),br,"both original rank-one terms")
            equal(br*x,(f["b"]*f["e0"])*(f["ell"]*x)-f["e0"]*(f["ell"]*f["b"]*x),"literal unit/top-row action")
            equal(comm(f["b"],f["tgen"]),comm(f["b"],f["a"])+f["t"]*br,"A plus original parameter term; centering scalar cancels")
            equal(x.H*f["h"]*x,(f["root"]*x).H*f["g"]*(f["root"]*x),"actual vector-norm isometry with all masses")
            equal((s.sqrt(7)*f["v"]).H*(s.sqrt(7)*f["v"]),f["g"],"mass seven kept in source observation")


TARGETS={"reverse_adjoint_commutator":"test_03_exact_adjoint_and_unconjugated_difference",
         "erase_Hermitian_cross_term":"test_04_isometry_and_full_Hermitian_error",
         "wrong_Sylvester_denominator":"test_05_Sylvester_and_exact_integral_entries"}


def child(args):
    global MUTATION
    MUTATION=args.mutation
    suite=(unittest.TestSuite([MetricTransferTests(TARGETS[MUTATION])]) if MUTATION else unittest.defaultTestLoader.loadTestsFromTestCase(MetricTransferTests))
    result=unittest.TextTestRunner(verbosity=2).run(suite)
    verify_inherited()
    row=dict(schema=1,source_sha256=NOTE_SHA,checker_sha256=digest(Path(__file__)),
             inherited_sealed_artifacts_unchanged=48,methods=result.testsRun,
             failures=len(result.failures),errors=len(result.errors),successful=result.wasSuccessful(),
             mutation=MUTATION,sympy_version=s.__version__,
             scope="Exact finite identities and one exact norm witness; the general norm inequality is established only by the separately reviewed written proof.")
    if args.receipt:
        Path(args.receipt).write_text(json.dumps(row,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    return 0 if result.wasSuccessful() else 1


def run_all():
    rows=[]
    for mutation in (None,*TARGETS):
        paired=[]
        for optimized in (False,True):
            name=(mutation or "normal")+("_optimized" if optimized else "_ordinary")
            receipt,log=ROOT/(name+".json"),ROOT/(name+".log")
            command=[sys.executable]+(["-O"] if optimized else [])+[str(Path(__file__)),"--receipt",str(receipt)]
            if mutation:
                command += ["--mutation",mutation]
            with log.open("w",encoding="utf-8",newline="\n") as out:
                process=subprocess.run(command,stdout=out,stderr=subprocess.STDOUT,timeout=240,check=False)
            row=json.loads(receipt.read_text(encoding="utf-8"))
            require(process.returncode==(1 if mutation else 0),name+": expected exit")
            require(row["methods"]==(1 if mutation else 9) and row["failures"]==(1 if mutation else 0) and row["errors"]==0,name+": exact outcome")
            paired.append(receipt.read_bytes())
            rows.append(dict(name=name,exit_code=process.returncode,command=command,
                             receipt=receipt.name,receipt_sha256=digest(receipt),log=log.name,log_sha256=digest(log)))
            print(name+": expected outcome",flush=True)
        require(paired[0]==paired[1],"paired ordinary/optimized receipts identical")
    verify_inherited()
    final=dict(schema=1,status="all_expected_outcomes_verified",source_sha256=NOTE_SHA,
               checker_sha256=digest(Path(__file__)),successful_methods_each_mode=9,
               substantive_mutations_each_mode=3,inherited_sealed_artifacts_unchanged=48,
               sequential=True,paired_receipts_identical=True,runs=rows)
    receipt=ROOT/"EXECUTION_RECEIPT.json"
    receipt.write_text(json.dumps(final,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps(dict(receipt=str(receipt),sha256=digest(receipt)),indent=2),flush=True)
    return 0


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--run-all",action="store_true")
    parser.add_argument("--receipt")
    parser.add_argument("--mutation",choices=tuple(TARGETS))
    args=parser.parse_args()
    return run_all() if args.run_all else child(args)


if __name__=="__main__":
    sys.exit(main())
