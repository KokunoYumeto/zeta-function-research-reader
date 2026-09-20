# Independent proof check: the six-step gamma ratio and finite derivative selection

20 September 2026. This note checks the mathematical part of result SZ-20260920-058. It does not edit the parent proof, run author macros, read a PDF, or perform publication, rendering, or index work.

## 1. Source identity and actual reading

The original source is Juan Arias de Reyna, *High Precision Computation of Riemann's Zeta Function by the Riemann–Siegel Formula, II*, [arXiv:2201.00342v1](https://arxiv.org/abs/2201.00342v1), original `main.tex`, SHA-256 `06786e7e7010b4a51bb431d7e885370d243f52956549d535f69391de120d8bdc`.

The existing source-reading ledger was consulted for identity and routing. Such a record is not evidence of independent full-paper reading. This check read these original-source ranges: 46–89; 580–603; 1141–1202; 1379–1578; 1743–1832; 2901–2938. It also searched the original source for the integer condition on L: line 709 states L≥1. In particular, this check read the definitions `defeps5` and `Fmcondition`, the unproved lemma `fincreasing`, and the complete proposition `PropAprTaylor` with its proof. The source's coefficient formula `c2n` was read, but no global correctness claim about the source's floating-point procedures is imported.

The local proof used for the first gamma inequality and the original two-cutoff Taylor theorem is `work/independent_arias_gamma_inequality/proof.tex`, result SZ-20260920-056, read completely, SHA-256 at this check `98216b521ba71831e955ee133069676cd4b5fe0828c6edcc4f1b259a24e0240f`. Its relevant exact locators are Theorem `thm:gamma`, Lemma `lem:trigamma`, and Proposition `prop:taylor`. The proof derives the gamma inequality independently of the unproved source lemmas. Its strict Taylor conclusion includes the equality case of the gamma comparison at m=0. This note repeats the cutoff argument below so all steps in the present receiver are visible; the already-proved first gamma inequality is a named dependency, not a new unproved assertion.

Part II attributes the derivative bound |F^(m)(p)|≤F_m to Juan Arias de Reyna, *High precision computation of Riemann's zeta function by the Riemann–Siegel formula, I*, Mathematics of Computation 80 (2011), no. 274, 995–1009, formula (55), and the even Taylor coefficients and their bound to formulas (47) and (56). Part I was not independently read here. The present theorem is proved for the precise coefficient class and derivative bounds stated below; their application to the author's specific F uses those explicitly attributed source facts.

## 2. Exact disproof of the printed global increase

For every real x>0 define the original positive function

\[
H(x)=\frac{5^x}{(2\pi)^{(x-1)/2}\Gamma((x+1)/2)}
\left(\frac{\Gamma(x+1)}{\Gamma(x/3+2)}\right)^{1/2}.
\]

All gamma arguments and all bases of powers are positive. Gamma's recurrence follows directly by integration by parts in Euler's integral. Applying that recurrence three times at (x+1)/2, six times at x+1, and twice at x/3+2 gives

\[
\begin{aligned}
\frac{H(x+6)}{H(x)}
&=\frac{5^6}{(2\pi)^3}
\frac{8}{(x+1)(x+3)(x+5)}
\left(\frac{9(x+1)(x+2)(x+3)(x+4)(x+5)(x+6)}
{(x+6)(x+9)}\right)^{1/2}\\
&=\frac{46875}{\pi^3}
\left(\frac{(x+2)(x+4)}
{(x+1)(x+3)(x+5)(x+9)}\right)^{1/2}.
\end{aligned}
\]

Every cancellation is between positive quantities, so there is no sign choice. Squaring yields exactly

\[
\boxed{\left(\frac{H(x+6)}{H(x)}\right)^2
=\frac{46875^2(x+2)(x+4)}
{\pi^6(x+1)(x+3)(x+5)(x+9)}.}
\]

For an elementary exact certificate of π>3, use

\[
\frac1{1+u^2}=\sum_{k=0}^{7}(-1)^k u^{2k}
+\frac{u^{16}}{1+u^2},\qquad 0\le u\le1.
\]

