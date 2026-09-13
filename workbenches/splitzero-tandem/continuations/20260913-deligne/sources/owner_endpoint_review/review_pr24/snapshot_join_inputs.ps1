$ErrorActionPreference = 'Stop'
$reviewRoot = $PSScriptRoot
$editionRoot = 'F:\user\Documents\Papors\Chatnotes\Zeta-Function-Foundation\agents\zenodo_workspace_publication\integration_20260912e'
$targetRoot = Join-Path $reviewRoot 'join_inputs'
[void](New-Item -ItemType Directory -Path $targetRoot -Force)
$mapping = [ordered]@{
  'ENDPOINT_GAMMA_JOIN.md'='ENDPOINT_GAMMA_JOIN.md'
  'GAMMA_TODA_JOIN.tex'='GAMMA_TODA_JOIN.tex'
  'gamma_review\source_stage\NOTE.tex'='GAMMA_SOURCE_NOTE.tex'
  'GAMMA_PRIMITIVE.tex'='GAMMA_PRIMITIVE.tex'
  'review_pr23\postmerge\ENDPOINT_CRITERION.after.md'='PR23_ENDPOINT_CORRECTED.md'
}
$items = @()
foreach ($entry in $mapping.GetEnumerator()) {
  $source = Join-Path $editionRoot $entry.Key
  $target = Join-Path $targetRoot $entry.Value
  $before = (Get-FileHash -LiteralPath $source -Algorithm SHA256).Hash.ToLowerInvariant()
  Copy-Item -LiteralPath $source -Destination $target
  $after = (Get-FileHash -LiteralPath $target -Algorithm SHA256).Hash.ToLowerInvariant()
  if ($before -ne $after) { throw 'Context copy hash mismatch' }
  $items += [ordered]@{edition_relative_source=$entry.Key.Replace('\','/'); snapshot=$entry.Value; sha256=$after; bytes=(Get-Item -LiteralPath $target).Length; original_modified=$false}
}
[IO.File]::WriteAllText((Join-Path $reviewRoot 'JOIN_INPUT_RECEIPT.json'),($items | ConvertTo-Json -Depth 8),[Text.UTF8Encoding]::new($false))
$items | ConvertTo-Json -Depth 5
