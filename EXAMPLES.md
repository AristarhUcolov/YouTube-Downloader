# YouTube Downloader - Usage Examples

**[English](#english)** | **[Русский](#русский)**

---

<a name="english"></a>
## 🇬🇧 English Version

# Usage Examples

## 📋 Table of Contents

- [GUI Examples](#gui-examples)
- [Command Line Examples](#command-line-examples)
- [Advanced Usage](#advanced-usage)
- [Troubleshooting](#troubleshooting)

---

## GUI Examples

### Basic Usage

1. **Single Video Download (MP3)**
   - Launch: `python yt_downloader.py`
   - Paste URL: `https://www.youtube.com/watch?v=dQw4w9WgXcQ`
   - Select format: MP3
   - Click Download

2. **Playlist Download (MP4)**
   - Paste playlist URL
   - Select format: MP4
   - Click Download
   - All videos will be saved with numbering

### New Features (v2.1.0)

#### Clipboard Monitoring

**Scenario:** You're browsing YouTube and want to download several videos quickly

1. Enable "Auto-detect YouTube links" checkbox
2. Go to YouTube, find a video
3. Press Ctrl+C on the video URL
4. Popup appears automatically
5. Choose MP3 or MP4
6. Click Download
7. Repeat for other videos!

**Benefits:**
- No need to switch windows
- No manual pasting
- Choose format on-the-fly

#### Smart Playlist Detection

**Scenario 1:** YouTube Radio Link
```
https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=RDdQw4w9WgXcQ&start_radio=1
```
- Paste this URL
- Dialog appears: "Single video only" or "Full playlist/radio"
- Choose "Single video only"
- Downloads only `dQw4w9WgXcQ`

**Scenario 2:** YouTube Mix
```
https://www.youtube.com/watch?v=VIDEO_ID&list=RDMM...
```
- Same dialog appears
- Choose what you need

---

## Command Line Examples

### Basic Downloads

```bash
# Single video as MP3
python yt_downloader.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# Single video as MP4
python yt_downloader.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ" --format mp4

# Playlist as MP3
python yt_downloader.py "https://www.youtube.com/playlist?list=PLrAXtmErZgOeiKm4sgNOknGvNjby9efdf" --format mp3
```

### Custom Output Directory

```bash
# Save to specific folder
python yt_downloader.py "VIDEO_URL" -o "D:\My Music"

# Save to subfolder
python yt_downloader.py "PLAYLIST_URL" -o "downloads/my_collection" --format mp3
```

### With Thumbnail Embedding

```bash
# MP3 with embedded album art
python yt_downloader.py "VIDEO_URL" --format mp3 --embed-thumbnail

# Playlist with thumbnails
python yt_downloader.py "PLAYLIST_URL" -o "music" --format mp3 --embed-thumbnail
```

### Using Russian Interface

```bash
# Launch GUI in Russian
python yt_downloader.py --lang ru

# CLI with Russian messages
python yt_downloader.py "VIDEO_URL" --lang ru
```

---

## Advanced Usage

### Batch Processing Script

Create a file `download_list.txt`:
```
https://www.youtube.com/watch?v=VIDEO_ID_1
https://www.youtube.com/watch?v=VIDEO_ID_2
https://www.youtube.com/watch?v=VIDEO_ID_3
```

Then run:
```bash
# Windows
for /F "tokens=*" %i in (download_list.txt) do python yt_downloader.py "%i" --format mp3

# Linux/Mac
while read url; do python yt_downloader.py "$url" --format mp3; done < download_list.txt
```

### Download Entire Channel Uploads

```bash
# Get channel uploads playlist URL
python yt_downloader.py "https://www.youtube.com/channel/CHANNEL_ID/videos" -o "channel_backup"
```

### Quality Selection

The script automatically selects best quality. For MP3, audio is extracted at 320kbps. For MP4, video is downloaded in highest available quality.

---

## Troubleshooting

### Issue: "yt-dlp not found"

**Solution:**
```bash
pip install -U yt-dlp
```

### Issue: "ffmpeg not found"

**Solutions:**

1. **Add to PATH** (Recommended)
   - Download from https://ffmpeg.org
   - Add to system PATH

2. **Local Installation**
   - Create `ffmpeg/` folder in project directory
   - Place `ffmpeg.exe` inside
   - Script will auto-detect it

### Issue: "Age-restricted video"

**Solution:** Some videos require authentication. Consider:
- Using official YouTube methods
- Check if video is available in your region

### Issue: Slow downloads

**Tips:**
- Check your internet connection
- YouTube may throttle download speeds
- Consider downloading during off-peak hours

### Issue: Clipboard monitoring not working

**Possible causes:**
1. Checkbox not enabled
2. Clipboard contains non-YouTube link
3. TclError (clipboard unavailable)

**Solution:**
- Ensure checkbox is checked
- Try copying URL again
- Restart application if persistent

---

## Tips & Tricks

### 1. Quick Format Switching
- Use radio buttons to switch between MP3/MP4
- Settings are remembered during session

### 2. Organized Downloads
```bash
# Music by genre
python yt_downloader.py "PLAYLIST_URL" -o "music/rock" --format mp3
python yt_downloader.py "PLAYLIST_URL" -o "music/jazz" --format mp3

# Videos by category
python yt_downloader.py "PLAYLIST_URL" -o "videos/tutorials" --format mp4
```

### 3. Playlist Numbering
- Files are automatically numbered: `001 - Title.mp3`, `002 - Title.mp3`
- Maintains playlist order

### 4. Keyboard Shortcuts (GUI)
- `Ctrl+C` in browser → Auto-detect (if enabled)
- `Alt+F4` → Close application
- `Tab` → Navigate between fields

### 5. Using with Browser Extensions
- Copy YouTube link with browser extension
- If clipboard monitoring is enabled, instant popup!

---

## Real-World Workflows

### Workflow 1: Music Collection
1. Find music playlist on YouTube
2. Enable clipboard monitoring
3. Copy playlist URL
4. Choose MP3 in popup
5. Choose "Full playlist"
6. Wait for download
7. Enjoy your music!

### Workflow 2: Video Archiving
1. Launch GUI (Russian interface if preferred)
2. Paste channel URL
3. Select MP4 format
4. Choose output folder
5. Start download
6. All videos saved with metadata

### Workflow 3: Quick Single Downloads
1. Browse YouTube
2. See interesting video
3. Copy URL (Ctrl+C)
4. Popup appears (if monitoring enabled)
5. Click Download
6. Done in seconds!

---

**[⬆️ Back to README](README.md)**

---

<a name="русский"></a>
## 🇷🇺 Русская версия

# Примеры использования

## 📋 Содержание

- [Примеры GUI](#примеры-gui)
- [Примеры командной строки](#примеры-командной-строки)
- [Продвинутое использование](#продвинутое-использование)
- [Устранение неполадок](#устранение-неполадок)

---

## Примеры GUI

### Базовое использование

1. **Загрузка одного видео (MP3)**
   - Запустите: `python yt_downloader.py`
   - Вставьте URL: `https://www.youtube.com/watch?v=dQw4w9WgXcQ`
   - Выберите формат: MP3
   - Нажмите Загрузить

2. **Загрузка плейлиста (MP4)**
   - Вставьте URL плейлиста
   - Выберите формат: MP4
   - Нажмите Загрузить
   - Все видео будут сохранены с нумерацией

### Новые функции (v2.1.0)

#### Мониторинг буфера обмена

**Сценарий:** Вы просматриваете YouTube и хотите быстро скачать несколько видео

1. Включите чекбокс "Автоопределение YouTube ссылок"
2. Перейдите на YouTube, найдите видео
3. Нажмите Ctrl+C на URL видео
4. Всплывающее окно появится автоматически
5. Выберите MP3 или MP4
6. Нажмите Загрузить
7. Повторите для других видео!

**Преимущества:**
- Не нужно переключать окна
- Не нужно вручную вставлять
- Выбирайте формат на лету

#### Умное определение плейлистов

**Сценарий 1:** Ссылка YouTube Radio
```
https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=RDdQw4w9WgXcQ&start_radio=1
```
- Вставьте этот URL
- Появится диалог: "Только одно видео" или "Полный плейлист/радио"
- Выберите "Только одно видео"
- Загрузится только `dQw4w9WgXcQ`

**Сценарий 2:** YouTube Mix
```
https://www.youtube.com/watch?v=VIDEO_ID&list=RDMM...
```
- Появится тот же диалог
- Выберите что нужно

---

## Примеры командной строки

### Базовые загрузки

```bash
# Одно видео как MP3
python yt_downloader.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# Одно видео как MP4
python yt_downloader.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ" --format mp4

# Плейлист как MP3
python yt_downloader.py "https://www.youtube.com/playlist?list=PLrAXtmErZgOeiKm4sgNOknGvNjby9efdf" --format mp3
```

### Пользовательская папка вывода

```bash
# Сохранить в определенную папку
python yt_downloader.py "VIDEO_URL" -o "D:\Моя Музыка"

# Сохранить в подпапку
python yt_downloader.py "PLAYLIST_URL" -o "downloads/моя_коллекция" --format mp3
```

### Со встраиванием обложки

```bash
# MP3 со встроенной обложкой альбома
python yt_downloader.py "VIDEO_URL" --format mp3 --embed-thumbnail

# Плейлист с обложками
python yt_downloader.py "PLAYLIST_URL" -o "music" --format mp3 --embed-thumbnail
```

### Использование русского интерфейса

```bash
# Запустить GUI на русском
python yt_downloader.py --lang ru

# CLI с русскими сообщениями
python yt_downloader.py "VIDEO_URL" --lang ru
```

---

## Продвинутое использование

### Скрипт пакетной обработки

Создайте файл `download_list.txt`:
```
https://www.youtube.com/watch?v=VIDEO_ID_1
https://www.youtube.com/watch?v=VIDEO_ID_2
https://www.youtube.com/watch?v=VIDEO_ID_3
```

Затем запустите:
```bash
# Windows
for /F "tokens=*" %i in (download_list.txt) do python yt_downloader.py "%i" --format mp3

# Linux/Mac
while read url; do python yt_downloader.py "$url" --format mp3; done < download_list.txt
```

### Загрузка всех видео канала

```bash
# Получите URL плейлиста загрузок канала
python yt_downloader.py "https://www.youtube.com/channel/CHANNEL_ID/videos" -o "резервная_копия_канала"
```

### Выбор качества

Скрипт автоматически выбирает лучшее качество. Для MP3 аудио извлекается в 320kbps. Для MP4 видео загружается в наивысшем доступном качестве.

---

## Устранение неполадок

### Проблема: "yt-dlp not found"

**Решение:**
```bash
pip install -U yt-dlp
```

### Проблема: "ffmpeg not found"

**Решения:**

1. **Добавить в PATH** (Рекомендуется)
   - Скачайте с https://ffmpeg.org
   - Добавьте в системный PATH

2. **Локальная установка**
   - Создайте папку `ffmpeg/` в директории проекта
   - Поместите `ffmpeg.exe` внутрь
   - Скрипт автоматически обнаружит его

### Проблема: "Age-restricted video"

**Решение:** Некоторые видео требуют аутентификации. Рассмотрите:
- Использование официальных методов YouTube
- Проверьте, доступно ли видео в вашем регионе

### Проблема: Медленные загрузки

**Советы:**
- Проверьте интернет-соединение
- YouTube может ограничивать скорость загрузки
- Рассмотрите загрузку в непиковые часы

### Проблема: Мониторинг буфера не работает

**Возможные причины:**
1. Чекбокс не включен
2. Буфер содержит не-YouTube ссылку
3. TclError (буфер недоступен)

**Решение:**
- Убедитесь, что чекбокс отмечен
- Попробуйте скопировать URL снова
- Перезапустите приложение, если проблема сохраняется

---

## Советы и трюки

### 1. Быстрое переключение формата
- Используйте радиокнопки для переключения между MP3/MP4
- Настройки запоминаются во время сеанса

### 2. Организованные загрузки
```bash
# Музыка по жанрам
python yt_downloader.py "PLAYLIST_URL" -o "музыка/рок" --format mp3
python yt_downloader.py "PLAYLIST_URL" -o "музыка/джаз" --format mp3

# Видео по категориям
python yt_downloader.py "PLAYLIST_URL" -o "видео/уроки" --format mp4
```

### 3. Нумерация плейлистов
- Файлы автоматически нумеруются: `001 - Название.mp3`, `002 - Название.mp3`
- Сохраняет порядок плейлиста

### 4. Клавиатурные сочетания (GUI)
- `Ctrl+C` в браузере → Автоопределение (если включено)
- `Alt+F4` → Закрыть приложение
- `Tab` → Навигация между полями

### 5. Использование с расширениями браузера
- Копируйте ссылку YouTube с расширением браузера
- Если мониторинг буфера включен, мгновенное всплывающее окно!

---

## Реальные рабочие процессы

### Рабочий процесс 1: Музыкальная коллекция
1. Найдите музыкальный плейлист на YouTube
2. Включите мониторинг буфера
3. Скопируйте URL плейлиста
4. Выберите MP3 во всплывающем окне
5. Выберите "Полный плейлист"
6. Дождитесь загрузки
7. Наслаждайтесь музыкой!

### Рабочий процесс 2: Архивирование видео
1. Запустите GUI (русский интерфейс, если предпочитаете)
2. Вставьте URL канала
3. Выберите формат MP4
4. Выберите папку вывода
5. Начните загрузку
6. Все видео сохранены с метаданными

### Рабочий процесс 3: Быстрые одиночные загрузки
1. Просматривайте YouTube
2. Увидели интересное видео
3. Скопируйте URL (Ctrl+C)
4. Появится всплывающее окно (если мониторинг включен)
5. Нажмите Загрузить
6. Готово за секунды!

---

**[⬆️ Back to README](README.md)**
