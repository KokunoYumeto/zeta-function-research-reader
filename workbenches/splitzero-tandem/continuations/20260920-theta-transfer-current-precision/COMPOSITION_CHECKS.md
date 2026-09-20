# Independent mathematical return

The proposed **192 C² theta** bound is valid, with all constants and domains as stated. The proof establishes the stronger bound **15 C² theta with exactly the same C**.

Full standalone proof: `NATIVE_MOMENT_PHASE_COMPOSITION.tex`, six pages, MC1–16.

The improvement uses the actual source order Hlo <= H <= U I, hence G0 <= U W. Therefore |z0|,|w0| <= C/2. PD11 gives

```text
R <= M theta [4 sqrt(2) u v + (2+sqrt(2)) v²]
  <= 6 M theta (u²+v²)
  <= 6 C theta.
```

The middle positive difference is exactly

```text
6 (u - sqrt(2) v / 3)² + (8/3 - sqrt(2)) v².
```

Retaining all three conjugated complex product error terms gives

```text
|conj(z) w - conj(z0) w0| <= 6 C² theta + 36 C² theta²
                         <= 15 C² theta.
```

Thus the verified stronger tolerance is theta=min(1/4,t*/(15 C²)), with scalar native-moment error epsilon <= theta h/d_src. C=0 gives zero product. MC16 gives the explicit composed original onefold eta_(2j) tolerance through degree 2N.

## Domain and map audit

- Exactly the original simple-quartet domain: k congruent 1 mod 4, k>=77, q=(k+1)², N>=q-1.
- J is the original map from parity coefficients onto E_k, not the observation Lambda J. Its full kernel and the separate fixed K=ker Lambda are retained.
- The complete S=c+iy triangular map, determinant phase, and original physical unit in J_(S,N) remain explicit.
- A=M_S and x are the same original action and class as the native metric varies; no midpoint orthogonal-polynomial class replaces x.
- epsilon_PD=2 theta is the relative-bracket parameter of PD4–19. It is not identified with the original integer outer-truncation expression. The new lower metric is the explicitly proved source-minimum metric; the native G is unchanged.
- All masses and original CAI constants are retained. No original moment or complex phase was assigned a numerical value. No sign or growing-degree conclusion is claimed.
- Later metric-dependent denominators and numerical midpoint-pairing errors retain their own enclosures.

## Exact checks

Both commands pass, using explicit exceptions rather than optimization-disabled assertions:

```text
python verify_moment_phase.py
python -O verify_moment_phase.py

PASS {'identity': 153, 'psd': 134, 'inequality': 708, 'negative': 13} total 1008
Both 192 and the stronger 15 use the same C; no native values assigned.
```

The script checks every scalar coefficient in PD11, the exact positive-square bound, the original 192 chain, the stronger 15 product bound, sharp projection examples, both parity moment blocks, non-unit mass, complete quotient/source order, fixed-kernel metric projections, complex pairings and all three product remainders. Negative cases detect omission of the metric-change term and complex conjugations. The initial negative-test fixture accidentally lay in K, making its products genuinely zero; the fixture was corrected to a non-kernel fixed class before the final exact runs. This was a test-fixture correction, not a failure of the mathematical bound.

These finite matrices and test measures verify universal identities only; none substitutes for the native arithmetic objects.

The stabilized draft-mode TeX check passes: six pages, no undefined references, overfull/underfull boxes, or duplicate-destination notices. Draft mode generates no PDF. No discovery, indexing, packaging, publication or outside-folder changes occurred.

## Final SHA-256 pins

```text
1437fe0c2804fd824960d7444149fc9c3defe34074fb2a907f2e31655de8f278  NATIVE_MOMENT_PHASE_COMPOSITION.tex
32a05e772b2f0060f99b5b619fad5982da1ae520bcba2272d3b05bc8653ecaba  verify_moment_phase.py
```
