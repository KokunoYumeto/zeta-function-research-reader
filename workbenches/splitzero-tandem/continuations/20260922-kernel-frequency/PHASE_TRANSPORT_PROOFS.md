# From the original relative spectra to the entire measured phase

This proof connects two different arrivals in the same intake: the full logarithmic spectral comparison in `04_uniform_return.md`, and the original measured phase and determinant recovery in `06_frequency_bridge.md`. Every bound below is finite. The quantities on its right sides are sums over the actual spectra, so the proof does not assign a missing arithmetic value. In particular it identifies exactly how an evaluated relative spectrum passes to a frequency calculation.

## PT1. Original spaces and the full observed resolvent

Let \(E=\mathbb C^q\), with its given positive Hermitian metric \(G\). Let \(T:E\to E\) be the given word, and \(\Lambda:E\to B\) the onto observation. Set \(K=\ker\Lambda\), and fix its injective frame \(I_K:\mathbb C^m\to E\). Retain
\[
 H=G^{-1}T^*GT,\quad H_K=I_K^*GI_K,\quad
 Q=(\Lambda G^{-1}\Lambda^*)^{-1},\quad L=G^{-1}\Lambda^*Q.
 \tag{PT1}
\]
The maps \(J_K=I_KH_K^{-1/2}\) and \(J_B=LQ^{-1/2}\) obey
\(J_K^*GJ_K=I\), \(J_B^*GJ_B=I\), and \(J_B^*GJ_K=0\). Indeed \(\Lambda I_K=0\), \(\Lambda L=I\), and direct multiplication proves these identities. Their ranges have complementary dimensions, hence \([J_B,J_K]\) is an isometry onto the original metric space. Write
\[
 [J_B,J_K]^*GH[J_B,J_K]=
 \begin{pmatrix}B_0&C^*\\C&A\end{pmatrix},\qquad A=J_K^*G HJ_K.
 \tag{PT2}
\]
This changes the coefficient representation together with its exact metric; it does not change \(T,\Lambda,K\) or their underlying forms. For \(z\) off the nonpositive real axis define the actual value-coordinate response
\[
 \mathscr Y(z)=\Lambda z(zI+H)^{-1}L.
 \tag{PT3}
\]
Its conjugate \(Q^{1/2}\mathscr YQ^{-1/2}\) is the observed block of the full resolvent in this isometry. Schur elimination, keeping every zero direction, proves
\[
 \det\mathscr Y(z)=\frac{\det(I_m+A/z)}{\det(I_q+H/z)}.
 \tag{PT4}
\]
For completeness the observed inverse block of \(zI+[B_0,C^*;C,A]\) has determinant \(\det(zI+A)/\det(zI+H)\). Multiplying that block by \(zI_{q-m}\) gives PT4; the powers of \(z\) cancel with precisely these full dimensions.

At \(z=i\omega\), \(\omega>0\), the Hermitian real part of the full response is positive, since the real part of \(i\omega(i\omega+H)^{-1}\) is \(\omega^2(\omega^2+H^2)^{-1}>0\). The measured phase is the continuous trace of the matrix logarithm, equal to zero at infinite frequency. It is not reduced modulo \(2\pi\). If the positive eigenvalues of \(H,A\) are \(\lambda_j,\alpha_j\), respectively, PT4 proves
\[
 \Theta(\omega)=\Im\operatorname{Tr}\Log\mathscr Y(i\omega)
 =\sum_j\arctan(\lambda_j/\omega)-\sum_j\arctan(\alpha_j/\omega).
 \tag{PT5}
\]
Both sides continue continuously from infinity, which fixes the same branch even when the scalar determinant winds. The full zero factors contribute one in PT4 and zero in PT5.

## PT2. Exact transport cost for a scalar phase

