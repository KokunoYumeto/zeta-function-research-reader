$ErrorActionPreference = 'Stop'
$reviewRoot = $PSScriptRoot
$expectedHead = 'dfcbba5cbf7fec8c9301fe242c13e741d762013e'
$repo = 'KokunoYumeto/zeta-function-research-reader'
function Get-FinalApi([string]$endpoint,[string]$name) {
  $raw=(& 'C:\Program Files\GitHub CLI\gh.exe' api --method GET "repos/$repo/$endpoint") -join "`n"
  if ($LASTEXITCODE -ne 0) { throw "Final read failed: $endpoint" }
  [IO.File]::WriteAllText((Join-Path $reviewRoot ('evidence\'+$name)),$raw,[Text.UTF8Encoding]::new($false))
  return ($raw | ConvertFrom-Json)
}
$pr=Get-FinalApi 'pulls/24' 'pr_final.json'
if ($pr.head.sha -ne $expectedHead) { throw 'PR24 head moved; seal only the prior pin with a drift qualification' }
$checks=Get-FinalApi "commits/$expectedHead/check-runs?per_page=100" 'checks_final.json'
$runs=Get-FinalApi "actions/runs?head_sha=$expectedHead&per_page=100" 'runs_final.json'
$fetch=Get-Content -LiteralPath (Join-Path $reviewRoot 'FETCH_RECEIPT.json') -Raw | ConvertFrom-Json
foreach ($source in $fetch.sources) {
  $path=Join-Path (Join-Path $reviewRoot 'files') $source.path
  if ((Get-FileHash -LiteralPath $path -Algorithm SHA256).Hash.ToLowerInvariant() -ne $source.sha256) { throw 'Original pinned source changed locally' }
}
$fresh=Get-Content -LiteralPath (Join-Path $reviewRoot 'FRESH_CORE_RECEIPT.json') -Raw | ConvertFrom-Json
$proposal=Get-Content -LiteralPath (Join-Path $reviewRoot 'PROPOSED_CORRECTION_RECEIPT.json') -Raw | ConvertFrom-Json
if (-not $fresh.both_full_modes_passed -or -not $fresh.records_identical -or -not $proposal.normal_optimized_records_identical) { throw 'Fresh/proposed test evidence missing' }
$inputs=@()
foreach ($file in (Get-ChildItem -LiteralPath $reviewRoot -Recurse -File | Where-Object { $_.Name -ne 'REVIEW_RECEIPT.json' })) {
  $inputs += [ordered]@{path=[IO.Path]::GetRelativePath($reviewRoot,$file.FullName).Replace('\','/'); bytes=$file.Length; sha256=(Get-FileHash -LiteralPath $file.FullName -Algorithm SHA256).Hash.ToLowerInvariant()}
}
$seal=[ordered]@{created_utc=[DateTime]::UtcNow.ToString('o'); pr=24; head=$expectedHead; head_tree=$fetch.head_tree; pr_state=$pr.state; draft=$pr.draft; final_mergeable=$pr.mergeable; final_mergeable_state=$pr.mergeable_state; final_check_count=$checks.total_count; final_actions_run_count=$runs.total_count; original_public_core_eight_methods_pass_normal_and_optimized=$true; original_negative_controls_fail=$true; additional_exact_interface_checks=18; proposed_correction_is_local_only=$true; proposed_eight_methods_pass_normal_and_optimized=$true; original_source_bytes_unchanged=$true; original_gamma_join_inputs_read_only=$true; remote_writes=$false; active_edition_writes=$false; local_lean_or_heavy_build=$false; public_review='REVIEW.md'; correction_suggestion='PROPOSED_CORRECTION.md'; correction_patch='PROPOSED_CORRECTION.patch'; inputs=$inputs}
[IO.File]::WriteAllText((Join-Path $reviewRoot 'REVIEW_RECEIPT.json'),($seal | ConvertTo-Json -Depth 20),[Text.UTF8Encoding]::new($false))
[pscustomobject]$seal | Select-Object head,pr_state,draft,final_mergeable,final_mergeable_state,final_check_count,final_actions_run_count | Format-List
@('REVIEW.md','PROPOSED_CORRECTION.md','PROPOSED_CORRECTION.patch','PROPOSED_CORRECTION_RECEIPT.json','REVIEW_RECEIPT.json') | ForEach-Object { $path=Join-Path $reviewRoot $_; [pscustomobject]@{file=$_; sha256=(Get-FileHash -LiteralPath $path -Algorithm SHA256).Hash.ToLowerInvariant()} } | ConvertTo-Json -Depth 5