Integrating and using π=4 arctan(1) gives

\[
\pi>4\sum_{k=0}^{7}\frac{(-1)^k}{2k+1}
=\frac{135904}{45045}>3,
\]

because 135904−3·45045=769>0. Hence, at x=2000,

\[
\begin{aligned}
\left(\frac{H(2006)}{H(2000)}\right)^2
&<\frac{46875^2\cdot2002\cdot2004}
{3^6\cdot2001\cdot2003\cdot2005\cdot2009}\\
&=\frac{8815447265625000}{11769279587774415}
=\frac{9328515625000}{12454264114047}<1.
\end{aligned}
\]

The reduction divides numerator and denominator by 945; the final denominator minus numerator is 3125748489047. Since H is positive, H(2006)<H(2000). This is an exact counterexample to `fincreasing` as printed, not an asymptotic estimate or a floating-point sample.

It is enough to disprove the printed lemma and the use of that lemma as a proof of monotonicity in the subsequent selection paragraph. Without a separate substitution of the original F_m formula, it does not by itself identify a counterexample to every parameter-specific statement about ε₅(m)/F_m. No such stronger claim is needed for the replacement below.

## 3. Original quantities and exact Taylor receiver

Let L≥1 be an integer and T=3L−3. Let A(σ), B₁, a, ε₄ be strictly positive real numbers. For every integer 0≤m≤T retain the source's definitions

\[
\varepsilon_5(m)
=\frac{(\pi^2 B_1a)^{m/3}\varepsilon_4}{316A(\sigma)}
\left(\frac{m!}{\Gamma(m/3+2)}\right)^{1/2},
\qquad
\widetilde\varepsilon_5(m)=\min\{4F_m,\varepsilon_5(m)\},
\]

where F_m>0 and |F^(m)(p)|≤F_m. Let p be real with |p|≤1 and

\[
F(z)=\sum_{j=0}^{\infty}c_{2j}z^{2j},\qquad
|c_{2j}|\le\frac{\pi^j}{2^{j+1}j!}.
\]

The source's p=1−2(a−⌊a⌋) belongs to (−1,1], so it satisfies this receiver domain. Coefficients may be complex. The finite-selection theorem below uses no claim that their values or bounds are monotone in m.

For every integer M≥1, choose any integer J≥12 satisfying the two original inequalities

\[
q_J:=\frac{(2\pi)^J}{J!}\le\frac{\varepsilon_4}{632A(\sigma)},
\qquad
q_J\le\frac{\varepsilon_4}{632A(\sigma)M}
\left(\frac{\pi^2B_1a\sqrt3e^2}{M^2}\right)^{(M-1)/3}.
\tag{J}
\]

The source defines the first such J. Its minimality is not used by any estimate here. Let

\[
P(z)=\sum_{j=0}^{J-1}c_{2j}z^{2j}.
\]

Then, for every integer 0≤m<M,

\[
|F^{(m)}(p)-P^{(m)}(p)|<\frac{\varepsilon_5(m)}2.
\tag{Taylor}
\]

Here are the exact steps. The coefficient bound gives uniform absolute convergence of the series on every compact disk, with majorant (1/2)exp(πR²/2). For fixed m the differentiated terms have a bound of the form (2j+1)^m π^j R^(2j)/(2^(j+1)j!), whose successive ratio tends to zero. Termwise differentiation is therefore valid. For 2j<m the derivative of z^(2j) is zero. For 2j≥m it is bounded on |p|≤1 by

\[
m!\binom{2j}{m}|p|^{2j-m}\le m!\,4^j.
\]

The exponent-zero term is the constant one, including at p=0. Thus there are no negative factorials or negative powers in this bound. For J≥12,

\[
|F^{(m)}(p)-P^{(m)}(p)|
\le\frac{m!}{2}\sum_{j\ge J}\frac{(2\pi)^j}{j!}
\le\frac{m!}{2}q_J\sum_{k\ge0}\left(\frac{2\pi}{J+1}\right)^k
<m!q_J.
\tag{Tail}
\]

The last inequality follows from J+1≥13>4π. An exact certificate for the latter is

