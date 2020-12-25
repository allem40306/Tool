import zipfile
import os
import unrar
import rarfile
import tarfile
import py7zr
from shutil import copy

# dst_dir = r"C:\Users\USER\Downloads\20201115232743_第一次上機考20201020_32份"
tar_dir = r"C:\Users\USER\Downloads\results"
root_dir = os.getcwd()

dir = [x[0] for x in os.walk('.')]
dir.pop(0)

for path in dir:
    print(path)
    os.chdir(path)
    files = os.listdir()
    for file in files:
        filename, file_extension = os.path.splitext(file)
        if file.endswith(".zip"):
            print(file + ' is a zip file')
            try:
                zipFile = zipfile.ZipFile(os.path.join(os.getcwd(), file))
                zipFile.extractall()
            except Exception as e:
                print(e)
        elif file.endswith(".rar"):
            print(file + ' is a rar file')
            try:
                rarFile = rarfile.RarFile(os.path.join(os.getcwd(), file))
                rarFile.extractall()
            except Exception as e:
                print(e)
        elif file.endswith(".tar"):
            print(file + ' is a tar file')
            try:
                rarFile = rarfile.RarFile(os.path.join(os.getcwd(), file))
                rarFile.extractall()
            except Exception as e:
                print(e)
        elif file.endswith(".7z"):
            print(file + ' is a 7z file')
            try:
                with py7zr.SevenZipFile(os.path.join(os.getcwd(), file), mode='r') as z:
                    z.extractall()
            except Exception as e:
                print(e)
    os.chdir(root_dir)

for path in dir:
    print(path)
    os.chdir(path)
    files = os.listdir()
    no = 0
    for namelist in os.listdir():
        if namelist.endswith(".asm") or namelist.endswith(".c")  or namelist.endswith(".cpp"):
            studentID = path[2:12]
            target_name = namelist.split('/' )
            target_path = os.path.join(tar_dir, studentID + str(no) + target_name[-1])
            dst_path = '.\\' + namelist
            print(dst_path)
            try:
                copy(dst_path,target_path)
            except:
                print(e)
                pass
            no +=1
    os.chdir(root_dir)
    