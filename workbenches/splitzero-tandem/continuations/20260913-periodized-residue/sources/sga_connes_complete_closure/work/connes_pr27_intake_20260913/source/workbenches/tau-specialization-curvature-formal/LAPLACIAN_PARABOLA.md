# A quantitative Laplacian bound from the original control form

13 September 2026. This is a written consequence of the source-preserving identities in `HOCHSCHILD_COMPARISON.md`, equations (H29)–(H30). It concerns the original Gram metric and does not require diagonalizability. The scalar enclosure below is not included in the selected Lean audit of this package.

Let \(G\succ0\), \(k\in\mathbb R\), and let the actual arithmetic action be \(A\). Set

\[
B=A-\frac{k}{2}I,\qquad W=A^*G+GA-kG,\qquad L=A^2-kA.
\tag{P1}
\]

Suppose a verified two-sided control is available on that same metric:

\[
-\varepsilon G\preceq W\preceq\varepsilon G,\qquad\varepsilon\ge0.
\tag{P2}
\]

The source's rank-two formula supplies an explicit way to evaluate the least such \(\varepsilon\); (P2) is not asserted to be uniformly small on growing arithmetic packets.

## Numerical-range enclosure

For every \(v\ne0\), put \(z=\langle v,Lv\rangle_G/\|v\|_G^2\). Then

\[
\boxed{\Re z\le\frac{\varepsilon^2-k^2}{4},\qquad
(\Im z)^2\le\varepsilon^2\left(\frac{\varepsilon^2-k^2}{4}-\Re z\right).}
\tag{P3}
\]

In particular every eigenvalue of \(L\) lies in the displayed closed left-facing parabola. This is stronger than a statement only about the eigenvalues: it controls the entire numerical range in the original \(G\)-inner product.

**Proof.** Normalize \(\|v\|_G=1\), put \(r=\|Bv\|_G\), and define

\[
a+ib=\langle v,G^{-1}WBv\rangle_G.
\tag{P4}
\]

The operator \(G^{-1}W\) is self-adjoint in the \(G\)-metric, and (P2) bounds its operator norm by \(\varepsilon\). Cauchy–Schwarz gives

\[
a^2+b^2\le\varepsilon^2r^2.
\tag{P5}
\]

The exact energy identity \(GL=WB-B^*GB-k^2G/4\) gives

\[
x:=\Re z=a-r^2-k^2/4,\qquad\Im z=b.
\tag{P6}
\]

First \(a\le\varepsilon r\), and completing the square proves

\[
x\le\varepsilon r-r^2-k^2/4
=\frac{\varepsilon^2-k^2}{4}-(r-\varepsilon/2)^2.
\tag{P7}
\]

For the second assertion, compute without discarding the cross term:

\[
\begin{aligned}
\varepsilon^2\left(\frac{\varepsilon^2-k^2}{4}-x\right)-b^2
&=(a-\varepsilon^2/2)^2+\varepsilon^2r^2-a^2-b^2\\
&\ge0.
\end{aligned}
\tag{P8}
\]

This proves both assertions, including \(\varepsilon=0\). No spectral simplicity, Euclidean normality, or commutation with the restriction-loss matrix is used.

## What it says about the Connes–Consani comparison

At weight one, the chapter's arithmetic Laplacian acts as \(A(A-I)\). Formula (P3) therefore turns a source-level rank-two control certificate into a quantitative spectral enclosure for that Laplacian. The positivity and adjoint belong to the original \(G=R^*R\), whose failure to be invariant was calculated rather than assumed away.

If \(0<\varepsilon<|k|\), the numerical range has strictly negative **real part**. This does not make its spectrum real; it is not the negative-real-spectrum conclusion in Connes and Consani's Corollary 4.3. At a finite positive error, the parabola retains non-real possibilities.

For a repeated block \(A=\rho I+N\), the action remains \(L=\rho(\rho-k)I+(2\rho-k)N+N^2\). Nothing in the proof deletes the nilpotent term. An exact positive self-adjoint realization on a full multiple-zero block would impose extra semisimplicity; (P3) avoids making that assumption.

For an actual tensor tower with action containing the character \(k\rho\), division by \(k^2\) gives the same enclosure for the fixed scalar \(\rho(\rho-1)\), with error ratio \(\varepsilon_k/k\). A separately proved limit \(\varepsilon_k/k\to0\) would collapse these enclosures to the negative real half-line. This records a precise quantitative contract for the original tower; the limit is not proved by the enclosure itself.

Reference: Connes, A., & Consani, C. (2023). Hochschild homology, trace map and \(\zeta\)-cycles. In *Cyclic cohomology at 40: Achievements and future prospects* (Vol. 105, pp. 83–101). American Mathematical Society. https://doi.org/10.1090/pspum/105/01896
