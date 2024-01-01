import os, glob, re

backslash_char = "\\"

def merge():
    n = int(input('number of files: ')) + 1
    ext = input('the extend name: ')
    filenames = [f"{i}.{ext}" for i in range(1, n)]
    with open('test.'+ ext, 'w') as outfile:
        for fname in filenames:
            with open(fname) as infile:
                for line in infile:
                    outfile.write(line)

def create():
    prefix = input('Input prefix: ')
    nameMode = int(input('name mode(1:number, 2:alpha): '))
    N = int(input('number of files: '))

    filenames = [f"{prefix}{chr(i + ord('1'))}" for i in range(0, N)] if nameMode == 1 else [f"{prefix}{chr(i + chr('A'))}" for i in range(0, N)]
    for filename in filenames:
        open(f"{filename}.txt", 'w')


def arrange(folder, mode = 0):
    while True:
        files = glob.glob(f"{folder}/*/*", recursive=True) if mode == 0 else glob.glob(f"{folder}/*", recursive=True)
        print(len(files))   
        for file in files:
            if mode == 0:
                os.rename(file,f"{folder}/{file.replace(folder,'').replace(backslash_char,'___')}")
            elif mode == 1:
                os.rename(file,f"{file.replace('___',backslash_char)}")
            else:
                os.rename(file, file.replace("", ""))
        if mode != 0 or len(files) == 0:
            break

def isNestedFolder(folder):
    for pathL1 in glob.glob(f"{folder}/*", recursive=True):
        for pathL2 in glob.glob(f"{pathL1}/*", recursive=True):
            if os.path.isdir(pathL2):
                print(pathL2)
                L2Name = pathL2[len(pathL1)+1:]
                for pathL3 in glob.glob(f"{pathL2}/*", recursive=True):
                    os.rename(pathL3,pathL3.replace(f"{L2Name}\\",f"{L2Name}-"))
                if len(glob.glob(f"{pathL2}/*", recursive=True)) == 0:
                    os.removedirs(pathL2)
