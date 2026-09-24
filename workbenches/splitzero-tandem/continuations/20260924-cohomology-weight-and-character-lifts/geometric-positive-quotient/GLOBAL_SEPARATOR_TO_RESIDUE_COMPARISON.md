# The full source separator and the original residue receiver

24 September 2026. Complete receiving proof, GSR0–GSR4. This calculation applies the full-module separation just constructed in GMS to the actual pairing and transfer in RTT and GTAH. Every coefficient operation occurs after complete-history arithmetic reconstruction. No addition, numerical coordinate, or parity is assigned to the supporting datum \(\tau\).

## GSR0. Actual source and the comparison being tested

The receiving source is `../tau_weight_cohomology_20260924/CC_GLOBAL_MULTIPLIER_SEPARATION.md`, GMS0–GMS11, read completely at SHA256 `3164c3ae00fbfbaf17bce809d48b7d0e56ff8a4c0991fdb374a4b11dd18bec59`. Its underlying separator is the already proved GSL corridor construction. Here \(M\) is its entire multiplier algebra, \(\mathcal B\) is the entire rapid-strip space, \(\mathcal I\) is the full original nontrivial-zero jet ideal, and \(\mathcal I_+\) is the full translated ideal. Put
\[
\mathcal Q=\mathcal B/\mathcal I,\qquad
\mathcal Q_+=\mathcal B/\mathcal I_+,\qquad
q:\mathcal B\longrightarrow\mathcal Q.
\tag{GSR0.1}
\]
The actual global multiplier \(c=E_+\in M\) satisfies, with every original multiplicity,
\[
c\mathcal B\subset\mathcal I_+,\qquad
(1-c)\mathcal B\subset\mathcal I,\qquad
c_{\mathcal Q}=1,\qquad c_{\mathcal Q_+}=0.
\tag{GSR0.2}
\]
These are GMS3.5–GMS3.6. They hold on the complete modules, not only on finite jets. The map \(\beta:\mathcal B\to\mathcal I_+\) is \(F\mapsto cF\). GMS5 constructs its chain-homotopy inverse property after derived Hom from \(\mathcal Q\); GMS6 retains the nonzero normal extension. We now calculate the effect of this particular map on the complete original Weil pairing and its residue receiver.

## GSR1. The exact multiplier involution in the residue pairing

