import zipfile
import os, os.path
import shutil

file_name = input("Introduzca nombre del archivo .zip: ")

def unzip():
    with zipfile.ZipFile(file_name) as zip_ref:
        zip_ref.extractall("extracted")


def copy_files(path_to_file):
    shutil.copytree(os.getcwd() + "/" +path_to_file, os.getcwd() + "/extract", symlinks=False, ignore=None, copy_function=shutil.copy2, ignore_dangling_symlinks=False, dirs_exist_ok=False)
    shutil.rmtree(os.getcwd() + "/extracted")

def walking_dir():
    dir = "extracted"
    is_dir = True
    while is_dir:
        for entry in os.scandir(dir):
            if entry.is_file():
                copy_files(dir)
                return True
            elif entry.is_dir():
                dir = entry.path
unzip()
walking_dir()

