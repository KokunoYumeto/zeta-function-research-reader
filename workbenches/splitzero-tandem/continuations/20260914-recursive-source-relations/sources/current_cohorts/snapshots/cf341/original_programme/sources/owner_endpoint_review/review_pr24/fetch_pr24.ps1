$ErrorActionPreference = 'Stop'
$reviewRoot = $PSScriptRoot
$evidenceRoot = Join-Path $reviewRoot 'evidence'
$sourceRoot = Join-Path $reviewRoot 'files'
[void](New-Item -ItemType Directory -Path $evidenceRoot -Force)
[void](New-Item -ItemType Directory -Path $sourceRoot -Force)
$repo = 'KokunoYumeto/zeta-function-research-reader'
$expectedHead = 'dfcbba5cbf7fec8c9301fe242c13e741d762013e'
$script:records = @()
function Get-RecordedApi([string]$endpoint,[string]$name,[bool]$isJson=$true) {
  $info = [Diagnostics.ProcessStartInfo]::new()
  $info.FileName = 'C:\Program Files\GitHub CLI\gh.exe'
  $info.UseShellExecute = $false
  $info.CreateNoWindow = $true
  $info.RedirectStandardOutput = $true
  $info.RedirectStandardError = $true
  foreach ($argument in @('api','--method','GET',"repos/$repo/$endpoint")) { [void]$info.ArgumentList.Add($argument) }
  $process = [Diagnostics.Process]::Start($info)
  $outTask = $process.StandardOutput.ReadToEndAsync()
  $errTask = $process.StandardError.ReadToEndAsync()
  $process.WaitForExit()
  $raw = $outTask.GetAwaiter().GetResult()
  $err = $errTask.GetAwaiter().GetResult()
  if ($process.ExitCode -ne 0) { throw "Read failed: $endpoint : $err" }
  $target = Join-Path $evidenceRoot $name
  [IO.File]::WriteAllText($target,$raw,[Text.UTF8Encoding]::new($false))
  $script:records += [ordered]@{endpoint=$endpoint; file=$name; bytes=(Get-Item -LiteralPath $target).Length; sha256=(Get-FileHash -LiteralPath $target -Algorithm SHA256).Hash.ToLowerInvariant()}
  if ($isJson) { return ($raw | ConvertFrom-Json) }
}
$pr = Get-RecordedApi 'pulls/24' 'pr_before.json'
if ($pr.head.sha -ne $expectedHead) { throw "Head moved to $($pr.head.sha); revise pin" }
$main = Get-RecordedApi 'git/ref/heads/main' 'main_ref.json'
$headCommit = Get-RecordedApi "git/commits/$expectedHead" 'head_commit.json'
$tree = Get-RecordedApi "git/trees/$($headCommit.tree.sha)?recursive=1" 'head_tree.json'
if ($tree.truncated) { throw 'Tree truncated' }
$compare = Get-RecordedApi "compare/$($main.object.sha)...$expectedHead" 'compare_current_main.json'
$files = Get-RecordedApi 'pulls/24/files?per_page=100' 'changed_files.json'
if (@($files).Count -ge 100) { throw 'PR files pagination required' }
$sources = @()
foreach ($file in $files) {
  if ($file.status -ne 'added') { throw "Unexpected nonadditive file $($file.filename)" }
  $entry = $tree.tree | Where-Object { $_.path -eq $file.filename }
  if (@($entry).Count -ne 1 -or $entry.sha -ne $file.sha) { throw 'File/tree mismatch' }
  $blob = Get-RecordedApi "git/blobs/$($entry.sha)" "blob_$($entry.sha).json"
  $target = Join-Path $sourceRoot $entry.path
  [void](New-Item -ItemType Directory -Path ([IO.Path]::GetDirectoryName($target)) -Force)
  [IO.File]::WriteAllBytes($target,[Convert]::FromBase64String($blob.content))
  $sources += [ordered]@{path=$entry.path; blob=$entry.sha; bytes=(Get-Item -LiteralPath $target).Length; sha256=(Get-FileHash -LiteralPath $target -Algorithm SHA256).Hash.ToLowerInvariant()}
}
$comments = Get-RecordedApi 'issues/24/comments?per_page=100' 'comments.json'
$checks = Get-RecordedApi "commits/$expectedHead/check-runs?per_page=100" 'checks.json'
$runs = Get-RecordedApi "actions/runs?head_sha=$expectedHead&per_page=100" 'runs.json'
if ($checks.total_count -gt 100 -or $runs.total_count -gt 100 -or @($comments).Count -ge 100) { throw 'Pagination required' }
$jobs = @()
foreach ($run in $runs.workflow_runs) {
  $response = Get-RecordedApi "actions/runs/$($run.id)/jobs?per_page=100" "jobs_$($run.id).json"
  if ($response.total_count -gt 100) { throw 'Jobs pagination required' }
  foreach ($job in $response.jobs) {
    $jobs += [ordered]@{head=$run.head_sha; run_id=$run.id; run_name=$run.name; event=$run.event; run_status=$run.status; run_conclusion=$run.conclusion; id=$job.id; name=$job.name; status=$job.status; conclusion=$job.conclusion; steps=$job.steps}
    if ($job.status -eq 'completed') { Get-RecordedApi "actions/jobs/$($job.id)/logs" "job_$($job.id).log" $false }
  }
}
$after = Get-RecordedApi 'pulls/24' 'pr_after.json'
if ($after.head.sha -ne $expectedHead) { throw 'Head moved during fetch' }
$receipt = [ordered]@{at_utc=[DateTime]::UtcNow.ToString('o'); head=$expectedHead; head_tree=$headCommit.tree.sha; main=$main.object.sha; draft=$after.draft; state=$after.state; mergeable=$after.mergeable; ahead=$compare.ahead_by; behind=$compare.behind_by; merge_base=$compare.merge_base_commit.sha; added_file_count=@($files).Count; sources=$sources; checks_count=$checks.total_count; run_count=$runs.total_count; jobs=$jobs; records=$script:records; remote_writes=$false; local_lean_or_heavy_build=$false}
[IO.File]::WriteAllText((Join-Path $reviewRoot 'FETCH_RECEIPT.json'),($receipt | ConvertTo-Json -Depth 30),[Text.UTF8Encoding]::new($false))
[pscustomobject]$receipt | Select-Object head,head_tree,main,draft,state,mergeable,ahead,behind,merge_base,added_file_count,checks_count,run_count | Format-List
$sources | ForEach-Object { [pscustomobject]$_ } | Format-Table -AutoSize
