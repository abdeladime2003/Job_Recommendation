#  Définir les chemins de base
$basePath = Split-Path -Parent $MyInvocation.MyCommand.Path
$logFile = "$basePath\logs\pipeline.log"
$scraper1 = "$basePath\scraping_emploi_ma\main.py"
$scraper2 = "$basePath\scraping_rekrute_com\main.py"
$scalaProjectPath = "$basePath\spark_transformation"

#  Fonction pour enregistrer les messages dans les logs
Function LogMessage($message, $type) {
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    $logEntry = "[$timestamp] [$type] $message"
    Add-Content -Path $logFile -Value $logEntry
    Write-Host $logEntry
}

#  Créer le dossier de logs s'il n'existe pas
if (!(Test-Path "$basePath\logs")) {
    New-Item -ItemType Directory -Path "$basePath\logs" | Out-Null
}

#  Lancer le scraper du site 1
LogMessage " Démarrage du pipeline..." "INFO"
LogMessage "Scraping site 1 en cours..." "INFO"
$site1 = Start-Process -FilePath "python" -ArgumentList $scraper1 -NoNewWindow -Wait -PassThru
if ($site1.ExitCode -eq 0) {
    LogMessage " Scraping site 1 terminé avec succès !" "SUCCESS"
} else {
    LogMessage " Échec du scraping site 1 !" "ERROR"
    Exit 1
}

#  Lancer le scraper du site 2
LogMessage "Scraping site 2 en cours..." "INFO"
$site2 = Start-Process -FilePath "python" -ArgumentList $scraper2 -NoNewWindow -Wait -PassThru
if ($site2.ExitCode -eq 0) {
    LogMessage " Scraping site 2 terminé avec succès !" "SUCCESS"
} else {
    LogMessage " Échec du scraping site 2 !" "ERROR"
    Exit 1
}

#  Exécuter SBT dans le répertoire Scala sans changer de dossier principal
LogMessage "Démarrage du traitement Scala..." "INFO"

# Vérifier si SBT est accessible
if (-not (Get-Command sbt -ErrorAction SilentlyContinue)) {
    LogMessage " Erreur : SBT n'est pas installé ou accessible dans le PATH." "ERROR"
    Exit 1
}

# Exécution de SBT avec redirection des sorties
LogMessage "Exécution de SBT en cours..." "INFO"
Start-Process -FilePath "sbt" -ArgumentList "run" -WorkingDirectory $scalaProjectPath -NoNewWindow -Wait -PassThru *> $sbtLogFile 2> $sbtErrorFile
LogMessage " Pipeline exécuté avec succès !" "SUCCESS"
