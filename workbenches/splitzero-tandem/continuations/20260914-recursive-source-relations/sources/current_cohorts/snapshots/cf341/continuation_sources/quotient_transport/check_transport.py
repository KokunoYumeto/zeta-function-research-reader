"""Numerical independent checks of finite polynomial block identities.

These finitely supported positive measures test the algebra and its edge
cases only. They are not substituted for the arithmetic or Gamma source in
the proof and are not evidence for an off-line zeta packet.
"""
from pathlib import Path
import json
import numpy as np

rng = np.random.default_rng(4172026)
results = []

def gs(cols, metric):
    out = []
    for z in cols.T:
        y = z.copy()
        for e in out:
            y -= e * (e.conj() @ metric @ y)
        y /= np.sqrt(np.real(y.conj() @ metric @ y))
        out.append(y)
    return np.array(out).T

for q in (1, 2, 3):
    for trial in range(4):
        k = 1
        n = 2*q+1
        nodes = np.linspace(-2, 2, 87)
        line = k/2 + 1j*nodes
        vand = np.vander(line, n, increasing=True)
        weights0 = 0.2 + rng.random(len(nodes))
        weights1 = 0.2 + rng.random(len(nodes))
        m0 = vand.conj().T @ (weights0[:, None]*vand)
        m1 = vand.conj().T @ (weights1[:, None]*vand)
        t = (trial+1)/5
        weights = (1-t)*weights0 + t*weights1
        metric = (1-t)*m0+t*m1
        roots = (0.5 + 0.2*rng.normal(size=q)
                 + 0.5j*rng.normal(size=q))
        if q > 1 and trial == 3:
            roots[-1] = roots[0]  # Retained multiple root.
        chi = np.polynomial.polynomial.polyfromroots(roots)
        boundary = np.zeros((n, q+1), dtype=complex)
        for j in range(q+1):
            boundary[j:j+q+1, j] = chi
        section = np.eye(n, dtype=complex)[:, :q]
        jmap = np.zeros((q, n), dtype=complex)
        for j in range(n):
            mono = np.zeros(j+1, dtype=complex)
            mono[j] = 1
            _, rem = np.polynomial.polynomial.polydiv(mono, chi)
            jmap[:len(rem), j] = rem
        relgram = boundary.conj().T @ metric @ boundary
        qproj = boundary @ np.linalg.solve(
            relgram, boundary.conj().T @ metric)
        pi = np.eye(n)-qproj
        r = pi @ section
        gram = r.conj().T @ metric @ r
        low = section.conj().T @ metric @ section
        pf = gs(np.eye(n, dtype=complex), metric)
        rf = gs(boundary, metric)
        cf = gs(r, metric)
        target = np.column_stack(
            [cf, rf[:, [0]], rf[:, 1:q], rf[:, [q]]])
        trans = target @ np.linalg.inv(pf)
        spec = np.array([0]*q + [1] + [2]*(q-1) + [1])
        w = pf @ np.diag(spec) @ np.linalg.inv(pf)
        u = trans @ w @ np.linalg.inv(trans)
        x = qproj @ trans + pi
        invx = np.linalg.inv(x)
        xdegree = np.linalg.solve(
            relgram, boundary.conj().T @ metric @ trans @ boundary)
        homotopy = np.linalg.solve(
            relgram, boundary.conj().T @ metric @ (trans-np.eye(n)))
        nil = pi @ w @ invx
        cmet = np.linalg.solve(metric, m1-m0)
        dotr = -qproj @ cmet @ r
        ddotg = -2*dotr.conj().T @ metric @ dotr
        speed2 = np.real(np.trace(np.linalg.solve(
            gram, dotr.conj().T @ metric @ dotr)))
        nu2 = np.real(np.trace(np.linalg.solve(
            gram, r.conj().T @ metric @ w @ w @ r)))
        ell = q-np.real(np.trace(np.linalg.solve(low, gram)))
        a = jmap @ trans @ r
        ablock = cf.conj().T @ metric @ trans @ cf
        dblock = rf.conj().T @ metric @ trans @ rf
        svd_left, _, svd_right = np.linalg.svd(dblock)
        polar_d = svd_left @ svd_right
        vobs = pi + rf @ polar_d @ rf.conj().T @ metric
        singular_a = np.linalg.svd(ablock, compute_uv=False)
        cvals = np.polynomial.polynomial.polyval(line, chi)
        beta = (np.sum(abs(cvals)**2*weights)**2
                / (np.sum(weights)*np.sum(abs(cvals)**4*weights)))
        lhs = np.trace((u-w) @ cmet)
        center = np.trace(w @ invx @ (cmet @ x-x @ cmet))
        whiten = np.linalg.cholesky(metric).conj().T
        iwhite = np.linalg.inv(whiten)
        def opnorm(z):
            return np.linalg.norm(whiten @ z @ iwhite)
        def hs2(z):
            return opnorm(z)**2
        residuals = {
            "unitary": opnorm(np.linalg.solve(
                metric, trans.conj().T @ metric @ trans)-np.eye(n)),
            "observation": np.linalg.norm(jmap @ x-jmap),
            "chain_map": np.linalg.norm(x @ boundary-boundary @ xdegree),
            "homotopy_degree_zero": opnorm(x-np.eye(n)-boundary @ homotopy),
            "homotopy_degree_minus_one": np.linalg.norm(
                xdegree-np.eye(q+1)-homotopy @ boundary),
            "intertwining_defect": opnorm(u @ x-x @ w+pi @ w),
            "nilpotent_conjugation": opnorm(x @ w @ invx-u-nil),
            "nilpotent_square": opnorm(nil @ nil),
            "quotient_metric": np.linalg.norm(
                a.conj().T @ gram @ a
                - gram @ np.linalg.solve(low, gram))
                / np.linalg.norm(gram),
            "determinant": abs(abs(np.linalg.det(x))**2
                - np.real(np.linalg.det(gram)/np.linalg.det(low))),
            "minimum_energy": abs(nu2-hs2(pi @ w)),
            "nilpotent_energy": abs(nu2-hs2(nil)),
            "signed_trace": abs(lhs-center+np.trace(nil @ cmet)),
            "unitary_repair_observation": np.linalg.norm(jmap @ vobs-jmap),
            "unitary_repair_unitarity": opnorm(np.linalg.solve(
                metric, vobs.conj().T @ metric @ vobs)-np.eye(n)),
            "unitary_repair_cost": abs(hs2(vobs-trans)
                - (4*q-2*np.real(np.trace(ablock))-2*np.sum(singular_a))),
            "aw_phase_triangular": np.linalg.norm(np.triu(ablock, k=1)),
            "aw_phase_determinant": abs(np.linalg.det(a)
                - np.sqrt(np.real(np.linalg.det(gram)/np.linalg.det(low)))),
            "speed": abs(speed2+0.5*np.real(
                np.trace(np.linalg.solve(gram, ddotg)))),
        }
        tolerance = 3e-6
        assert max(residuals.values()) < tolerance, (q, trial, residuals)
        assert beta > 0 and beta <= ell+tolerance
        assert ell <= nu2+tolerance and nu2 <= 4*ell+tolerance
        assert abs(np.real(lhs-center)) <= np.sqrt(nu2*speed2)+tolerance
        determinant_ratio = np.real(np.linalg.det(gram)/np.linalg.det(low))
        assert hs2(vobs-trans) <= (
            4*q*(1-determinant_ratio**(1/(2*q)))+tolerance)
        # A genuinely different class-preserving candidate must obey
        # the attained intertwining minimum.
        perturb = 0.05*(rng.normal(size=(n, n))
                        + 1j*rng.normal(size=(n, n)))
        competitor = x+qproj @ perturb
        assert hs2(u @ competitor-competitor @ w) >= nu2-tolerance
        results.append({"q": q, "trial": trial, "multiple_root": trial == 3
                        and q > 1, "max_residual": max(residuals.values()),
                        "beta": beta, "ell": ell, "nu_squared": nu2,
                        "speed_squared": speed2})

out = {"description": __doc__, "cases": results,
       "maximum_residual": max(x["max_residual"] for x in results)}
Path(__file__).with_name("checks.json").write_text(
    json.dumps(out, indent=2), encoding="utf-8")
print(json.dumps({"cases_passed": len(results),
                  "maximum_residual": out["maximum_residual"]}))
