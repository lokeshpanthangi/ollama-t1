@echo off
REM Ollama Chat CLI Launcher
REM This batch file makes it easier to run the Ollama Chat CLI script

IF "%~1"=="" (
    echo Usage: chat.bat "Your prompt here" [model_name]
    echo.
    echo Example: chat.bat "Tell me a joke" llama3
    echo.
    echo If model_name is not specified, llama3 will be used by default.
    exit /b 1
)

SET prompt=%~1
SET model=llama3

IF NOT "%~2"=="" (
    SET model=%~2
)

python ollama_chat.py -m %model% -p "%prompt%"