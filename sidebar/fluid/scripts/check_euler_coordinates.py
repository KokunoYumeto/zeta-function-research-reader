"""Exact symbolic checks for the axisymmetric Euler/Navier--Stokes reduction.

Run from any directory with Python and SymPy.  The output JSON is written into
the sibling ``checks`` directory.  All fields are arbitrary smooth functions;
no evolution equation, boundary condition, or alleged singularity is assumed.
The coordinate calculation takes place on r > 0, with y1 = z, y2 = r**2/2.
This script checks algebraic differential identities, not a global existence
or a finite-time singularity claim.
"""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


def main() -> None:
    t, z = sp.symbols("t z", real=True)
    r = sp.symbols("r", positive=True)
    nu = sp.symbols("nu", nonnegative=True)
    psi = sp.Function("Psi")(t, r, z)
    gamma = sp.Function("Gamma")(t, r, z)
    pressure = sp.Function("p")(t, r, z)
    fr = sp.Function("f_r")(t, r, z)
    fphi = sp.Function("f_phi")(t, r, z)
    fz = sp.Function("f_z")(t, r, z)

    # The sign of Psi is part of the chosen convention and is retained.
    ur = sp.diff(psi, z) / r
    uz = -sp.diff(psi, r) / r
    uphi = gamma / r
    omega = sp.diff(ur, z) - sp.diff(uz, r)
    xi = omega / r

    def material(a: sp.Expr) -> sp.Expr:
        return sp.diff(a, t) + ur * sp.diff(a, r) + uz * sp.diff(a, z)

    def laplacian(a: sp.Expr) -> sp.Expr:
        return sp.diff(a, z, 2) + sp.diff(a, r, 2) + sp.diff(a, r) / r

    def lminus(a: sp.Expr) -> sp.Expr:
        return sp.diff(a, z, 2) + sp.diff(a, r, 2) - sp.diff(a, r) / r

    def lplus(a: sp.Expr) -> sp.Expr:
        return sp.diff(a, z, 2) + sp.diff(a, r, 2) + 3 * sp.diff(a, r) / r

    # These are the full cylindrical momentum residuals, including arbitrary p
    # and arbitrary force.  Their vanishing has not been assumed.
    rr = (material(ur) - uphi**2 / r + sp.diff(pressure, r)
          - nu * (laplacian(ur) - ur / r**2) - fr)
    rz = material(uz) + sp.diff(pressure, z) - nu * laplacian(uz) - fz
    rphi = (material(uphi) + ur * uphi / r
            - nu * (laplacian(uphi) - uphi / r**2) - fphi)
    gamma_residual = material(gamma) - nu * lminus(gamma) - r * fphi
    xi_residual = (material(xi) - sp.diff(gamma**2, z) / r**4
                   - nu * lplus(xi)
                   - (sp.diff(fr, z) - sp.diff(fz, r)) / r)

    checks: list[dict[str, object]] = []

    def check(name: str, identity: str, difference: sp.Expr) -> None:
        # Expand rational differential polynomials in arbitrary smooth fields;
        # exact cancellation leaves the integer zero, without a numerical test.
        reduced = sp.cancel(sp.expand(difference.doit()))
        checks.append({"name": name, "identity": identity,
                       "passed": reduced == 0,
                       "exact_remainder": sp.sstr(reduced)})

    check("divergence_free_streamfunction",
          "partial_r u_r + u_r/r + partial_z u_z = 0",
          sp.diff(ur, r) + ur / r + sp.diff(uz, z))
    check("vorticity_streamfunction_sign",
          "xi = (Psi_zz + Psi_rr - Psi_r/r)/r^2",
          xi - lminus(psi) / r**2)
    check("azimuthal_momentum_residual",
          "r R_phi = D Gamma - nu L_minus Gamma - r f_phi",
          r * rphi - gamma_residual)
    check("meridional_curl_momentum_residual",
          "partial_z R_r - partial_r R_z = r [D xi - r^-4 partial_z(Gamma^2) - nu L_plus xi - (partial_z f_r - partial_r f_z)/r]",
          sp.diff(rr, z) - sp.diff(rz, r) - r * xi_residual)
    check("pressure_curl_cancellation",
          "partial_z(partial_r p) - partial_r(partial_z p) = 0",
          sp.diff(pressure, r, z) - sp.diff(pressure, z, r))
    check("vector_laplacian_curl",
          "partial_z(Delta_scalar u_r - u_r/r^2) - partial_r(Delta_scalar u_z) = r L_plus xi",
          sp.diff(laplacian(ur) - ur / r**2, z)
          - sp.diff(laplacian(uz), r) - r * lplus(xi))

    y1, y2 = sp.symbols("y1 y2", real=True)
    a = sp.Function("a")(t, y1, y2)
    psi_y = sp.Function("psi")(t, y1, y2)
    u_z_y = sp.Function("U_z")(t, y1, y2)
    u_r_y = sp.Function("U_r")(t, y1, y2)

    def pullback(expression: sp.Expr) -> sp.Expr:
        return expression.subs({y1: z, y2: r**2 / 2}, simultaneous=True)

    a_rz = pullback(a)
    check("volume_coordinate_lminus",
          "L_minus[a(t,z,r^2/2)] = [a_y1y1 + 2 y2 a_y2y2](t,z,r^2/2)",
          lminus(a_rz) - pullback(sp.diff(a, y1, 2) + 2 * y2 * sp.diff(a, y2, 2)))
    check("volume_coordinate_lplus",
          "L_plus[a(t,z,r^2/2)] = [a_y1y1 + 2 y2 a_y2y2 + 4 a_y2](t,z,r^2/2)",
          lplus(a_rz) - pullback(sp.diff(a, y1, 2) + 2 * y2 * sp.diff(a, y2, 2) + 4 * sp.diff(a, y2)))
    check("volume_coordinate_material_derivative",
          "(partial_t + u_z partial_z + u_r partial_r) a_pull = [partial_t a + U_z partial_y1 a + sqrt(2 y2) U_r partial_y2 a]_pull",
          sp.diff(a_rz, t) + pullback(u_z_y) * sp.diff(a_rz, z)
          + pullback(u_r_y) * sp.diff(a_rz, r)
          - (pullback(sp.diff(a, t) + u_z_y * sp.diff(a, y1))
             + r * pullback(u_r_y * sp.diff(a, y2))))
    psi_pull = pullback(psi_y)
    check("volume_velocity_first_component",
          "v1 = u_z = -psi_y2",
          -sp.diff(psi_pull, r) / r + pullback(sp.diff(psi_y, y2)))
    check("volume_velocity_second_component",
          "v2 = r u_r = psi_y1",
          sp.diff(psi_pull, z) - pullback(sp.diff(psi_y, y1)))
    check("volume_velocity_divergence",
          "partial_y1(-psi_y2) + partial_y2(psi_y1) = 0",
          -sp.diff(psi_y, y2, y1) + sp.diff(psi_y, y1, y2))
    check("volume_vorticity_streamfunction",
          "xi_pull = [(psi_y1y1 + 2 y2 psi_y2y2)/(2 y2)]_pull",
          lminus(psi_pull) / r**2
          - pullback((sp.diff(psi_y, y1, 2) + 2 * y2 * sp.diff(psi_y, y2, 2)) / (2 * y2)))
    check("volume_swirl_source",
          "[partial_y1(a^2)/(4 y2^2)]_pull = r^-4 partial_z(a_pull^2)",
          pullback(sp.diff(a**2, y1) / (4 * y2**2))
          - sp.diff(a_rz**2, z) / r**4)
    coordinate_jacobian = sp.Matrix([z, r**2 / 2]).jacobian([z, r]).det()
    check("volume_coordinate_jacobian",
          "det partial(y1,y2)/partial(z,r) = r; dy1 wedge dy2 = r dz wedge dr",
          coordinate_jacobian - r)

    result = {
        "schema_version": 1,
        "title": "Axisymmetric Euler/Navier--Stokes coordinate identities",
        "sympy_version": sp.__version__,
        "method": "Exact expansion and rational cancellation of differential polynomials in arbitrary smooth symbolic functions",
        "domain": "r > 0; y1=z; y2=r^2/2 > 0; nu >= 0",
        "conventions": {
            "cylindrical_order": "(u_r,u_phi,u_z)",
            "streamfunction": "u_r=Psi_z/r; u_z=-Psi_r/r",
            "swirl": "u_phi=Gamma/r",
            "vorticity": "xi=(partial_z u_r-partial_r u_z)/r",
            "volume_velocity": "v=(u_z,r u_r)=(-psi_y2,psi_y1)",
            "D": "partial_t + u_r partial_r + u_z partial_z",
            "L_minus": "partial_z^2 + partial_r^2 - r^-1 partial_r",
            "L_plus": "partial_z^2 + partial_r^2 + 3r^-1 partial_r"
        },
        "scope": "Checks differential identities only; does not establish global pressure recovery, axis regularity, boundary conditions, singularity formation, or a Millennium Problem counterexample.",
        "all_passed": all(item["passed"] for item in checks),
        "check_count": len(checks),
        "checks": checks,
    }
    destination = Path(__file__).resolve().parents[1] / "checks" / "euler_coordinates_symbolic.json"
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"all_passed": result["all_passed"], "check_count": len(checks),
                      "output": str(destination)}, indent=2))
    if not result["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
