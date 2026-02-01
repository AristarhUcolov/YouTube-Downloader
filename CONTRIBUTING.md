# Contributing to YouTube Downloader

**[English](#english)** | **[Русский](#русский)**

---

<a name="english"></a>
## 🇬🇧 English Version

# Contributing to YouTube Downloader

Thank you for considering contributing to YouTube Downloader! This document provides guidelines and instructions for contributing.

## 🌟 Ways to Contribute

### 1. Report Bugs 🐛
Found a bug? Please open an issue with:
- Clear description of the problem
- Steps to reproduce
- Expected vs actual behavior
- Python version, OS version
- Error messages/screenshots

### 2. Suggest Features 💡
Have an idea? Open an issue with:
- Feature description
- Use case / problem it solves
- Proposed implementation (optional)
- Mockups or examples (optional)

### 3. Submit Code 💻
Want to code? Follow the process below!

### 4. Improve Documentation 📚
- Fix typos
- Add examples
- Translate to new languages
- Clarify instructions

### 5. Help Others 🤝
- Answer questions in issues
- Share tips and tricks
- Write tutorials

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Git
- Basic knowledge of Python, tkinter

### Setup Development Environment

1. **Fork the repository**
   - Click "Fork" button on GitHub

2. **Clone your fork**
```bash
git clone https://github.com/AristarhUcolov/youtube-downloader.git
cd youtube-downloader
```

3. **Add upstream remote**
```bash
git remote add upstream https://github.com/AristarhUcolov/youtube-downloader.git
```

4. **Create virtual environment (recommended)**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

5. **Install dependencies**
```bash
pip install -r requirements.txt
```

6. **Test the application**
```bash
python yt_downloader.py
```

---

## 📝 Coding Guidelines

### Code Style

- **Follow PEP 8**: Use consistent indentation (4 spaces), naming conventions
- **Comments**: Write clear comments for complex logic
- **Docstrings**: Add docstrings for functions/classes
```python
def my_function(param):
    """
    Brief description of function.
    
    Args:
        param (type): Description of parameter
        
    Returns:
        type: Description of return value
    """
    pass
```

### Naming Conventions

- **Functions/variables**: `snake_case`
- **Classes**: `PascalCase`
- **Constants**: `UPPER_SNAKE_CASE`
- **Private methods**: `_private_method`

### Good Practices

✅ **Do:**
- Write clear, self-documenting code
- Add error handling (try/except blocks)
- Test your changes before submitting
- Keep commits atomic (one feature/fix per commit)
- Write descriptive commit messages

❌ **Don't:**
- Submit untested code
- Mix multiple unrelated changes in one PR
- Remove existing features without discussion
- Hardcode values (use constants)
- Use `print()` for debugging (use logging)

---

## 🔧 Making Changes

### 1. Create a Branch

```bash
# Sync with upstream
git fetch upstream
git checkout main
git merge upstream/main

# Create feature branch
git checkout -b feature/your-feature-name
```

Branch naming:
- `feature/` - new features
- `fix/` - bug fixes
- `docs/` - documentation
- `refactor/` - code refactoring
- `test/` - test additions

### 2. Make Your Changes

- Edit the relevant files
- Follow coding guidelines
- Add comments where needed
- Update documentation if needed

### 3. Test Your Changes

**Basic testing:**
```bash
# Test GUI
python yt_downloader.py

# Test CLI
python yt_downloader.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ" --format mp3

# Test with playlist
python yt_downloader.py "https://www.youtube.com/playlist?list=PLAYLIST_ID"
```

**Test checklist:**
- ✅ GUI opens without errors
- ✅ Download works (MP3 and MP4)
- ✅ Clipboard monitoring works (if modified)
- ✅ Playlist detection works (if modified)
- ✅ Language switching works
- ✅ No console errors
- ✅ Works on different URLs

### 4. Commit Your Changes

```bash
# Stage changes
git add .

# Commit with clear message
git commit -m "Add feature: clipboard monitoring"
```

**Good commit messages:**
```
Add feature: clipboard monitoring for YouTube links
Fix issue: button not re-enabling after download
Update docs: add FAQ section
Refactor: extract URL parsing into separate function
```

**Bad commit messages:**
```
Fixed stuff
Update
Changes
asdf
```

### 5. Push to Your Fork

```bash
git push origin feature/your-feature-name
```

---

## 🎯 Submitting Pull Request

### Before Submitting

**Checklist:**
- ✅ Code follows style guidelines
- ✅ All tests pass
- ✅ No console errors
- ✅ Documentation updated (if needed)
- ✅ Commit messages are clear
- ✅ Branch is up to date with main

### Creating the PR

1. Go to your fork on GitHub
2. Click "Compare & pull request"
3. Fill in the template:

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Code refactoring

## Testing
Describe how you tested your changes

## Screenshots (if applicable)
Add screenshots for UI changes

## Checklist
- [ ] Code follows style guidelines
- [ ] Tests pass
- [ ] Documentation updated
```

4. Click "Create pull request"

### After Submitting

- Respond to code review comments
- Make requested changes
- Push updates (they'll appear in the PR automatically)

---

## 🌍 Adding Translations

Want to add a new language? Great!

### Steps:

1. **Edit `yt_downloader.py`**
2. **Find the `TRANSLATIONS` dictionary**
```python
TRANSLATIONS = {
    'en': {
        'title': 'YouTube Downloader',
        # ... more keys
    },
    'ru': {
        'title': 'YouTube Загрузчик',
        # ... more keys
    }
}
```

3. **Add your language**
```python
TRANSLATIONS = {
    'en': { ... },
    'ru': { ... },
    'es': {  # Spanish example
        'title': 'Descargador de YouTube',
        'paste_url': 'Pegar enlace de YouTube',
        # ... translate all keys
    }
}
```

4. **Update language button**
Find the `on_language_change()` function and add logic for your language.

5. **Test thoroughly**
- All labels translate correctly
- No text is cut off
- Buttons work properly

6. **Update README**
Add your language to the supported list.

---

## 🐛 Debugging Tips

### Common Issues

**Issue: "ModuleNotFoundError: No module named 'yt_dlp'"**
```bash
pip install yt-dlp
```

**Issue: "Tkinter not found"**
```bash
# Linux
sudo apt-get install python3-tk
```

**Issue: GUI doesn't update**
- Check if `root.update_idletasks()` is called
- Verify threading is used for downloads

### Debugging Tools

**Python debugger:**
```python
import pdb; pdb.set_trace()  # Set breakpoint
```

**Logging:**
```python
import logging
logging.basicConfig(level=logging.DEBUG)
logging.debug("Debug message")
```

**Print variables:**
```python
print(f"URL: {url}, Format: {format}")
```

---

## 📋 Feature Request Process

1. **Check existing issues** - Someone may have already suggested it
2. **Open new issue** with template
3. **Discussion** - Community discusses feasibility
4. **Approval** - Maintainer approves for implementation
5. **Implementation** - You or someone else codes it
6. **Review** - Code review and testing
7. **Merge** - Feature added to main branch

---

## ✨ Recognition

Contributors are recognized in:
- [CHANGELOG.md](CHANGELOG.md) - Credited for each contribution
- GitHub Contributors page
- Special thanks in releases

---

## 💬 Communication

- **GitHub Issues** - Bug reports, features, discussions
- **Pull Requests** - Code reviews, feedback
- **Email** - For private matters

---

## 📜 Code of Conduct

### Our Pledge

We pledge to make participation in our project a harassment-free experience for everyone.

### Our Standards

**Positive behavior:**
- Using welcoming language
- Respecting differing viewpoints
- Accepting constructive criticism
- Focusing on what's best for the community

**Unacceptable behavior:**
- Harassment, insults, derogatory comments
- Publishing private information
- Trolling, inflammatory comments
- Other unprofessional conduct

### Enforcement

Violations may result in:
1. Warning
2. Temporary ban
3. Permanent ban

Report violations to: [maintainer email]

---

## 🙏 Thank You!

Your contributions make this project better for everyone. Whether it's code, documentation, bug reports, or ideas - every contribution matters!

**Happy coding! 🚀**

---

**[⬆️ Back to README](README.md)**

---

<a name="русский"></a>
## 🇷🇺 Русская версия

# Участие в разработке YouTube Downloader

Спасибо за рассмотрение возможности внести вклад в YouTube Downloader! Этот документ предоставляет руководства и инструкции для участия.

## 🌟 Способы участия

### 1. Сообщайте об ошибках 🐛
Нашли баг? Пожалуйста, откройте issue с:
- Четким описанием проблемы
- Шагами для воспроизведения
- Ожидаемое vs фактическое поведение
- Версией Python, версией ОС
- Сообщениями об ошибках/скриншотами

### 2. Предлагайте функции 💡
Есть идея? Откройте issue с:
- Описанием функции
- Вариантом использования / проблемой, которую она решает
- Предлагаемой реализацией (опционально)
- Макетами или примерами (опционально)

### 3. Отправляйте код 💻
Хотите кодить? Следуйте процессу ниже!

### 4. Улучшайте документацию 📚
- Исправляйте опечатки
- Добавляйте примеры
- Переводите на новые языки
- Уточняйте инструкции

### 5. Помогайте другим 🤝
- Отвечайте на вопросы в issues
- Делитесь советами и трюками
- Пишите руководства

---

## 🚀 Начало работы

### Требования

- Python 3.8 или выше
- Git
- Базовые знания Python, tkinter

### Настройка среды разработки

1. **Сделайте Fork репозитория**
   - Нажмите кнопку "Fork" на GitHub

2. **Клонируйте свой fork**
```bash
git clone https://github.com/AristarhUcolov/youtube-downloader.git
cd youtube-downloader
```

3. **Добавьте upstream remote**
```bash
git remote add upstream https://github.com/AristarhUcolov/youtube-downloader.git
```

4. **Создайте виртуальное окружение (рекомендуется)**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

5. **Установите зависимости**
```bash
pip install -r requirements.txt
```

6. **Протестируйте приложение**
```bash
python yt_downloader.py
```

---

## 📝 Руководства по кодированию

### Стиль кода

- **Следуйте PEP 8**: Используйте последовательные отступы (4 пробела), соглашения об именовании
- **Комментарии**: Пишите четкие комментарии для сложной логики
- **Docstrings**: Добавляйте docstrings для функций/классов
```python
def my_function(param):
    """
    Краткое описание функции.
    
    Args:
        param (type): Описание параметра
        
    Returns:
        type: Описание возвращаемого значения
    """
    pass
```

### Соглашения об именовании

- **Функции/переменные**: `snake_case`
- **Классы**: `PascalCase`
- **Константы**: `UPPER_SNAKE_CASE`
- **Приватные методы**: `_private_method`

### Хорошие практики

✅ **Делайте:**
- Пишите четкий, самодокументируемый код
- Добавляйте обработку ошибок (try/except блоки)
- Тестируйте изменения перед отправкой
- Держите коммиты атомарными (одна функция/исправление на коммит)
- Пишите описательные сообщения коммитов

❌ **Не делайте:**
- Не отправляйте непротестированный код
- Не смешивайте несколько несвязанных изменений в одном PR
- Не удаляйте существующие функции без обсуждения
- Не используйте hardcode значения (используйте константы)
- Не используйте `print()` для отладки (используйте логирование)

---

## 🔧 Внесение изменений

### 1. Создайте ветку

```bash
# Синхронизируйтесь с upstream
git fetch upstream
git checkout main
git merge upstream/main

# Создайте ветку функции
git checkout -b feature/название-вашей-функции
```

Именование веток:
- `feature/` - новые функции
- `fix/` - исправления багов
- `docs/` - документация
- `refactor/` - рефакторинг кода
- `test/` - добавление тестов

### 2. Внесите изменения

- Отредактируйте соответствующие файлы
- Следуйте руководствам по кодированию
- Добавляйте комментарии где необходимо
- Обновите документацию при необходимости

### 3. Протестируйте изменения

**Базовое тестирование:**
```bash
# Тест GUI
python yt_downloader.py

# Тест CLI
python yt_downloader.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ" --format mp3

# Тест с плейлистом
python yt_downloader.py "https://www.youtube.com/playlist?list=PLAYLIST_ID"
```

**Чеклист тестирования:**
- ✅ GUI открывается без ошибок
- ✅ Загрузка работает (MP3 и MP4)
- ✅ Мониторинг буфера работает (если изменен)
- ✅ Определение плейлистов работает (если изменено)
- ✅ Переключение языков работает
- ✅ Нет ошибок в консоли
- ✅ Работает с разными URLs

### 4. Зафиксируйте изменения

```bash
# Добавьте изменения
git add .

# Коммит с четким сообщением
git commit -m "Добавить функцию: мониторинг буфера обмена"
```

**Хорошие сообщения коммитов:**
```
Добавить функцию: мониторинг буфера для YouTube ссылок
Исправить проблему: кнопка не активируется после загрузки
Обновить документацию: добавить секцию FAQ
Рефакторинг: извлечь парсинг URL в отдельную функцию
```

**Плохие сообщения коммитов:**
```
Исправлено
Обновление
Изменения
asdf
```

### 5. Отправьте в свой fork

```bash
git push origin feature/название-вашей-функции
```

---

## 🎯 Отправка Pull Request

### Перед отправкой

**Чеклист:**
- ✅ Код следует руководствам по стилю
- ✅ Все тесты проходят
- ✅ Нет ошибок в консоли
- ✅ Документация обновлена (если нужно)
- ✅ Сообщения коммитов четкие
- ✅ Ветка актуальна с main

### Создание PR

1. Перейдите на свой fork на GitHub
2. Нажмите "Compare & pull request"
3. Заполните шаблон:

```markdown
## Описание
Краткое описание изменений

## Тип изменения
- [ ] Исправление бага
- [ ] Новая функция
- [ ] Обновление документации
- [ ] Рефакторинг кода

## Тестирование
Опишите, как вы тестировали изменения

## Скриншоты (если применимо)
Добавьте скриншоты для изменений UI

## Чеклист
- [ ] Код следует руководствам по стилю
- [ ] Тесты проходят
- [ ] Документация обновлена
```

4. Нажмите "Create pull request"

### После отправки

- Отвечайте на комментарии code review
- Вносите запрошенные изменения
- Отправляйте обновления (они появятся в PR автоматически)

---

## 🌍 Добавление переводов

Хотите добавить новый язык? Отлично!

### Шаги:

1. **Отредактируйте `yt_downloader.py`**
2. **Найдите словарь `TRANSLATIONS`**
```python
TRANSLATIONS = {
    'en': {
        'title': 'YouTube Downloader',
        # ... больше ключей
    },
    'ru': {
        'title': 'YouTube Загрузчик',
        # ... больше ключей
    }
}
```

3. **Добавьте ваш язык**
```python
TRANSLATIONS = {
    'en': { ... },
    'ru': { ... },
    'es': {  # Пример испанского
        'title': 'Descargador de YouTube',
        'paste_url': 'Pegar enlace de YouTube',
        # ... переведите все ключи
    }
}
```

4. **Обновите кнопку языка**
Найдите функцию `on_language_change()` и добавьте логику для вашего языка.

5. **Тщательно протестируйте**
- Все метки переводятся корректно
- Текст не обрезается
- Кнопки работают правильно

6. **Обновите README**
Добавьте ваш язык в список поддерживаемых.

---

## 🐛 Советы по отладке

### Распространенные проблемы

**Проблема: "ModuleNotFoundError: No module named 'yt_dlp'"**
```bash
pip install yt-dlp
```

**Проблема: "Tkinter not found"**
```bash
# Linux
sudo apt-get install python3-tk
```

**Проблема: GUI не обновляется**
- Проверьте, вызывается ли `root.update_idletasks()`
- Проверьте, что используется threading для загрузок

### Инструменты отладки

**Отладчик Python:**
```python
import pdb; pdb.set_trace()  # Установить точку останова
```

**Логирование:**
```python
import logging
logging.basicConfig(level=logging.DEBUG)
logging.debug("Отладочное сообщение")
```

**Вывод переменных:**
```python
print(f"URL: {url}, Формат: {format}")
```

---

## 📋 Процесс запроса функций

1. **Проверьте существующие issues** - Кто-то мог уже предложить это
2. **Откройте новый issue** с шаблоном
3. **Обсуждение** - Сообщество обсуждает осуществимость
4. **Одобрение** - Поддерживающий одобряет для реализации
5. **Реализация** - Вы или кто-то другой кодирует это
6. **Ревью** - Code review и тестирование
7. **Слияние** - Функция добавлена в main ветку

---

## ✨ Признание

Контрибьюторы признаются в:
- [CHANGELOG.md](CHANGELOG.md) - Упоминание за каждый вклад
- Странице Contributors GitHub
- Особая благодарность в релизах

---

## 💬 Коммуникация

- **GitHub Issues** - Сообщения об ошибках, функции, обсуждения
- **Pull Requests** - Code reviews, обратная связь
- **Email** - Для личных вопросов

---

## 📜 Кодекс поведения

### Наше обязательство

Мы обязуемся сделать участие в нашем проекте опытом без преследований для всех.

### Наши стандарты

**Позитивное поведение:**
- Использование приветливого языка
- Уважение различных точек зрения
- Принятие конструктивной критики
- Фокус на том, что лучше для сообщества

**Неприемлемое поведение:**
- Преследование, оскорбления, унизительные комментарии
- Публикация личной информации
- Троллинг, провокационные комментарии
- Другое непрофессиональное поведение

### Применение

Нарушения могут привести к:
1. Предупреждению
2. Временному бану
3. Постоянному бану

Сообщайте о нарушениях: [email поддерживающего]

---

## 🙏 Спасибо!

Ваш вклад делает этот проект лучше для всех. Будь то код, документация, сообщения об ошибках или идеи - каждый вклад имеет значение!

**Счастливого кодирования! 🚀**

---

**[⬆️ Back to README](README.md)**