For \(h\in M\), define the multiplier
\[
h^\#(s)=\overline{h(1-\overline s)}.
\tag{GSR1.1}
\]
This is an entire function: conjugating a Taylor expansion of \(h\) at \(1-\overline{s_0}\) gives its Taylor expansion at \(s_0\), with coefficient \((-1)^j\overline{h^{(j)}(1-\overline{s_0})}/j!\). Its polynomial bound on a strip of width \(A\) follows from that of \(h\) on width \(A+1\). Thus \(h^\#\in M\). Direct substitution proves \((h^\#)^\#=h\), \((hk)^\#=h^\#k^\#\), and \((\alpha h)^\#=\overline\alpha h^\#\). These are statements about reconstructed coefficient functions.

Let \(\rho^\#=1-\overline\rho\). The exact functional equation of the original zeta function gives this involution on its nontrivial-zero divisor, preserving multiplicities. RTT9 retains its complete multiplier and exceptional terms. For \(F,G\in\mathcal Q\), retain
\[
W(F,G)=\sum_{\rho}m_\rho F(\rho)\overline{G(\rho^\#)}.
\tag{GSR1.2}
\]
Each fixed multiplier has polynomial growth on the zero strip, while representatives of \(F,G\) have arbitrary rapid strip decay. The zero-count bound used in RTT1 therefore proves absolute convergence after multiplication by \(h\) or \(h^\#\). Since \(\overline{h^\#(\rho^\#)}=h(\rho)\), termwise substitution proves
\[
W(m_hF,G)=W(F,m_{h^\#}G).
\tag{GSR1.3}
\]
Let \(\mathsf S:\mathcal Q\to\mathcal H_{\rm res}\) and \(\widehat\iota:\mathcal H_{\rm res}\to\mathcal Q'_\beta\) be the actual RTT5 and GTR10 maps. Equation (GSR1.3), with \(h\) replaced by \(h^\#\), gives the complete typed covariance
\[
\widehat\iota\mathsf S m_h
=m_{h^\#}'\widehat\iota\mathsf S.
\tag{GSR1.4}
\]
Indeed both sides evaluated at \(G\) and then at \(F\) are \(W(F,m_hG)\). The transpose is strong-continuous because the continuous multiplier sends bounded subsets of \(\mathcal Q\) to bounded subsets. For \(h(s)=a^s\), its reflected multiplier is exactly \(a^{1-s}\), so (GSR1.4) recovers the full degree-weighted transfer \(a(T_{1/a})'\). No degree factor is removed.

## GSR2. Every full jet survives the separator on the original quotient

At each original zero \(\rho\), the germ \(c-1\) vanishes to order \(m_\rho\). Applying the Taylor formula from GSR1 at \(\rho^\#\), and using \(m_{\rho^\#}=m_\rho\), proves that \(c^\#-1\) has the same vanishing order at \(\rho\). The full Leibniz formula then gives
\[
m_c=1_{\mathcal Q},\qquad m_{c^\#}=1_{\mathcal Q},
\qquad
\mathsf S m_c=\mathsf S,
\qquad m_{c^\#}'=1_{\mathcal Q'_\beta}.
\tag{GSR2.1}
\]
This includes every higher jet in \(\mathcal Q\). It is stronger than merely saying that \(c(\rho)=1\). In particular the exact residue identity is
\[
\widehat{\mathcal R}(F,\mathsf S(cG))
=\widehat{\mathcal R}(F,\mathsf SG)
=W(F,G).
\tag{GSR2.2}
\]
On the value Hilbert space \(H\), the multiplier induced by \(c\) is the identity as well. With GTAH's actual positive-adjoint defect \(\mathsf D_a=T_a^*-aT_{1/a}\), we therefore obtain
\[
m_c\mathsf D_a^*\mathsf D_a
=\mathsf D_a^*\mathsf D_a m_c
=\mathsf D_a^*\mathsf D_a.
\tag{GSR2.3}
\]
The injective anti-linear receiver \(\mathsf A:H\to\mathcal H_{\rm res}\) from RTT6.2 retains this entire operator by GTAH6.7. Thus the full separator has an exact compatible action on the residue pairing, but that action does not change its value or its positive-adjoint defect. This is a calculation of the proposed use of \(c\), not a conclusion about other maps supplied by the full source geometry.

## GSR3. The representative lift and its complete kernel

The actual inclusion \(\mathcal I_+\hookrightarrow\mathcal B\) followed by \(q\) gives a continuous surjection
\[
q_{\mathrm{res}}:\mathcal I_+\longrightarrow\mathcal Q,\qquad F\longmapsto[F]_{\mathcal I}.
\tag{GSR3.1}
\]
This map restricts the original quotient map to the full translated ideal. To prove surjectivity, take any representative \(F\in\mathcal B\). Then \(cF\in\mathcal I_+\) and \(q(cF)=q(F)\) by (GSR0.2). Its kernel is exactly \(\mathcal I\cap\mathcal I_+\). Consequently
\[
0\longrightarrow\mathcal I\cap\mathcal I_+
\longrightarrow\mathcal I_+
\xrightarrow{\ q_{\mathrm{res}}\ }\mathcal Q\longrightarrow0,
\qquad q_{\mathrm{res}}\beta=q
\tag{GSR3.2}
\]
is a strict exact sequence of Fréchet spaces and continuous \(M\)-maps. The ideals are closed; the open mapping theorem applies to the displayed continuous surjection between Fréchet spaces. This proves strictness, retaining its entire kernel.

There is no \(M\)-linear section of this displayed surjection. Fix an actual original zero \(\rho\) and use the original entire source factor
\[
F_0(s)=\frac{s(s-1)}8\pi^{-s/2}\Gamma(s/2)\zeta(s),
\qquad v_\rho(s)=\frac{F_0(s)}{s-\rho}\in\mathcal B.
\tag{GSR3.3}
\]
The original quotient class \([v_\rho]\) is nonzero because its vanishing order at \(\rho\) is exactly \(m_\rho-1\), whereas \((s-\rho)[v_\rho]=[F_0]=0\). An \(M\)-linear section would send this nonzero class to an entire function killed by \(s-\rho\). That function must vanish on \(\mathbb C\setminus\{\rho\}\) and hence everywhere, a contradiction. The existence of an actual nontrivial zeta zero here is the established original-zeta fact already used in CW8 and GMS6; no off-line zero is presumed.

This identifies the precise kind of lift already constructed: \(\beta\) lifts representatives from \(\mathcal B\), and its derived comparison is GMS5. It does not supply a section from \(\mathcal Q\). The dual restriction has the injective continuous map
\[
q_{\mathrm{res}}' :\mathcal Q'_\beta\longrightarrow(\mathcal I_+)'_\beta,
\quad \lambda\longmapsto\lambda\circ q_{\mathrm{res}},
\qquad
\beta' q_{\mathrm{res}}'=q'.
\tag{GSR3.4}
\]
Injectivity follows from surjectivity of \(q_{\mathrm{res}}\); continuity follows from bounded-set preservation. The last identity is the transpose of (GSR3.2). In particular it applies to \(\lambda=\widehat\iota\mathsf SG\), giving an exact comparison of the original trace through the full normal source. No assertion about an inverse for the strong subspace topology is needed.

## GSR4. What this test supplies for the next attempt

GMS's full-module separation now has its exact receiving map to the original-zeta residue trace: (GSR1.4), (GSR2.2), and (GSR3.4). The local and global source factors, all multiplicities, all nilpotent coordinates, and the entire normal kernel remain. The derived lifting construction and the positive-adjoint calculation concern these actual connected objects.

For the requested positivity step, this test rules out treating the separator's action itself as a sign-changing or defect-annihilating operation on \(\mathcal Q\): that action is exactly the identity. What would advance the argument is a source-derived adjoint identity for the actual transfer, rather than its central multiplier action. The concrete target is GTAH's \(T_a^*=aT_{1/a}\) on the established value completion, with its actual maps back to the full source and residue dual. Its first attempted construction, reflection averaging, has already been calculated in GTAH2–GTAH3 and has the retained positive degree defect; its second attempted source correction, the full separator, is calculated here. Further work must use additional source structure and these measured defects, without declaring the target identity or positivity as an assumption.

Human-source context remains Connes–Consani's actual source sheaf, [arXiv:0903.2024v3, §5](https://arxiv.org/abs/0903.2024v3), and Deligne's weight-controlled lifting argument, [Weil II, §3.6](https://numdam.org/item/PMIHES_1980__52__137_0/). This note does not claim a new reading of either entire paper or an established purity theorem.
