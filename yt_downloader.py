#!/usr/bin/env python3
"""YouTube Downloader - Download videos/playlists as MP3 or MP4.

Version: 2.1.0
Author: Aristarh Ucolov
License: MIT

Requirements:
- Python 3.8+
- yt-dlp (pip install -U yt-dlp)
- ffmpeg (in PATH or in local ffmpeg folder)

Usage:
    python yt_downloader.py URL -o outdir --format mp3
    python yt_downloader.py  # Opens GUI

Features:
    - Clipboard monitoring for YouTube links
    - Smart playlist/radio detection
    - MP3 (320kbps) and MP4 format support
    - Bilingual interface (English/Russian)

Note: Only download content you have rights to download.
"""
__version__ = '2.1.0'

import argparse
import os
import re
import shutil
import subprocess
import sys
import threading
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText
import tkinter.ttk as ttk
import time
import webbrowser


def check_requirements():
    def find_local_ffmpeg():
        names = ('ffmpeg.exe', 'ffmpeg')
        script_dir = os.path.dirname(os.path.abspath(__file__))
        cwd = os.getcwd()
        candidates = [
            script_dir,
            os.path.join(script_dir, 'ffmpeg'),
            os.path.join(script_dir, 'ffmpeg', 'bin'),
            cwd,
            os.path.join(cwd, 'ffmpeg'),
            os.path.join(cwd, 'ffmpeg', 'bin'),
        ]
        for d in candidates:
            if not d:
                continue
            for n in names:
                fp = os.path.join(d, n)
                if os.path.isfile(fp):
                    return os.path.abspath(d)
        return None

    local = find_local_ffmpeg()
    if shutil.which('ffmpeg') is None:
        if local:
            os.environ['PATH'] = local + os.pathsep + os.environ.get('PATH', '')
            exe = 'ffmpeg.exe' if os.name == 'nt' else 'ffmpeg'
            print(f'ffmpeg не найден в PATH, использую локальную копию: {os.path.join(local, exe)}')
        else:
            print('ffmpeg не найден в PATH. Установите ffmpeg (https://ffmpeg.org/) и добавьте в PATH, или поместите папку ffmpeg рядом со скриптом.')
            return False
    try:
        import yt_dlp  # noqa: F401
    except Exception:
        print('Модуль yt-dlp не установлен. Установите: pip install -U yt-dlp')
        return False
    return True


def build_yt_dlp_command(url: str, outdir: str, embed_thumbnail: bool, is_playlist: bool, outformat: str = 'mp3'):
    # choose filename template depending on whether it's a playlist
    if is_playlist:
        outtmpl = os.path.join(outdir, '%(playlist_index)s - %(title)s.%(ext)s')
    else:
        outtmpl = os.path.join(outdir, '%(title)s.%(ext)s')

    # Default: MP3 extraction
    if outformat == 'mp3':
        cmd = [
            'yt-dlp',
            '-o', outtmpl,
            '-f', 'bestaudio/best',
            '--extract-audio',
            '--audio-format', 'mp3',
            '--audio-quality', '0',
            '--postprocessor-args', '-ar 44100 -ac 2 -b:a 320k',
            '--add-metadata',
            url,
        ]
        if embed_thumbnail:
            cmd += ['--embed-thumbnail']
    else:
        # MP4: download best video+audio and merge into mp4 container
        cmd = [
            'yt-dlp',
            '-o', outtmpl,
            '-f', 'bestvideo+bestaudio/best',
            '--merge-output-format', 'mp4',
            '--add-metadata',
            url,
        ]

    return cmd


def is_playlist_url(u: str) -> bool:
    """Check if URL is a playlist."""
    if not u:
        return False
    return 'list=' in u or 'playlist' in u


def is_youtube_url(url):
    """Check if URL is a YouTube link."""
    youtube_patterns = [
        r'(?:https?://)?(?:www\.)?youtube\.com/watch\?v=',
        r'(?:https?://)?(?:www\.)?youtube\.com/playlist\?list=',
        r'(?:https?://)?youtu\.be/',
    ]
    return any(re.search(pattern, url) for pattern in youtube_patterns)


