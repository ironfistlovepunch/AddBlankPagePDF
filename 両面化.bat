REM ファイル編集
set pypath=%~dp0
rem pyファイルはbatファイルと同じフォルダに置くためbatのパス=pyパスである

echo %pypath%
echo %1

for /f "usebackq" %%t in (`%pypath%pdf両面化.py "%1"`) do set work=%%t
echo %work%