\[
0<\int_0^1\frac{u^4(1-u)^4}{1+u^2}\,du=\frac{22}{7}-\pi,
\qquad \frac{88}{7}<13.
\]

For the cutoff argument put C=ε₄/(632A(σ)), D=π²B₁a and

\[
Q(r)=\frac{CD^{r/3}}{\sqrt{\Gamma(r+1)\Gamma(r/3+2)}},\qquad r\ge0.
\]

The proved gamma inequality in result 056 is

\[
\Gamma(r+1)\Gamma(r/3+2)
\le(r+1)^2\left(\frac{(r+1)^4}{3e^4}\right)^{r/3},
\]

with equality at r=0 and strict inequality for r>0. Its reciprocal square root gives

\[
Q(r)\ge\frac{C}{r+1}
\left(\frac{D\sqrt3 e^2}{(r+1)^2}\right)^{r/3}.
\tag{Q lower bound}
\]

Also (log Q)″(r)=−ψ′(r+1)/2−ψ′(r/3+2)/18<0, using the positive trigamma series proved in result 056. Thus Q is log-concave. The first inequality in (J) gives q_J≤Q(0); the second and the Q lower bound give q_J≤Q(M−1). If M>1 and 0≤r≤M−1, concavity gives

\[
\log Q(r)\ge\left(1-\frac r{M-1}\right)\log Q(0)
+\frac r{M-1}\log Q(M-1)\ge\log q_J.
\]

For M=1 only r=0 is needed and both conditions (J) coincide. Consequently m!q_J≤m!Q(m)=ε₅(m)/2 for every integer 0≤m<M. Combining with the strict tail estimate proves (Taylor), including m=0. Since q_(J+1)/q_J=2π/(J+1) is eventually less than 1/2, q_J tends to zero. Both right sides of (J) are positive constants; hence a qualifying J exists.

## 4. Exact finite selection, with no monotonicity assumption

Define the finite subset

\[
B=\{m\in\{0,\ldots,T\}:\varepsilon_5(m)\le F_m\}.
\]

For every m outside B, F_m<ε₅(m) and F_m<4F_m. It follows that

\[
|F^{(m)}(p)-0|\le F_m
<\min\{4F_m,\varepsilon_5(m)\}
=\widetilde\varepsilon_5(m).
\tag{zero branch}
\]

Thus zero is a valid output with the original strict error allowance for each such index.

If B is empty, take every output to be zero and stop. No M or J is required. In particular, one must not substitute M=0 into (J).

If B is nonempty, set M=1+max B, so 1≤M≤T+1. Choose J using (J). For each m∈B, choose a rational complex number y_m satisfying

\[
|y_m-P^{(m)}(p)|<\varepsilon_5(m)/2.
\tag{evaluation}
\]

For m∈B, ε₅(m)≤F_m<4F_m, so the original minimum is exactly ε₅(m). Hence (Taylor), (evaluation), and the triangle inequality give

\[
|F^{(m)}(p)-y_m|
<\varepsilon_5(m)
=\widetilde\varepsilon_5(m).
\]

For m∉B use zero, as already proved. This establishes every required derivative output on 0≤m≤T. The set B need not be an initial interval: holes below M remain zero outputs. Equality ε₅(m)=F_m belongs to B and presents no analytic difficulty.

The proof preserves `defeps5`, whose operation is min. The later source paragraph prints max while asserting that the value equals ε₅(m) under ε₅(m)≤F_m. That equality is true for the original min and false for max. The original source file is not altered here.

## 5. Certified finite selection without an equality oracle

The exact set B is mathematically well defined, but computing its membership using comparison of arbitrary real values is a separate issue. An executable version takes certified rational enclosures for each positive F_m and ε₅(m), with enclosure widths tending to zero on refinement. For the source's specific objects, such certified access must come from their defining formulas or independently checked numerical routines; it is not supplied by an unverified floating-point sample.

At each refinement stage write the enclosures as

\[
F_m\in[f_m^-,f_m^+],\qquad
\varepsilon_5(m)\in[e_m^-,e_m^+].
\]

Use either of the following strict certificates:

