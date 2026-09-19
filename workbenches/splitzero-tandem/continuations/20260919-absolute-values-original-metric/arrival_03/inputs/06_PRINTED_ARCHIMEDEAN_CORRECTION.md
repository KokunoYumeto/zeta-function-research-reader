# Exact correction to the archived Guinand–Weil comparison

19 September 2026. This is a correction to the programme's local equation labelled `guinand-weil-arch-map`, not a claim that Guinand's published theorem is false. The original source file is preserved unchanged. The false local equality cannot be completed by supplying another proof of it.

## 1. The two originally printed functionals

The Original Six Readers text defines

    g(t)=sqrt(2/pi) integral_0^infinity f(x) cos(tx) dx,
    2 H_f=integral_0^infinity f(x)[1/x-exp(-x/2)/sinh x] dx,
    K(x)=exp(|x|/2)/|exp(x)-exp(-x)|.

Its asserted comparison is

    2 integral f(x)exp(-x/2) dx
       -PF integral_R f(|x|)K(x) dx-f(0)log(2pi)
     =2H_f+sqrt(2/pi) integral_0^infinity g(t)log(t/(2pi))dt.       (G1)

The finite part uses the original subtraction f(0)log Lambda. Both quantities are well defined on, in particular, half-line functions which are continuous and piecewise C^2, with integrable second derivative on their finitely many pieces, finitely many first-derivative jumps, and exponential decay of the function and its first two derivatives. Such functions are an explicitly specified subspace of the recorded Weil/Guinand common test domain. Their cosine transforms are O((1+t)^(-2)), by two integrations by parts, with the derivative-jump terms retained.

## 2. Direct evaluation of the Fourier logarithm

For this test subspace, ordinary cosine inversion at zero gives

    sqrt(2/pi) integral g(t)dt=f(0).

Use the actual reference test exp(-x), whose cosine transform is sqrt(2/pi)/(1+t^2). The logarithmic integral of that reference is -log(2pi), since substitution t->1/t makes integral log t/(1+t^2) vanish.

For h(x)=f(x)-f(0)exp(-x), h(0)=0 and integral |h(x)|/x dx is finite. The identity log t=integral_0^infinity (exp(-r)-exp(-tr))dr/r, applied first on finite intervals, and the exact Laplace cosine integral

    integral_0^infinity exp(-rt) cos(tx)dt=r/(r^2+x^2)

give

    sqrt(2/pi) integral g_h(t)log t dt
      =-(2/pi) integral_0^infinity integral_0^infinity
                      h(x)/(r^2+x^2) dx dr
      =-integral_0^infinity h(x)/x dx.

The double integral is absolutely convergent after replacing h by |h| because integral_0^infinity dr/(r^2+x^2)=pi/(2x). The mean-zero transform removes the first Frullani term. The O(t^(-2)) transform bound controls the truncated limits. Thus

    sqrt(2/pi) integral g(t)log(t/(2pi))dt
      =-integral [f(x)-f(0)exp(-x)]/x dx-f(0)log(2pi).            (G2)

This is a direct calculation, with the cosine convention unchanged.

## 3. Direct evaluation of the finite part and its difference

The same regulated-reference argument used in the Montgomery calculation gives

    PF integral_R f(|x|)K(x)dx
      =integral_0^infinity {
            f(x)exp(x/2)/sinh x-f(0)exp(-x)/x }dx.              (G3)

The reference regulated integral is f(0)log(1+Lambda), so its difference from the original f(0)log Lambda tends to zero. The terms in braces are integrable at zero and infinity.

Substitute (G2)–(G3) into the difference of the two sides of (G1). Every singular subtraction and constant cancels explicitly. The remaining kernel is

    2exp(-x/2)+(exp(-x/2)-exp(x/2))/sinh x
       =2exp(-x/2)-sech(x/2).

Therefore the exact corrected comparison is

    [left side of (G1)]-[right side of (G1)]
      =integral_0^infinity f(x)
                    [2exp(-x/2)-sech(x/2)]dx.                 (G4)

It is not the zero functional. This identifies the exact relation between the two originally printed expressions instead of silently changing either definition.

## 4. A single admissible test refutes the printed equality

Take f(x)=exp(-3x/2). This is in the stated original intersection domain and in the explicit subspace above. Its transform is

    g(t)=sqrt(2/pi) (3/2)/(t^2+9/4).

The finite part is gamma_E-log 2, by (G3) or the digamma sum -log 2-psi(1). The complete values are

    PF=gamma_E-log 2,
    2 H_f=2-gamma_E-log 3,
    sqrt(2/pi) integral g(t)log(t/(2pi))dt=log(3/(4pi)).

Consequently the left side of (G1) is 1-gamma_E-log pi, while the right side is 2-gamma_E-log pi-2log 2. Their difference is exactly

    2log 2-1 >0.                                             (G5)

Thus the source's claim that (G1) was an algebraic corollary is invalid with the displayed kernels. The original Montgomery completion in note 03 uses the correctly evaluated Weil kernel directly and does not use (G1). The corrected equation (G4), and not the false equality, is the valid receiving expression on the explicit common test subspace.
