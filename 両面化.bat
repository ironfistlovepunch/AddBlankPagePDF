REM �t�@�C���ҏW
set pypath=%~dp0
rem py�t�@�C����bat�t�@�C���Ɠ����t�H���_�ɒu������bat�̃p�X=py�p�X�ł���

echo %pypath%
echo %1

for /f "usebackq" %%t in (`%pypath%pdf���ʉ�.py "%1"`) do set work=%%t
echo %work%