| Output branch | Rational certificate | Proved exact inequality |
| --- | --- | --- |
| zero | f_m^+<e_m^- | F_m<ε₅(m) |
| compute | e_m^+<2f_m^- | ε₅(m)<2F_m |

If both certificates hold, either branch is valid; for a deterministic implementation give the zero branch priority. If neither holds, refine. These tests use only strict rational comparisons.

For any two strictly positive real numbers F and ε, either F<ε, or ε≤F<2F. Thus the two exact open conditions F<ε and ε<2F cover all allowed data. If one strict inequality is true, its positive gap eventually exceeds the sum of the enclosure errors, and its rational certificate is then found. Therefore classification terminates for each index, and it terminates for the entire finite index set. Equality ε=F is covered by the compute branch, while equality ε=2F is covered by the zero branch. No equality decision is needed.

Let C be the set classified for computation. If C is empty, all outputs are zero and the proof in the zero branch applies at every index. Otherwise set M=1+max C and use (J). Every m∈C satisfies ε₅(m)<2F_m<4F_m, so its original allowance is again exactly ε₅(m). Applying (Taylor) and (evaluation) proves total error strictly below that allowance. Every m∉C has a certified zero branch. In particular, B⊆C, but C may contain some indices from the overlap F_m<ε₅(m)<2F_m. This enlargement changes no error claim.

The use of 2F_m in the compute certificate is sufficient, but not maximal: the same proof works with ε₅(m)<cF_m for any fixed 1<c≤4. The proposed value 2 is valid and gives a substantial overlap with the zero branch. No change to that proposed value is required.

## 6. Cutoff certification and exact rational polynomial evaluation

Computability claims require representations, while the preceding analytic statements apply to all real data satisfying their written hypotheses. The following construction makes the effective content explicit and does not require selecting the first J with an undecidable non-strict real comparison.

Find positive rational lower bounds for the two right sides of (J) by refining their certified enclosures until the lower endpoints are positive. Let b>0 be a rational number no greater than both lower bounds. Since 2π<44/7, search for an integer J≥12 with

\[
\frac{(44/7)^J}{J!}<b.
\]

This is a strict comparison of rational numbers and the search terminates, since successive ratios are (44/7)/(J+1), eventually less than 1/2. The chosen J satisfies both original conditions (J), regardless of whether it is their first solution. Thus the receiver retains the original constants while avoiding a second equality-oracle issue at the cutoff.

Here is a complete finite error construction for (evaluation). Suppose certified approximations to p and the finite coefficient list c₀,c₂,…,c_(2J−2) can be refined to arbitrary accuracy. For the source coefficients, formula `c2n` is an explicit finite expression in Euler numbers, π, 1/√2, and exp(3πi/8). This fact supports such refinement by exact-integer operations and certified elementary constants, without relying on the source's later floating-point schedules. No identity connecting those formulas to F beyond the source's stated coefficient identity is independently claimed here.

For a derivative index m, let

\[
I_m=\{j:0\le j<J,\ 2j\ge m\},\quad
k_{jm}=2j-m,\quad d_{jm}=\frac{(2j)!}{(2j-m)!}.
\]

If I_m is empty, P^(m) is identically zero, so take y_m=0 with evaluation error zero. Otherwise choose rational bounds

\[
U_j=\frac{(22/7)^j}{2^{j+1}j!}\ge |c_{2j}|,
\qquad
K_m=\sum_{j\in I_m}d_{jm}(1+k_{jm}U_j)>0.
\]

For the finitely many required indices with nonempty I_m, choose a positive rational η such that ηK_m<ε₅(m)/2 for all of them. Certified positive rational lower bounds for ε₅(m) make this a finite rational choice. Find rational complex coefficients ĉ_(2j) with |ĉ_(2j)−c_(2j)|≤η, and a rational r∈[−1,1] with |r−p|≤η. For p, first approximate by a rational and then clamp to [−1,1]; this cannot increase the distance to p. For a complex coefficient, coordinate errors no greater than η/2 imply its modulus error is less than η.

Compute exactly in rational complex arithmetic

