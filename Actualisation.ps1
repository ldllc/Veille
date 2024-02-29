$dossierActualisation = Join-Path -Path $PSScriptRoot -ChildPath "Scripts\Actualisation"
$scriptActualisation = Join-Path -Path $dossierActualisation -ChildPath "Actualisation.py"

if (Test-Path -Path $dossierActualisation -PathType Container) {
    Set-Location -Path $dossierActualisation
    python $scriptActualisation
} else {
    Write-Host "Le dossier Actualisation n'existe pas."
}