def analyze_youtube_url(url):
    """Analyze YouTube URL and detect if it contains playlist/radio parameters.
    
    Returns tuple: (is_playlist, clean_url, video_id, playlist_id)
    """
    # Check if URL contains list parameter
    has_list = '&list=' in url or '?list=' in url
    
    # Extract video ID
    video_match = re.search(r'(?:v=|youtu\.be/)([a-zA-Z0-9_-]{11})', url)
    video_id = video_match.group(1) if video_match else None
    
    # Extract playlist ID
    playlist_match = re.search(r'[?&]list=([^&]+)', url)
    playlist_id = playlist_match.group(1) if playlist_match else None
    
    # Clean URL (remove list parameters)
    clean_url = url
    if has_list and video_id:
        # Keep only video URL
        if 'youtu.be/' in url:
            clean_url = f'https://youtu.be/{video_id}'
        else:
            clean_url = f'https://www.youtube.com/watch?v={video_id}'
    
    return has_list, clean_url, video_id, playlist_id




def launch_download(url, outdir, embed_thumbnail, outformat='mp3', text_widget=None, start_button=None, progress_bar=None, stop_callback=None):
    os.makedirs(outdir, exist_ok=True)
    is_playlist = is_playlist_url(url)
    cmd = build_yt_dlp_command(url, outdir, embed_thumbnail, is_playlist, outformat)

    # If yt-dlp executable not found, prefer calling the bundled `yt_dlp` module
    # directly (this works when the script is bundled into an exe). Only
    # fall back to `python -m yt_dlp` if the module is not importable.
    run_as_module = False
    if shutil.which('yt-dlp') is None and shutil.which('yt-dlp.exe') is None:
        try:
            import yt_dlp  # type: ignore
            run_as_module = True
            if text_widget:
                text_widget.insert(tk.END, "yt-dlp не найден в PATH — использую встроенный модуль yt_dlp\n")
        except Exception:
            # last-ditch: try to run via the Python interpreter as a module
            cmd = [sys.executable, '-m', 'yt_dlp'] + cmd[1:]
            if text_widget:
                text_widget.insert(tk.END, f"yt-dlp не найден в PATH и модуль yt_dlp не импортируется — пытаюсь: {sys.executable} -m yt_dlp\n")

    # Show running message and disable controls
    if text_widget:
        text_widget.insert(tk.END, f"Запуск: {' '.join(cmd)}\n")
        text_widget.see(tk.END)
    if start_button:
        start_button.config(state='disabled')
    if progress_bar:
        try:
            progress_bar.start(10)
        except Exception:
            pass

    def run_proc():
        # If we determined we can run the bundled module, call it in-process.
        if run_as_module:
            try:
                import yt_dlp  # type: ignore
                if text_widget:
                    text_widget.insert(tk.END, "Выполняю встроенный yt_dlp.main(...)\n")
                    text_widget.see(tk.END)
                # yt_dlp.main expects a list of args similar to CLI (without argv[0])
                ret = yt_dlp.main(cmd[1:])
                if text_widget:
                    text_widget.insert(tk.END, f"Завершено с кодом {ret}\n")
                    text_widget.see(tk.END)
            except Exception as e:
                if text_widget:
                    text_widget.insert(tk.END, f"Ошибка при выполнении встроенного yt_dlp: {e}\n")
                    text_widget.see(tk.END)
            if progress_bar:
                try:
                    progress_bar.stop()
                except Exception:
                    pass
            if stop_callback:
                stop_callback()
            if start_button:
                start_button.config(state='normal')
            return

        # Otherwise run as external process
        try:
            proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        except Exception as e:
            if text_widget:
                text_widget.insert(tk.END, f"Ошибка запуска: {e}\n")
            if progress_bar:
                try:
                    progress_bar.stop()
                except Exception:
                    pass
            if stop_callback:
                stop_callback()
            if start_button:
                start_button.config(state='normal')
            return

        for line in proc.stdout:
            if text_widget:
                text_widget.insert(tk.END, line)
                text_widget.see(tk.END)
        proc.wait()
        if text_widget:
            text_widget.insert(tk.END, f"Завершено с кодом {proc.returncode}\n")
            text_widget.see(tk.END)
        if progress_bar:
            try:
                progress_bar.stop()
            except Exception:
                pass
        if stop_callback:
            stop_callback()
        if start_button:
            start_button.config(state='normal')

    threading.Thread(target=run_proc, daemon=True).start()


