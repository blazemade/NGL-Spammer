@echo of

if not "%1" == "max" (
    start /MAX cmd /c "%~f0" max
    exit /b
)

python NGL_spammer.py


