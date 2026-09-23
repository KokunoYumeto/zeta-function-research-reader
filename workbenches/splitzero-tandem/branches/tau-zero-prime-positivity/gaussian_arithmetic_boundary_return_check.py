"""Bounded numerical checks for GAB10--49; the Markdown contains the proof."""

from pathlib import Path
import hashlib
import json
import mpmath as mp

mp.mp.dps = 70
ROOT = Path(__file__).resolve().parent
PROOF = ROOT / "GAUSSIAN_ARITHMETIC_BOUNDARY_RETURN.md"
checks = []


def serial(x):
    if isinstance(x, mp.mpc):
        return {"real": mp.nstr(x.real, 60), "imag": mp.nstr(x.imag, 60)}
    return mp.nstr(x, 60)


def record(name, error, threshold, **data):
    error = abs(error)
    passed = bool(error < threshold)
    row = {
        "name": name,
        "absolute_error": serial(error),
        "threshold": serial(threshold),
        "passed": passed,
    }
    row.update({k: serial(v) for k, v in data.items()})
    checks.append(row)
    if not passed:
        raise AssertionError(row)


def gaussian_series(lam, s):
    # All lambda used here are positive real numbers.
    # For A=max(0,-Re(s)), x>=L gives
    # x^A exp(-lambda*x²) <= L^A exp(-lambda*L²)
    #                  exp(-(lambda-A/(2L²))*(x²-L²)).
    # Monotonicity and Gaussian integration bound the omitted discrete tail.
    A = max(mp.mpf(0), -mp.re(s))
    L = int(mp.ceil(mp.sqrt(mp.mpf(300) / lam))) + 1
    c = lam - A / (2 * L**2)
    assert c > 0
    tail_bound = L**A * mp.exp(-lam * L**2) / (2 * c * L)
    assert tail_bound < mp.mpf("1e-120")
    value = mp.fsum(mp.exp(-lam * n*n) * mp.power(n, -s)
                    for n in range(1, L+1))
    return value, tail_bound, L


def singular(lam, s):
    return mp.gamma((1-s)/2) * mp.power(lam, (s-1)/2) / 2


def expansion(lam, s, N):
    return singular(lam, s) + mp.fsum(
        mp.power(-lam, k) * mp.zeta(s-2*k) / mp.factorial(k)
        for k in range(N+1)
    )


def collision_expansion(lam, j, N):
    h = mp.fsum(mp.mpf(1)/r for r in range(1, j+1))
    return (
        mp.fsum(mp.power(-lam, k)*mp.zeta(1+2*j-2*k)/mp.factorial(k)
                for k in range(N+1) if k != j)
        + mp.power(-lam, j) * (h+mp.euler-mp.log(lam))/(2*mp.factorial(j))
    )


for s in [mp.mpf("0.3")+mp.mpf("1.7")*1j,
          mp.mpf("-2.4")+mp.mpf("0.8")*1j]:
    lam = mp.mpf("0.003")
    z, bound, terms = gaussian_series(lam, s)
    # N=5 includes every residue through lambda^5.
    err = z - expansion(lam, s, 5)
    record("finite expansion away from collisions", err, mp.mpf("1e-13"),
           lam=lam, s=s, tail_bound=bound, terms=terms)

for j in [0, 1, 2]:
    lam = mp.mpf("0.003")
    z, bound, terms = gaussian_series(lam, 1+2*j)
    err = z - collision_expansion(lam, j, 5)
    record("positive-odd collision including logarithm", err, mp.mpf("1e-13"),
           lam=lam, j=j, tail_bound=bound, terms=terms)
    h = mp.mpf("1e-25") * 1j
    grouped = (singular(lam, 1+2*j+h)
               + mp.power(-lam, j)*mp.zeta(1+h)/mp.factorial(j))
    harmonic = mp.fsum(mp.mpf(1)/r for r in range(1, j+1))
    collision = mp.power(-lam, j)*(harmonic+mp.euler-mp.log(lam))/(2*mp.factorial(j))
    record("removable collision from distinct-pole coordinates",
           grouped-collision, mp.mpf("1e-22"), lam=lam, j=j)
    z_near, _, _ = gaussian_series(lam, 1+2*j+h)
    Y = z_near - singular(lam, 1+2*j+h)
    record("retained coordinate positive-odd residue",
           h*Y-mp.power(-lam,j)/mp.factorial(j),
           mp.mpf("1e-22"), lam=lam, j=j)

