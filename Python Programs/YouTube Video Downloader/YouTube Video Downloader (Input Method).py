#!/bin/env python
# Requires: youtube_dl module
# Requires: ffmpeg
# Usage:
#
# python youtube2mp3.py <URL>, ...
# 
# Example:
# 
# python youtube2mp3.py https://youtu.be/krGYd5tZe0A (Kausalya Suprabatham)

import youtube_dl
import sys


ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp4',
        'preferredquality': '192',
    }],
}


with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        downloads=input('Enter the URL of the YouTube file')
        ydl.download("ytsearch:",downloads)