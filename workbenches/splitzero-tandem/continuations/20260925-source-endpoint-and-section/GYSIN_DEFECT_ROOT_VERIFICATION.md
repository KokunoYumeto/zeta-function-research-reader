# Mathematical verification of the complete Gysin comparison

24 September 2026. Complete root verification of GDC0–GDC14 in GYSIN_DEFECT_CLOSURE_AND_POSITIVE_RECEIVER.md, SHA256 5d0f471b3250e4ee894caca68232c556d64a137a49a9fe25a641db61b94f79ab. This includes the typesetting repair placing parentheses around \(N_0\) before its strong-dual subscript.

## Coverage and review provenance

The root read every section and formula of the independent first derivation, then checked and integrated the complete restriction-topology proof, explicit bounds, and restoration of both endpoint lines. A separate mathematical reviewer read complete RGR0–RGR12 and independently derived the scale ratio, strong annihilator argument and strong-open restriction theorem. That session ended before a complete audit of the final written GDC version. This note records complete root verification and those independent constituent derivations; it does not claim a complete independent final-version audit.

The received RGR source has SHA256 dd0c5fe172b2d4e2c18a337a1a92d06d9a523196f349ffa34bdb6cef1969e814. Its complete text and originating task's review receipt are retained under sources/programme/cc_sheaf. Root read RGR0–RGR12 completely. PTQ0–PTQ11 and PSC0–PSC9 are already present with their precise review scopes. SDT supplies the proved topology of the actual coefficient spaces; no new complete reading of a human paper is claimed here.

## Coefficients, conjugation and closure

