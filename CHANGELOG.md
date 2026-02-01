# Changelog

All notable changes to this project will be documented in this file.

## [2.1.0] - 2026-02-01

### 🚀 Major New Features

#### Clipboard Monitoring 📎
- **Auto-detect YouTube links** - Automatically monitors clipboard for YouTube URLs
- **Smart notification dialog** - Shows popup when YouTube link is detected
- **Quick format selection** - Choose MP3 or MP4 directly in the detection dialog
- **One-click download** - Start download immediately from clipboard notification
- **Toggle on/off** - Optional checkbox to enable/disable monitoring

#### Smart Playlist Detection 🎯
- **Intelligent URL parsing** - Detects when link contains playlist/radio parameters (`&list=`)
- **User choice dialog** - Asks whether to download single video or full playlist/radio
- **Clean URL extraction** - Automatically removes playlist parameters when downloading single video
- **Regex-based analysis** - Extracts video_id and playlist_id from complex URLs
- **Handles all formats** - Works with youtube.com/watch, youtu.be, and playlist URLs

### Added
- New checkbox "Auto-detect YouTube links" in GUI
- Automatic clipboard monitoring with 1-second interval
- Modal dialog windows for user choices (playlist selection, format selection)
- `analyze_youtube_url()` function - Analyzes and parses YouTube URLs
- `is_youtube_url()` function - Validates if string is YouTube link
- `process_download()` function - Handles smart playlist detection before download
- Support for radio/mix playlists (e.g., `&list=RD...&start_radio=1`)

### Changed
- URL processing now includes playlist detection before download
- GUI layout adjusted to accommodate clipboard monitoring checkbox
- Download button now triggers smart URL processing instead of direct download
- Added translations for new features (clipboard_monitor, playlist_detected, etc.)

### Technical
- Added `re` module import for regex pattern matching
- Implemented clipboard polling with `root.clipboard_get()`
- Added state tracking for clipboard to avoid duplicate notifications
- Modal dialogs use `tk.Toplevel` with `grab_set()` for focus management
- URL cleaning algorithm removes `&list=` parameters while preserving video ID

### User Experience
- ⚡ Faster workflow: Copy link → Auto-popup → Choose format → Download
- 🎯 No more accidental playlist downloads from single video links
- 🖱️ Fewer clicks required to start downloads
- 💡 Clear visual feedback with detection dialogs

## [2.0.0] - 2026-02-01

### Added
- **MP4 video download support** - Now supports both MP3 (audio) and MP4 (video) formats
- **Dynamic language switching** - Switch between English and Russian without restarting
- **Improved GUI layout** - Better organized interface with ttk widgets
- **Progress indicator** - Visual feedback during downloads with progress bar
- **Enhanced UI** - Modern look with better spacing and organization
- **Comprehensive documentation** - Full README in English and Russian
- **Format selection** - Radio buttons to choose between MP3 and MP4
- **Thumbnail embedding** - Optional thumbnail embedding for MP3 files

### Changed
- Renamed `yt_playlist_to_mp3.py` to `yt_downloader.py` for better clarity
- Updated GUI to use ttk (themed widgets) for modern appearance
- Improved language support with real-time UI updates
- Enhanced error handling and user feedback
- Reorganized UI layout for better usability
- Updated all documentation files (README.md, README_RU.md, BUILD_EXE.md)

### Fixed
- Language switching now works dynamically in GUI
- Better fallback for bundled yt-dlp module in exe builds
- Fixed UI element alignment and spacing
- Improved progress bar behavior

### Technical
- Added language update callbacks for all UI elements
- Implemented widget reference dictionary for dynamic updates
- Enhanced subprocess handling for better output capture
- Improved ffmpeg detection and path handling

## [1.0.0] - Initial Release

### Added
- Basic MP3 download functionality
- Playlist support
- Simple GUI interface
- Command-line interface
- ffmpeg integration
- Basic Russian localization

---

For detailed information, see [README.md](README.md) (available in English and Russian)
