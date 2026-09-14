# Exact AU.19 weight optimization — durable lane log

Parent task received verbatim:

> Root read complete final AU1–49. For useful bounded next math independently while integration runs: optimize finite AU19 weights τ without assuming arithmetic asymptotic. Because E_q has q+1cols, nullvector is full monic ψ coefficient list χ_j in u chart; exact minors det E[:,omitj] carry signed χ_j detZ. Prove precise signed identity and exact optimization of D(τ)=sum_j a_j product_l≠j τ_l on closed simplex sumτ1 with a_j=|ψ_j|² times full b factorial products. Retain original coefficients inclzeros, phases, rawfactorials, q. Characterize interior/boundary maximizers and give rigorous evaluable one-dimensional scalar characterization/inequalities; if possible derive sharper original bound and analyze whether this impacts leading cost. This is standalone next calculation, no edits to sealed AU proof/manifest or current reader. Don't merely assume optimizer. Full proof with exact maps.

The sealed AU source and manifest remain unchanged. Both attempted independent
delegations (new agent and follow-up to the completed reviewer) were rejected
by the available agent-thread limit; the parent was informed. Work proceeds
locally, with independent review to be assigned when capacity permits.

Derived results:

- Exact cofactor identity: det E[:,omit j]=(-1)^(q-j) ψ_j det Z.
- For β_j=b^(2j)/(2j)!, η_j=|ψ_j|²/β_j, determinant equals
  |det Z|² (product β_j) D_η(τ), including every zero coefficient.
- Boundary optimum iff some coefficient is at least the sum of the others;
  its omitted coordinate is zero, all others equal 1/q. The sole degeneracy
  consists of exactly two equal positive coefficients: their two τ coordinates
  have sum 1/q, and all other coordinates equal 1/q.
- Otherwise the optimum is unique and interior. At zero η coordinates,
  τ=1/q. On positive coordinates τ_i=(1-y_i)/q, where sum y_i=1 and
  η_i=c y_i(1-y_i). A strictly monotone scalar equation determines either
  all small quadratic roots, or one large root at the unique maximal η_i.
- The exact optimized value is 4/(q^q t) times product(1-y_i), t=4/c.
- Improvement over equal weights is at most q log(1+1/q)<1 natural-log unit.
  This is sharp for a single positive coefficient and does not change either
  q log k or q² leading cost. Full quartet parity gives a strictly positive
  improvement smaller than that upper bound.

Proof, finite checker, PDF and final review status will be sealed separately
from AU when complete.


## OW.40 finalization — 13 September 2026

The complete current source OW.1–40 and OW.22a was read again, together with both preceding full mathematical reviews and the newly independent OW.30–40/R48 derivation. No mathematical correction was needed. The current primary TeX is SHA-256 677482a95ecbeafecf26f898f7426fb74ba31a5375cbe8862551e2c1a78e0952. Its complete proofs preserve the original source mass, source chart, raw derivatives, signed minors, all q+1 moment factors and every zero coefficient.

The earlier less-than-one gain concerns precisely the old separate-moment family. The source now also proves H_q <= S_q diag(beta_j^-1) < (M_k/2) diag(beta_j^-1), with the literal finite sum S_q=sum beta_j mu_(2j). The full stronger diagonal family H_q <= (sum r_j mu_(2j)) diag(r_j^-1) is optimized by the exact bijection t_j=r_j mu_(2j)/sum r_l mu_(2l). Its cofactor polynomial has kappa_j=|psi_j|^2 mu_(2j), and its bound is U_mom=sum_(j=0)^q log mu_(2j)-log d(kappa)-log V_(2q-1)^nu. OW.39 preserves every term of the exact gain, including q log(2(q+1)); its q log k ratio is 2 for fixed multiplicity one and 3 for fixed multiplicity greater than one. OW.40 proves the complete original-kernel comparison loss by the quotient-first Schur complement V_q=det H_q/(psi* H_q psi). These are full proofs in the source and new independent review, with no additional arithmetic asymptotic assumed.

R48 was read completely and agrees with these exact formulas. No global or frozen publication file was edited. A separate final PDF build retained the earlier twelve-page PDF and its mismatched older nine-page image history without changing any bytes there. The new twelve-page PDF was compiled twice, rendered at 110 dpi, and all twelve individual pages were actually viewed. The build has no TeX warning, overfull/underfull box, missing equation label, or visual defect.

No mathematical checker was rerun during finalization. Twenty original completed command events were recovered from their exact session records: eight historical jobs at 153 checks and twelve current jobs at 207 checks. Each current result matches its original completed execution, including flags, failure list and concrete interpreter path. Both current positive jobs pass all 207 checks. In each mode, the minor-sign control rejects eight identities, factorial two, stationarity-sign twenty-two, cosh-factor two and omitted-zero-moment product two. All event records, raw emitted output and existing result JSON files are retained. A current version probe records Python/SymPy now and is not claimed to retroactively establish versions omitted from the original event.

The final manifest and portable dependency specification distinguish the twelve current jobs from the eight historical jobs and retain the sealed AU dependency closure. No Lean was run and no arithmetic-source asymptotic was inferred from the explicit finite density fixtures.