# Independent contour evaluation of the exact remainder, with a bounded
# truncation. The proof supplies its full infinite-contour convergence.
s = mp.mpf("0.3")+mp.mpf("1.7")*1j
lam = mp.mpf("0.2")
left = mp.mpf("-2.5")
def integrand(t):
    z = left + 1j*t
    return mp.gamma(z)*mp.power(lam,-z)*mp.zeta(s+2*z)/(2*mp.pi)
remainder = mp.quad(integrand, [-70,-40,-20,-10,-4,0,4,10,20,40,70])
z, bound, terms = gaussian_series(lam,s)
record("left-contour remainder N=2 alpha=1/2",
       z-expansion(lam,s,2)-remainder, mp.mpf("1e-33"),
       lam=lam, s=s, contour_height=70, tail_bound=bound)

rho = mp.zetazero(1)
lam = mp.mpf("0.0001")
d = lam/mp.pi
z, bound, terms = gaussian_series(lam,rho)
S = singular(lam,rho)
Y = z-S
B = mp.power(mp.pi,-rho/2)*mp.gamma(rho/2)
I = 2*mp.sqrt(d)*B*z
full_sector = (mp.power(mp.pi,-mp.mpf("0.5"))*mp.gamma(rho/2)
               *mp.gamma((1-rho)/2)*mp.power(d,rho/2))
record("full MRT singular-sector multiplier identity",
       2*mp.sqrt(d)*B*S-full_sector, mp.mpf("1e-65"),
       lam=lam, rho=rho)
record("nonzero first retained coefficient with next two corrections",
       Y/lam+mp.zeta(rho-2)-lam*mp.zeta(rho-4)/2+lam**2*mp.zeta(rho-6)/6,
       mp.mpf("1e-9"), lam=lam, rho=rho, tail_bound=bound, terms=terms)
predicted = (-2*mp.pi*B*mp.zeta(rho-2)*mp.power(d,mp.mpf("1.5"))
             + mp.pi**2*B*mp.zeta(rho-4)*mp.power(d,mp.mpf("2.5"))
             - mp.pi**3*B*mp.zeta(rho-6)*mp.power(d,mp.mpf("3.5"))/3)
record("full MRT retained residual through d^(7/2)",
       I-full_sector-predicted, mp.mpf("1e-20"), d=d, rho=rho)

s = mp.mpf("0.7")+mp.mpf("2.1")*1j
lam = mp.mpf("0.1")
derivative = mp.diff(lambda x: singular(x,s),lam)
record("singular-sector exact shift derivative",
       derivative+singular(lam,s-2), mp.mpf("1e-65"), s=s, lam=lam)

# Independent real-half-plane integral for the continuous measure moment.
s = mp.mpf("-0.3")
lam = mp.mpf("0.2")
continuous_moment = mp.quad(lambda u: mp.exp(-lam*u*u)*mp.power(u,-s),
                            [0,1,3,10,mp.inf])
record("continuous Gaussian measure gives the full singular sector",
       continuous_moment-singular(lam,s), mp.mpf("1e-65"), s=s, lam=lam)

result = {
    "scope": "Bounded numerical regression checks; analytic proofs are GAB1--49.",
    "precision_decimal_digits": mp.mp.dps,
    "proof_sha256": hashlib.sha256(PROOF.read_bytes()).hexdigest(),
    "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "check_count": len(checks),
    "all_passed": all(x["passed"] for x in checks),
    "checks": checks,
}
out = ROOT / "gaussian_arithmetic_boundary_return_check.json"
out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"check_count":result["check_count"],"all_passed":result["all_passed"],
                  "proof_sha256":result["proof_sha256"],"output":str(out)},indent=2))
