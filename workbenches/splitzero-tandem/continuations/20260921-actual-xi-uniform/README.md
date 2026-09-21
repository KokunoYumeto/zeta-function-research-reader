# Actual Xi data and the two conductor inverse rates

Result SZ-20260921-011. Read **ACTUAL_XI_UNIFORM_CONDUCTOR.pdf**, the complete 28-page continuation with two figures, exact proofs and source citations. The cumulative source is FABLE_TO_ORIGINAL_CONDUCTOR.tex; it retains the preceding constructions and proofs.

The originating Jacobian counterexample was announced by **Levent Alpöge**, whose [original announcement](https://x.com/__alpoge__/status/2079028340955197566) credits Akhil for the question and Fable for the work. The canonical ES reader identifies Akhil Mathew and Claude Fable 5. [Terence Tao's exposition](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/) gives the polynomial and its geometry. The original counterexample and its discovery are not results of this Split-Zero calculation.

Section1 and ALF1-3 state the exact programme role. The ES reader's four-dimensional extension provides four labelled inputs. Exact conjugacies transport its collision into the original conductor spaces. The subsequent calculation studies rank loss and the actual Xi data there, retaining the distinction between the nonlinear collision and the linear conductor. The original three-point fibre is not relabelled as a four-point fibre.

This folder contains exactly19 files. Extract supporting_proofs.zip and prior_figures.zip beside them to reconstruct the complete source tree. They include the preceding proofs, original source providers, archived Alpöge announcement, original author-source archives, independent reviews, exact checkers, interval receipts and reproducible figure sources. The archives do not overwrite the current cumulative or reader.

For verification, run `python independent/check_actual_unit_hermite_pullback.py`, `python independent/check_real_pair_uniform_coefficients.py` and `python certify_actual_xi_pullback.py`. They require SymPy and python-flint; the recorded interval run uses python-flint0.9.0,768 bits and one worker. Generate the figures with `python generate_actual_xi_uniform_figures.py`, then build with `python build_actual_xi_uniform.py`; use `python render_actual_xi_uniform.py` for page renders. Matplotlib, Pillow, PyMuPDF and pdflatex are used for these artifact steps.

The arithmetic calculation excludes the tested quartet on its stated small parameter rectangle and proves positive zeroth moment for the Xi-derived extension on the full certified period interval. The geometric calculation proves both leading inverse singular rates at the original growing Gamma cutoffs. These are separate exact conclusions with their domains retained, not a global RH conclusion.

All28 reader pages and both figures were inspected. The reader has zero overfull boxes or unresolved citations. The cumulative draft retains151 inherited width warnings; no full cumulative-PDF layout claim is made. MANIFEST.json seals the files but is not a remote publication receipt.
