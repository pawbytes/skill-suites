@echo off
REM =============================================================================
REM Chrome Profile Discovery Script for Agent-Browser (Windows)
REM =============================================================================
REM Lists available Chrome profiles for authenticated sessions
REM
REM Usage:
REM   chrome-profiles.bat [--paths]
REM =============================================================================

setlocal enabledelayedexpansion

set SHOW_PATHS=false

for %%a in (%*) do (
    if "%%a"=="--paths" set SHOW_PATHS=true
)

REM Find Chrome User Data directory
set CHROME_DATA=
if exist "%LOCALAPPDATA%\Google\Chrome\User Data" (
    set CHROME_DATA=%LOCALAPPDATA%\Google\Chrome\User Data
) else if exist "%APPDATA%\Google\Chrome\User Data" (
    set CHROME_DATA=%APPDATA%\Google\Chrome\User Data
)

if not defined CHROME_DATA (
    echo Error: Chrome profiles directory not found
    echo Checked: %%LOCALAPPDATA%%\Google\Chrome\User Data
    exit /b 1
)

echo Chrome Profiles Directory: %CHROME_DATA%
echo.
echo Available Profiles:
echo ============================================================

REM List Default profile
if exist "%CHROME_DATA%\Default" (
    echo   [Default] Default Profile
    if "%SHOW_PATHS%"=="true" (
        echo            Path: %CHROME_DATA%\Default
        echo.
    )
)

REM List other profiles (Profile 1, Profile 2, etc.)
set PROFILE_COUNT=1
:loop
if exist "%CHROME_DATA%\Profile !PROFILE_COUNT!" (
    echo   [Profile !PROFILE_COUNT!] Profile !PROFILE_COUNT!
    if "%SHOW_PATHS%"=="true" (
        echo                   Path: %CHROME_DATA%\Profile !PROFILE_COUNT!
        echo.
    )
    set /a PROFILE_COUNT+=1
    goto loop
)

echo.
echo Usage with agent-browser:
echo ============================================================
echo.
echo   REM Use a profile for authenticated sessions:
echo   agent-browser --profile "C:\Users\%USERNAME%\.chrome-profiles\myprofile" open https://linkedin.com
echo.
echo   REM Or set environment variable:
echo   set AGENT_BROWSER_PROFILE=C:\Users\%USERNAME%\.chrome-profiles\myprofile
echo   agent-browser open https://linkedin.com
echo.
echo   REM For gated content (social media, etc.):
echo   agent-browser --profile "path\to\profile" open https://twitter.com
echo.

endlocal