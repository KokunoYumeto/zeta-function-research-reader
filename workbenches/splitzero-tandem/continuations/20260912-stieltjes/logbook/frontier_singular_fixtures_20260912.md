# Independent singular-frontier and relative-loss evidence

Date: 2026-09-12. Assigned scope: singular zero Jordan blocks of the finite frontier matrix and the determinant/energy formulas from the actual vectors `b = Tplus - R F`. No source or parent fragment was edited. The formulas below are proved for arbitrary stated finite matrices; the six Jordan fixtures and four realized-loss fixtures supplement those proofs.

## 1. Exact zero Jordan structure

Let `T : C^(2r) -> C^n`, let `J0 = [[0,I_r],[I_r,0]]`, and put `K=T* T`, `A_fr=J0 K`, `W_fr=T J0 T*`. Set `H=ran K=(ker K)^perp`, `d0=dim ker K`, and `S=(K^(1/2) J0 K^(1/2))|H`. The operator `S:H->H` is Hermitian. Put `q=dim ker S`.

Since `J0` is invertible, `ker A_fr=ker K`. The exact identities are

```
K^(1/2) A_fr = S K^(1/2),
A_fr^2 = J0 K^(1/2) S K^(1/2),
A_fr^3 = J0 K^(1/2) S^2 K^(1/2).
```

Here the copies of `K^(1/2)` landing in or starting from `H` are understood with their displayed domains, not as inverted singular matrices. The map `K^(1/2):C^(2r)->H` is onto, and `J0 K^(1/2):H->C^(2r)` is injective. Consequently `rank A_fr^2=rank S`, while `rank A_fr^3=rank S^2=rank S`, the last equality following from the Hermitian spectral decomposition. The equality of these two ranks excludes every zero Jordan block of length at least three. Also

```
dim ker A_fr^2 - dim ker A_fr
  = (2r-rank S) - (2r-rank K)
  = dim H-rank S = q.
```

The left side counts the zero blocks of length at least two. There are therefore exactly `q` blocks of length two and `d0-q` blocks of length one. In particular `q<=d0`. The algebraic multiplicity of zero is `d0+q`. This includes `K=0`, where `q=0` and all `2r` blocks have length one.

For completeness, in the decomposition `H direct_sum ker K`, the upper-left block of `A_fr` is `(P_H J0|H) K_H`, which is similar to `S` through the invertible `K_H^(1/2)`. Its upper-right block is zero. Hence

```
det(lambda I_(2r)-A_fr)=lambda^d0 det(lambda I_H-S).
```

For any nonzero eigenvalue, `K^(1/2)` intertwines its generalized eigenspace with that of `S`. The restriction is injective, since its kernel lies in `ker A_fr`; it is onto by the algebraic multiplicities in the characteristic-polynomial identity. Thus every nonzero eigenvalue of `A_fr` is real and semisimple. The exact intertwiner, together with the zero blocks just computed, retains the singular information lost by a mere list of nonzero eigenvalues.

The polar map `Q:H->ran T`, defined by `Q(K^(1/2)x)=Tx`, is well-defined because `ker T=ker K`; its norm identity makes it a surjective isometry. Then

```
(W_fr)|ran T = Q S Q*,
W_fr T = T A_fr,
q = nullity((W_fr)|ran T) = rank T - rank W_fr.
```

The nullity of the full `n by n` matrix `W_fr` is not the stated `q` when `ran T` is proper: `W_fr` also vanishes on `(ran T)^perp`. The displayed restriction is the exact necessary typing.

### Mixed singular fixture

For `r=2`, take

```
T = [[1,0,0,0], [0,2,0,0], [0,0,0,3]],
K = diag(1,4,0,9),
A_fr = [[0,0,0,0], [0,0,0,9], [1,0,0,0], [0,4,0,0]],
W_fr = [[0,0,0], [0,0,6], [0,6,0]].
```

Here `A_fr e1=e3`, `A_fr e3=0`, while the invariant span of `e2,e4` has matrix `[[0,9],[4,0]]` and eigenvalues `6,-6`. Thus the zero block has length two and simultaneously both nonzero real signs occur. The characteristic polynomial is `lambda^2(lambda-6)(lambda+6)`, `d0=q=1`.

Additional exact fixtures cover the zero matrix, a single nilpotent block, three semisimple zero blocks together with eigenvalue `2`, simultaneous zero blocks of lengths one and two with nonzero eigenvalues `2,6,-6`, and a genuinely complex, non-diagonal `K` obtained by an explicitly recorded rational unitary change commuting with `J0`.

## 2. Actual geometric relative loss and chi

Let `G` be positive definite of size `d by d`, let `Omega` be positive definite of size `r by r` (diagonal in the source), and let `F,E:C^r->C^d` be arbitrary complex matrices. Let `R:C^d->C^(d+r)` and `Tplus:C^r->C^(d+r)` obey `R*R=G`, `Tplus*Tplus=Omega`, `Tplus*R=0`. These are realized exactly by the stacked positive square roots

