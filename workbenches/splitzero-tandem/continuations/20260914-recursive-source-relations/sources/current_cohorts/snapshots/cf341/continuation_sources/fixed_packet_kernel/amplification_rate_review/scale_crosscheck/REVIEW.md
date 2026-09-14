# Independent arithmetic scale cross-check

Task received verbatim from the parent reviewer:

> Bounded independent arithmetic cross-check only, no sources edits: q=ell(k+1)^2, ell=1+k(m−1), L=2δell(k+1)floor((k+1)^2/4), fixedδ>0,m≥1. TW8 logA/a exact from constants: logA=(k−1)logMα+(p+1)logk+log(C_h/cΓ); loga=(k−3)(logθ−α)−B log(k−2)+logc_h−logCΓ−B/2 log2. p=8m−9/2,B=42+8m,M=B/2. DefineD_n=[1+4(n+M)^2]^M, Λ=log(A/a)+logD_2q,E=2log(A/a)+logD_q−1+logD_q. Compute exact leading Λ,E constants and ratio (2q−1)Λ/L. μ/M etc fixed positive. Also L/qk parity and q²/L growth. Return formulas/proofs concise. I am reading endpoint normalized-boundary evidence and drafting rate-review.

No mathematical source has been edited. In the expression for E, the two final summands are read as log D_{q−1} and log D_q. All logarithms below are natural logarithms. All asymptotics keep δ, m and every positive tail constant fixed and take integer k to infinity, k≥3.

Put

\[
s=\log M_\alpha-\log\theta+\alpha,\qquad
H=p+1+B=16m+\frac{77}{2},
\]
\[
C_0=-\log M_\alpha+3(\log\theta-\alpha)
 +\log\frac{C_h C_\Gamma}{c_\Gamma c_h}
 +\frac B2\log2.
\]

Direct subtraction of the two given expressions, retaining every constant, gives the exact identity

\[
\log(A/a)=ks+H\log k+C_0+B\log(1-2/k).
\tag{SC1}
\]

For m=1 set d=2 and r=1. For m>1 set d=3 and r=m−1. The exact polynomial

\[
q=(m-1)k^3+(2m-1)k^2+(m+1)k+1
\]

shows that \(\log q=d\log k+\log r+O(k^{-1})\). The case m=1 is included by its separate choice of d and r, not by substituting r=0 into a logarithm.

For any fixed c>0 and any fixed a, when cq+a+M>0,

\[
\begin{split}
\log D_{cq+a}
={}&B\log q+B\log(2c)
 +B\log\left(1+\frac{a+M}{cq}\right)\\
 &+M\log\left(1+\frac1{4(cq+a+M)^2}\right).
\end{split}
\tag{SC2}
\]

This is an exact factorization of the original expression for D; it does not change its argument or weight constant M. In particular,

\[
\log D_{2q}=B\log q+B\log4+O(q^{-1}),
\]
\[
\log D_{q-1}+\log D_q=2B\log q+2B\log2+O(q^{-1}).
\]

Consequently, with

\[
a_\Lambda=H+Bd,\quad
C_\Lambda=C_0+B\log r+B\log4,\quad
C_E=2C_0+2B\log r+2B\log2,
\]

the requested expansions, including their constant terms, are

\[
\Lambda=ks+a_\Lambda\log k+C_\Lambda+O(k^{-1}),
\tag{SC3}
\]
\[
E=2ks+2a_\Lambda\log k+C_E+O(k^{-1}).
\tag{SC4}
\]

Here

\[
a_\Lambda=
\begin{cases}
309/2,&m=1,\\
40m+329/2,&m>1.
\end{cases}
\]

In particular,

\[
E-2\Lambda=-B\log4+O(q^{-1}).
\tag{SC5}
\]

The O(q^{-1}) in SC5 follows directly from SC2: the entire log(A/a) expression cancels exactly, including its k and log k terms. No positivity of s has been inserted. If s>0, the leading linear constants in Λ and E are s and 2s; if s=0, their leading logarithmic constants are a_Λ and 2a_Λ.

For the parity calculation put ε_k=1 for even k and ε_k=0 for odd k. Then

\[
\left\lfloor\frac{(k+1)^2}{4}\right\rfloor
=\frac{(k+1)^2-\varepsilon_k}{4},
\]

and direct cancellation of the common original factors ell and k+1 gives

\[
\frac{L}{qk}
=\frac\delta2\left(\frac{k+1}{k}
 -\frac{\varepsilon_k}{k(k+1)}\right)
=\begin{cases}
\dfrac{\delta(k+2)}{2(k+1)},&k\text{ even},\\[4pt]
\dfrac{\delta(k+1)}{2k},&k\text{ odd}.
\end{cases}
\tag{SC6}
\]

In particular L/(qk) tends to δ/2. The requested amplification ratio has the exact form

\[
\frac{(2q-1)\Lambda}{L}
=\frac4\delta\left(1-\frac1{2q}\right)
 \frac{\Lambda}{k+1-\varepsilon_k/(k+1)}.
\tag{SC7}
\]

Substituting SC3 and expanding only this exact quotient gives

\[
\frac{(2q-1)\Lambda}{L}
=\frac{4s}{\delta}
 +\frac4{\delta k}\bigl(a_\Lambda\log k+C_\Lambda-s\bigr)
 +O\left(\frac{\log k}{k^2}\right).
\tag{SC8}
\]

The limit is 4s/δ. It is zero only when s=0, with the other constants held fixed as stipulated.

Finally the exact growth expression is

\[
\frac{q^2}{L}
=\frac2\delta\,[1+k(m-1)]\,
 \frac{(k+1)^3}{(k+1)^2-\varepsilon_k}.
\tag{SC9}
\]

Therefore

\[
\frac{q^2}{L}\sim
\begin{cases}
2k/\delta,&m=1,\\
2(m-1)k^2/\delta,&m>1.
\end{cases}
\tag{SC10}
\]

This uses only the exact input formulas and elementary logarithmic expansions. It supplies no uniform-in-k consequence of any fixed-k kernel theorem.
