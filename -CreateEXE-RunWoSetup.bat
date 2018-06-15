set mode=-w -F
set script=gaTectum_app
set scriptType=pyw


@echo off
cls
Echo Create environment variable "python" with path to WinPython 
Echo %script%.%scriptType%
Echo %mode%

:startProg
set WinPythonPath=%python%
rem set WinPythonPath=D:\Portable Programs\WinPython-64bit-3.4.3.5
set PYTHONCMD="%WinPythonPath%\WinPython Command Prompt.exe"
set folder=%cd%

Echo [1] - For pyi-makespec (create a spec-file) & Echo [2] - For pyinstaller (compile from spec) & Echo [3] - For pyi-makespec + pyinstaller (create a spec-file and compile)
set /P choise=Make a choise:

if %choise%==1 goto pyi-makespec
if %choise%==2 goto pyinstaller
if %choise%==3 goto all
cls
goto startProg
:pyi-makespec
%PYTHONCMD% "cd /d %folder% & pyi-makespec %mode% %script%.%scriptType%"
goto end
:pyinstaller
%PYTHONCMD% "cd /d %folder% & pyinstaller spec.spec"
goto end
:all
%PYTHONCMD% "cd /d %folder% & pyi-makespec %mode% %script%.%scriptType% & pause & pyinstaller spec.spec""
goto end
:end