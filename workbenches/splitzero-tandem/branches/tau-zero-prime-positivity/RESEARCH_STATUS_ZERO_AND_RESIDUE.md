# Supported-zero identities, heat automorphisms, and residue observations

23 September 2026. This dated research note records the calculated maps and their current mathematical scope. It accompanies the complete proofs.

## The original zero identity and its exact maps

The original supported-zero algebra is
\[
A=\{\tau,e\},\qquad 1_A=e,\qquad e^{-1}=e.
\]
This inverse exists without localization. The complete maps on semimodules, including both adjunctions and every local zero, are proved in [ZH1–ZH8](SUPPORTED_ZERO_HEAT_IDENTITY_DERIVATION.md). The ambient identity remains \(1_{G(R)}=1_R^\bullet\); the inclusion and retraction are specified, rather than identifying these two units.

ZH9–ZH21 constructs a function space on which the actual heat evolution has an inverse for every real time, lifts it to the original split-zero semimodule, and proves the exact evaluation criterion
\[
G(\operatorname{ev}_z)(H_t^\bullet)=e\quad\Longleftrightarrow\quad H_t(z)=0.
\]
The identity action on the zero semilattice occurs both at a known time with nonreal zeros and at a known time with all zeros real. [HZ17–HZ24](supporting_proofs/TAU_HEAT_ZERO_LOCALIZATION_DERIVATION.md) proves local persistence of nonreal zeros and gives the exact heat specialization maps. The literature used is Brad Rodgers and Terence Tao, arXiv:1801.05914v5, and Dave Platt and Tim Trudgian, arXiv:2004.09765v1, at the original-TeX locators in the source account.

## The surviving infinitesimal and its changed observation

The original collision residue is
\[
D(T)=-T^3/16\quad\text{on }\mathbb C[T]/(T^4).
\]
It is nonzero. Its regular trace vanishes. [RD1–RD20](COLLISION_RESIDUE_DUALITY_DERIVATION.md) proves how it survives in perfect residue duality and where the Jacobian kills its trace:
\[
Q_{\rm tr}(f,g)=Q_{\rm res}(f,-4iT^3g).
\]
The residue form has inertia \((2,2,0)\), and its change under the generated automorphism is an explicitly computed form with both signs. No positive arithmetic form is obtained by declaring this different pairing positive.

On the actual programme packet, all original amplitude jets and the Weil involution give the exact identity
\[
B_h(f,g)=Q_h(Uf,-ih'Ug),\qquad
\operatorname{rad}B_h=H^{-1}(L_{E_h/\mathbb C}).
\]
RD28a proves a perfect pairing between that cotangent kernel and its cotangent cokernel. This supplies a further nonzero observation of the retained infinitesimal data. RD29–RD31b uses the complete supported-zero Weil identity to compute the exact endpoint compensation. Its positive endpoint witness changes no divisor-trace value.

## Current arithmetic scope

These results leave a definite arithmetic question: the sign of the actual Weil form on its retained value quotient. The new observations and exact maps are retained for continued investigation; the sign on that entire quotient remains undetermined.
