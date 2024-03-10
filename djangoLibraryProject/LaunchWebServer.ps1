# Activate Python project environment
# Replace 'path\to\venv\Scripts\Activate.ps1' with the path to your virtual environment activation script

param(
    [bool]$dectivate = $false
)
if($dectivate)
{
    $dac = "..\djangohtmxenv\Scripts\deactivate.bat"
    & $dac
    Write-Host "Running"
    exit 0
}
$pathToVenv = "..\djangohtmxenv\Scripts\Activate.ps1"
if (Test-Path $pathToVenv) {
    & $pathToVenv
} else {
    Write-Host "Virtual environment activation script not found."
    exit 1
}

# Set environment variable for DJANGO_SETTINGS_MODULE
$env:DJANGO_SETTINGS_MODULE = "djangoLibraryProject.settings"

#Run Migrations 

$runmakemigration= "python"
$argument= "manage.py "
$make= "makemigrations"
& $runmakemigration $argument $make

$runmigrate ="migrate"
& $runmakemigration $argument $runmigrate

# Run web server 

$runserverscript = "python manage.py runserver"

$cmd = "$runServerScript"
Write-Host "Running webserer server: $cmd"
Invoke-Expression $cmd