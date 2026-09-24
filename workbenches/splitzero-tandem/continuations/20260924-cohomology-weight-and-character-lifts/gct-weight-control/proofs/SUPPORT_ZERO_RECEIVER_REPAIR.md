# Retaining support at every zero coefficient

24 September 2026. ZR1-ZR5. This corrects the support-retention wording of M9.7 and S7 while retaining their linear isomorphisms and synthesis theorem. The correction was supplied by the receiving task in ITEM26_GLOBAL_RECEIVERS_INTEGRATION.md, I26.10; its complete argument is reproduced and propagated here. The record set below is the programme's existing set of labels, not an arithmetic value assigned to an unsupported element.

## ZR1. Exact domain of the linear statement

Let \(\mathcal Q=\mathcal B/\mathcal I\) be the actual original-zeta quotient, and let \(J:\mathcal Q\to\prod_\rho\mathbb C^{m_\rho}\) be the injective map of all zero jets proved in S7. Let \(\mathcal L\) be the retained set of support records. Write \(e_\ell\) for the basis of the free vector space \(\mathbb C^{(\mathcal L)}\). The linear comparison
\[
J\otimes\mathrm{id}:\mathcal Q\otimes\mathbb C^{(\mathcal L)}
\longrightarrow (\prod_\rho\mathbb C^{m_\rho})\otimes\mathbb C^{(\mathcal L)}
\tag{ZR1.1}
\]
is injective: every tensor has a finite expansion \(\sum q_\ell\otimes e_\ell\), and the coordinate functional at each \(e_\ell\) makes a zero image imply \(Jq_\ell=0\), hence \(q_\ell=0\). This proves precisely the linear assertion. However,
\[
0_{\mathcal Q}\otimes e_\ell=0_{\mathcal Q}\otimes e_{\ell'}=0
\tag{ZR1.2}
\]
for every pair of records. The passage from a labelled coefficient to a tensor has already identified its zero sections. Injectivity of ZR1.1 does not undo that earlier map.

## ZR2. Exact record-retaining quotient and observation

Retain the disjoint family
\[
\widehat{\mathcal Q}=\coprod_{\ell\in\mathcal L}\{\ell\}\times\mathcal Q.
\tag{ZR2.1}
\]
It is equivalently the quotient of \(\mathcal L\times\mathcal B\) by
\((\ell,f)\sim(\ell',g)\) exactly when \(\ell=\ell'\) and \(f-g\in\mathcal I\). This is an equivalence relation since \(\mathcal I\) is a vector subspace. The map to ZR2.1 is \((\ell,f)\mapsto(\ell,[f])\); its fibres are exactly that relation, proving the comparison. All subtractions occur in the coefficient functions. No addition is defined on \(\mathcal L\).

The complete observation is
\[
\widehat J(\ell,q)=(\ell,Jq).
\tag{ZR2.2}
\]
If its two values agree, their first coordinates give equal records and its second coordinates give equal coefficient classes by injectivity of \(J\). Thus \(\widehat J\) is injective. The fibre of the coefficient-only zero observation is exactly
\[
\coprod_{\ell\in\mathcal L}\{(\ell,0_{\mathcal Q})\}.
\tag{ZR2.3}
\]
It contains every original record, including those that must distinguish absence from a supported zero.

## ZR3. The map to the previous tensors, with its full fibres

Define
\[
c:\widehat{\mathcal Q}\longrightarrow
\mathcal Q\otimes\mathbb C^{(\mathcal L)},\qquad
c(\ell,q)=q\otimes e_\ell.
\tag{ZR3.1}
\]
Its zero fibre is exactly ZR2.3, because the coordinate functional at \(\ell\) recovers \(q\). If its common output is nonzero, equality of two images with different labels is impossible: the coordinate functional at the first label would give \(q=0\). Equality with the same label gives equal coefficients. Thus every nonzero fibre in its image is a singleton; tensors with several nonzero label coordinates are outside its image. This states every fibre without asserting that the map is surjective. The square with \(\widehat J\), \(c\), and \(J\otimes\mathrm{id}\) commutes by evaluation on \((\ell,q)\).

## ZR4. Arithmetic action, projectors, and the full pairing

Every existing coefficient operator \(A:\mathcal Q\to\mathcal Q\) lifts as
\[
\widehat A(\ell,q)=(\ell,Aq).
\tag{ZR4.1}
\]
It satisfies \(\widehat A\widehat B=\widehat{AB}\), \(\widehat{\mathrm{id}}=\mathrm{id}\), and \(c\widehat A=(A\otimes\mathrm{id})c\) by direct substitution. This applies to all actual prime operators, every IAR coefficient operator, and every zero projector. Addition of operators remains fibrewise addition on \(\mathcal Q\); it is not an operation on the primitive records. An operator sending a coefficient to zero sends \((\ell,q)\) to \((\ell,0)\), retaining its record.

The full Weil pairing has the record-preserving receiver
\[
((\ell,x),(\ell',y))\longmapsto(\ell,\ell',W(x,y)).
\tag{ZR4.2}
\]
Projection to the last coordinate is exactly the previous form, with all its endpoint, Gamma, prime and original-zero contributions unchanged. Its weighted-adjoint identity is therefore the same equality of last coordinates with the same two retained labels. A vanishing form value deletes neither input record. No sign or positivity is inferred from this recording map.

## ZR5. The two coefficient sections at zero

The formal coefficient algebra \(C_{\rm rec}\) of M9.7 has independent basis elements \(U=[\tau]\) and \(f=[1]\). Its two linear sections \(q\mapsto q\otimes U\) and \(q\mapsto q\otimes f\) are distinct maps, but both take zero to zero. Their linear difference is injective, as M9.7 proves; that still does not distinguish which zero section was selected.

To retain that already specified selection, use the record set \(\mathcal L\times\{U,f\}\) and apply ZR2. The maps from the two selected families to the previous coefficient receiver are exactly
\[
(\ell,U,q)\longmapsto q\otimes U\otimes e_\ell,
\qquad
(\ell,f,q)\longmapsto q\otimes f\otimes e_\ell.
\tag{ZR5.1}
\]
For nonzero coefficients their images are distinct by the independent basis coordinates. At zero the original records remain distinct in the domain and their comparison images coincide. This proves both the retained distinction and the specific loss under linear observation. It assigns no source sum, difference, parity or numerical value to \(\tau\).