Put \(f(t)=\arctan(e^t)\). Direct differentiation gives
\[
 f'(t)=\frac1{2\cosh t},\qquad 0<f'(t)\le\tfrac12,
 \qquad\int_{\mathbb R}f'(t)\,dt=\frac\pi2.
 \tag{PT6}
\]
For any two real numbers \(a,b\), the fundamental theorem of calculus and Tonelli's theorem give the exact identities
\[
 \int_{\mathbb R}|f(a-x)-f(b-x)|\,dx=\frac\pi2|a-b|,
\]
\[
 \int_{\mathbb R}[f(a-x)-f(b-x)]\,dx=\frac\pi2(a-b),
 \qquad\sup_x|f(a-x)-f(b-x)|\le\tfrac12|a-b|.
 \tag{PT7}
\]
To see the absolute-value equality, first take \(a\ge b\). The difference is \(\int_b^a f'(t-x)dt\ge0\); its integral is \((a-b)\pi/2\). Interchanging \(a,b\) proves the remaining case. This also proves absolute convergence, so no subtraction of two divergent integrals is being made.

For two lists of positive numbers \(\alpha_j,\widetilde\alpha_j\), of the same length, define
\(D=\sum_j|\log\alpha_j-\log\widetilde\alpha_j|\) with the actual chosen pairing. Summation of PT7 yields
\[
 \left\|\sum_j\arctan(\alpha_j/e^x)
              -\sum_j\arctan(\widetilde\alpha_j/e^x)\right\|_{L^1(dx)}
 \le\frac\pi2D,
\]
\[
 \sup_{\omega>0}\left|\sum_j\arctan(\alpha_j/\omega)
                 -\sum_j\arctan(\widetilde\alpha_j/\omega)\right|
 \le\frac D2.
 \tag{PT8}
\]
No common eigenvectors are required. The logarithmic matching cost is smallest for increasing-to-increasing pairing: if \(a\le b\) and \(c\le d\), then
\(|a-c|+|b-d|\le|a-d|+|b-c|\). This follows because \(t\mapsto|t-c|-|t-d|\) is increasing. Replacing each crossed pair proves the assertion by a finite sequence of swaps. Thus ordered spectral pairing uses the full relative information without an eigenvector identification.

## PT3. Four original cutoffs and the complete phase curve

Now use the original four metrics at
\[
 N_0=q-1,\quad N_1=q,\quad N_2=2q-1,\quad N_3=2q,
 \qquad\mathcal Rg=g_{N_0}+g_{N_1}-g_{N_2}-g_{N_3}.
 \tag{PT9}
\]
For this theorem let the word rank be the common original \(\Delta\), and let \(T|_K\) be injective, as on the original conductor-transverse lane. Every \(A_N\) then has its full \(m\) positive eigenvalues. PT1–8 themselves need no such transversality. Let
\[
 D_i=\sum_{j=1}^m|\log\alpha_{j,N_i}-\log\alpha_{j,N_{i+2}}|,
 \qquad i=0,1.
 \tag{PT10}
\]
Choose two real centres \(c_L,c_H\), kept explicit, and put \(c_{N_0}=c_{N_1}=c_L\), \(c_{N_2}=c_{N_3}=c_H\). Define the actual full-word deviations
\[
 E_N=\sum_{j=1}^{\Delta}|\log\lambda_{j,N}-c_N|,
 \qquad\mathcal B=D_0+D_1+\sum_NE_N.
 \tag{PT11}
\]
The complete finite comparison is
\[
 \left\|\mathcal R\Theta(e^x)-2\Delta[f(c_L-x)-f(c_H-x)]\right\|_{L^1(dx)}
 \le\frac\pi2\mathcal B,
\]
\[
 \sup_{\omega>0}\left|\mathcal R\Theta(\omega)-2\Delta
  [\arctan(e^{c_L}/\omega)-\arctan(e^{c_H}/\omega)]\right|
 \le\frac{\mathcal B}2.
 \tag{PT12}
\]
Proof: substitute PT5 at every cutoff. Pair the actual \(m\) compressed eigenvalues only between \(N_i,N_{i+2}\), and apply PT8, costing \(\pi(D_0+D_1)/2\) in integral and \((D_0+D_1)/2\) uniformly. Apply PT7 to each of the \(4\Delta\) word eigenvalues and its stated centre; this costs the remaining terms in PT11. The triangle inequality with the unchanged four signs gives PT12. All directions, including the full observed zero-word factors, were retained before the scalar integration.

The signed phase integral has the exact determinant value
\[
 \frac2\pi\int_0^\infty\mathcal R\Theta(\omega)\frac{d\omega}{\omega}
 =\mathcal R\log\det{}^+H_N-\mathcal R\log\det A_N.
 \tag{PT13}
\]
Here equal positive ranks at the four cutoffs permit pairing within each low/high pair, and PT7 proves absolute convergence and the formula. Put
\[
 F_N=(TI_K)^*G_N(TI_K),\qquad
 \mathcal K=\mathcal R\log\det H_{K,N}.
\]
Since \(A_N=H_{K,N}^{-1/2}F_NH_{K,N}^{-1/2}\), its complete determinant is \(\det A_N=\det F_N/\det H_{K,N}\). Therefore
\[
 \boxed{\mathcal K=\frac2\pi\int_0^\infty\mathcal R\Theta(\omega)
 \frac{d\omega}{\omega}-\mathcal R\log\det{}^+H_N+
 \mathcal R\log\det F_N.}
 \tag{PT14}
\]
This recovers FD13 from the original maps and proves the exact receiving morphism for PT12. In particular the two earlier quantities \(D_0,D_1\) control the frequency calculation, rather than being replaced by the determinant difference alone.

## PT4. Exact smoothing constant and a finite transition error

Retain the physical word scale \(\omega=q^{2q}e^{bq}\), and write
\(c_L=2q\log q+q\eta_L\), \(c_H=2q\log q+q\eta_H\), \(\eta_H\le\eta_L\). The exact scalar smoothing constant is Catalan's integral
\[
 G_{\rm Cat}=\int_0^1\frac{\arctan t}{t}\,dt
 =\sum_{n=0}^{\infty}\frac{(-1)^n}{(2n+1)^2}.
 \tag{PT15}
\]
For the series identity, integrate the finite geometric identity for \(1/(1+t^2)\), then integrate its arctangent remainder divided by \(t\). The remainder is bounded by \(1/(2n+3)^2\), which tends to zero; thus the displayed series follows without an endpoint interchange assumption. Substitution \(t=e^{-qu}\) gives
\[
 \int_{\mathbb R}|\arctan(e^{q(a-b)})-\tfrac\pi2\mathbf1_{b<a}|\,db
 =\frac{2G_{\rm Cat}}q.
 \tag{PT16}
\]
The two half-lines give the same integral because \(\arctan t+\arctan(1/t)=\pi/2\). The single value at equality does not affect any integral. From PT12 and PT16 one obtains the explicit bound on the original phase transition
\[
 \boxed{
 \int_{\mathbb R}\left|\frac{\mathcal R\Theta(q^{2q}e^{bq})}{k}
 -\frac{\pi\Delta}{k}\mathbf1_{\eta_H<b<\eta_L}\right|db
 \le\frac{\pi\mathcal B}{2kq}+
       \frac{8\Delta G_{\rm Cat}}{kq}.}
 \tag{PT17}
\]
This is an integral estimate over the entire real frequency exponent, with no discarded low or high region. For the actual \(\Delta=16k-48\), replacing \(\pi\Delta/k\) by \(16\pi\) adds exactly
\(48\pi(\eta_L-\eta_H)/k\) to the error bound. The transition location remains the original \(\eta_H,\eta_L\). At an exact transition point PT12, not a step-function value, is the finite formula.

## PT5. Root-scale restriction and finite quadrature

On the original root scale \(\omega=k^{2q}e^{bq}\), define
\(w_H=(c_H-2q\log k)/q\), \(w_L=(c_L-2q\log k)/q\). If \(b\le b_+\), then
\[
 0\le \arctan(e^{q(w_L-b)})-\arctan(e^{q(w_H-b)})
 \le e^{q(b-w_H)}.
 \tag{PT18}
\]
Indeed the difference is \(\arctan(e^{q(b-w_H)})-\arctan(e^{q(b-w_L)})\), and \(\arctan t\le t\). PT12 therefore gives, on every finite interval \([b_-,b_+]\) of length \(L\),
\[
 \int_{b_-}^{b_+}|\mathcal R\Theta(k^{2q}e^{bq})|\,db
 \le\frac{\pi\mathcal B}{2q}+2\Delta L e^{q(b_+-w_H)}.
 \tag{PT19}
\]
No small-frequency phase has been set to zero. The omitted profile is bounded by its original high endpoint \(w_H\), and \(\mathcal B\) remains explicit.

For a grid on this interval with maximum mesh width \(h\), the composite trapezoid obeys
\[
 \left|\operatorname{Trap}(g)-\int_{b_-}^{b_+}g(b)db\right|
 \le\frac h2\operatorname{Var}(g).
 \tag{PT20}
\]
To prove it on one cell \([a,b]\), integrate \((t-(a+b)/2)\,dg(t)\); integration by parts gives trapezoid minus integral, whose absolute value is at most \((b-a)\operatorname{Var}_{[a,b]}g/2\). Sum the cells. Every scalar arctangent in PT5 has total variation at most \(\pi/2\). Thus the four-endpoint sum satisfies
\(\operatorname{Var}(\mathcal R\Theta)\le2\pi(\Delta+m)\).
For values with error at most \(\varepsilon\) at each node after forming the signed sum, the resulting finite integral has total error
\[
 \left|\frac{2q}{\pi}\operatorname{Trap}(\mathcal R\Theta)
       -\frac{2q}{\pi}\int_{b_-}^{b_+}\mathcal R\Theta\,db\right|
 \le2q(\Delta+m)h+\frac{2qL\varepsilon}{\pi}.
 \tag{PT21}
\]
The sum error is at most four times a per-cutoff error; that factor must be retained when using individual measurements. FD's angle-tail estimate can give a smaller mesh error for its separated numerator; PT21 instead controls the complete original phase directly and needs no tail hypothesis on its eigenvalues.

Combining PT19 and PT21 bounds the measured phase-area correction at root scale by
\[
 \mathcal B+\frac{4q\Delta L}{\pi}e^{q(b_+-w_H)}
 +2q(\Delta+m)h+\frac{2qL\varepsilon}{\pi}.
 \tag{PT22}
\]
These are the exact quantities to pass from the uniform-return arrival to the finite phase receiver. Their analytic evaluation uses that arrival's proved spectral estimates at their actual scope. A value assigned to the integral without these terms would lose the original projection error.

## Source use and acceptance scope

The finite observed-space construction is the existing [MR1–29 proof](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/e40b46fde72c245dd79ef5691f59c21d6cbf0c75/workbenches/splitzero-tandem/continuations/20260922-original-observation-recovery/MATRIX_RECOVERY_PROOFS.md#L7). The exact phase-area argument is supplied in the frequency arrival, FD10–14. The noncommuting logarithmic transport leading to \(D_i\) is supplied in the earlier uniform-return arrival, Sections2–3. Both complete arrivals must accompany any publication of this continuation. PT1–22 above give all finite proofs used here independently, so these programme citations do not replace a proof step.

The finite Schur map has a human-source reference in Geneviève Dusson, Israel Michael Sigal and Benjamin Stamm, *The Feshbach–Schur map and perturbation theory*, [arXiv:2105.02058v1](https://arxiv.org/abs/2105.02058v1), Theorem1.2. Its original TeX was previously read for this programme. PT4 proves the particular finite determinant identity needed here. PT6–22 are derived explicitly above; the symbol for Catalan's constant denotes the integral and series in PT15, not an imported estimate.

The coefficient \(\mathcal K=(8k-16)C_\partial q+o(kq)\) is now proved in the accompanying CK14, with the complete growing-jet and diagonal arguments PJ1–70 and the exact elliptic identification EL1–14. CK15–18 also prove \(\mathcal B=o(kq)\) on the retained fixed-period domain, so PT17 applies to the entire original measured phase with an error tending to zero in integral norm. The intake ledger records this combined conclusion across all six arrivals. Nothing here assigns an actual zeta zero, a native projected-current sign, or an RH conclusion.
