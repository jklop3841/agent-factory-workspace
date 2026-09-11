param(
    [Parameter(Mandatory = $true)]
    [string]$ModelId,

    [Parameter(Mandatory = $true)]
    [string]$ModelVersion,

    [string]$BaseUrl = "http://127.0.0.1:11434/v1/chat/completions",
    [string]$Python = "python",
    [int]$TimeoutSeconds = 120,
    [string]$OutRoot = "results/local-pilot"
)

$ErrorActionPreference = "Stop"

$Here = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $Here

$env:LRI_MODEL = $ModelId
$env:LRI_OPENAI_BASE_URL = $BaseUrl
$env:LRI_TIMEOUT_SECONDS = [string]$TimeoutSeconds
if (-not $env:LRI_TEMPERATURE) { $env:LRI_TEMPERATURE = "0.2" }
if (-not $env:LRI_TOP_P) { $env:LRI_TOP_P = "1.0" }

$Stamp = Get-Date -Format "yyyyMMdd-HHmmss"
$RunRoot = Join-Path $OutRoot $Stamp
$Hidden = Join-Path $RunRoot "hidden"
$PilotResults = Join-Path $RunRoot "pilot"
$ConfigPath = Join-Path $RunRoot "config.pilot.frozen.json"
$DoctorPath = Join-Path $RunRoot "ADAPTER_DOCTOR.json"
$MetaPath = Join-Path $RunRoot "PILOT_LAUNCH_METADATA.json"

New-Item -ItemType Directory -Path $RunRoot -Force | Out-Null

Write-Host "[1/6] Adapter doctor: exactly two real-model requests..."
& $Python doctor_adapter.py `
    --task-adapter "$Python adapters/local_openai_compatible.py" `
    --mutation-adapter "$Python adapters/local_openai_compatible.py" `
    --timeout $TimeoutSeconds | Tee-Object -FilePath $DoctorPath
if ($LASTEXITCODE -ne 0) { throw "Adapter doctor failed. Evidence run remains blocked." }

$Doctor = Get-Content $DoctorPath -Raw | ConvertFrom-Json
if ($Doctor.status -ne "pass") { throw "Adapter doctor did not pass." }

Write-Host "[2/6] Freeze pilot configuration..."
$Config = Get-Content "config.local-model.pilot.template.json" -Raw | ConvertFrom-Json
$Config.frozen_timestamp = (Get-Date).ToUniversalTime().ToString("o")
$Config.model.id = $ModelId
$Config.model.version = $ModelVersion
$Config.model.temperature = [double]$env:LRI_TEMPERATURE
$Config.model.top_p = [double]$env:LRI_TOP_P
$Config | ConvertTo-Json -Depth 20 | Set-Content -Encoding utf8 $ConfigPath

Write-Host "[3/6] Estimate worst-case pilot call topology..."
& $Python estimate_budget.py `
    --config $ConfigPath `
    --training-per-phase 4 `
    --heldout-per-phase 6 `
    --primary-repeats 1 `
    --full-matrix-repeats 1 | Set-Content -Encoding utf8 (Join-Path $RunRoot "CALL_BUDGET_ESTIMATE.json")
if ($LASTEXITCODE -ne 0) { throw "Call estimator failed." }

$Estimate = Get-Content (Join-Path $RunRoot "CALL_BUDGET_ESTIMATE.json") -Raw | ConvertFrom-Json
$PrimaryCalls = $Estimate.matrix.primary_A_B_C_calls_per_run
if ($PrimaryCalls -ne 48) {
    throw "Pilot topology changed unexpectedly: expected 48 model calls, got $PrimaryCalls. Review before running."
}

Write-Host "[4/6] Freeze non-evidence pilot task bundle..."
$PilotSeed = "LOCAL-PILOT-$Stamp-$ModelId"
& $Python freeze_tasks.py `
    --seed $PilotSeed `
    --out $Hidden `
    --training-per-phase 4 `
    --heldout-per-phase 6 `
    --publish-seed | Set-Content -Encoding utf8 (Join-Path $RunRoot "FREEZE_OUTPUT.json")
if ($LASTEXITCODE -ne 0) { throw "Pilot task freeze failed." }

Write-Host "[5/6] Run 48-call A/B/C pilot..."
& $Python run_pilot.py `
    --config $ConfigPath `
    --freeze-dir $Hidden `
    --controller-script batch_controller.py `
    --task-adapter "$Python adapters/local_openai_compatible.py" `
    --mutation-adapter "$Python adapters/local_openai_compatible.py" `
    --out-dir $PilotResults `
    --timeout $TimeoutSeconds | Set-Content -Encoding utf8 (Join-Path $RunRoot "PILOT_STDOUT.json")
if ($LASTEXITCODE -ne 0) { throw "Pilot matrix failed. Do not start the evidence run." }

$PilotSummary = Get-Content (Join-Path $PilotResults "PILOT_SUMMARY.json") -Raw | ConvertFrom-Json
if (-not $PilotSummary.pilot_acceptance_checks.B_C_core_fairness) {
    throw "Pilot B/C fairness check failed. Do not start the evidence run."
}

Write-Host "[6/6] Write launch metadata and stop before evidence run..."
$Metadata = [ordered]@{
    protocol = "lri-local-pilot-launch-v0.1"
    created_at = (Get-Date).ToUniversalTime().ToString("o")
    model_id = $ModelId
    model_version = $ModelVersion
    endpoint = $BaseUrl
    exact_token_accounting_available = $Doctor.exact_token_accounting_available
    expected_primary_model_calls = $PrimaryCalls
    actual_pilot_model_call_attempts = $PilotSummary.total_model_call_attempts
    B_C_core_fairness = $PilotSummary.pilot_acceptance_checks.B_C_core_fairness
    evidence_status = "operational_pilot_not_evidence"
    next_gate = "Review this pilot. Then freeze a NEW private master seed and the final evidence configuration. This script intentionally does not start the evidence-bearing 20-run study."
}
$Metadata | ConvertTo-Json -Depth 10 | Set-Content -Encoding utf8 $MetaPath

Write-Host ""
Write-Host "Pilot completed: $RunRoot"
Write-Host "Evidence status remains E0."
Write-Host "This launcher intentionally stops here and does NOT start the 20-run evidence study."
