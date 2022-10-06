from __future__ import unicode_literals
import youtube_dl

ydl_opts = {}
video_url = input("Enter video url: ")

try:
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])
except:
    print("An error occured")



