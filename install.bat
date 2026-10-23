@echo off
chcp 65001 >nul
echo Установка необходимых пакетов, пожалуйста подождите...

pip install cryptography keyboard
if %errorlevel% equ 0 (
    echo Необходимые пакеты установлены. Можно  запускать программу!
) else (
    echo Произошла ошибка при установке пакетов. Убедитесь, что python установлен и добавлен в PATH
)

pause