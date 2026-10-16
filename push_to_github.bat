@echo off
title Push SIR Saathi AI to GitHub
echo ===================================================
echo   Push SIR Saathi AI to your GitHub Repository
echo ===================================================
echo.
set /p REPO_URL="Enter your GitHub Repository URL (e.g. https://github.com/username/sir-saathi-ai.git): "
if "%REPO_URL%"=="" (
    echo Error: No repository URL provided.
    pause
    exit /b 1
)

echo.
echo Adding remote origin...
git remote remove origin 2>nul
git remote add origin %REPO_URL%
git branch -M main

echo.
echo Pushing main branch to GitHub...
git push -u origin main

echo.
echo ===================================================
echo   Done! Check your GitHub repository.
echo ===================================================
pause
