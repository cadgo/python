#$steamAppsDir = (Get-Item HKCU:\Software\Valve\Steam).GetValue("SteamPath")
#$libFolder = $steamAppsDir+'\config\libraryfolders.vdf'
$libFolder = "libraryfolders_sample.vdf"


$game_path=(get-Content $libFolder | select-string -Pattern path)

#$game_list=$game_path -replace "`t", "" -replace "`"", "" -replace "path", ""
$game_path| % {$_ -replace "`t", "" -replace "`"", "" -replace "path", ""} 
