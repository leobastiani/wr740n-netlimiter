@ECHO OFF
if NOT EXIST %~dp0\lag.txt (
	echo.>%~dp0\lag.txt
	call hide me
	call netlimiter start
	nircmdc waitprocess "League of Legends.exe"
	call netlimiter stop
	del %~dp0\lag.txt
	call show me
	exit
)
