# Source erratum: the unit quotient and fixed-modulus character sector

This erratum concerns the programme's BCM crosswalk, not Ha and Paugam's paper.

The affected public version is [the crosswalk at commit e1dc06a](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/e1dc06aa68bb810cf7d8b0006942f5b036b8b765/satellites/21_bcm_shimura_dirichlet_crosswalk.tex). Its bytes were freshly verified during the retrospective. The corrected satellite is published alongside this report. Older compiled programme readers have not been rebuilt as part of this bounded erratum.

The primary source is Eugene Ha and Frédéric Paugam, [Bost–Connes–Marcolli systems for Shimura varieties. I. Definitions and formal analytic properties](https://arxiv.org/abs/math/0507101v1), author TeX subsections `Dedekind-zeta` and `Dirichlet-zeta`. The macro `OFh` in that source means the profinite completion of the ring of integers.

## Correct quotient

For a number field F, write O_F for its ring of integers and put

\[
\widehat O_F^{\natural}=\widehat O_F\cap\mathbb A_{F,f}^{\times}.
\]

The semigroup of nonzero integral ideals is

\[
\widehat O_F^{\times}\backslash\widehat O_F^{\natural}.
\]

Our displayed quotient omitted the hat on the unit group. Quotienting by global units O_F^× is a different operation and does not give the stated ideal semigroup. The two occurrences in the local satellite are corrected.

## Keep the chosen modulus

The all-ideal formula for a finite unramified ideal-class character is valid as stated at that scope. In the ray-modulus semigroup, however, the ideals are required to be prime to the modulus. Consequently its trivial-character trace is

\[
\sum_{(I,\mathfrak m)=1}\operatorname{Nm}(I)^{-s}
=\zeta_F(s)\prod_{\mathfrak p\mid\mathfrak m}
\left(1-\operatorname{Nm}(\mathfrak p)^{-s}\right),
\qquad \Re s>1.
\]

This follows by removing exactly the local geometric-series factors belonging to prime divisors of the fixed modulus in the absolutely convergent ideal Euler product. No change of modulus is implicit in selecting the trivial character. The local satellite now distinguishes the all-ideal class-character formula from this fixed-modulus formula.

The rational trace with its original trivial class datum remains the Riemann zeta function. The general number-field trace with its original ideal semigroup remains the Dedekind zeta function. The correction does not turn the Hamiltonian energy spectrum into the zeta-zero spectrum and makes no statement resolving RH.

Audit status: original source passages checked directly; corrected source published with the report; not a re-verification of every earlier BCM-dependent programme calculation.
