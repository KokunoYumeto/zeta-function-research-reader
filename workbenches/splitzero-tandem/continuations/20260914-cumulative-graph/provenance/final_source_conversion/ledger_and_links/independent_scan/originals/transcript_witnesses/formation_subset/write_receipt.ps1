$ErrorActionPreference = 'Stop'
$stagingRoot = 'workspace:\work\backpropagation_20260913\cohort_staging'
$outputRoot = Join-Path $stagingRoot 'ledger_exponent_correction\independent_scan\originals\transcript_witnesses\formation_subset'
$ledgerPath = Join-Path $stagingRoot 'snapshots\transcript\ledger_publication\sources\formation.md'
$turn0756 = Join-Path $stagingRoot 'snapshots\transcript\sources\turns\A0756.md'
$turn0952 = Join-Path $stagingRoot 'snapshots\transcript\sources\turns\A0952.md'
$utf8 = [Text.UTF8Encoding]::new($false)
function Get-Sha256Text([string]$Value) {
    $sha = [Security.Cryptography.SHA256]::Create()
    try { return ([BitConverter]::ToString($sha.ComputeHash($utf8.GetBytes($Value)))).Replace('-', '').ToLowerInvariant() }
    finally { $sha.Dispose() }
}
function Get-Snippet([string]$Path, [int]$First, [int]$Last) {
    $raw = [IO.File]::ReadAllText($Path, $utf8)
    $lines = [regex]::Matches($raw, '(?m)^[^\r\n]*(?:\r\n|\n|$)')
    if ($First -lt 1 -or $Last -gt $lines.Count -or $Last -lt $First) { throw 'Invalid witness range' }
    $start = $lines[$First - 1].Index
    $end = $lines[$Last - 1].Index + $lines[$Last - 1].Length
    $snippet = $raw.Substring($start, $end - $start)
    return [ordered]@{ path = $Path; first_line = $First; last_line = $Last; exact_snippet = $snippet; snippet_sha256_utf8 = (Get-Sha256Text $snippet) }
}
$sourceHashesBefore = @($ledgerPath, $turn0756, $turn0952) | ForEach-Object {
    [ordered]@{ path = $_; sha256 = (Get-FileHash -LiteralPath $_ -Algorithm SHA256).Hash.ToLowerInvariant() }
}
$queries = @(
    [ordered]@{
        id = 'BF05_paired_holonomy'; ledger_line = 133; turn = $turn0756
        ledger_formula_literal = 'diag(e^{-aL},e^{aL})'
        ranges = ,@(1191,1197)
        finding = 'Witness found; literal mismatch. The transcript uses D_a and an explicit pmatrix, with ordered diagonal entries e^{-aL} and e^{aL} and both off-diagonal entries 0. The ledger diag(...) spelling is absent. Both exponential subexpressions match literally.'
    },
    [ordered]@{
        id = 'BF08_polynomial'; ledger_line = 193; turn = $turn0756
        ledger_formula_literal = 'P_{a,b}(s)=((s−1/2−a)^2+b²)((s−1/2+a)^2+b²)'
        ranges = @(@(1604,1611), @(1623,1629))
        finding = 'Witness found; literal mismatch. Transcript retains the two factors in the same order with -a then +a, using TeX \\tfrac12, ASCII minus, b^2, \\big delimiters, and line breaks. The exact ledger formula string is absent. a,b>0 occurs at line 1604; the further restriction 0<a<1/2 occurs at line 1629. Four roots occur at line 1626.'
    },
    [ordered]@{
        id = 'BF17_comparison_image'; ledger_line = 377; turn = $turn0952
        ledger_formula_literal = 'c_i:H_c^i→H^i, image I^i'
        ranges = @(@(254,260), @(262,276), @(290,295))
        finding = 'Witness found; literal mismatch. Transcript gives c_i on a separate line, retains (X,\\mathcal F) in both source and target, spells the arrow \\longrightarrow, and explicitly defines I^i:=\\operatorname{im}(c_i). The ledger condensed literal is absent. The factorization through the image is retained at lines 293–294.'
    }
)
$records = foreach ($query in $queries) {
    $turnRaw = [IO.File]::ReadAllText($query.turn, $utf8)
    $ledgerSnippet = Get-Snippet $ledgerPath $query.ledger_line $query.ledger_line
    if (-not $ledgerSnippet.exact_snippet.Contains($query.ledger_formula_literal)) { throw ('Ledger literal not found at specified line: ' + $query.id) }
    $witnesses = @($query.ranges | ForEach-Object { Get-Snippet $query.turn $_[0] $_[1] })
    [ordered]@{
        id = $query.id
        ledger = $ledgerSnippet
        ledger_formula_literal = $query.ledger_formula_literal
        literal_formula_found_in_turn = $turnRaw.Contains($query.ledger_formula_literal)
        status = 'witness_found_literal_mismatch'
        finding = $query.finding
        witnesses = $witnesses
    }
}
$sourceHashesAfter = @($ledgerPath, $turn0756, $turn0952) | ForEach-Object {
    [ordered]@{ path = $_; sha256 = (Get-FileHash -LiteralPath $_ -Algorithm SHA256).Hash.ToLowerInvariant() }
}
for ($index = 0; $index -lt $sourceHashesBefore.Count; $index++) {
    if ($sourceHashesBefore[$index].sha256 -cne $sourceHashesAfter[$index].sha256) { throw 'Read-only source changed during receipt generation' }
}
$receipt = [ordered]@{
    scope = 'Bounded read-only formation formula witness search: BF05, BF08, BF17; transcript turns A0756.md and A0952.md only.'
    created_utc = [DateTime]::UtcNow.ToString('o')
    provenance = (Join-Path $stagingRoot 'ledger_exponent_correction\independent_scan\USER_INPUTS_VERBATIM.md')
    method = 'Line numbers are one-based in the named UTF-8 files. Each exact_snippet includes the original selected lines and their original line endings, including any trailing line ending. Snippet SHA256 hashes its UTF-8 bytes without a BOM. File SHA256 hashes the original file bytes. Literal checks use ordinal substring matching without mathematical or textual normalization. Representation comparisons are stated separately from literal match results.'
    original_files = $sourceHashesBefore
    source_hashes_unchanged = $true
    formulas_requested = 3
    witness_found = 3
    literal_mismatch = 3
    unmatched = 0
    records = @($records)
}
$receiptPath = Join-Path $outputRoot 'FORMATION_TRANSCRIPT_WITNESSES.json'
[IO.File]::WriteAllText($receiptPath, ($receipt | ConvertTo-Json -Depth 12) + "`n", $utf8)
[IO.File]::WriteAllText((Join-Path $outputRoot 'LOGBOOK.md'), "# Formation transcript witness scan`n`nBounded assignment: inspect formation.md lines 133, 193, and 377 against A0756.md and A0952.md only; do not edit active files, render PDFs, or re-extract sessions. Shared user-input provenance already exists at independent_scan/USER_INPUTS_VERBATIM.md.`n`nCompleted: all three formula witnesses found. All three ledger formula strings differ literally from transcript spelling; exact original snippets, one-based ranges, and SHA256 values are retained in FORMATION_TRANSCRIPT_WITNESSES.json. No requested formula is unmatched. No source edits were made. The receipt generator verifies that all three source file hashes remain unchanged. No independent mathematical theorem validation was performed or claimed.`n`nTo do: parent integration only.`n", $utf8)
[ordered]@{ receipt_path = $receiptPath; receipt_sha256 = (Get-FileHash -LiteralPath $receiptPath -Algorithm SHA256).Hash.ToLowerInvariant(); witness_found = 3; literal_mismatch = 3; unmatched = 0 } | ConvertTo-Json
