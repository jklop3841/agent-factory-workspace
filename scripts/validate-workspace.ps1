$ErrorActionPreference = "Stop"

$root = Resolve-Path (Join-Path $PSScriptRoot "..\..\..")
$requiredPaths = @(
    "00-inbox",
    "01-projects\agent-factory-workspace",
    "02-baselines\agent-factory-template-pack-v0.1.0.zip",
    "03-task-cards\TASK-20260312-AF-WORKSPACE-BOOTSTRAP.md",
    "04-handoffs\HANDOFF-20260312-AF-WORKSPACE-BOOTSTRAP.md",
    "06-templates\PRD-master.md",
    "06-templates\SPEC-master.md",
    "06-templates\TASK-CARD-master.md",
    "06-templates\HANDOFF-master.md",
    "06-templates\ACCEPTANCE-master.md",
    "06-templates\REVIEW-master.md",
    "docs\START-HERE.md",
    "docs\AGENT-FACTORY-FILE-TREE.md",
    "01-projects\agent-factory-workspace\docs\PRD.md",
    "01-projects\agent-factory-workspace\docs\SPEC.md",
    "01-projects\agent-factory-workspace\docs\ACCEPTANCE.md",
    "01-projects\agent-factory-workspace\config\workspace.template.json"
)

$missing = @()

foreach ($path in $requiredPaths) {
    $fullPath = Join-Path $root $path
    if (Test-Path $fullPath) {
        Write-Host "[ok] $path"
    } else {
        Write-Host "[missing] $path"
        $missing += $path
    }
}

if ($missing.Count -gt 0) {
    throw "Workspace validation failed. Missing: $($missing -join ', ')"
}

Write-Host ""
Write-Host "Workspace validation passed."