\[
y_m=\sum_{j\in I_m}d_{jm}\widehat c_{2j}r^{k_{jm}}.
\]

For real r,p∈[−1,1] and integer k≥1, factorization of r^k−p^k gives |r^k−p^k|≤k|r−p|; for k=0 the difference is zero. Therefore

\[
\begin{aligned}
|y_m-P^{(m)}(p)|
&\le\sum_{j\in I_m}d_{jm}
\left(|\widehat c_{2j}-c_{2j}|\,|r|^{k_{jm}}
+|c_{2j}|\,|r^{k_{jm}}-p^{k_{jm}}|\right)\\
&\le\eta\sum_{j\in I_m}d_{jm}(1+k_{jm}U_j)
=\eta K_m<\varepsilon_5(m)/2.
\end{aligned}
\]

This proves (evaluation), including k=0, p=0, p=±1, and m exceeding the degree of P. Finite rational arithmetic incurs no further rounding error. The construction proves existence and termination of certified finite evaluation; it makes no speed claim and does not verify any preexisting implementation.

## 7. Conservative option: compute the entire finite list

Set M=T+1, and choose J≥12 satisfying both original conditions (J) and

\[
q_J\le\min_{0\le m\le T}\frac{2F_m}{m!}.
\tag{full-list cutoff}
\]

The extra minimum is positive because the index set is finite and every F_m is strictly positive. Existence follows again from q_J→0. An effective choice uses a positive rational lower bound for this additional minimum along with the two bounds in Section 6.

For every required index, (Tail), (Taylor), and the extra cutoff give simultaneously

\[
|F^{(m)}(p)-P^{(m)}(p)|<\varepsilon_5(m)/2,
\qquad
|F^{(m)}(p)-P^{(m)}(p)|<2F_m.
\]

Consequently

\[
|F^{(m)}(p)-P^{(m)}(p)|
<\min\{\varepsilon_5(m)/2,2F_m\}
=\widetilde\varepsilon_5(m)/2.
\]

Use the rational polynomial construction with ε₅(m)/2 replaced by the positive target \(\widetilde\varepsilon_5(m)/2\). The total error is then strictly smaller than the original \(\widetilde\varepsilon_5(m)\) for every m. This option uses no derivative-selection comparisons at all.

## 8. Endpoint and scope conclusions

The data L≥1 make T≥0. At L=1, T=0 and a nonempty computed set gives M=1; the two original cutoff bounds coincide and the proof still applies. An empty computed set invokes neither M nor J. At m=0, the gamma-product comparison is an equality, but the Taylor tail comparison is strict, so the final allowance remains strict. Indices beyond the polynomial degree contribute exact zero polynomial derivatives, not undefined negative factorials. The coefficient and tail bounds hold at p=0 and both endpoints of [−1,1]. All denominators and tolerances used above are strictly positive on the specified domain.

The proposed ratio, the exact rational counterexample, the finite-set replacement, the strict-overlap refinement, and the conservative full-list cutoff are correct. Two practical qualifications are essential: effective input values need certified convergent enclosures, and the implementation should choose any certified qualifying J rather than promise to compute the first J through non-strict comparisons of arbitrary real numbers.

This establishes a finite derivative-output repair with the source's original error allowances and unchanged Taylor cutoff constants. It does not prove the Riemann hypothesis, verify the second technical gamma inequality, certify all coefficient identities from Part I, or certify a complete Riemann–Siegel implementation.

## 9. Direct review of the parent proof

After completing the independent derivation above, the parent `work/arias_finite_derivative_repair_20260920/proof.tex` was read completely. The checked snapshot has SHA-256 `b1ffb3234069434ab573e7de2d6ac5bbd5bc3a2f6bb1badea704f9cb2209c5ae`. Its statements and proofs of `thm:ratio`, `prop:finite`, `prop:overlap`, the Taylor-error composition, and the full-list cutoff agree with the independent derivation. No mathematical error was found in that snapshot. It states the convergent rational-enclosure input model and permits strict cutoff certification without minimality. The explicit K_m evaluation constant in Section 6 above is a proved strengthening of its finite interval-evaluation argument, not a correction of an invalid bound.
