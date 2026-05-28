# Frequently Asked Questions (FAQ)

**[English](#english)** | **[Русский](#русский)**

---

<a name="english"></a>
## 🇬🇧 English Version

# Frequently Asked Questions (FAQ)

## 📋 General Questions

### What is YouTube Downloader?

YouTube Downloader is a desktop application that allows you to download videos and audio from YouTube in MP3 or MP4 format. It features a user-friendly GUI with bilingual support (English/Russian), clipboard monitoring, and smart playlist detection.

### Is it legal to download YouTube videos?

Downloading YouTube videos may violate YouTube's Terms of Service. This tool is provided for educational purposes and personal use only. Users are responsible for ensuring their usage complies with local laws and YouTube's policies.

### Is it free?

Yes, the software is completely free and open-source. However, if you find it useful, you can [support the developer](https://buymeacoffee.com/aristarh.ucolov).

---

## 💻 Installation & Setup

### What do I need to run this?

**Required:**
- Windows (7/10/11), macOS, or Linux
- Python 3.8 or higher (for source version)
- Internet connection

**Optional:**
- ffmpeg (for audio conversion) - auto-included in .exe version

### How do I install Python dependencies?

```bash
pip install -r requirements.txt
```

Or manually:
```bash
pip install yt-dlp
```

### Do I need ffmpeg?

Yes, ffmpeg is required for audio extraction (MP3). Options:
1. **Bundled**: Use the .exe version (ffmpeg included)
2. **Manual**: Download from https://ffmpeg.org and add to PATH
3. **Local**: Place `ffmpeg.exe` in `ffmpeg/` folder in project directory

### How do I create an .exe file?

Follow instructions in [BUILD_EXE.md](BUILD_EXE.md):
```bash
pip install pyinstaller
python -m PyInstaller --onefile --noconsole --add-data "ffmpeg;ffmpeg" yt_downloader.py
```

---

## 🎯 Features & Usage

### How does clipboard monitoring work?

1. Enable the "Auto-detect YouTube links" checkbox
2. The app monitors your clipboard every second
3. When you copy a YouTube URL, a popup appears
4. Choose format (MP3/MP4) and click Download
5. The URL is remembered to avoid duplicate popups

### What is smart playlist detection?

When you copy a YouTube link like:
```
https://www.youtube.com/watch?v=VIDEO_ID&list=PLAYLIST_ID
```

The app detects the `&list=` parameter and asks:
- Download single video only?
- Download full playlist/radio?

This prevents accidentally downloading 50+ videos from a YouTube Radio or Mix.

### Can I switch languages?

Yes! Click the **EN/RU** button in the top-right corner of the GUI. The interface immediately switches between English and Russian.

### Can I download playlists?

Yes! Simply paste the playlist URL:
```
https://www.youtube.com/playlist?list=PLAYLIST_ID
```

All videos will be downloaded and numbered: `001 - Title.mp3`, `002 - Title.mp3`, etc.

### What quality do downloads have?

- **MP3**: 320 kbps (highest quality audio)
- **MP4**: Best available video quality (up to 1080p/4K depending on source)

### Where are files saved?

Default location: `downloads/` folder in the project directory.

You can specify a custom folder:
- GUI: Enter path in "Output folder" field
- CLI: Use `-o "path/to/folder"`

---

## 🐛 Troubleshooting

### "yt-dlp not found" error

**Solution:**
```bash
pip install --upgrade yt-dlp
```

Or install manually from: https://github.com/yt-dlp/yt-dlp

### "ffmpeg not found" error

**Solutions:**
1. Use the .exe version (ffmpeg bundled)
2. Download ffmpeg from https://ffmpeg.org
3. Add ffmpeg to system PATH
4. Place `ffmpeg.exe` in `ffmpeg/` folder

### Downloads are very slow

**Possible causes:**
- Slow internet connection
- YouTube throttling (common for large files)
- Peak hours (try downloading at night)

**Solutions:**
- Check your internet speed
- Wait and retry later
- Use VPN if region-throttled

### Clipboard monitoring doesn't work

**Checklist:**
- ✅ Is the checkbox enabled?
- ✅ Did you copy a valid YouTube URL?
- ✅ Is the application running?
- ✅ Try closing and restarting

**Common issue:** If you copy the same URL twice, the popup won't appear again (by design).

### "HTTP Error 429: Too Many Requests"

**Cause:** YouTube is rate-limiting your IP address.

**Solutions:**
- Wait 15-30 minutes before trying again
- Use a VPN to change your IP
- Reduce download frequency

### Video is age-restricted

**Solution:** Some age-restricted videos cannot be downloaded without authentication. Consider:
- Using YouTube Premium
- Checking if video is available in your region

### Playlist download stops after a few videos

**Possible causes:**
- Network interruption
- yt-dlp rate limiting
- Individual video errors

**Solution:**
- Check terminal/log output for specific errors
- Resume by re-running (yt-dlp skips existing files)
- Use `--ignore-errors` flag in CLI mode

### GUI doesn't open

**Possible causes:**
- Tkinter not installed
- Python version too old

**Solutions:**
```bash
# Check Python version
python --version  # Should be 3.8+

# Install tkinter (Linux)
sudo apt-get install python3-tk

# Reinstall Python (Windows)
# Download from python.org and check "tcl/tk" during installation
```

### Button stays disabled after download

This was fixed in v2.1.0. Update to the latest version:
```bash
git pull
```

Or download the latest .exe.

---

## ⚙️ Advanced Usage

### Can I use this in my own project?

Yes! This project is MIT licensed. You can:
- Use the code in your projects
- Modify and distribute
- Include in commercial software

Just maintain the original license notice.

### How do I contribute?

Contributions are welcome! To contribute:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

See [Contributing Guidelines](#) for details.

### Can I run this on a server?

Yes, you can use the CLI version:
```bash
python yt_downloader.py "VIDEO_URL" --format mp3 -o "/var/www/downloads"
```

However, clipboard monitoring requires a GUI environment (X11/Wayland).

### Can I change the default quality?

Currently, the app uses best available quality. To customize:

1. Edit `yt_downloader.py`
2. Find the `yt_opts` dictionary
3. Add format selection:
```python
'format': 'bestvideo[height<=720]+bestaudio/best[height<=720]'  # Max 720p
```

### How do I download subtitles?

Currently not supported in GUI. For CLI, modify the script to add:
```python
'writesubtitles': True,
'subtitleslangs': ['en', 'ru']
```

### Can I schedule downloads?

Use Windows Task Scheduler or cron (Linux/Mac) with CLI mode:
```bash
# Windows Task Scheduler
python yt_downloader.py "URL" --format mp3

# Linux cron (daily at 2 AM)
0 2 * * * /usr/bin/python3 /path/to/yt_downloader.py "URL"
```

---

## 🔒 Privacy & Security

### Does this send my data anywhere?

No. The application:
- ✅ Runs entirely on your local machine
- ✅ Connects only to YouTube servers
- ✅ Does not collect or transmit user data
- ✅ No telemetry or analytics

### Is my clipboard data safe?

Yes. Clipboard monitoring:
- Only activates when the checkbox is enabled
- Only reads clipboard content (doesn't modify it)
- Only processes YouTube URLs (ignores other content)
- Doesn't store clipboard history

### Can I use this offline?

No, an internet connection is required to:
- Fetch video/audio streams from YouTube
- Download metadata

However, once downloaded, files can be played offline.

---

## 💝 Support & Donation

### How can I support the developer?

If you find this software useful:

☕ **Buy Me a Coffee**: https://buymeacoffee.com/aristarh.ucolov

💜 **DonationAlerts**: https://www.donationalerts.com/r/aristarh_ucolov

### I found a bug. Where do I report it?

Please open an issue on GitHub with:
- Detailed description
- Steps to reproduce
- Python version
- OS version
- Error messages (if any)

### I have a feature request

Great! Open a GitHub issue with:
- Feature description
- Use case
- Proposed implementation (optional)

---

## 📚 Additional Resources

- **[README.md](README.md)** - Main documentation
- **[CHANGELOG.md](CHANGELOG.md)** - Version history
- **[EXAMPLES.md](EXAMPLES.md)** - Usage examples
- **[BUILD_EXE.md](BUILD_EXE.md)** - Build instructions
- **[GitHub Repository](#)** - Source code

---

## 🌐 Language Support

### Can I add my language?

Yes! To add a new language:

1. Edit `yt_downloader.py`
2. Find the `TRANSLATIONS` dictionary
3. Add your language:
```python
TRANSLATIONS = {
    'en': { 'title': 'YouTube Downloader', ... },
    'ru': { 'title': 'YouTube Загрузчик', ... },
    'es': { 'title': 'Descargador de YouTube', ... }  # Your language
}
```
4. Update language switch button logic
5. Submit a pull request!

### Why only English and Russian?

The developer is fluent in both languages. Additional languages are welcome via community contributions!

---

<a name="русский"></a>
## 🇷🇺 Русская версия

# Часто задаваемые вопросы (FAQ)

## 📋 Общие вопросы

### Что такое YouTube Downloader?

YouTube Downloader - это настольное приложение, которое позволяет загружать видео и аудио с YouTube в форматах MP3 или MP4. Оно имеет удобный графический интерфейс с двуязычной поддержкой (английский/русский), мониторингом буфера обмена и умным определением плейлистов.

### Законно ли скачивать видео с YouTube?

Загрузка видео с YouTube может нарушать Условия использования YouTube. Этот инструмент предоставляется только в образовательных целях и для личного использования. Пользователи несут ответственность за соблюдение местных законов и политики YouTube.

### Это бесплатно?

Да, программное обеспечение полностью бесплатное и с открытым исходным кодом. Однако, если вы найдете его полезным, вы можете [поддержать разработчика](https://buymeacoffee.com/aristarh.ucolov).

---

## 💻 Установка и настройка

### Что мне нужно для запуска?

**Требуется:**
- Windows (7/10/11), macOS или Linux
- Python 3.8 или выше (для версии с исходным кодом)
- Интернет-соединение

**Опционально:**
- ffmpeg (для конвертации аудио) - автоматически включен в .exe версию

### Как установить зависимости Python?

```bash
pip install -r requirements.txt
```

Или вручную:
```bash
pip install yt-dlp
```

### Нужен ли мне ffmpeg?

Да, ffmpeg требуется для извлечения аудио (MP3). Варианты:
1. **В комплекте**: Используйте .exe версию (ffmpeg включен)
2. **Вручную**: Скачайте с https://ffmpeg.org и добавьте в PATH
3. **Локально**: Поместите `ffmpeg.exe` в папку `ffmpeg/` в директории проекта

### Как создать .exe файл?

Следуйте инструкциям в [BUILD_EXE.md](BUILD_EXE.md):
```bash
pip install pyinstaller
python -m PyInstaller --onefile --noconsole --add-data "ffmpeg;ffmpeg" yt_downloader.py
```

---

## 🎯 Функции и использование

### Как работает мониторинг буфера обмена?

1. Включите чекбокс "Автоопределение YouTube ссылок"
2. Приложение проверяет буфер обмена каждую секунду
3. Когда вы копируете URL YouTube, появляется всплывающее окно
4. Выберите формат (MP3/MP4) и нажмите Загрузить
5. URL запоминается, чтобы избежать повторных всплывающих окон

### Что такое умное определение плейлистов?

Когда вы копируете ссылку YouTube вроде:
```
https://www.youtube.com/watch?v=VIDEO_ID&list=PLAYLIST_ID
```

Приложение определяет параметр `&list=` и спрашивает:
- Загрузить только одно видео?
- Загрузить весь плейлист/радио?

Это предотвращает случайную загрузку 50+ видео из YouTube Radio или Mix.

### Могу ли я переключать языки?

Да! Нажмите кнопку **EN/RU** в правом верхнем углу GUI. Интерфейс немедленно переключится между английским и русским.

### Могу ли я скачивать плейлисты?

Да! Просто вставьте URL плейлиста:
```
https://www.youtube.com/playlist?list=PLAYLIST_ID
```

Все видео будут загружены и пронумерованы: `001 - Название.mp3`, `002 - Название.mp3` и т.д.

### Какое качество у загрузок?

- **MP3**: 320 kbps (максимальное качество аудио)
- **MP4**: Лучшее доступное качество видео (до 1080p/4K в зависимости от источника)

### Куда сохраняются файлы?

Местоположение по умолчанию: папка `downloads/` в директории проекта.

Вы можете указать свою папку:
- GUI: Введите путь в поле "Папка вывода"
- CLI: Используйте `-o "путь/к/папке"`

---

## 🐛 Устранение неполадок

### Ошибка "yt-dlp not found"

**Решение:**
```bash
pip install --upgrade yt-dlp
```

Или установите вручную с: https://github.com/yt-dlp/yt-dlp

### Ошибка "ffmpeg not found"

**Решения:**
1. Используйте .exe версию (ffmpeg в комплекте)
2. Скачайте ffmpeg с https://ffmpeg.org
3. Добавьте ffmpeg в системный PATH
4. Поместите `ffmpeg.exe` в папку `ffmpeg/`

### Загрузки очень медленные

**Возможные причины:**
- Медленное интернет-соединение
- Ограничение YouTube (часто для больших файлов)
- Пиковые часы (попробуйте загружать ночью)

**Решения:**
- Проверьте скорость интернета
- Подождите и повторите попытку позже
- Используйте VPN, если есть региональное ограничение

### Мониторинг буфера не работает

**Чеклист:**
- ✅ Включен ли чекбокс?
- ✅ Скопировали ли вы действительный URL YouTube?
- ✅ Запущено ли приложение?
- ✅ Попробуйте закрыть и перезапустить

**Частая проблема:** Если вы копируете один и тот же URL дважды, всплывающее окно не появится снова (это задумано).

### "HTTP Error 429: Too Many Requests"

**Причина:** YouTube ограничивает ваш IP-адрес.

**Решения:**
- Подождите 15-30 минут перед повторной попыткой
- Используйте VPN для смены IP
- Уменьшите частоту загрузок

### Видео с возрастным ограничением

**Решение:** Некоторые видео с возрастным ограничением нельзя загрузить без аутентификации. Рассмотрите:
- Использование YouTube Premium
- Проверьте, доступно ли видео в вашем регионе

### Загрузка плейлиста останавливается после нескольких видео

**Возможные причины:**
- Прерывание сети
- Ограничение yt-dlp
- Ошибки отдельных видео

**Решение:**
- Проверьте вывод терминала/лога на конкретные ошибки
- Возобновите, запустив снова (yt-dlp пропускает существующие файлы)
- Используйте флаг `--ignore-errors` в CLI режиме

### GUI не открывается

**Возможные причины:**
- Tkinter не установлен
- Слишком старая версия Python

**Решения:**
```bash
# Проверьте версию Python
python --version  # Должна быть 3.8+

# Установите tkinter (Linux)
sudo apt-get install python3-tk

# Переустановите Python (Windows)
# Скачайте с python.org и отметьте "tcl/tk" при установке
```

### Кнопка остается неактивной после загрузки

Это было исправлено в v2.1.0. Обновитесь до последней версии:
```bash
git pull
```

Или скачайте последний .exe.

---

## ⚙️ Продвинутое использование

### Могу ли я использовать это в своем проекте?

Да! Этот проект лицензирован по MIT. Вы можете:
- Использовать код в своих проектах
- Изменять и распространять
- Включать в коммерческое ПО

Просто сохраните оригинальное уведомление о лицензии.

### Как я могу внести вклад?

Вклады приветствуются! Чтобы внести вклад:
1. Сделайте Fork репозитория
2. Создайте ветку функции
3. Внесите изменения
4. Отправьте pull request

См. [Руководство по вкладу](CONTRIBUTING.md) для подробностей.

### Могу ли я запустить это на сервере?

Да, вы можете использовать CLI версию:
```bash
python yt_downloader.py "VIDEO_URL" --format mp3 -o "/var/www/downloads"
```

Однако мониторинг буфера обмена требует GUI окружения (X11/Wayland).

### Могу ли я изменить качество по умолчанию?

В настоящее время приложение использует лучшее доступное качество. Для настройки:

1. Отредактируйте `yt_downloader.py`
2. Найдите словарь `yt_opts`
3. Добавьте выбор формата:
```python
'format': 'bestvideo[height<=720]+bestaudio/best[height<=720]'  # Макс 720p
```

### Как загрузить субтитры?

В настоящее время не поддерживается в GUI. Для CLI измените скрипт, добавив:
```python
'writesubtitles': True,
'subtitleslangs': ['en', 'ru']
```

### Могу ли я запланировать загрузки?

Используйте Планировщик задач Windows или cron (Linux/Mac) с CLI режимом:
```bash
# Планировщик задач Windows
python yt_downloader.py "URL" --format mp3

# Linux cron (ежедневно в 2 ночи)
0 2 * * * /usr/bin/python3 /path/to/yt_downloader.py "URL"
```

---

## 🔒 Конфиденциальность и безопасность

### Отправляет ли это мои данные куда-либо?

Нет. Приложение:
- ✅ Работает полностью на вашей локальной машине
- ✅ Подключается только к серверам YouTube
- ✅ Не собирает и не передает пользовательские данные
- ✅ Нет телеметрии или аналитики

### Безопасны ли данные моего буфера обмена?

Да. Мониторинг буфера обмена:
- Активируется только при включенном чекбоксе
- Только читает содержимое буфера (не изменяет его)
- Обрабатывает только URL YouTube (игнорирует другое содержимое)
- Не хранит историю буфера

### Могу ли я использовать это офлайн?

Нет, требуется интернет-соединение для:
- Получения видео/аудио потоков с YouTube
- Загрузки метаданных

Однако после загрузки файлы можно воспроизводить офлайн.

---

## 💝 Поддержка и донаты

### Как я могу поддержать разработчика?

Если вы нашли это программное обеспечение полезным:

☕ **Угостить кофе**: https://buymeacoffee.com/aristarh.ucolov

💜 **DonationAlerts**: https://www.donationalerts.com/r/aristarh_ucolov

### Я нашел баг. Где сообщить об этом?

Пожалуйста, откройте issue на GitHub с:
- Подробным описанием
- Шагами для воспроизведения
- Версией Python
- Версией ОС
- Сообщениями об ошибках (если есть)

### У меня есть запрос на функцию

Отлично! Откройте GitHub issue с:
- Описанием функции
- Вариантом использования
- Предлагаемой реализацией (опционально)

---

## 📚 Дополнительные ресурсы

- **[README.md](README.md)** - Основная документация
- **[CHANGELOG.md](CHANGELOG.md)** - История версий
- **[EXAMPLES.md](EXAMPLES.md)** - Примеры использования
- **[BUILD_EXE.md](BUILD_EXE.md)** - Инструкции по сборке
- **[GitHub Repository](#)** - Исходный код

---

## 🌐 Языковая поддержка

### Могу ли я добавить свой язык?

Да! Чтобы добавить новый язык:

1. Отредактируйте `yt_downloader.py`
2. Найдите словарь `TRANSLATIONS`
3. Добавьте ваш язык:
```python
TRANSLATIONS = {
    'en': { 'title': 'YouTube Downloader', ... },
    'ru': { 'title': 'YouTube Загрузчик', ... },
    'es': { 'title': 'Descargador de YouTube', ... }  # Ваш язык
}
```
4. Обновите логику кнопки переключения языка
5. Отправьте pull request!

### Почему только английский и русский?

Разработчик свободно владеет обоими языками. Дополнительные языки приветствуются через вклады сообщества!

---

**Last Updated:** v2.1.0 (February 2026)

**[⬆️ Back to README](README.md)**
