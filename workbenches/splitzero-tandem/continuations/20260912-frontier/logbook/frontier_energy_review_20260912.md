# Independent review: frontier energy and the full singular zero fibre

Date: 2026-09-12. Reviewer task: `frontier_energy_review`.

Input read completely: `output/split_zero_rh_tandem_2026-09-12/sources/web_symmetric_frontier_delivery/Tau_Symmetric_Frontier_Control/NOTE.tex`, especially §§3–4 and the eigenline formula (8.1). SHA256: `734B6C935892EBD9D18B506F6B592F1CA3489AFCB95D5C669A489F4CA04656CF`.

Scope: verify the parent task's proposed exact energy bridge and singular spectral correspondence. No original source or main TeX is edited. The arguments below use the source's actual maps, with their original Gram matrices. Square-root coordinate maps are invertible comparisons, not replacements of an arithmetic metric.

## 1. Declared objects and all coordinate maps

Fix tensor degree k≥1 and M≥k(d−1), with the nonempty full-order arithmetic packet and all source conventions unchanged. Write n=dim E_k and r=binomial(M+k,k−1). The source supplies

\[
R=R_M:\mathbb C^n\longrightarrow\mathcal H_k,\quad
G=R^*R>0,\quad
T_+:\mathbb C^r\longrightarrow\mathcal H_k,
\]
\[
T_+^*T_+=\Omega=\operatorname{diag}(\omega_\beta)>0,
\qquad T_+^*R=0,
\]
\[
F=[z_\beta]:\mathbb C^r\to\mathbb C^n,\qquad
E=[w_\beta]:\mathbb C^r\to\mathbb C^n.
\]

The letter E in this review denotes the source matrix E_+, not the arithmetic quotient. Its original source type and columns are retained by this declaration. The actual relation isomorphism and Gram are

\[
b=T_+-RF:\mathbb C^r\xrightarrow{\sim}\mathcal E_M,
\qquad H=b^*b=\Omega+F^*GF.
\]

The two original finite-domain maps into the relation layer are

\[
Y=-bH^{-1}F^*G,\qquad C=b\Omega^{-1}E^*G.
\]

Set

\[
U=G^{1/2}F\Omega^{-1/2},\qquad
V=G^{1/2}E\Omega^{-1/2},\qquad
T=[U,V]:\mathbb C^{2r}\to\mathbb C^n.
\]

All square roots are the unique positive Hermitian square roots of the displayed positive matrices; their inverses exist. Thus these equations give reversible coordinate comparisons for F and E:

\[
F=G^{-1/2}U\Omega^{1/2},\qquad
E=G^{-1/2}V\Omega^{1/2}.
\]

In particular none of the source norms \(\omega_\beta\), source jets \(z_\beta,w_\beta\), or the unit in those jets has been assigned a new value.

## 2. Relative loss, determinant, and actual defect energy

The source representative update gives

\[
G_+=G_{M+1}=G-Y^*Y=G-GFH^{-1}F^*G.
\]

Since

\[
H=\Omega^{1/2}(I_r+U^*U)\Omega^{1/2},
\]

the relative loss is exactly

\[
\Pi:=G^{-1/2}(G-G_+)G^{-1/2}
=U(I_r+U^*U)^{-1}U^*.
\]

Multiplication by I_n+UU* proves directly that

\[
I_n-\Pi=(I_n+UU^*)^{-1}.
\]

For example, using \((I_n+UU^*)U=U(I_r+U^*U)\), the product of I_n+UU* with the left side equals I_n+UU*−UU*=I_n. Consequently G_+>0 and

\[
\frac{\det G_+}{\det G}
=\det(I_n-\Pi)=\det(I_n+UU^*)^{-1}.
\]

If \(\lambda=\lambda_{\max}(UU^*)\), then the spectral theorem for the positive matrix UU* gives

\[
\|\Pi\|=\frac{\lambda}{1+\lambda}<1.
\]

