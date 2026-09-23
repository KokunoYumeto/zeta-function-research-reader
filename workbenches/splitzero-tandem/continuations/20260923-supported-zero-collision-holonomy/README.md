# Supported Zero, Heat Collisions, and Holonomy

Read `SUPPORTED_ZERO_COLLISION_HOLONOMY.pdf` and its complete standalone LaTeX source. This 60-page reader develops the full support lattice, the actual heat-flow endpoint, the original arithmetic residue and Weil receivers, and the conductor and holonomy of every local real-zero collision. The preceding 40-page proof is retained. The new sections begin on page 41.

The separate HC, HH and PFH files contain the complete new derivations. The two figures have reproducible TikZ sources, in the conductor file and the separate holonomy figure. `NEW_RESULTS_2026-09-23.md` states the new results with proof locators; `RESULT_INDEX.json` records their mathematical role. `SOURCE_READING_AND_USE.json` records human authors, exact source versions, citations and the passages actually read.

The two Python files require SymPy. They reproduce 86 and 68 exact auxiliary identities, respectively. They supplement the analytic proofs; they do not certify a zeta zero or an RH conclusion. The full reader builds with LuaLaTeX using `reproduce_reader.py`; a TeX installation with the packages named in the source is required.

The fixed-point calculation retains every zero-support label. The full arithmetic prime action retains amplitudes and all jets, even when its common fixed amplitude is zero. The original arithmetic Weil identification is proved at time zero; the surrounding heat fibres carry their explicitly computed deformed trace forms.
