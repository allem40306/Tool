import os, glob

backslash_char = "\\"

def Merge():
    n = int(input('number of files: ')) + 1
    ext = input('the extend name: ')
    filenames = [f"{i}.{ext}" for i in range(1, n)]
    with open('test.'+ ext, 'w') as outfile:
        for fname in filenames:
            with open(fname) as infile:
                for line in infile:
                    outfile.write(line)

def Create():
    prefix = input('Input prefix: ')
    nameMode = int(input('name mode(1:number, 2:alpha): '))
    N = int(input('number of files: '))

    filenames = [f"{prefix}{chr(i + ord('1'))}" for i in range(0, N)] if nameMode == 1 else [f"{prefix}{chr(i + chr('A'))}" for i in range(0, N)]
    for filename in filenames:
        open(f"{filename}.txt", 'w')


def fileArrange(folder, mode = 0):
    while True:
        files = glob.glob(f"{folder}/*/*", recursive=True)
        for file in files:
            if mode == 0:
                os.rename(file,f"{folder}/{file.replace(folder,'').replace(backslash_char,'___')}")
            elif mode == 1:
                os.rename(file,f"{file.replace('___',backslash_char)}")
            else:
                os.rename(file,f"{file.replace(' ','')}")
        if mode != 0 or len(files) == 0:
            break

if __name__ == "__main__":
	Create()