This lambda is exactly the source's \(\lambda_{k,M}\). Indeed substituting \(v=G^{1/2}x\) into its quotient gives

\[
\frac{v^*F\Omega^{-1}F^*v}{v^*G^{-1}v}
=\frac{x^*UU^*x}{x^*x}.
\]

The original defect energy is

\[
\chi=\operatorname{Tr}(G^{-1}C^*C).
\]

Using b*b=H without replacing b yields

\[
\begin{aligned}
\chi
&=\operatorname{Tr}(E\Omega^{-1}H\Omega^{-1}E^*G)\\
&=\operatorname{Tr}(V(I_r+U^*U)V^*)\\
&=\|V\|_{\rm HS}^2+\|VU^*\|_{\rm HS}^2.
\end{aligned}
\]

Every trace is finite-dimensional and cyclic rearrangement is between finite matrices. Both summands are nonnegative and the equality includes the cross-coordinate term VU*.

For completeness the full relative weight is

\[
\widetilde W:=G^{-1/2}WG^{-1/2}
=UV^*+VU^*=T J_0T^*,
\qquad J_0=\begin{pmatrix}0&I_r\\I_r&0\end{pmatrix}.
\]

To verify its sign from the original relation maps, calculate

\[
Y^*C=-GFH^{-1}b^*b\Omega^{-1}E^*G
=-GF\Omega^{-1}E^*G.
\]

Thus \(W=-(Y^*C+C^*Y)=G(F\Omega^{-1}E^*+E\Omega^{-1}F^*)G\), proving the displayed coordinate equation with the original minus signs intact.

There is also a direct energy estimate with these exact maps. Set y=YG^{-1/2} and c=CG^{-1/2}. For every unit x,

\[
|x^*\widetilde Wx|
=2|\operatorname{Re}\langle yx,cx\rangle|
\le2\|yx\|\|cx\|
\le2\sqrt{\|\Pi\|\chi}.
\]

Here y*y=Pi, and \(\|c\|_{op}^2\le\operatorname{Tr}(c^*c)=\chi\). Therefore

\[
\epsilon_{k,M}^2\le4\frac{\lambda_{k,M}}{1+\lambda_{k,M}}\chi_{k,M}.
\]

This inequality supplements the full signed matrix; it does not replace that matrix with a scalar.

## 3. Original border coordinates and the Hermitian quotient

The source's original border matrix is

\[
B=[F,E],\qquad
\mathsf J=\begin{pmatrix}0&\Omega^{-1}\\\Omega^{-1}&0\end{pmatrix},
\qquad A_{\rm bord}=\mathsf J B^*GB.
\]

Let

\[
D_\Omega=\operatorname{diag}(\Omega^{1/2},\Omega^{1/2}),
\qquad K=T^*T=D_\Omega^{-1}B^*GBD_\Omega^{-1}.
\]

Then \(\mathsf J=D_\Omega^{-1}J_0D_\Omega^{-1}\), and direct substitution proves the exact similarity

\[
D_\Omega A_{\rm bord}D_\Omega^{-1}=J_0K=:A_0.
\]

Keep the complete original coordinate space \(\mathscr X=\mathbb C^{2r}\), its subspaces

\[
N=\ker K=\ker T,\qquad \mathscr R=\operatorname{ran}K=N^\perp,
\]

and its positive square root P=K^{1/2}. The equality of the two kernels follows from x*Kx=||Tx||². The spectral theorem gives ranP=ranK and kerP=N. Define

\[
H_0=PJ_0P:\mathscr X\to\mathscr X.
\]

This operator is Hermitian, kills N, and has range in R. The exact intertwining equation is

\[
PA_0=PJ_0K=H_0P.
\]

It proves the short exact sequence of represented vector spaces

\[
0\longrightarrow(N,0)\longrightarrow(\mathscr X,A_0)
\xrightarrow{P}(\mathscr R,H_0|_{\mathscr R})\longrightarrow0.
\]

