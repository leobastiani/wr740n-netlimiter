@ECHO OFF
if NOT EXIST %~dp0\lag.txt (
	echo.>%~dp0\lag.txt
	if ["%~1"] == [""] (
		call hide me
	)
	call netlimiter start %*
	nircmdc waitprocess "LeagueClient.exe"
	call netlimiter stop %*
	del %~dp0\lag.txt
	if ["%~1"] == [""] (
		call show me
	)
	exit
)
