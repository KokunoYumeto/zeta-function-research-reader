# Two heat observations of the original theta quotient

The Split-Zero programme starts with the theta source whose Mellin transform is \(2\xi/h\), where \(h\) retains the complete orders of the selected zeros. Polynomial observations of that source give a cyclic quotient with its own least-norm metric \(G\). The existing correction \(Q\) connects the attained selfadjoint compression \(A\) to the original quotient multiplication operator through \(T(t)=A-tQ\).

This edition calculates actual heat functions of that same operator. It retains both the holomorphic trace \(\operatorname{tr}e^{-sT^2}\) and the singular-value trace \(\operatorname{tr}e^{-sT^{\dagger_G}T}\). Their small-time difference recovers the existing arithmetic allowance \(t^2\epsilon^2\), with proved finite error bounds. A selfadjoint dilation recovers \(T\) and exactly doubles the second trace; it does not identify the two observations.

[Read the complete proofs](COMPLETE_PROOFS.tex), [the mathematical figure and caption](FIGURE_CAPTION.md), or [the machine-readable result/use index](RESULT_INDEX.json). Individual proofs: [NH1–36](NATIVE_HEAT_ACTION.tex), [HM1–19](HEAT_METRIC_COMPARISON.tex), [DS1–12](HEAT_DYSON_STOPPING.tex). Three complete cumulative LaTeX successors are retained under [cumulative](cumulative), with an [exact insertion record](CUMULATIVE_INSERTION.json).

Human sources: Alain Connes, [*Heat Expansion and Zeta*](https://arxiv.org/abs/2402.13082v1), and Alain Connes and Walter D. van Suijlekom, [*Quadratic Forms, Real Zeros and Echoes of the Spectral Action*](https://arxiv.org/abs/2511.23257v1). Their original LaTeX was read directly; citations occur at the point of use. [Source-use details](HUMAN_SOURCE_USE.json) distinguish those papers from local independent derivations and the incoming stopping-rule calculation.

The [independent full proof](INDEPENDENT_HEAT_CURVATURE.tex), ID1–8, also calculates the exact curvature at outgoing parameter zero. Its divided-difference weights prove the sharp uniform boundary at heat time times the squared compression norm equal to one. The separate [labelled sign-change example](FIGURE_CAPTION.md) keeps its original metric and all constants; it is not arithmetic zero data.

Exact checks and deliberate-failure controls pass in normal and optimized Python. [Validation](VALIDATION.md) states their scope. No uniform decay of the original arithmetic allowance or RH conclusion is proved by these finite formulas.