The last arrow has quotient inverse induced by \((K|_{\mathscr R})^{-1/2}:\mathscr R\to\mathscr X\). This is the full morphism relating the displayed non-Hermitian matrix to the Hermitian quotient. It retains the zero-action subspace N rather than deleting it.

The exact polar map is

\[
Q|_{\mathscr R}=T(K|_{\mathscr R})^{-1/2},\qquad Q|_N=0.
\]

For x,y in R its inner products satisfy

\[
\langle Qx,Qy\rangle=x^*(K|_{\mathscr R})^{-1/2}K(K|_{\mathscr R})^{-1/2}y=x^*y.
\]

It is onto ranT because T=QP and P is onto R. Hence Q is an isometry R→ranT and, extended by zero, is a partial isometry with Q*Q the orthogonal projection onto R and QQ* the orthogonal projection onto ranT. Direct substitution gives

\[
\widetilde W=QH_0Q^*.
\]

Thus \(QH_0|_{\mathscr R}=(\widetilde W|_{\operatorname{ran}T})Q\). The complete arithmetic coordinate space also retains the orthogonal direct summand kerT*, on which the actual relative weight is zero:

\[
(\mathbb C^n,\widetilde W)
\cong(\mathscr R,H_0|_{\mathscr R})\oplus(\ker T^*,0).
\]

In the original border coordinates the quotient arrow is \(PD_\Omega\), its kernel is \(D_\Omega^{-1}N\), and the arithmetic arrow is

\[
QPD_\Omega=G^{1/2}B.
\]

These equations retain the original Omega factors and explicitly identify the kernel of the source border comparison.

For nonzero eigenvalues the quotient has no omitted Jordan data. If H_0z=mu z with z in R and mu≠0, define

\[
\ell_\mu(z)=\mu^{-1}J_0Pz.
\]

Then \(P\ell_\mu(z)=z\) and \(A_0\ell_\mu(z)=\mu\ell_\mu(z)\). Conversely any nonzero generalized eigenvector projects to the corresponding H_0 generalized eigenspace and the projection is injective on that generalized eigenspace, because its kernel N has only eigenvalue zero. H_0 is Hermitian, so each such generalized eigenspace is an eigenspace. All nonzero eigenvalues of the source border matrix are therefore real and semisimple, with precisely the multiplicities supplied by the arithmetic Hermitian weight.

## 4. Entire generalized zero fibre, including the extension map

Put

\[
Z_0=\ker(H_0|_{\mathscr R}),\qquad q=\dim Z_0.
\]

The generalized zero eigenspace of A_0 is exactly

\[
\mathscr E_0=P^{-1}(Z_0).
\]

Proof in both directions: if Px lies in Z_0, then PA_0x=H_0Px=0, so A_0x lies in N and A_0²x=0. Conversely, if A_0^j x=0 for some j≥1, the intertwining gives H_0^j Px=0. The restriction H_0|R is Hermitian, so its generalized zero space equals its kernel. Thus Px lies in Z_0. This proves the claim and, without any nonsingularity assumption, shows that the nilpotent index of the zero fibre is at most two.

The exact zero-fibre sequence is

\[
0\longrightarrow N\longrightarrow\mathscr E_0\xrightarrow{P}Z_0\longrightarrow0.
\]

Define an explicit lift and extension map

\[
L_0z=(K|_{\mathscr R})^{-1/2}z,\qquad
N_0z=J_0Pz,\qquad z\in Z_0.
\]

These satisfy

\[
PL_0z=z,\quad A_0L_0z=N_0z,\quad PN_0z=H_0z=0,
\quad A_0N_0z=0.
\]

Moreover N_0:Z_0→N is injective: if J_0Pz=0, invertibility of J_0 gives Pz=0, and z in R forces z=0. It follows that q≤dimN. In the fully specified vector-space coordinates

\[
N\oplus Z_0\longrightarrow\mathscr E_0,
\quad(n,z)\longmapsto n+L_0z,
\]

whose inverse is x↦(x−L_0Px,Px), the operator is exactly

