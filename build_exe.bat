@echo off
REM Build single-file Windows executable for yt_downloader.py
REM Installs build-time deps and runs PyInstaller. Run from project root.

pip install -r requirements.txt

REM If there is a local ffmpeg folder next to the script, include it in the bundle
set FFMPEG_ARG=
if exist ffmpeg (
    set FFMPEG_ARG=--add-data "ffmpeg;ffmpeg"
)

REM If there is an icon file, include it
set ICON_ARG=
if exist icon.ico (
    set ICON_ARG=--icon "icon.ico"
)

pyinstaller --onefile --noconsole %FFMPEG_ARG% %ICON_ARG% --name "YouTube_Downloader_v2.1.0" yt_downloader.py

echo.
echo Build finished. Check the dist folder for yt_downloader.exe
pause