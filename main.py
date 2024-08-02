from youtubesearchpython import VideosSearch # Импортира библиотеката за търсене на видеа в YouTube
import yt_dlp as youtube_dl # Импортира библиотеката за изтегляне на видеа и аудио от YouTube
import os # Импортира библиотеката за работа с файловата система
import re # Импортира библиотеката за работа с регулярни изрази

def download_video_as_mp3(youtube_url, output_path):
    # Опции за yt-dlp, които указват как да се изтегли и конвертира видеото
    ydl_opts = {
        'format': 'bestaudio/best', # Избира най-доброто качество на аудио
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'), # Шаблон за името на изходния файл
        'postprocessors': [{ # Опции за обработка след изтегляне
            'key': 'FFmpegExtractAudio', # Използва FFmpeg за извличане на аудио
            'preferredcodec': 'mp3', # Формат на конвертирания файл
            'preferredquality': '192', # Качество на MP3 файла
        }],
        'ffmpeg_location': 'C:\Users\Jiga\Downloads\ffmpeg-2024-08-01-git-bcf08c1171-full_build\ffmpeg-2024-08-01-git-bcf08c1171-full_build\bin', # Път до папката с ffmpeg (трябва да се актуализира спрямо реалния път)
        'noplaylist': True, # Не изтегля плейлисти, само единични видеа
    }

    try:
        # Създава обект за работа с yt-dlp и изтегля видеото
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_url])
            print(f"Downloaded and converted to MP3 from {youtube_url}")
    except Exception as e:
        print(f"An error occurred while downloading {youtube_url}: {e}")

def search_and_download(song_title, output_path, counter):
    # Създава обект за търсене на видеа по заглавие на песента
    video_search = VideosSearch(song_title, limit=1)
    results = video_search.result()
    if results['result']:
        # Ако има резултати, взема първия резултат (видео) и извиква функцията за изтегляне
        video_url = results['result'][0]['link']
        download_video_as_mp3(video_url, output_path)
        counter['count'] += 1
        print(f"Total downloaded: {counter['count']}")
    else:
        print(f"No results found for: {song_title}")

def process_song_list(file_path, output_path):
    # Отваря файла с песните и чете съдържанието му
    with open(file_path, 'r', encoding='utf-8', errors='replace') as file:
        songs = file.readlines()

    # Проверява дали папката за изходни файлове съществува, ако не, я създава
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    counter = {'count': 0}  # Initialize counter

    for song in songs:
        # Премахва номерацията и допълнителните интервали от заглавието на песента
        song_title = re.sub(r'^\d+\.\s*', '', song).strip()  # Remove numbering and extra spaces
        if song_title:
            # Извиква функцията за търсене и изтегляне на песента
            search_and_download(song_title, output_path, counter)

    print(f"Finished processing. Total songs downloaded: {counter['count']}")

# използвани функции
list_file = r'C:\Users\Jiga\Desktop\trip_songs.txt'  # Път до документа със списъка с песни
download_folder = 'C:/Users/Jiga/Desktop/Downloads'   # Път до папката, където ще се запазят изтеглените MP3 файлове
process_song_list(list_file, download_folder) # обработка на списъка с песни
