@ECHO OFF
SETLOCAL EnableDelayedExpansion

if EXIST %~dp0\lag.txt (
	set /p ans=lag.bat is already been running, should it run again? [y]:
	if ["!ans!"] == ["y"] (
		del %~dp0\lag.txt
	)
)

if NOT EXIST %~dp0\lag.txt (
	echo.>%~dp0\lag.txt
	call netlimiter start %*
	if ["%ERRORLEVEL%"] NEQ ["0"] (
		pause
		goto:eof
	)
	if ["%~1"] == [""] (
		call hide me
	)
	nircmdc waitprocess "LeagueClient.exe"
	call netlimiter stop %*
	del %~dp0\lag.txt
	if ["%~1"] == [""] (
		call show me
	)
	exit
)