\[
(n,z)\longmapsto(N_0z,0).
\]

Consequently a basis z_1,…,z_q of Z_0 gives q original length-two chains

\[
L_0z_j\ \xmapsto{A_0}\ N_0z_j\ \xmapsto{A_0}\ 0.
\]

Extend the independent vectors N_0z_j to a basis of N; each additional basis vector is a length-one zero chain. The precise Jordan count is therefore q blocks of size two and dimN−q blocks of size one. If N=0 the entire zero fibre is absent. If q=0 and N≠0, the zero fibre is semisimple. In original border coordinates every displayed vector is transported by D_Omega^{-1}; no original coordinate fibre is discarded.

The arithmetic zero fibre has dimension q+n−rankK. The border generalized zero fibre has dimension dimN+q. Their different dimensions and the border's possible nontrivial nilpotent chains are related by the explicit maps above; equality of nonzero spectra alone would omit these data.

## 5. Positive Gamma and the accumulated arithmetic volume estimate

The actual arithmetic measure has omega_j>0 for every j. The source measure is |g/h|²dy/(2pi); it has positive density except on a discrete zero set, and a nonzero polynomial cannot vanish almost everywhere for that measure. Every monic orthogonal polynomial therefore has a strictly positive squared norm. Thus a_0=0 and a_j=omega_j/omega_{j−1}>0 for j≥1.

For k≥1 and any alpha with |alpha|=M,

\[
\sum_{j=1}^k\bigl(a_{\alpha_j+1}+(k-1)a_{\alpha_j}\bigr)>0,
\]

because each of the k terms a_{alpha_j+1} is strictly positive and the remaining terms are nonnegative. The finite maximum Gamma_{k,M} is therefore finite and strictly positive, including M=0 and d=1 whenever those endpoints are permitted by the source. Division by Gamma in the following bound is legitimate.

Define the original half-line departure explicitly as

\[
\delta_\rho=\operatorname{Re}\rho-\tfrac12,
\qquad \Delta=\max_{\rho\in Z}|\delta_\rho|.
\]

For any actual eigenvector Av=rho v, the source retained tensor vector v^{tensor k} has the exact Rayleigh quotient 2k delta_rho. This remains a nonzero tensor eigenvector even in a full-order nonsquarefree packet. The definition of the two-sided relative excess gives

\[
2k\Delta\le\epsilon_{k,M}\le2\sqrt{\Gamma_{k,M}\lambda_{k,M}}.
\]

It follows that

\[
\boxed{\lambda_{k,M}\ge\frac{k^2\Delta^2}{\Gamma_{k,M}}.}
\]

The definition of delta is essential: if delta instead denotes 2Re(rho)−1, the numerator is k²max|delta|²/4. No factor of two may be dropped between those conventions.

Let integers a<b satisfy a≥k(d−1), and retain the same packet and tensor degree at every step. Telescoping the already-proved determinant formula gives

\[
\begin{aligned}
\log\frac{\det G_{k,a}}{\det G_{k,b}}
&=\sum_{M=a}^{b-1}\log\det(I+U_MU_M^*)\\
&\ge\sum_{M=a}^{b-1}\log(1+\lambda_{k,M})\\
&\ge\sum_{M=a}^{b-1}\log\left(1+\frac{k^2\Delta^2}{\Gamma_{k,M}}\right).
\end{aligned}
\]

All logarithms have positive real arguments. The first inequality follows by taking the product of 1 plus every nonnegative eigenvalue of U_MU_M*: that product is at least 1 plus its largest eigenvalue. The determinant is an additional observable of the unchanged full Gram update.

The energy inequality of §2 also implies

\[
k^2\Delta^2\le\frac{\lambda_{k,M}}{1+\lambda_{k,M}}\chi_{k,M}.
\]

When Delta>0, this forces chi_{k,M}>k²Delta² because lambda/(1+lambda)<1, and hence gives the exact further bounds

