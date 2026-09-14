from pathlib import Path
import importlib.util
root=Path(__file__).resolve().parent
p=root/"reviews/theta_certified_hankel_exact_rational_review_20260913.py"
spec=importlib.util.spec_from_file_location("exact_review",p)
m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
m.DIR=root/"calculation"
m.INPUT=m.DIR/"certificate_dimension16_1024.json"
m.REPLAY=m.DIR/"reviewer_replay_dimension16_1024.json"
m.OUTPUT=root/"exact_rational_reproduction.json"
m.main()
