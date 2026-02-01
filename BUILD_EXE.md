# Building Standalone Executable (.exe)

This guide explains how to build a standalone Windows executable from the YouTube Downloader Python script.

## Prerequisites

- Python 3.8 or higher installed on Windows
- Git (optional, for cloning the repository)

## Quick Build

1. **Open Command Prompt or PowerShell** in the project directory (where `yt_downloader.py` is located)

2. **Optional: Place ffmpeg folder** in the project root if you want to bundle ffmpeg with the executable
   - Create a folder named `ffmpeg` next to `yt_downloader.py`
   - Place `ffmpeg.exe` in `ffmpeg\bin\` or directly in `ffmpeg\`

3. **Run the build script**:
   ```cmd
   build_exe.bat
   ```

The script will:
- Install required dependencies (`yt-dlp`, `pyinstaller`)
- Detect and include the local `ffmpeg` folder if present
- Build a single-file executable using PyInstaller
- Place the resulting `yt_downloader.exe` in the `dist/` folder

## Manual Build Steps

If you prefer to build manually or customize the process:

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Build with PyInstaller**:
   
   **Without bundled ffmpeg:**
   ```bash
   pyinstaller --onefile yt_downloader.py
   ```
   
   **With bundled ffmpeg folder:**
   ```bash
   pyinstaller --onefile --add-data "ffmpeg;ffmpeg" yt_downloader.py
   ```

3. **Find the executable**:
   The compiled `yt_downloader.exe` will be in the `dist/` folder.

## Advanced Options

### Create a GUI application (no console window)

To hide the console window when running the GUI:
```bash
pyinstaller --onefile --windowed yt_downloader.py
```

### Add an icon

If you have a custom icon file (`icon.ico`):
```bash
pyinstaller --onefile --icon=icon.ico yt_downloader.py
```

### Custom spec file

For advanced customization, PyInstaller creates a `.spec` file. You can modify it and rebuild:
```bash
pyinstaller yt_downloader.spec
```

## Important Notes

### About ffmpeg

`ffmpeg` is an external binary tool, not a Python library. You have several options:

1. **Bundle ffmpeg with the exe** (recommended for portability):
   - Place `ffmpeg` folder in project root before building
   - Use `--add-data "ffmpeg;ffmpeg"` flag

2. **Require users to install ffmpeg separately**:
   - Users must download ffmpeg and add it to their system PATH
   - Smaller exe file size

3. **Ship ffmpeg alongside the exe**:
   - Place ffmpeg folder next to the exe after building
   - The script will automatically detect it

### Distribution

When distributing your executable:

- **With bundled ffmpeg**: Just share the `yt_downloader.exe` file
- **Without bundled ffmpeg**: Include instructions for users to install ffmpeg

### Antivirus Warnings

Some antivirus software may flag PyInstaller-created executables as suspicious. This is a false positive. You can:
- Add the exe to your antivirus exceptions
- Sign the executable with a code signing certificate
- Build from source on the target machine

## Testing

After building, test the executable:

1. **Test GUI mode**:
   ```cmd
   dist\yt_downloader.exe
   ```

2. **Test CLI mode**:
   ```cmd
   dist\yt_downloader.exe "https://www.youtube.com/watch?v=dQw4w9WgXcQ" --format mp3
   ```

3. **Test on a clean Windows machine** (without Python installed) to ensure portability

## Troubleshooting

### "ffmpeg not found" error
- Ensure ffmpeg is bundled or installed on the system
- Check that the `ffmpeg` folder structure is correct

### "yt-dlp not found" error
- This shouldn't happen if built correctly - yt-dlp is bundled as a Python module
- Rebuild with `--hidden-import yt_dlp` if necessary

### Large exe file size
- This is normal for PyInstaller executables (typically 20-50 MB)
- Consider UPX compression: `pyinstaller --onefile --upx-dir=path/to/upx yt_downloader.py`

### Module import errors
- Add missing modules to the spec file or use `--hidden-import` flag

## File Size Optimization

The exe will be approximately:
- **Without ffmpeg**: ~15-25 MB
- **With ffmpeg bundled**: ~70-100 MB (includes ffmpeg binary)

To reduce size:
- Don't bundle ffmpeg (require separate installation)
- Use UPX compression
- Use `--exclude-module` to remove unnecessary modules

## Alternative: Using Auto-py-to-exe

For a GUI-based approach to building:

1. Install auto-py-to-exe:
   ```bash
   pip install auto-py-to-exe
   ```

2. Run it:
   ```bash
   auto-py-to-exe
   ```

3. Configure options in the GUI and build

---

**For questions or issues, please open an issue on GitHub.**

**Documentation**: [README.md](README.md) (English/Русский)