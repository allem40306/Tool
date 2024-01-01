import os, subprocess


videoList = [".flac", ".mp3", ".tak"]

def process(inputFolder = f"{os.getcwd()}/in", outputFolder = f"{os.getcwd()}/out", oid=0, isTransExt = 1):
    optionList = ["", "-ab 320k  -af channelmap=0"]
    for file in os.listdir(inputFolder):
        filename, file_extension = os.path.splitext(file) 
        if file_extension.lower() not in videoList:
            continue
        inputFile = f"{inputFolder}/{file}"
        outputFile = f"{outputFolder}/{filename}.mp3" if isTransExt else f"{outputFolder}/{file}"
        subprocess.call(f'ffmpeg -i "{inputFile}" {optionList[oid]} "{outputFile}"')

def merge(folder = f"{os.getcwd()}\in"):
    if os.path.exists("audio.txt"):
        os.remove("audio.txt")
    f = open("audio.txt","w",encoding="utf-8")
    for file in os.listdir(folder):
        filename, file_extension = os.path.splitext(file) 
        f.write(f"file '{folder}/{file}'\n",)
    f.close()
    subprocess.call(f'ffmpeg -f concat -safe 0 -i audio.txt -c copy "{folder}/output.mp3"')
