# Native arithmetic metric bounds and the full conductor receiver

The Split-Zero programme keeps the theta source, its arithmetic convolution measure, its original polynomial relations and the finite observations of the resulting quotient. This edition calculates how the even and odd parts of that source relate to two explicit Pollaczek weights, then uses the relation to bound the original observation metric. It also includes the exact receiver of the eight signed ES–Fable states into that metric.

[Complete literature and observation proofs in LaTeX](LITERATURE_RECEIVERS_COMPLETE.tex) · [Machine-readable results and programme uses](RESULT_INDEX.json) · [Point-of-use citation map](CITATION_USE_MAP.json).

## The new calculations

- **Original parity and source bounds — SZ-20260920-019.** The full change of variable, density multipliers, quotient algebra, Taylor unit and complex polynomial phases are calculated. The paper's Stieltjes ratio yields positive finite resolvent sums that bound the actual arithmetic Gram and its original quotient metric. Both the multiple-orthogonality residual and the exact native Christoffel relation are proved. [Complete proof](PARITY_POLLACZEK_NATIVE_RECEIVER.tex). Human input: [Aptekarev, López Lagomasino and Martínez-Finkelshtein, arXiv:1410.1261v1](https://arxiv.org/abs/1410.1261v1), read in original author LaTeX; its asymptotics are not simply transferred to a different weight.
- **Growing-degree and conductor return — same result, TR1–10.** The earlier programme's total-degree convolution bound strengthens the truncation estimate. At the original degree windows, at most `O_h(q³/t)` resolvent terms suffice for an absolute four-endpoint log-determinant error at most `t`. The complete calculation also bounds the full conductor metric and the energy of its pair-flip mixing defect. [Full derivation](NATIVE_TRUNCATION_CONDUCTOR_RETURN.tex). This bounds truncation length, not the cost of certifying the native integrals; the constants and full source maps are retained.
- **Eight signed states in the original observation — SZ-20260920-016.** The full original conductor minimum, its exact positive correction to the restricted four-plane minimum, all eight state coordinates and the complete monodromy mixing defect are evaluated as original matrices. The terminal-class residual is retained. [Complete proof](original_minimum/EIGHT_STATE_ORIGINAL_MINIMUM.tex) · [Independent full derivation](original_minimum/independent/EIGHT_STATE_QUOTIENT_REDERIVATION.tex).
- **Connections, factor completion and original arithmetic action — SZ-20260920-020/021.** The owning task's entire accepted cumulative conductor proof is included, with the rational signed-frame connection, complete boundary charts, selected-root singular constants and corner-cardinal action lift. [Complete cumulative conductor paper](FABLE_TO_ORIGINAL_CONDUCTOR.tex). Its separate source package retains the original received derivation, all independent proofs and exact check scripts. The human and received-source contributions are distinguished in the paper.

The complete earlier Gamma-kernel, theta-closure and Jacobi-commutant proofs remain included. No result here evaluates the remaining native complex projected-current asymptotic or proves or disproves RH. A polynomial source trajectory escaping at complex time is not claimed to be real-time fluid blowup.

## Complete cumulative sources

These are the full preceding manuscripts with every new proof body and the complete conductor paper appended. No earlier equations, citations or source credits are removed. The insertion manifest verifies exact recovery of each predecessor. A fresh rendering of these large cumulative sources is not claimed.

- [Joint note](cumulative/09_UPDATED_JOINT_NOTE.tex)
- [Signed return](cumulative/10_UPDATED_SIGNED_RETURN.tex)
- [Kernel and multiplicity proofs](cumulative/14_CURRENT_KERNEL_AND_MULTIPLICITY_PROOFS.tex)

## Checks and scope

The complete analytic proofs are the authority. `check_parity_symbolic.py` checks the original coordinate, recurrence and quotient identities. `check_native_truncation_return.py` checks exact finite positive resolvent matrices, complex observations, successive quotients and two deliberately wrong alternatives; it passes with ordinary and optimized Python. These checks are not numerical evaluations of hypothetical zeta zeros. The original-minimum task's separate exact diagnostics and source pins are preserved.

All new proofs have point-of-use citations and full bibliographies. The citation map explicitly limits its audit to this edition's new calculations; it does not claim that every historical manuscript has completed provenance repair. These are additive GitHub sources. No Zenodo, Overleaf, timer or UI update is implied.
