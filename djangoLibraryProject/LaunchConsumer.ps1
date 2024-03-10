# Activate Python project environment
# Replace 'path\to\venv\Scripts\Activate.ps1' with the path to your virtual environment activation script
$pathToVenv = "..\djangohtmxenv\Scripts\Activate.ps1"
if (Test-Path $pathToVenv) {
    & $pathToVenv
} else {
    Write-Host "Virtual environment activation script not found."
    exit 1
}

# Set environment variable for DJANGO_SETTINGS_MODULE
$env:DJANGO_SETTINGS_MODULE = "djangoLibraryProject.settings"

# Run the Huey consumer
$consumerScript = "huey_consumer"
$hueyInstance = "consumer.tasks.huey"
$cmd = "$consumerScript $hueyInstance"
Write-Host "Running Huey consumer: $cmd"
Invoke-Expression $cmd