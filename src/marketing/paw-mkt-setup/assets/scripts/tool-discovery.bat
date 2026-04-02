@echo off
REM =============================================================================
REM Tool Discovery Script for Agentic Marketing Suite (Windows)
REM =============================================================================
REM This script checks all CLI tools required by the marketing suite skills.
REM
REM Usage:
REM   tool-discovery.bat [--json] [--verbose]
REM =============================================================================

setlocal enabledelayedexpansion

set OUTPUT_JSON=false
set VERBOSE=false

for %%a in (%*) do (
    if "%%a"=="--json" set OUTPUT_JSON=true
    if "%%a"=="--verbose" set VERBOSE=true
)

REM Results
set TOOLS_AVAILABLE=0
set TOOLS_MISSING=0
set TOOLS_PARTIAL=0

if "%VERBOSE%"=="true" if "%OUTPUT_JSON%"=="false" (
    echo.
    echo ============================================================
    echo   Agentic Marketing Suite - Tool Discovery
    echo ============================================================
    echo.
    echo CLI Tools:
)

REM Check Node.js
where node >nul 2>&1
if %ERRORLEVEL%==0 (
    set NODE_STATUS=available
    set /a TOOLS_AVAILABLE+=1
    if "%VERBOSE%"=="true" echo   [OK] node: available
) else (
    set NODE_STATUS=missing
    set /a TOOLS_MISSING+=1
    if "%VERBOSE%"=="true" echo   [MISSING] node: not found
)

REM Check npm
where npm >nul 2>&1
if %ERRORLEVEL%==0 (
    set NPM_STATUS=available
    set /a TOOLS_AVAILABLE+=1
    if "%VERBOSE%"=="true" echo   [OK] npm: available
) else (
    set NPM_STATUS=missing
    set /a TOOLS_MISSING+=1
    if "%VERBOSE%"=="true" echo   [MISSING] npm: not found
)

REM Check npx
where npx >nul 2>&1
if %ERRORLEVEL%==0 (
    set NPX_STATUS=available
    set /a TOOLS_AVAILABLE+=1
    if "%VERBOSE%"=="true" echo   [OK] npx: available
) else (
    set NPX_STATUS=missing
    set /a TOOLS_MISSING+=1
    if "%VERBOSE%"=="true" echo   [MISSING] npx: not found
)

REM Check Python
where python >nul 2>&1
if %ERRORLEVEL%==0 (
    set PYTHON_STATUS=available
    set /a TOOLS_AVAILABLE+=1
    if "%VERBOSE%"=="true" echo   [OK] python: available
) else (
    where python3 >nul 2>&1
    if %ERRORLEVEL%==0 (
        set PYTHON_STATUS=available
        set /a TOOLS_AVAILABLE+=1
        if "%VERBOSE%"=="true" echo   [OK] python3: available
    ) else (
        set PYTHON_STATUS=missing
        set /a TOOLS_MISSING+=1
        if "%VERBOSE%"=="true" echo   [MISSING] python: not found
    )
)

REM Check Git
where git >nul 2>&1
if %ERRORLEVEL%==0 (
    set GIT_STATUS=available
    set /a TOOLS_AVAILABLE+=1
    if "%VERBOSE%"=="true" echo   [OK] git: available
) else (
    set GIT_STATUS=missing
    set /a TOOLS_MISSING+=1
    if "%VERBOSE%"=="true" echo   [MISSING] git: not found
)

REM Check agent-browser
where agent-browser >nul 2>&1
if %ERRORLEVEL%==0 (
    agent-browser --version >nul 2>&1
    if %ERRORLEVEL%==0 (
        set AGENTBROWSER_STATUS=available
        set /a TOOLS_AVAILABLE+=1
        if "%VERBOSE%"=="true" echo   [OK] agent-browser: available
    ) else (
        set AGENTBROWSER_STATUS=partial
        set /a TOOLS_PARTIAL+=1
        if "%VERBOSE%"=="true" echo   [PARTIAL] agent-browser: installed but browser not ready
    )
) else (
    set AGENTBROWSER_STATUS=missing
    set /a TOOLS_MISSING+=1
    if "%VERBOSE%"=="true" echo   [MISSING] agent-browser: not found
)

REM Check Chrome profiles directory
set CHROME_PROFILES=
if exist "%LOCALAPPDATA%\Google\Chrome\User Data" (
    set CHROME_PROFILES=%LOCALAPPDATA%\Google\Chrome\User Data
) else if exist "%APPDATA%\Google\Chrome\User Data" (
    set CHROME_PROFILES=%APPDATA%\Google\Chrome\User Data
)

REM Output results
if "%OUTPUT_JSON%"=="true" (
    echo {
    echo   "cli_tools": {
    echo     "node": "%NODE_STATUS%",
    echo     "npm": "%NPM_STATUS%",
    echo     "npx": "%NPX_STATUS%",
    echo     "python": "%PYTHON_STATUS%",
    echo     "git": "%GIT_STATUS%",
    echo     "agent-browser": "%AGENTBROWSER_STATUS%"
    echo   },
    echo   "summary": {
    echo     "available": %TOOLS_AVAILABLE%,
    echo     "missing": %TOOLS_MISSING%,
    echo     "partial": %TOOLS_PARTIAL%
    echo   },
    echo   "chrome_profiles_dir": "!CHROME_PROFILES!",
    echo   "chrome_available": %if defined CHROME_PROFILES (echo true) else (echo false)%
    echo }
) else (
    echo.
    echo ============================================================
    echo   Summary
    echo ============================================================
    echo.
    echo CLI Tools: %TOOLS_AVAILABLE% available, %TOOLS_PARTIAL% partial, %TOOLS_MISSING% missing
    echo.

    if defined CHROME_PROFILES (
        echo Chrome Profiles Directory:
        echo   !CHROME_PROFILES!
        echo.
        echo Tip: Use --profile flag with agent-browser for authenticated sessions
        echo   Example: agent-browser --profile C:\Users\%USERNAME%\.chrome-profiles\myprofile open https://linkedin.com
    ) else (
        echo Chrome profiles directory not found
    )

    echo.
    if "%AGENTBROWSER_STATUS%"=="missing" (
        echo [!] Recommended Action:
        echo     Install agent-browser for live website research:
        echo     npx skills add https://github.com/vercel-labs/agent-browser --skill agent-browser
    ) else if "%AGENTBROWSER_STATUS%"=="partial" (
        echo [!] Action Required:
        echo     Complete agent-browser setup by installing Chromium:
        echo     npx playwright install chromium
    )
)

endlocal