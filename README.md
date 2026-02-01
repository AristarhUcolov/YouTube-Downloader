# YouTube Downloader

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-2.1.0-brightgreen.svg)](CHANGELOG.md)

**[English](#english)** | **[Русский](#русский)**

📚 **Documentation:** [FAQ](FAQ.md) • [Examples](EXAMPLES.md) • [Changelog](CHANGELOG.md) • [Build Guide](BUILD_EXE.md)

---

<a name="english"></a>
## 🇬🇧 English Version

A simple and intuitive YouTube downloader with GUI support. Download videos and playlists as MP3 (audio) or MP4 (video) with maximum quality.

## ✨ Features

- 🎵 **MP3 Audio** - Extract audio in 320 kbps MP3 format
- 🎬 **MP4 Video** - Download videos in best available quality
- 📋 **Playlist Support** - Download entire playlists with automatic numbering
- 🎯 **Smart Playlist Detection** - Automatically detects playlist/radio links and asks what to download
- 📎 **Clipboard Monitoring** - Auto-detect YouTube links from clipboard (optional)
- 🖼️ **Embed Thumbnails** - Optional thumbnail embedding in MP3 files
- 🌐 **Multilingual** - English and Russian interface with real-time switching
- 💻 **GUI & CLI** - Easy-to-use graphical interface or command-line usage
- 📦 **Portable** - Can be built as standalone .exe for Windows
- ☕ **Support Developer** - Built-in donation links (Buy Me a Coffee & Bank Transfer)

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- ffmpeg (for audio/video conversion)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/AristarhUcolov/YouTube-Downloader.git
cd YouTube-Downloader
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Install ffmpeg** (if not already installed)
   - **Windows**: Download from [ffmpeg.org](https://ffmpeg.org/download.html) and add to PATH, or place `ffmpeg` folder in the project directory
   - **macOS**: `brew install ffmpeg`
   - **Linux**: `sudo apt install ffmpeg` (Debian/Ubuntu) or `sudo yum install ffmpeg` (CentOS/RHEL)

### Usage

> 📚 **Need more help?** Check out [EXAMPLES.md](EXAMPLES.md) for detailed usage examples and [FAQ.md](FAQ.md) for common questions.

#### GUI Mode (Default)
Simply run the script without arguments:
```bash
python yt_downloader.py
```

**New in v2.1.0:**
- ✅ **Clipboard Monitoring**: Enable the checkbox to auto-detect YouTube links when you copy them
- ✅ **Smart URLs**: When you paste a link with `&list=`, you'll be asked if you want just the video or the whole playlist
- ✅ **Quick Format Selection**: Choose MP3/MP4 directly in the clipboard detection dialog

#### Command Line Mode
```bash
# Download video as MP3
python yt_downloader.py "https://www.youtube.com/watch?v=VIDEO_ID" --format mp3

# Download video as MP4
python yt_downloader.py "https://www.youtube.com/watch?v=VIDEO_ID" --format mp4

# Download playlist with custom output folder
python yt_downloader.py "https://www.youtube.com/playlist?list=PLAYLIST_ID" -o my_music --format mp3

# Embed thumbnail
python yt_downloader.py "VIDEO_URL" --embed-thumbnail --format mp3
```

### Command Line Options

| Option | Description | Default |
|--------|-------------|---------|
| `url` | YouTube video or playlist URL | - |
| `-o, --outdir` | Output folder | `downloads` |
| `--format` | Output format: `mp3` or `mp4` | `mp3` |
| `--embed-thumbnail` | Embed thumbnail in MP3 files | `False` |
| `--lang` | UI language: `en` or `ru` | `en` |

## 🏗️ Building Standalone Executable (Windows)

Want to create a portable `.exe` file? Follow these steps:

1. **Ensure PyInstaller is installed**
```bash
pip install -r requirements.txt
```

2. **Run the build script**
```bash
build_exe.bat
```

3. **Find your executable**
The compiled `yt_downloader.exe` will be in the `dist/` folder.

**Note**: If you have a local `ffmpeg` folder in your project directory, it will be automatically included in the exe bundle.

For more details, see [BUILD_EXE.md](BUILD_EXE.md).

## 📁 Project Structure

```
youtube-downloader/
├── yt_downloader.py          # Main application
├── requirements.txt          # Python dependencies
├── build_exe.bat             # Windows build script
├── .gitignore                # Git ignore rules
│
├── 📚 Documentation
│   ├── README.md             # This file (EN/RU)
│   ├── CHANGELOG.md          # Version history
│   ├── FAQ.md                # Frequently asked questions
│   ├── EXAMPLES.md           # Usage examples
│   ├── BUILD_EXE.md          # Build instructions
│   ├── CONTRIBUTING.md       # Contribution guidelines
│   ├── LICENSE               # MIT License
│   └── PROJECT_STATUS.md     # Development roadmap
│
├── 🔧 GitHub
│   └── .github/
│       ├── ISSUE_TEMPLATE/
│       │   ├── bug_report.md
│       │   └── feature_request.md
│       └── PULL_REQUEST_TEMPLATE.md
│
├── 📦 Output
│   ├── downloads/            # Downloaded files
│   ├── dist/                 # Compiled .exe
│   └── build/                # Build artifacts
│
└── 🛠️ Dependencies
    └── ffmpeg/               # Optional: local ffmpeg
```

## 🛠️ Technologies Used

- **Python 3.8+** - Core programming language
- **tkinter** - GUI framework (built-in)
- **yt-dlp** - YouTube download engine
- **ffmpeg** - Audio/video processing
- **PyInstaller** - Executable bundling

## 🎯 New Features in v2.1.0

### 📋 Clipboard Monitoring

The app can now automatically detect YouTube links when you copy them:

1. **Enable the checkbox** "Auto-detect YouTube links" in the GUI
2. **Copy any YouTube link** from your browser (Ctrl+C)
3. **Popup appears automatically** asking if you want to download
4. **Choose format** (MP3 or MP4) in the popup
5. **Click Download** - done!

**Perfect for:** Quickly downloading multiple videos while browsing YouTube without switching windows.

### 🎯 Smart Playlist Detection

The app now intelligently handles links with playlist/radio parameters:

**Problem solved:** 
- Links like `https://www.youtube.com/watch?v=VIDEO_ID&list=RD...&start_radio=1` 
- Previously downloaded the entire radio/playlist instead of just the video

**How it works:**
1. Paste a link with `&list=` parameter
2. Dialog appears asking: "Single video only" or "Full playlist/radio"?
3. Choose what you want
4. The app automatically removes playlist parameters for single video downloads

**Examples:**
- YouTube Radio: `&list=RD...&start_radio=1`
- YouTube Mix: `&list=RDMM...`
- Regular playlist: `&list=PL...`
- Watch Later: `&list=WL`

## ❓ FAQ

### How do I download a playlist?
Just paste the playlist URL in the GUI or command line. The script automatically detects playlists and downloads all videos.

### Why is ffmpeg required?
ffmpeg is used to convert downloaded audio/video to the desired format (MP3/MP4) and to embed thumbnails.

### Can I download age-restricted or private videos?
This depends on yt-dlp's capabilities. Some restricted content may not be downloadable.

### Where are downloaded files saved?
By default, files are saved to the `downloads/` folder in the project directory. You can change this in the GUI or using the `-o` option.

## ⚖️ Legal Notice

**Important**: This tool is for personal use only. Downloading copyrighted content without permission is illegal in many jurisdictions. Only download videos that you have the right to download (e.g., your own content, Creative Commons licensed content, or content with explicit download permission from the creator).

The developers of this tool are not responsible for any misuse or legal consequences arising from using this software.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

For detailed guidelines, see [CONTRIBUTING.md](CONTRIBUTING.md).

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🌟 Support

If you found this project helpful, please give it a ⭐️!

### ☕ Buy Me a Coffee

If you'd like to support the development of this project, you can buy me a coffee:

[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20A%20Coffee-support-yellow?style=for-the-badge&logo=buy-me-a-coffee)](https://buymeacoffee.com/aristarh.ucolov)

**Direct link**: [buymeacoffee.com/aristarh.ucolov](https://buymeacoffee.com/aristarh.ucolov)

### 💳 Bank Transfer

You can also support via direct bank transfer:

```
Bank: Moldindconbank
Card Number: 4028 1202 1106 0963
Recipient: Aristarh Ucolov
```

## 📧 Contact

For questions or suggestions, please open an issue on GitHub.

---

**Made with ❤️ for the community**

**[⬆️ Back to top](#youtube-downloader)**

---

<a name="русский"></a>
## 🇷🇺 Русская версия

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

Простой и интуитивный загрузчик YouTube с поддержкой графического интерфейса. Скачивайте видео и плейлисты в формате MP3 (аудио) или MP4 (видео) с максимальным качеством.

### ✨ Возможности

- 🎵 **MP3 Аудио** - Извлечение аудио в формате MP3 320 kbps
- 🎬 **MP4 Видео** - Скачивание видео в лучшем доступном качестве
- 📋 **Поддержка плейлистов** - Загрузка целых плейлистов с автоматической нумерацией
- 🎯 **Умное определение плейлистов** - Автоматически определяет ссылки с плейлистом/радио и предлагает выбор
- 📎 **Мониторинг буфера обмена** - Автоопределение YouTube ссылок из буфера (опционально)
- 🖼️ **Встраивание обложек** - Опциональное встраивание обложек в MP3 файлы
- 🌐 **Мультиязычность** - Интерфейс на английском и русском языках с мгновенной сменой
- 💻 **GUI и CLI** - Удобный графический интерфейс или использование через командную строку
- 📦 **Портативность** - Возможность сборки в автономный .exe для Windows
- ☕ **Поддержка разработчика** - Встроенные ссылки на донат (Buy Me a Coffee и банковский перевод)

### 🚀 Быстрый старт

#### Требования

- Python 3.8 или выше
- ffmpeg (для конвертации аудио/видео)

#### Установка

1. **Клонируйте репозиторий**
```bash
git clone https://github.com/AristarhUcolov/YouTube-Downloader.git
cd YouTube-Downloader
```

2. **Установите зависимости**
```bash
pip install -r requirements.txt
```

3. **Установите ffmpeg** (если еще не установлен)
   - **Windows**: Скачайте с [ffmpeg.org](https://ffmpeg.org/download.html) и добавьте в PATH, или поместите папку `ffmpeg` в директорию проекта
   - **macOS**: `brew install ffmpeg`
   - **Linux**: `sudo apt install ffmpeg` (Debian/Ubuntu) или `sudo yum install ffmpeg` (CentOS/RHEL)

#### Использование

> 📚 **Нужна помощь?** Смотрите [EXAMPLES.md](EXAMPLES.md) для подробных примеров использования и [FAQ.md](FAQ.md) для ответов на частые вопросы.

##### Режим GUI (по умолчанию)
Просто запустите скрипт без аргументов:
```bash
python yt_downloader.py
```

**Новое в v2.1.0:**
- ✅ **Мониторинг буфера**: Включите чекбокс, чтобы автоматически определять YouTube ссылки при копировании
- ✅ **Умные URL**: Когда вставляете ссылку с `&list=`, программа спросит: только видео или весь плейлист
- ✅ **Быстрый выбор формата**: Выбирайте MP3/MP4 прямо в диалоге обнаружения ссылки

##### Режим командной строки
```bash
# Скачать видео как MP3
python yt_downloader.py "https://www.youtube.com/watch?v=VIDEO_ID" --format mp3

# Скачать видео как MP4
python yt_downloader.py "https://www.youtube.com/watch?v=VIDEO_ID" --format mp4

# Скачать плейлист с пользовательской папкой вывода
python yt_downloader.py "https://www.youtube.com/playlist?list=PLAYLIST_ID" -o моя_музыка --format mp3

# Встроить обложку
python yt_downloader.py "VIDEO_URL" --embed-thumbnail --format mp3

# Использовать русский язык в GUI
python yt_downloader.py --lang ru
```

#### Опции командной строки

| Опция | Описание | По умолчанию |
|-------|----------|--------------|
| `url` | URL видео или плейлиста YouTube | - |
| `-o, --outdir` | Папка для сохранения | `downloads` |
| `--format` | Формат вывода: `mp3` или `mp4` | `mp3` |
| `--embed-thumbnail` | Встроить обложку в MP3 файлы | `False` |
| `--lang` | Язык интерфейса: `en` или `ru` | `en` |

### 🏗️ Сборка автономного приложения (Windows)

Хотите создать портативный `.exe` файл? Выполните следующие шаги:

1. **Убедитесь, что PyInstaller установлен**
```bash
pip install -r requirements.txt
```

2. **Запустите скрипт сборки**
```bash
build_exe.bat
```

3. **Найдите ваш исполняемый файл**
Скомпилированный `yt_downloader.exe` будет находиться в папке `dist/`.

**Примечание**: Если у вас есть локальная папка `ffmpeg` в директории проекта, она будет автоматически включена в exe-файл.

Подробнее см. [BUILD_EXE.md](BUILD_EXE.md).

### 📁 Структура проекта

```
youtube-downloader/
├── yt_downloader.py          # Основное приложение
├── requirements.txt          # Зависимости Python
├── build_exe.bat             # Скрипт сборки для Windows
├── .gitignore                # Правила игнорирования Git
│
├── 📚 Документация
│   ├── README.md             # Этот файл (EN/RU)
│   ├── CHANGELOG.md          # История версий
│   ├── FAQ.md                # Частые вопросы
│   ├── EXAMPLES.md           # Примеры использования
│   ├── BUILD_EXE.md          # Инструкции по сборке
│   ├── CONTRIBUTING.md       # Руководство для контрибьюторов
│   ├── LICENSE               # Лицензия MIT
│   └── PROJECT_STATUS.md     # Дорожная карта разработки
│
├── 🔧 GitHub
│   └── .github/
│       ├── ISSUE_TEMPLATE/
│       │   ├── bug_report.md
│       │   └── feature_request.md
│       └── PULL_REQUEST_TEMPLATE.md
│
├── 📦 Выходные файлы
│   ├── downloads/            # Загруженные файлы
│   ├── dist/                 # Скомпилированный .exe
│   └── build/                # Артефакты сборки
│
└── 🛠️ Зависимости
    └── ffmpeg/               # Опционально: локальный ffmpeg
```

### 🛠️ Используемые технологии

- **Python 3.8+** - Основной язык программирования
- **tkinter** - Фреймворк GUI (встроенный)
- **yt-dlp** - Движок загрузки YouTube
- **ffmpeg** - Обработка аудио/видео
- **PyInstaller** - Создание исполняемых файлов

## 🎯 Новые возможности в v2.1.0

### 📋 Мониторинг буфера обмена

Программа теперь автоматически определяет YouTube ссылки при копировании:

1. **Включите чекбокс** "Автоопределение ссылок YouTube" в интерфейсе
2. **Скопируйте любую YouTube ссылку** из браузера (Ctrl+C)
3. **Появится всплывающее окно** с предложением скачать
4. **Выберите формат** (MP3 или MP4) во всплывающем окне
5. **Нажмите Скачать** - готово!

**Идеально для:** Быстрой загрузки нескольких видео во время просмотра YouTube без переключения окон.

### 🎯 Умное определение плейлистов

Программа теперь интеллектуально обрабатывает ссылки с параметрами плейлиста/радио:

**Решённая проблема:** 
- Ссылки типа `https://www.youtube.com/watch?v=VIDEO_ID&list=RD...&start_radio=1` 
- Раньше скачивался весь радио/плейлист вместо одного видео

**Как работает:**
1. Вставьте ссылку с параметром `&list=`
2. Появится диалог: "Только это видео" или "Весь плейлист/радио"?
3. Выберите нужное
4. Программа автоматически удалит параметры плейлиста для скачивания одного видео

**Примеры:**
- YouTube Радио: `&list=RD...&start_radio=1`
- YouTube Микс: `&list=RDMM...`
- Обычный плейлист: `&list=PL...`
- Смотреть позже: `&list=WL`
### ❓ Часто задаваемые вопросы

#### Как скачать плейлист?
Просто вставьте URL плейлиста в GUI или командную строку. Скрипт автоматически определяет плейлисты и загружает все видео.

#### Зачем нужен ffmpeg?
ffmpeg используется для конвертации загруженного аудио/видео в желаемый формат (MP3/MP4) и для встраивания обложек.

#### Можно ли скачать видео с возрастным ограничением или приватные видео?
Это зависит от возможностей yt-dlp. Некоторый ограниченный контент может быть недоступен для загрузки.

#### Куда сохраняются загруженные файлы?
По умолчанию файлы сохраняются в папку `downloads/` в директории проекта. Вы можете изменить это в GUI или используя опцию `-o`.

### ⚖️ Юридическое уведомление

**Важно**: Этот инструмент предназначен только для личного использования. Загрузка контента, защищенного авторским правом, без разрешения является незаконной во многих юрисдикциях. Загружайте только те видео, на которые у вас есть права (например, ваш собственный контент, контент под лицензией Creative Commons или контент с явным разрешением на загрузку от создателя).

Разработчики этого инструмента не несут ответственности за любое неправомерное использование или юридические последствия, возникающие в результате использования этого программного обеспечения.

### 🤝 Участие в разработке

Приветствуются любые вклады! Пожалуйста, не стесняйтесь отправлять Pull Request.

1. Сделайте Fork проекта
2. Создайте ветку для вашей функции (`git checkout -b feature/AmazingFeature`)
3. Зафиксируйте ваши изменения (`git commit -m 'Add some AmazingFeature'`)
4. Отправьте в ветку (`git push origin feature/AmazingFeature`)
5. Откройте Pull Request

Подробные инструкции смотрите в [CONTRIBUTING.md](CONTRIBUTING.md).

### 📝 Лицензия

Этот проект лицензирован под лицензией MIT - см. файл [LICENSE](LICENSE) для подробностей.

### 🌟 Поддержка

Если вам помог этот проект, пожалуйста, поставьте ⭐️!

#### ☕ Угостить кофе

Если вы хотите поддержать разработку этого проекта, можете угостить меня кофе:

[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20A%20Coffee-%D0%BF%D0%BE%D0%B4%D0%B4%D0%B5%D1%80%D0%B6%D0%B0%D1%82%D1%8C-yellow?style=for-the-badge&logo=buy-me-a-coffee)](https://buymeacoffee.com/aristarh.ucolov)

**Прямая ссылка**: [buymeacoffee.com/aristarh.ucolov](https://buymeacoffee.com/aristarh.ucolov)

#### 💳 Банковский перевод

Также можете поддержать через банковский перевод:

```
Банк: Moldindconbank
Номер карты: 4028 1202 1106 0963
Получатель: Aristarh Ucolov
```

### 📧 Контакты

По вопросам или предложениям, пожалуйста, откройте issue на GitHub.

---

**Сделано с ❤️ для сообщества**

**[⬆️ Вернуться наверх](#youtube-downloader)** | **[Switch to English](#english)**
