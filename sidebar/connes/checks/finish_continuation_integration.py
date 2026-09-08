"""Apply the final reviewed source clarification and public continuation metadata."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
old = """The function is unchanged by the finite unit subgroup; evenness
removes the real sign, so it is in the trivial-character component."""
new = r"""Every norm-one rational idele class has a representative consisting
of a real sign and finite units. Indeed, for an idele $g$ put
$q=\prod_p p^{v_p(g_p)}\in\mathbb Q_{>0}$, a finite product.
Then $g_p/q\in\mathbb Z_p^*$ for every prime, while the
norm-one identity gives $|g_\infty|=q$. Dividing by the diagonal
rational $q$ gives the asserted representative. The function
is unchanged by the finite units; evenness removes the real sign.
It therefore lies in the entire trivial-character component."""
for relative in ("tex/connes_quotient_heat_transport.tex",
                 "sources/source_sobolev_followup/sobolev_comparison.tex"):
    path = ROOT / relative
    text = path.read_text(encoding="utf-8")
    if old in text:
        assert text.count(old) == 1
        path.write_text(text.replace(old,new),encoding="utf-8")
path = ROOT / "README.md"
text = path.read_text(encoding="utf-8")
text = text.replace("the three entries","the four entries")
paragraph = ("The latest extension proves a homeomorphism between the original even "
 "Schwartz input space and its fully specified meromorphic Mellin space, including "
 "inverse estimates and every origin residue. It characterizes the exact Schwartz "
 "trace intersection and the sharp exponential boundary: Xi(s) exp(as) has an "
 "original Schwartz input exactly when |Re a| < pi/4. The meromorphic zeta heat "
 "connection has full pole cancellation, convergent numerator-jet evolution, and "
 "an exact Schwartz preservation domain that is proper at every nonzero time. "
 "A further primary-source comparison constructs the specified Sobolev cokernel "
 "ingress, its exact truncated-real-jet kernel and common test map to the source "
 "quotient; all spectral signs and the adelic factor 2 are retained.\n\n")
if paragraph not in text:
    text = text.replace("## Reproduce\n",paragraph+"## Reproduce\n")
path.write_text(text,encoding="utf-8")
print("Final source clarification and reader metadata applied.")
