from pathlib import Path
import hashlib
import json

base = Path(__file__).resolve().parent
target = base / 'single_primary_boundary_control.tex'
companion = base / 'single_primary_finite_field' / 'single_primary_finite_field.tex'
marker = '% BEGIN COMPLETE FINITE-FIELD COMPANION SPF'
core = target.read_text(encoding='utf-8').split(marker)[0].rstrip() + '\n'
part = companion.read_text(encoding='utf-8').rstrip() + '\n'
actual = hashlib.sha256(companion.read_bytes()).hexdigest()
expected = '538b2da5adf307b54396e46f0848a49c63f0d81072844d191768016255c4fd53'
assert actual == expected, (actual, expected)
assembled = core + '\n' + marker + '\n% Verified companion SHA256: ' + actual + '\n' + part + '% END COMPLETE FINITE-FIELD COMPANION SPF\n'
target.write_text(assembled, encoding='utf-8', newline='\n')
receipt = {
    'complex_equations': 'SP.1-SP.36',
    'finite_field_equations': 'SPF.1-SPF.29',
    'complex_core_sha256_before_embedding': 'b68000ac12f65176f112c42af282656cee9640bd472f0705d43613bc053e5f52',
    'finite_field_companion_sha256': actual,
    'combined_sha256': hashlib.sha256(target.read_bytes()).hexdigest(),
    'marked_original_sha256': '40749e2a9d599a322e7b125eb43ad0878a066a51b61da52cc3bb2ffb94cbd841',
    'bc_sha256': '6575b8e33ff00bef8b08e214b974b9bd1e966c3bed4b573c5ca274206a69e9fa',
    'scope': 'The actual full single-primary packet h=(s-rho)^m at t=0. Tensor invariants are not asserted to vanish.'
}
(base / 'single_primary_assembly_receipt.json').write_text(json.dumps(receipt, indent=2)+'\n', encoding='utf-8')
print(json.dumps(receipt, indent=2))
