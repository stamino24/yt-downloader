import tkinter as tk
from threading import Thread
import yt_dlp

def get_video_title():
    url = get_url.get()
    options = {
        'quiet': True,
    }
    with yt_dlp.YoutubeDL(options) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        title[0] = info_dict.get('title', None)
    print(title[0])
def download_mp4_thread():
    print('debug mp4')
    url = get_url.get()
    get_video_title()
    options = {
        'format': f'{quality[0]}[ext=mp4]/best',
    }
    try:
        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([url])
    except Exception:
        print('Error...')
    print('You can close the window')
def download_mp3_thread():
    print('debug mp3')
    url = get_url.get()
    get_video_title()
    options = {
        'format': 'bestaudio/best',
        'extractaudio': True,
        'audioformat': 'mp3',
        'outtmpl': f'{title[0]}.mp3',
    }
    try:
        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([url])
    except Exception:
        print('Error...')
    print('You can close the window')

def downloadstart(x):
    if x == 1:
        thread = Thread(target=download_mp4_thread)
        download_state.config(text='downloading mp4 file, close the window when the console says to')
        print('thread started... downloading')

    if x == 2:
        thread = Thread(target=download_mp3_thread)
        download_state.config(text='downloading mp3 file, close the window when the console says to')
        print('thread started... downloading')

    if x == 3:
        thread = Thread(target=changequality)
    thread.start()

def changequality():
    if cont[0]%2==0:
        quality[0] = 'worst'
        quality_btt.config(text='worst')
        cont[0]+=1

    else:
        cont[0]+=1
        quality[0] = 'best'
        quality_btt.config(text='best')
    print('quality set to', quality[0])


quality = ['best']
cont = [0]
title = ['']

window = tk.Tk()
window.title("yt downloader")
window.resizable(width=False, height=False)
window.minsize(width=300, height=70)
tk.Label(text='link:').grid(row=0, column=0, padx=10, pady=10)

get_url = tk.Entry(width=50)
get_url.grid(row=0, column=1, padx=5, pady=10)

quality_btt = tk.Button(text='best', command=lambda:downloadstart(3))
quality_btt.grid(row=0, column=4, padx=5, pady=10)

mp4_download = tk.Button(text='mp4', command=lambda:downloadstart(1))
mp4_download.grid(row=0, column=5, padx=5, pady=10)

mp3_download = tk.Button(text='mp3', command=lambda:downloadstart(2))
mp3_download.grid(row=0, column=6, padx=5, pady=10)

download_state = tk.Label(text='waiting...')
download_state.grid(row=1, column=1)

window.mainloop()
