from __future__ import unicode_literals
import os, subprocess
import youtube_dl

def videoDownload(urls = []):
    ydl_opts = {'format': 'bestvideo[ext=mp4]+bestaudio[ext=mp4]/mp4+best[height<=720]'
    }
    for url in urls:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

def videoProcess(inputFolder = f"{os.getcwd()}/in", outputFolder = f"{os.getcwd()}/out", oid=0, isTransExt = 1, isMeta = 0, isMerge = 0):
    videoList = [".3gp", ".asx", ".avi", ".mp4", ".mkv", ".mov", ".flv", ".ts", ".wmv", ".mpg", ".mpeg", ".ogv", ".vob"]
    optionList = ["", "-s hd720 -crf 23 -c:a aac -strict -2", "-vf scale=1280:-1 -crf 23 -c:a aac -strict -2", "-qscale 0 -r 24", "-vf \"transpose=1\""]
    for file in os.listdir(inputFolder):
        filename, file_extension = os.path.splitext(file) 
        if file_extension.lower() not in videoList:
            continue
        inputFile = f"{inputFolder}/{file}"
        outputFile = f"{outputFolder}/{filename}.mp4" if isTransExt else f"{outputFolder}/{file}"
        subprocess.call(f"ffmpeg -i {inputFile} -c:v libx264 {optionList[oid]}  {outputFile}")
        if isMeta:
            subprocess.call(f"ffmpeg -i {inputFile} -f ffmetadata {outputFolder}/{file}.txt")
        if file_extension.lower() == ".mkv":
            subprocess.call(f"ffmpeg -i {inputFile} -map 0:3 -c copy {outputFolder}/{filename}.ass")
    if isMerge:
        subprocess.call(f"。ffmpeg -f concat -i videos.txt -c copy {outputFolder}/output.mp4")