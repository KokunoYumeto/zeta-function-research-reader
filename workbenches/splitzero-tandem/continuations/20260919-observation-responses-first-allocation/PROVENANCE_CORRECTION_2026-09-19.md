# Origin and continuity of the construction

The programme begins with the idea dated **12 July 2025**, originally presented as *An Algebraic Structure Incorporating a Z/1Z-Symmetric Element Adjoined to the Integers: Construction, Analysis, and Generalizations*. The user identifies this as the first version of their idea; the [Zenodo record](https://zenodo.org/records/17555345) records the publication date as 2025-07-12. Its original terminology is retained here. The name “Split-Zero” belongs to the subsequent development.

The construction was subsequently developed into *A Note on the Globalization Semiring G(Z)*, dated March 2026, and then the wider programme. The first note's date and the start of a particular GitHub directory do not replace the 2025 origin.

The existing [Project Atlas: Split-Zero Geometry and Common Deformation Registers](https://zenodo.org/records/21443852), dated 19 July 2026, provides the public map to the earlier results compendium, proof sources, formal checks and visual work. It must be linked as an established programme resource. The September RH/cohomology integration is a later strand of this continuing work.

## Exact continuity of the original construction

The original source `11.tex`, Section 3, Construction `construction_S` and Definitions `def:addition_S` and `def:multiplication_S`, defines

\[
\mathcal S=\mathbb Z\sqcup\{\mathcal T\},\qquad \mathcal T\notin\mathbb Z.
\]

On the integer component its operations are ordinary integer addition and multiplication. It also specifies

\[
n+\mathcal T=\mathcal T+n=n,\quad
\mathcal T+\mathcal T=\mathcal T,\quad
n\mathcal T=\mathcal T n=\mathcal T,\quad
\mathcal T^2=\mathcal T.
\]

The globalization note's first definition gives these same operations on \(G(\mathbb Z)=\mathbb Z\sqcup\{\tau\}\). The map

\[
\phi:\mathcal S\longrightarrow G(\mathbb Z),\qquad
\phi(n)=n\ (n\in\mathbb Z),\qquad \phi(\mathcal T)=\tau
\]

is an isomorphism of commutative unital semirings. Indeed, it is a bijection with inverse fixing every integer and sending \(\tau\) to \(\mathcal T\). For two integer arguments it preserves both operations because both definitions use the integer operations. For one integer and one adjoined argument, addition returns the integer and multiplication returns the adjoined argument on both sides, in either order. For two adjoined arguments both operations return the adjoined argument. These four cases exhaust the domain of each operation. It preserves the additive identity \(\mathcal T\mapsto\tau\) and multiplicative identity \(1\mapsto1\). In particular it retains the distinction \(0_{\mathbb Z}\ne\mathcal T\), transporting it to \(0_{\mathbb Z}\ne\tau\).

This establishes continuity of the defining mathematical object across the change of notation and title. It does not require the original manuscript to use the later name.

## Correction to the September chronology

The previous chronology began with a September repository date and gave two March papers as the earlier origin references. It omitted the July 2025 origin and the established Project Atlas. The corrected chronology references the original paper and the Atlas, while retaining the September commits solely as dates of that repository strand. It does not expand the overview into a catalogue of the intervening papers.

Understanding the wider corpus remains a separate mathematical responsibility: an unread paper's relevance cannot be judged from its absence in a dependency index. Reading the Atlas and checking the original definition do not establish that all preceding proofs have been read or integrated. The earlier request for an overview explaining the mathematical results also remains outstanding; this correction repairs provenance.

## Evidence and preservation

The source record's `publication_date` is 2025-07-12. The supplied Zenodo version has a later record-creation timestamp and is version index 5; neither field is substituted for the work's date or the user's account of its origin. The downloaded TeX has an empty title-page date. The exact record metadata and source bytes are retained locally in `zenodo_17555345/`; the Atlas metadata and source are retained in `zenodo_21443852/`. Historical editions and their hashes remain unchanged. Human and project credit in the sources remain attached to them.
