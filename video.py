from __future__ import unicode_literals
import os, subprocess
import youtube_dl
from functools import wraps

videoList = [".3gp", ".asf", ".asx", ".avi", ".mp4", ".mkv", ".mov", ".flv", ".ts", ".wmv", ".mpg", ".mpeg", ".ogv", ".rmvb", ".vob", ".webm"]

def download(urls = []):
    ydl_opts = {'format': 'bestvideo[ext=mp4]+bestaudio[ext=mp4]/mp4+best[height<=720]'}
    for url in urls:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

def downloadByYouget(urls = [], isList = 0):
    optionList = ["", "--playlist"]
    for url in urls:
        subprocess.call(f"you-get -o ./out {optionList[isList]} {url}")

def ffmpeg_decorator(f, inputFolder = f"{os.getcwd()}/in", outputFolder = f"{os.getcwd()}/out"):
    @wraps(f)
    def wrap(**kwargs):
        for pathname in os.listdir(inputFolder):
            filename, file_extension = os.path.splitext(pathname) 
            if file_extension.lower() not in videoList:
                continue
            f(inputFolder, outputFolder, pathname, filename, **kwargs)
    return wrap

@ffmpeg_decorator
def process(*args, **kwargs):
    oid = int(kwargs['oid']) if 'oid' in kwargs else 0
    optionList = ["", "-s hd720 -crf 23 -c:a aac -strict -2", "-vf scale=-1: -crf 23 -c:a aac -strict -2", "-qscale 0 -r 24", "-vf \"transpose=1\""]
    inputFile = f"{args[0]}/{args[2]}"
    outputFile = f"{args[1]}/{args[3]}.mp4"
    subprocess.call(f'ffmpeg -i "{inputFile}" -c:v libx264 {optionList[oid]}  "{outputFile}"')

@ffmpeg_decorator
def exportMetadata(*args, **kwargs):
    inputFile = f"{args[0]}/{args[2]}"
    outputFile = f"{args[1]}/{args[3]}.txt"
    subprocess.call(f'ffmpeg -i "{inputFile}" -f ffmetadata "{outputFile}"')

@ffmpeg_decorator
def exportSubtitle(*args, **kwargs):
    subExt = kwargs['subExt'] if 'subExt' in kwargs else 'ass'
    channel = int(kwargs['channel']) if 'channel' in kwargs else 0
    inputFile = f"{args[0]}/{args[2]}"
    outputSubtitle = f"{args[1]}/{args[3]}.{subExt}"
    print(outputSubtitle)
    subprocess.call(f'ffmpeg -i "{inputFile}" -map 0:{channel} -c copy "{outputSubtitle}"')

@ffmpeg_decorator
def importSubtitle(*args, **kwargs):
    subExt = kwargs['subExt'] if 'subExt' in kwargs else 'ass'
    inputFile = f"{args[0]}/{args[2]}"
    inputSubtitle = f"{args[0]}/{args[3]}.{subExt}"
    inputSubtitle = inputSubtitle.replace("\\","\\\\\\").replace(":\\","\\\\:\\\\")
    outputFile = f"{args[1]}/{args[2]}"
    subprocess.call(f'ffmpeg -i "{inputFile}" -vf "ass={inputSubtitle}" "{outputFile}"')
    # subprocess.call(f'ffmpeg -i "{inputFile}" -i "{inputSubtitle}" -c copy -c:s mov_text "{outputFile}"')

def merge(inputFolder = f"{os.getcwd()}/in", outputFolder = f"{os.getcwd()}/out"):
    if os.path.exists("videos.txt"):
        os.remove("videos.txt")
    with open("videos.txt","w",encoding="utf-8") as f:
        for file in os.listdir(inputFolder):
            filename, file_extension = os.path.splitext(file)
            f.write(f"file '{inputFolder}/{file}'\n",)
        f.close()
    subprocess.call(f'ffmpeg -f concat -safe 0 -i videos.txt -c copy "{outputFolder}/output.mp4"')
