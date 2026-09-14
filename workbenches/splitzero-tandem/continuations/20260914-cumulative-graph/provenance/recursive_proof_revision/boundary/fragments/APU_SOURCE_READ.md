# Actual analytic-pole u-connection: complete source read and propagation receipt

Author/read auditor: single_primary_dependency_audit. Date: 2026-09-13.

## Read scope and exact input

The complete 321-line AP1–26 source was read at:

workspace:/work/cumulative_actual_tau_draft_inputs_20260913_v21/source_snapshot/sources/next_edition/analytic_pole_conversions_v2/build/analytic_pole/endpoint_analytic_pole_source.tex

SHA256: b15d25864e0c298478947e2e67e4642bb1b007cccd08b6db21ec4bac740ce221.

The original has the full rational-pole complex, its exact residue cohomology, the t-connection, finite scaling, period matrix, actual Taylor gauge, dual, and exact marked endpoint. Its u-connection had not been calculated in that source. No historical source was edited by this task.

Earlier in this task the complete single-primary source SP.1–36 and SPF.1–29 was read; its original theta-source maps and the full Taylor-unit convention are retained in APU20–22. The full marked-family boundary source provides the same polynomial u-connection used here: ordinary division of f s^b by h−t with the derivative of its quotient retained. APU6 proves the required polynomial remainder directly again.

## New full proof and stable pins

The completed includable proof is:

workspace:/work/backpropagation_20260913/boundary/fragments/analytic_pole_u_connection.tex

It has complete proofs APU1–23, including the actual downstream finite-scaling derivatives requested by the parent.

Proof SHA256: 1b42c530ccee6fd019b8536170277e3909ba43bfe4e3b2fefab3f7b9fc666c05.

Exact checker:

workspace:/work/backpropagation_20260913/boundary/fragments/check_analytic_pole_u_connection.py

SHA256: 9bfa0c0cab0d199d4f8a6749666e4658a8bc80399a3daccc94ba5823fbe85795.

Machine receipt:

workspace:/work/backpropagation_20260913/boundary/fragments/analytic_pole_u_connection_exact_checks.json

SHA256: b0e3b77955a70d84bdda7f0ab51e8fc24a76751020fdb8b761b7dc3019d24470.

## Exact hypotheses and endpoint boundaries

The original h is monic of degree d>0, with every selected actual zero order. The actual Taylor representative nu has degree less than d, is coprime to h, and retains all its coefficients and multiplicities. Its roots p are fixed with respect to u and t; the ring is C[s,nu^−1]. The calculation is on C*_u × C_t.

No denominator h(p)−t is introduced into the new connection. In particular the formulas remain valid when t=h(p), with the original fixed-pole frame retained. The displayed endpoint map J0 at u=t=0 uses h(p)≠0, which follows from the original gcd(h,nu)=1. It assigns no limiting value to the singular u-connection and does not evaluate the formal contraction at a nonzero analytic parameter.

When nu is constant, its pole set is empty. Every additional block and loop/residue row is the empty map; the complete polynomial connection remains. The proof explicitly includes this case.

## Full original AP locators and the actual propagation

1. AP1–4, lines 7–62: D=u partial_s+h−t, w=exp((Phi−ts)/u), localization, fixed principal parts, higher-pole reduction, exact weighted-residue cokernel. These feed APU1–8. Degree-zero connection is partial_u−f/u²+1/u; degree-one connection is partial_u−f/u². The exact chain identity is proved before passing to cohomology.

2. AP5–6, lines 64–86: original polynomial injection and basis (1,...,s^(d−1),r_p). These become the horizontal polynomial submodule and actual extension of the two-parameter flat bundle in APU9–12. No replacement quotient or arbitrary splitting is inserted.

3. AP7–10, lines 88–123: original t-connection L=u partial_t−A_ext, with A_ext=[[A,B0],[0,P]]. APU9 retains it as nabla_t=partial_t−A_ext/u, and supplies its previously missing companion

   \[
   \Omega_u=
   \begin{bmatrix}
   -C(t)/u^2+B(t)/u&-Q(t)/u^2\\
   0&-\operatorname{diag}(f(p,t))/u^2
   \end{bmatrix}.
   \]

   The exact pole-column polynomial is

   \[
   Q_p=\frac{f(s,t)-f(p,t)}{s-p}-\frac{h(s)-t}{d+1}.
   \]

   The ordinary quotient is the constant 1/(d+1); its derivative correction is zero. This is the reason that the candidate Q_p formula is valid, proved directly rather than assumed.

4. AP11–13, lines 125–150: the original weighted-residue map is [0,W_res], where W_res=diag(exp(f(p,t)/u)). It has NO 2 pi i in its definition. APU11–13 preserve this and separately define W_loop=(2 pi i)W_res. They prove both maps horizontal in both parameters, as well as the exact frame change r_p/w(p) and its retained polynomial coupling. This corrects the candidate's conflation of weighted residues with oriented loop periods.

