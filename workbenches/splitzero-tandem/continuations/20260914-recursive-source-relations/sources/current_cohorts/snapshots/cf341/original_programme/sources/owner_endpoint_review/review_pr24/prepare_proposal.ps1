$ErrorActionPreference = 'Stop'
$reviewRoot = $PSScriptRoot
$sourceRoot = Join-Path $reviewRoot 'files\workbenches\tau-confluent-transfer'
$proposalRoot = Join-Path $reviewRoot 'proposed'
[void](New-Item -ItemType Directory -Path $proposalRoot -Force)
foreach ($name in @('RESEARCH_NOTE.md','check_transfer_core.py')) {
  $source = Join-Path $sourceRoot $name
  $target = Join-Path $proposalRoot $name
  if (Test-Path -LiteralPath $target) { throw 'Proposal exists; do not overwrite an authored proposal' }
  Copy-Item -LiteralPath $source -Destination $target
}