\[
\lambda_{k,M}\ge\frac{k^2\Delta^2}{\chi_{k,M}-k^2\Delta^2},
\qquad
\log\det(I+U_MU_M^*)
\ge-\log\left(1-\frac{k^2\Delta^2}{\chi_{k,M}}\right).
\]

This is a deduction from the actual defect energy, not an assumption that the missing arithmetic asymptotics hold.

## 6. Review verdict and evidence scope

All proposed identities in the assigned bridge are proved above with their exact domains, coordinate maps, kernels, and zero generalized eigenspaces. No mathematical correction to the parent's proposed bridge is required. The departure convention must be declared explicitly before the lower estimate, and the full zero-fibre statement must retain the positive-rank quotient R rather than including the already-known kernel N a second time in q.

The complete new parent fragment `tex/frontier_energy_dissipation.tex`, FE.1–FE.23, was also read and checked at SHA256 `573E0432A71F949A9D485CAAFD611708CEEE6FBAEE84CD82EB833F6ED39F85DE`. Its written arguments agree with this independent derivation. Two explicit-domain repairs were requested: state a≥k(d−1) before FE.23; and define the FE.17 inverse L=(K^(1/2)|R)^(-1) on all R before restricting it to Z_0, because the later nonzero-eigenvalue proof also uses L. The nonzero eigenvector lift x+n/lambda has the correct positive sign. The source rank identities and all empty-rank/zero-departure cases verify.

For any original fixed support label lambda, every displayed linear map has the exact supported lift (lambda,x)↦(lambda,Tx), and external absence maps to external absence. In particular the original two-step zero chain is (lambda,Lz)↦(lambda,N_0z)↦(lambda,0). Its final value is the supported zero at lambda; it is not external absence. Thus the entire singular extension has a retained support-valued morphism, as do the quotient and coordinate similarities above.

Both requested domain repairs and the supported zero chain were verified in the FE.1–FE.23 revision at SHA256 `E956920ED36BA4FE37624ECFFEDCFCDE1D4E0F9DC5E4A7B1D077BA2C0EAE86B5`.

Final current proof review: `tex/frontier_energy_dissipation.tex`, FE.1–FE.25, SHA256 `856A8648F00ED023D52C5437F0B2085164BB943001E309FFE9C067230BE89A0A`. The final appended FE.24–FE.25 argument was read in its entirety against the independently derived energy estimate in §§2 and 5 above. FE.24 follows from the original signed cross-pairing, the exact operator norm squared lambda/(1+lambda) of the relative loss map, and the Hilbert–Schmidt upper bound chi for the relative derivative map. For delta_*>0 the eigenline forces chi>k²delta_*²; rearrangement therefore proves the middle FE.25 inequality with positive denominator, and the determinant bound proves its logarithmic inequality with strictly positive logarithm argument. The stated accumulated interval k(d−1)≤a<b is admissible. For delta_*=0 the proof retains undivided FE.24 and assigns no value to a possible 0/0 expression. This final FE.1–FE.25 fragment is approved at the written-proof scope above. The unchanged 102-check suites need no rerun for this analytically proved extension.

The child task `singular_frontier_fixture` supplied a complete independent proof and persisted exact fixtures. I read its entire checker and proof note and inspected both positive receipts and the six recorded negative-control errors. There are 102 exact records in each positive run (normal and `-O`), covering six Jordan fixtures and four direct geometric realizations of the actual relation maps. All records pass. Three deliberate errors are each rejected normally and under `-O`: a false nilpotent-square identity, replacing the actual size-two zero chain by two size-one chains, and omitting the mixed term from chi. The last error gives the false value 265/36 against the actual 10219/648. Final checker SHA256: `18BEDD42FAF6F76A38DB2F6A65E44D3A6B377D29E0123DEDFF0092F38C46D52D`.

These finite examples supplement the proofs and do not prove the infinite arithmetic source or any RH estimate. The standalone package contains the checker in `scripts/check_frontier_singular_fixtures_20260912.py`, positive and negative receipts in `checks/`, and both proof review notes in `logbook/`.