```
R=[G^(1/2);0],       Tplus=[0;Omega^(1/2)].
```

Define

```
b=Tplus-RF,               H=b*b=Omega+F*GF,
Y=-b H^(-1) F*G,          C=b Omega^(-1) E*G,
Delta=Y*Y,               Gnext=G-Delta,
U=G^(1/2) F Omega^(-1/2), V=G^(1/2) E Omega^(-1/2).
```

Because `b*R=-F*G`, `Y=bH^(-1)b*R` is the orthogonal projection of `R` onto `ran b`. Therefore `(R-Y)*(R-Y)=Gnext`. Direct multiplication, using
`H=Omega^(1/2)(I_r+U*U)Omega^(1/2)`, proves

```
Pi = G^(-1/2) Delta G^(-1/2) = U(I_r+U*U)^(-1)U*,
I_d-Pi = (I_d+UU*)^(-1),
Gnext = G^(1/2)(I_d+UU*)^(-1)G^(1/2) > 0,
det(Gnext)/det(G) = det(I_d+UU*)^(-1),
tau = Tr(G^(-1)Delta) = Tr(Pi).
```

For the second identity, multiply `I_d-U(I_r+U*U)^(-1)U*` by `I_d+UU*`; the two terms with a left factor `U` cancel because `(I_r+U*U)^(-1)(I_r+U*U)=I_r`. The remaining determinant identity follows by taking determinants of the positive congruence, without treating `G` and `Delta` as commuting.

The other exact products are

```
Y*C = -GF Omega^(-1)E*G,
G^(-1/2) [-(Y*C+C*Y)] G^(-1/2) = UV*+VU*,
G^(-1/2) C*C G^(-1/2) = V(I_r+U*U)V*.
```

Taking traces of the last equality gives

```
chi = Tr(G^(-1)C*C)
    = Tr(V*V)+Tr((VU*)*(VU*))
    = ||V||_HS^2 + ||VU*||_HS^2.
```

Thus `T=[U,V]` and `J0` from section 1 realize the original relative weight as `W_fr=T J0 T*`. No independent replacement of `Y` or `C` is used.

### Rational noncommuting fixture

Choose the positive square root `G^(1/2)=[[2,1],[1,2]]`, `Omega^(1/2)=diag(2,3)`,

```
G=[[5,4],[4,5]], Omega=diag(4,9),
F=[[1,2],[-1,1]], E=[[i,1],[2,-i]].
```

The exact realized quantities are

```
Pi = (1/299) [[190,71],[71,154]],
det(Gnext)/det(G)=36/299,
tau=344/299,
chi=10219/648,
UV*+VU* = [[29/9,35/18-i/12],[35/18+i/12,-10/9]].
```

The checker also retains the `F=0`, `E=0`, and rectangular `d=2,r=3` cases. In particular `F=0` gives zero loss and determinant ratio one while `chi=||V||_HS^2` can remain positive; no division by loss or by its rank is used.

## 3. Reproduction and scope

Files relative to the standalone package root:

- `scripts/check_frontier_singular_fixtures_20260912.py`: reproducible SymPy exact-arithmetic checker.
- `checks/frontier_singular_fixtures_20260912.json`: 102 exact checks passed.
- `checks/frontier_singular_fixtures_20260912_optimized.json`: the same 102 passed under `python -O`.
- `checks/frontier_singular_negative_controls_20260912.json`: six deliberate-error runs and their recorded rejection messages.

From that root, reproduce positive checks with:

```text
python scripts/check_frontier_singular_fixtures_20260912.py --output checks/frontier_singular_reproduced.json
python -O scripts/check_frontier_singular_fixtures_20260912.py --output checks/frontier_singular_reproduced_optimized.json
```

For deliberate-error runs add `--negative-control --negative-case CASE`, where CASE is `nilpotent-square`, `semisimple-zero`, or `chi-without-mixed-term`; each must exit 1 before writing a success receipt. Run each both normally and under `-O`.
- `frontier_singular_negative_controls_20260912.json`: commands, expected status 1, actual status 1, and the complete mismatch output for six negative-control runs.

Run the script with `--output PATH`. The `--negative-control` option defaults to deliberately replacing a nilpotent square by the identity. Add `--negative-case semisimple-zero` to demand two length-one zero blocks for the actual nilpotent fixture `T=[1,0]`; the checker rejects the false claim and reports the actual single length-two block. Add `--negative-case chi-without-mixed-term` to omit the mixed term from the actual noncommuting geometric fixture; the checker rejects the claimed `chi=265/36` against its exact actual value `10219/648` (difference `5449/648`). All three negative cases exited with status 1 and their explicit mismatch both normally and under `-O`. The checker uses no Python `assert`, so optimization does not disable its validation. Its receipts contain all exact fixture matrices, characteristic polynomials, block counts, loss matrices, determinant ratios, and chi values. These finite checks do not assert an arithmetic asymptotic estimate or RH.

No mathematical error was found in the assigned identities. The restriction `W_fr|ran T` is essential when computing `q` from a rectangular `T`.
