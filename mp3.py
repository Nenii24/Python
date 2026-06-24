import os
import yt_dlp

class DownloaderModel:

    def descargar_mp3(self, link):
        carpeta = os.path.join(os.path.expanduser("~"), "Downloads")

        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(carpeta, '%(title)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])