5. AP14–18, lines 152–198, and AP19b, lines 226–236: the already existing entire finite transport is retained with its full extension integral. APU23 propagates the new connection through the actual base map F_a(u,t)=(u,t+ua):

   \[
   \partial_uC_a=-\Omega_u(u,t)C_a
       +C_a\bigl(\Omega_u(u,t+ua)+a\Omega_t(u,t+ua)\bigr),
   \]

   \[
   \partial_tC_a=-\Omega_t(u,t)C_a
       +C_a\Omega_t(u,t+ua).
   \]

   The proof differentiates the inverse period matrix and the shifted factor separately. It retains the a Omega_t term caused by the original parameter shift. It then differentiates the actual identity [0,W_res(u,t)] C_a=[0,W_res(u,t+ua)] and proves its compatibility in both parameters. Multiplication by the unchanged 2 pi i yields the loop version. This is a concrete propagated result in the older finite-scaling calculation.

6. AP19–19b, lines 200–236: original rapid-decay contours, fixed pole detours, positive loop orientations, entire full period matrix and determinant. APU14–15 prove partial_u Pi_ext=Pi_ext Omega_u by locally fixed decaying contours and justified differentiation. They retain partial_t Pi_ext=Pi_ext Omega_t and the entire original block determinant, including every pole phase and 2 pi i.

7. AP20–21, lines 238–256: the full actual Taylor gauge D^nu=nu D nu^−1 and target weight w/nu. APU16 uses the fact that nu is fixed in both parameters to prove it intertwines both chain connections. It retains the transported frame nu times each original polynomial and pole column and the literal equality (w/nu)(nu F)=wF, including poles cancelled in the bare rational representative but present in its weighted form.

8. AP22, lines 258–267: the original ordinary linear dual. APU17 supplies its second connection partial_u−Omega_u^T, proves horizontal injection by transposing the actual residue identities, and retains the inverse transpose of the full gauge. It assigns no positive form to that algebraic operation.

9. AP23–26, lines 275–315: the old exact endpoint quotient J0 and its invariant kernel. APU18–22 carry these to the original theta complex by the actual Euler representatives. The endpoint map is sigma_h [nu] J0, equivalently v -> [(J0 v)(D_Euler)F_h]. Its source boundary identity is written and proved; changing the representative by hT contributes exactly Theta T(D_Euler)phi_*. The whole original Taylor unit and its inverse remain in this map. The marked action commutes because J0 A_ext(0)=A(0)J0 and [nu] commutes with A(0).

10. AP27-style closing scope at line 317 and provenance lines 319–321: revise the current scope to say the complete two-parameter connection, finite-scaling pullback, residue/loop horizontality, gauge and dual have now been calculated in APU1–23. Preserve the old text in provenance and keep the generic arithmetic comparison/metric calculation as its separate unsolved calculation.

## Sign and flatness checks in the proof

The connection convention is nabla=partial+Omega on coefficient columns, so period rows satisfy partial Pi=Pi Omega and the ordinary dual is partial−Omega^T.

The two chain identities are proved directly. Mixed curvature vanishes before cohomology because [partial_u,−s/u]=s/u² and [−f/u²,partial_t]=−s/u².

The original extension matrices also satisfy the fully explicit identities

\[
\partial_tQ_p=-\frac d{d+1}e_0,\qquad
B e_0=\frac1{d+1}e_0,\qquad
(A-pI)Q_p=C e_0-f(p)e_0.
\]

They cancel the upper-right curvature as

\[
\frac{B_0+Q_t-BB_0}{u^2}
\;+\;
\frac{CB_0+QP-AQ-B_0F}{u^3}=0.
\]

Both denominators and signs have been checked from the rational identity and ordinary monic remainders. No t derivative of a moving pole is missing because the original Taylor polynomial, and hence every p, is fixed in this calculation.

The parent independently read the complete AP source and APU1–22 and accepted these derivations, then requested APU23. That final downstream proof is newly supplied here for its final read. An attempted additional child audit could not start because all concurrent-agent slots were occupied; it is not represented as a completed independent review.

## Exact checks actually run

The checker used generic monic h=s^d+sum_(j<d) a_j s^j for d=1,2,3,4, with indeterminate coefficients a_j, primitive constant c, fixed pole p, and parameters u,t. These fixtures test polynomial identities; they are not asserted actual zeta-zero packets.

All 52 exact SymPy checks passed:

- constant ordinary pole quotient, its exact remainder, and its t derivative;
- exact polynomial constant column and full extension identity;
- every entry of the complete u/t curvature matrix;
- degree-correct chain identities and flatness on parameter-dependent rational representatives;
- full repeated-polynomial gauge and its u-chain identity;
- both weighted-residue matrix identities.

APU23 is proved symbolically in the manuscript from the exact inverse derivative and shifted product derivative; this task does not describe numerical evidence as its proof.

No Lean run, arithmetic-zero certificate, new uniform source-norm estimate, source normalization, historical-source rewrite, or publication occurred in this bounded task. The parent owns incorporation into the living cumulative sources and their compilation.