def main():
    parser = argparse.ArgumentParser(
        description='Download YouTube videos/playlists as MP3 or MP4',
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument('url', nargs='?', default='', help='YouTube URL (video or playlist)')
    parser.add_argument('-o', '--outdir', default='downloads', help='Output directory')
    parser.add_argument('--format', choices=['mp3', 'mp4'], default='mp3', help='Output format (mp3 or mp4)')
    parser.add_argument('--embed-thumbnail', action='store_true', help='Embed thumbnail')
    parser.add_argument('--lang', choices=['ru', 'en'], default='ru', help='UI language')

    args = parser.parse_args()
    check_requirements()
    lang = args.lang

    # If URL provided on command line, run headless
    if args.url:
        os.makedirs(args.outdir, exist_ok=True)
        launch_download(args.url, args.outdir, args.embed_thumbnail, outformat=args.format)
        return

    # Otherwise open enhanced Tkinter GUI
    TRANSLATIONS = {
        'ru': {
            'title': 'YouTube Downloader - Аудио/Видео',
            'url_label': 'YouTube URL:',
            'out_label': 'Папка сохранения:',
            'browse': 'Обзор...',
            'embed': 'Встраивать обложку',
            'format': 'Формат:',
            'lang_label': 'Язык:',
            'start': 'Скачать',
            'no_url': 'Введите ссылку на видео или плейлист',
            'running': 'Запуск:',
            'support': '☕ Поддержать проект',
            'support_msg': 'Поддержите разработку!\n\n☕ Buy Me a Coffee:\nhttps://buymeacoffee.com/aristarh.ucolov\n\n💳 Банковский перевод:\nБанк: Moldindconbank\nКарта: 4028 1202 1106 0963\nПолучатель: Aristarh Ucolov',
            'clipboard_monitor': 'Автоопределение ссылок YouTube',
            'clipboard_detected': 'Обнаружена ссылка YouTube!',
            'clipboard_ask': 'Загрузить это видео?\n\n{url}',
            'choose_format': 'Выберите формат загрузки:',
            'playlist_detected': 'Обнаружен плейлист',
            'playlist_ask': 'Эта ссылка содержит плейлист/радио.\n\nЧто вы хотите загрузить?',
            'single_video': 'Только это видео',
            'full_playlist': 'Весь плейлист/радио'
        },
        'en': {
            'title': 'YouTube Downloader - Audio/Video',
            'url_label': 'YouTube URL:',
            'out_label': 'Output folder:',
            'browse': 'Browse...',
            'embed': 'Embed thumbnail',
            'format': 'Format:',
            'lang_label': 'Language:',
            'start': 'Download',
            'no_url': 'Enter a video or playlist URL',
            'running': 'Running:',
            'support': '☕ Support Project',
            'support_msg': 'Support the development!\n\n☕ Buy Me a Coffee:\nhttps://buymeacoffee.com/aristarh.ucolov\n\n💳 Bank Transfer:\nBank: Moldindconbank\nCard: 4028 1202 1106 0963\nRecipient: Aristarh Ucolov',
            'clipboard_monitor': 'Auto-detect YouTube links',
            'clipboard_detected': 'YouTube link detected!',
            'clipboard_ask': 'Download this video?\n\n{url}',
            'choose_format': 'Choose download format:',
            'playlist_detected': 'Playlist detected',
            'playlist_ask': 'This link contains a playlist/radio.\n\nWhat would you like to download?',
            'single_video': 'Single video only',
            'full_playlist': 'Full playlist/radio'
        }
    }

    root = tk.Tk()
    root.title(TRANSLATIONS[lang]['title'])
    root.geometry('800x600')

    style = ttk.Style(root)
    try:
        style.theme_use('clam')
    except Exception:
        pass

    frm = ttk.Frame(root, padding=12)
    frm.pack(fill=tk.BOTH, expand=True)

    # Store widgets that need language updates
    widgets_to_update = {}

    # Row 0: URL and Language selector
    url_label = ttk.Label(frm, text=TRANSLATIONS[lang]['url_label'])
    url_label.grid(row=0, column=0, sticky='w', pady=4)
    widgets_to_update['url_label'] = url_label

    url_var = tk.StringVar()
    url_entry = ttk.Entry(frm, textvariable=url_var, width=50)
    url_entry.grid(row=0, column=1, columnspan=2, sticky='we', padx=6, pady=4)

    lang_label = ttk.Label(frm, text=TRANSLATIONS[lang]['lang_label'])
    lang_label.grid(row=0, column=3, sticky='e', padx=(12, 4), pady=4)
    widgets_to_update['lang_label'] = lang_label

    lang_var = tk.StringVar(value=lang)
    lang_combo = ttk.Combobox(frm, values=['ru', 'en'], textvariable=lang_var, width=8, state='readonly')
    lang_combo.grid(row=0, column=4, sticky='e', pady=4)

    # Row 1: Output folder
    out_label = ttk.Label(frm, text=TRANSLATIONS[lang]['out_label'])
    out_label.grid(row=1, column=0, sticky='w', pady=4)
    widgets_to_update['out_label'] = out_label

    out_var = tk.StringVar(value=args.outdir)
    out_entry = ttk.Entry(frm, textvariable=out_var, width=50)
    out_entry.grid(row=1, column=1, columnspan=2, sticky='we', padx=6, pady=4)

    def choose_folder():
        d = filedialog.askdirectory(initialdir=os.path.expanduser('~'))
        if d:
            out_var.set(d)

    browse_btn = ttk.Button(frm, text=TRANSLATIONS[lang]['browse'], command=choose_folder)
    browse_btn.grid(row=1, column=3, columnspan=2, sticky='e', pady=4)
    widgets_to_update['browse_btn'] = browse_btn

    # Row 2: Format selection
    format_label = ttk.Label(frm, text=TRANSLATIONS[lang]['format'])
    format_label.grid(row=2, column=0, sticky='w', pady=4)
    widgets_to_update['format_label'] = format_label

    fmt_frame = ttk.Frame(frm)
    fmt_frame.grid(row=2, column=1, columnspan=2, sticky='w', padx=6, pady=4)
    fmt_var = tk.StringVar(value=args.format)
    ttk.Radiobutton(fmt_frame, text='MP3 (Audio)', variable=fmt_var, value='mp3').pack(side='left', padx=(0, 12))
    ttk.Radiobutton(fmt_frame, text='MP4 (Video)', variable=fmt_var, value='mp4').pack(side='left')

    # Row 2: Embed checkbox
    embed_var = tk.BooleanVar(value=args.embed_thumbnail)
    embed_check = ttk.Checkbutton(frm, text=TRANSLATIONS[lang]['embed'], variable=embed_var)
    embed_check.grid(row=2, column=3, columnspan=2, sticky='e', pady=4)
    widgets_to_update['embed_check'] = embed_check

    # Row 2.5: Clipboard monitoring checkbox
    clipboard_var = tk.BooleanVar(value=False)
    clipboard_check = ttk.Checkbutton(frm, text=TRANSLATIONS[lang]['clipboard_monitor'], variable=clipboard_var)
    clipboard_check.grid(row=3, column=0, columnspan=3, sticky='w', pady=4)
    widgets_to_update['clipboard_check'] = clipboard_check

    # Row 3: Start button
    start_btn = ttk.Button(frm, text=TRANSLATIONS[lang]['start'])
    start_btn.grid(row=4, column=0, columnspan=3, pady=(12, 8), sticky='ew')
    widgets_to_update['start_btn'] = start_btn

    # Row 3: Support button
    def show_support():
        result = messagebox.showinfo(
            TRANSLATIONS[lang]['support'],
            TRANSLATIONS[lang]['support_msg']
        )
        # Open donation link in browser
        webbrowser.open('https://buymeacoffee.com/aristarh.ucolov')

    support_btn = ttk.Button(frm, text=TRANSLATIONS[lang]['support'], command=show_support)
    support_btn.grid(row=4, column=3, columnspan=2, pady=(12, 8), sticky='ew')
    widgets_to_update['support_btn'] = support_btn

    # Row 4: Log area
    log = ScrolledText(frm, height=18, wrap=tk.WORD)
    log.grid(row=5, column=0, columnspan=5, pady=(4, 4), sticky='nsew')

    # Row 5: Progress bar
    progress = ttk.Progressbar(frm, mode='indeterminate')
    progress.grid(row=6, column=0, columnspan=5, sticky='we', pady=(4, 0))

    # Update UI when language changes
    def on_language_change(event=None):
        nonlocal lang
        new_lang = lang_var.get()
        if new_lang != lang:
            lang = new_lang
            root.title(TRANSLATIONS[lang]['title'])
            widgets_to_update['url_label'].config(text=TRANSLATIONS[lang]['url_label'])
            widgets_to_update['out_label'].config(text=TRANSLATIONS[lang]['out_label'])
            widgets_to_update['browse_btn'].config(text=TRANSLATIONS[lang]['browse'])
            widgets_to_update['format_label'].config(text=TRANSLATIONS[lang]['format'])
            widgets_to_update['embed_check'].config(text=TRANSLATIONS[lang]['embed'])
            widgets_to_update['clipboard_check'].config(text=TRANSLATIONS[lang]['clipboard_monitor'])
            widgets_to_update['lang_label'].config(text=TRANSLATIONS[lang]['lang_label'])
            widgets_to_update['start_btn'].config(text=TRANSLATIONS[lang]['start'])
            widgets_to_update['support_btn'].config(text=TRANSLATIONS[lang]['support'])

    lang_combo.bind('<<ComboboxSelected>>', on_language_change)

    # Simple animated start button (pulse)
    start_btn_ref = start_btn

    pulse_state = {'on': False, 'job': None}

    def pulse():
        pulse_state['on'] = not pulse_state['on']
        try:
            start_btn_ref.state(['!alternate'] if pulse_state['on'] else ['alternate'])
        except Exception:
            pass
        pulse_state['job'] = root.after(600, pulse)

    def stop_pulse():
        if pulse_state['job']:
            root.after_cancel(pulse_state['job'])
            pulse_state['job'] = None

    def process_download(url):
        """Process download with playlist detection."""
        # Check if URL contains playlist/radio
        has_list, clean_url, video_id, playlist_id = analyze_youtube_url(url)
        
        final_url = url
        if has_list and video_id:
            # Ask user what to download
            dialog = tk.Toplevel(root)
            dialog.title(TRANSLATIONS[lang]['playlist_detected'])
            dialog.transient(root)
            dialog.grab_set()
            
            # Center dialog
            dialog.geometry('400x180')
            dialog.resizable(False, False)
            
            # Message
            msg_frame = ttk.Frame(dialog, padding=20)
            msg_frame.pack(fill='both', expand=True)
            
            ttk.Label(msg_frame, text=TRANSLATIONS[lang]['playlist_ask'], wraplength=360).pack(pady=(0, 20))
            
            # Buttons
            result = {'choice': None}
            
            def choose_single():
                result['choice'] = 'single'
                dialog.destroy()
            
            def choose_playlist():
                result['choice'] = 'playlist'
                dialog.destroy()
            
            btn_frame = ttk.Frame(msg_frame)
            btn_frame.pack()
            
            ttk.Button(btn_frame, text=TRANSLATIONS[lang]['single_video'], command=choose_single, width=20).pack(side='left', padx=5)
            ttk.Button(btn_frame, text=TRANSLATIONS[lang]['full_playlist'], command=choose_playlist, width=20).pack(side='left', padx=5)
            
            # Wait for choice
            root.wait_window(dialog)
            
            if result['choice'] == 'single':
                final_url = clean_url
            elif result['choice'] == 'playlist':
                final_url = url
            else:
                # User closed dialog
                return
        
        # Start download
        start_btn_ref.config(state='disabled')
        pulse()
        launch_download(final_url, out_var.get(), embed_var.get(), outformat=fmt_var.get(), text_widget=log, start_button=start_btn_ref, progress_bar=progress, stop_callback=stop_pulse)

    def on_start():
        url = url_var.get().strip()
        if not url:
            messagebox.showwarning('No URL', TRANSLATIONS[lang]['no_url'])
            return
        process_download(url)

    start_btn_ref.config(command=on_start)

    # Clipboard monitoring
    clipboard_state = {'last': '', 'job': None}
    
    def check_clipboard():
        """Check clipboard for YouTube links."""
        if not clipboard_var.get():
            # Monitoring disabled
            return
        
        try:
            clip = root.clipboard_get()
            if clip != clipboard_state['last'] and is_youtube_url(clip):
                clipboard_state['last'] = clip
                
                # Show dialog
                dialog = tk.Toplevel(root)
                dialog.title(TRANSLATIONS[lang]['clipboard_detected'])
                dialog.transient(root)
                dialog.grab_set()
                
                # Center dialog
                dialog.geometry('450x220')
                dialog.resizable(False, False)
                
                msg_frame = ttk.Frame(dialog, padding=20)
                msg_frame.pack(fill='both', expand=True)
                
                ttk.Label(msg_frame, text=TRANSLATIONS[lang]['clipboard_ask'].format(url=clip[:60] + ('...' if len(clip) > 60 else '')), wraplength=410).pack(pady=(0, 15))
                
                # Format selection
                ttk.Label(msg_frame, text=TRANSLATIONS[lang]['choose_format']).pack(pady=(0, 10))
                
                fmt_choice = tk.StringVar(value='mp3')
                fmt_frame_popup = ttk.Frame(msg_frame)
                fmt_frame_popup.pack(pady=(0, 20))
                ttk.Radiobutton(fmt_frame_popup, text='MP3', variable=fmt_choice, value='mp3').pack(side='left', padx=10)
                ttk.Radiobutton(fmt_frame_popup, text='MP4', variable=fmt_choice, value='mp4').pack(side='left', padx=10)
                
                # Buttons
                def download_clip():
                    fmt_var.set(fmt_choice.get())
                    url_var.set(clip)
                    dialog.destroy()
                    process_download(clip)
                
                def cancel_clip():
                    dialog.destroy()
                
                btn_frame = ttk.Frame(msg_frame)
                btn_frame.pack()
                ttk.Button(btn_frame, text=TRANSLATIONS[lang]['start'], command=download_clip, width=15).pack(side='left', padx=5)
                ttk.Button(btn_frame, text='Cancel' if lang == 'en' else 'Отмена', command=cancel_clip, width=15).pack(side='left', padx=5)
                
        except tk.TclError:
            # Clipboard empty or unavailable
            pass
        
        # Schedule next check
        clipboard_state['job'] = root.after(1000, check_clipboard)
    
    # Start clipboard monitoring
    check_clipboard()

    frm.grid_columnconfigure(1, weight=1)
    frm.grid_rowconfigure(5, weight=1)

    root.mainloop()


if __name__ == '__main__':
    main()
