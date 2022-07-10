@echo off
SET PATH=<Path-In-Python-3.xx>\;<Path-In-Python-3.xx>\Scripts\;%PATH%
SET WORKON_HOME=%CD%\win-env\
cmd.exe /s /k pushd "%V"
