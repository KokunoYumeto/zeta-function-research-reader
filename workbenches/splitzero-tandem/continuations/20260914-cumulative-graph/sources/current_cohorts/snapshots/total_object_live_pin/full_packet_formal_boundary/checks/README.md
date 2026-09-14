# Exact checks of the full-packet formal phase comparison

Run from the repository root:

```powershell
python work/rh_counterfactual_20260913/total_object/full_packet_formal_boundary/checks/check_formal_phase_comparison.py
```

The script uses Python 3 and SymPy. All calculations use exact rational arithmetic. The JSON receipt contains the original global connection matrices, local critical values and exponents, phase branches, all stored comparison matrices, and the original Taylor CRT matrix and its weighted coordinate map.

These are algebraic test inputs, not claimed Riemann-zeta zeros or RH evidence. They check formulas in the proof and do not substitute finite testing for the general proof.

## Inputs and retained constants

The first input is `h=(s-2)(s-3)^2`, with local branches `b_2=b_3=1`. The second and third inputs are `h=(s-2)(s-10)^2`, with branch pairs `(8,2)` and `(-8,2)` respectively. Each polynomial has two distinct primary factors of unequal multiplicities. The branch identity is exactly `b_rho^(m_rho+1)=a_rho(0)`; the nonunit and negative branches check the scaling and orientation factors. Every primitive is the integral of the original monic polynomial with its value fixed to zero at `s=0`.

## Checks actually executed

- 243 scalar connection equalities: `T' + D T = T G`, coefficient by coefficient for powers `u^-2` through `u^6`, with all `T_0,...,T_8` retained.
- 156 scalar inverse-coordinate equalities: both `w(psi(w))=w` and `psi(w(y))=y` through degree 12.
- 216 scalar pullback equalities: direct series substitution with the derivative factor versus the independent Lagrange-residue coefficient formula through degree 11.
- 156 local relation checks: the exact remainder annihilates `(u*d/dw+w^m)w^r` through the tested ranges, including the omitted congruence class `w^(m+q(m+1))`.
- 486 scalar formal inverse equalities: both `T S=I` and `S T=I` through degree 8.
- The weighted CRT factorization `T_0=W J`, its inverse, and both determinant factors are checked exactly. The three determinants are `1,1,-1`.
- Every positive coefficient of `det T` through degree 8 vanishes, retaining the branch-dependent constant determinant.

The connection truncation is valid because its coefficient at `u^r` uses only `T_(r+2)` and `T_(r+1)`. The local coefficient of `u^q w^a` uses precisely the pullback coefficient at `w^(a+qN)`. Higher local powers cannot alter a lower power of `u`.

## Independent algebra check

The separate reviewer `independent_formula_check` confirmed the following derivations without consulting the script's output.

Formal change of residues gives

```text
[w^n] (rho+psi(w))^b psi'(w)
 = [y^n] (rho+y)^b a_rho(y)^(-(n+1)/N),
```

where the fractional power uses the specified branch. Equivalently, write `a_rho=b_rho^N A_rho`, `A_rho(0)=1`, and retain the explicit factor `b_rho^(-(n+1))`.

The local relation `L(w^(j+1))=w^(j+N)+u(j+1)w^j` gives the stated remainder and its sign. The commutator `[∂_u-Phi/u^2,L]=L/u` proves that the connection descends after localizing at `u`. Applying the descended connection to the coordinate matrix yields the orientation `T'+D T=T G`.

With original coefficient jets ordered by roots and ascending local exponent, the CRT determinant is

```text
det J = product_(rho<sigma) (sigma-rho)^(m_rho*m_sigma).
```

The coordinate map on local one-form jets is lower triangular with diagonal `b_rho^-1,...,b_rho^-m_rho`, hence

```text
det T_0 = det J * product_rho b_rho^(-m_rho*(m_rho+1)/2).
```

For the first input the original matrices are

```text
C = [[-12, -3/2, -3],
     [1/2, -41/4, 2],
     [-1/12, -1/6, -139/12]],
B = [[1/4, -2/3, -1/12],
     [0, 1/2, -4/3],
     [0, 0, 3/4]],
T_0 = [[1, 2, 4],
       [1, 3, 9],
       [-1/2, -1/2, 3/2]].
```

These agree with the machine receipt. The independent reviewer also recovered the original critical values `Phi(2)=-34/3`, `Phi(3)=-45/4` and the exact trace equality. No parent mathematical source was edited by this check task.
