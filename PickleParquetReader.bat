@echo off
SET script_dir=%~dp0
start /B pythonw "%script_dir%pickleparquetreader.py" "%~1"