GDC0 uses the original source row \(0\to J\to A\to Q\to0\) after complete arithmetic reconstruction. It assigns no coefficient value or operation to tau. In
\[
A_H(y)(F)=\sum_\rho m_\rho F(\rho)\overline{y_{\rho^\#}},
\]
the Hilbert inner product is linear in the first variable. Thus \(A_H\) is anti-linear and \(\sigma_r:\overline H\to Q'\) is linear. Reflection fixes \(\gamma\), changes \(\sigma\) to \(1-\sigma\), and negates \(d_r\), producing exactly the minus sign in GDC1.2.

The coordinate choice \(y_{\rho^\#}=1/(m_\rho d_r(\rho^\#))\) gives the value functional at each actual off-line point, because conjugating the resulting product still gives \(1\). This proves the preannihilator \(N_O\), without unrestricted source interpolation. SDT's strong-bidual theorem makes separation of the strong closure an evaluation at an actual \(F\in Q\); that proves \(\overline{I_r}^{\,\beta}=N_O^\perp\). The closed strong embedding \(q'\) then proves the ambient closure \(A_O^\perp\). Neither image is presumed closed.

## Scale maps and supported complexes

The unscaled differences factor as
\[
r^\sigma-r^{1-\sigma}
 =(\sigma-\tfrac12)\int_0^1(\log r)
\left(r^{1/2+u(\sigma-1/2)}+r^{1/2-u(\sigma-1/2)}\right)\,du.
\]
The two positive bounds in GDC3.2a control the actual diagonal ratio and its reciprocal on the entire open strip. Setting its line value to \(1\) preserves bounded invertibility; no analytic dependence on a hypothetical moving zero is required. Direct coordinate multiplication proves \(D_r=D_tV_{r,t}\), the cocycle identity, and equality of the images before closure. The parameter \(1\) is explicitly excluded.

The current differential in GDC4.1 uses \(+\delta_pa_r\). Therefore the map to scale \(t\) is identity on currents and \(\overline V_{r,t}\) on the supported coefficient. Substitution proves it is a cochain isomorphism with the specified inverse. The positive-Dirac costalk is \([\overline H\xrightarrow{+a_r}B]\); the literal shifted-cone target coordinate has the opposite sign, exactly as in RGR6. The coefficient reflection sign is unrelated to this cone-coordinate comparison.

The domain decomposition supplies the literal direct summand \(i_*\overline{H_L}\), and the complement has injective costalk differential. Thus \(H^0(i^!\mathscr E_r)\) is exactly the conjugate of the universal positive receiver. The raw degree-one quotient is retained. Restoring \(i_*E_p'[-1]\) adds both original endpoint lines in degree one, with all receiving maps identity on them.

## Topology of the original dual extension

The source row \(0\to J\to A_O\to N_O\to0\) is strict by the preimage definition and openness of the original quotient. The transpose's left strong embedding follows from SDT's constructive compact lifting, applied to this actual quotient. The unseparated pushout row GDC6.1 follows by direct kernel and image calculation. Its closure-of-zero row is retained explicitly.

For the stronger right-hand topology, the proof applies to each actual Fréchet space \(X\) whose bounded sets have compact closure and each stated closed subspace \(L\). For every compact absolutely convex \(K\subset X\), an element \(\lambda\in L'\) bounded by \(1/2\) on \(K\cap L\) extends to an element of \(X'\) bounded strictly by \(1\) on \(K\). The proof of GDC7.6 is valid: a contrary sequence approaches a point of \(K\cap L\), and continuity of \(\lambda\) there contradicts its bound. The gauge of \(K+U\) is a continuous seminorm. Complex Hahn–Banach extends the functional with this same gauge bound; compactness makes the bound on \(K\) strictly below \(1\). These polars form a base of strong neighborhoods, proving openness.

For bounded lifts of dual families, strong boundedness implies pointwise boundedness. The given Baire argument makes the family equicontinuous on the closed Fréchet subspace. Its inherited topology supplies one ambient seminorm controlling the family. Extending every member with this same seminorm gives a strongly bounded family in the ambient dual. This proves the asserted bounded lifting without constructing a linear section.

It follows that the maps \(\alpha,\eta\) in GDC7.3 are actual strong topological isomorphisms and both rows are strict. This is a proved strengthening of the initial draft's continuous bijections. It does not replace the unseparated quotient by the separated one.

## Residue, jets and receiving triangle

On \(N_O\), the quotient residue is exactly the positive line sum. Line isolators prove injectivity of the map from \(\overline{H_{\rm pos}}\); they do not prove surjectivity onto the full source dual. The closure of the original residue image is \(N_0^\perp/S_O\), whose complementary quotient retains all functionals on \(N_0\). The source compatibility quotient \(Q/(N_L+N_O)\) remains in the exact row GDC9.1.

The compact-test inclusion \(A_O\hookrightarrow A\) transposes to the displayed continuous cochain map of current complexes. Restriction kills exactly \(A_O^\perp\), the closed defect image, so the target attaching map is zero. The source complex is not declared split. In the vector-sheaf category, the comparison of the two fibre triangles with identical supported term gives the retained coefficient fibre \(\underline{A_O^\perp}[1]\) and the exact triangle GDC10.4. This is compatible with the independently exhibited current map and the proved strong topological identification of its coefficient quotient.

At every actual multiplicity block, the off-line condition kills its value and retains its \(m_\rho-1\) higher-jet coordinates; at line points it retains all \(m_\rho\) coordinates. Original residue unit, complementary point, signs and multiplicity factors in GDC11.3 agree with RGR2.7. The Cauchy–Schwarz tail estimate proves strong convergence of the residue functionals, not convergence of primal finite numerators.

Finally \(A_HT_n=n(T_{1/n})'A_H\) follows directly by conjugating the multiplier at \(\rho^\#\), yielding \(n^{1-\rho}\). This gives GDC12's source-conjugate covariance and full degree \(n\). No noninteger geometric cover or extra angular degree is inferred. Original \(\zeta\), full \(F_0\) comparison, endpoint and trivial-zero values and the two Weil contributions remain as written.

The outcome is the actual closure, dual source, scale isomorphism and quotient receiving map. It does not establish vanishing of the original Gysin defect or identify this analytic coefficient construction with Deligne's complete arithmetic weight argument.
