#$steamAppsDir = (Get-Item HKCU:\Software\Valve\Steam).GetValue("SteamPath")
#$libFolder = $steamAppsDir+'\config\libraryfolders.vdf'
$libFolder = "libraryfolders_sample.vdf"


$game_path=(get-Content $libFolder | select-string -Pattern path)

$nnn=$game_path[1] -replace "`t", "" -replace "`"", "" -replace "path", ""
write-host $nnn
