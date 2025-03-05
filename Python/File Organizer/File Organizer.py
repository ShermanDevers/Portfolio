import os
import shutil
import time

download_dir = input(
    "Download folder location (ex: /path/to/downloaded_files): "
)

doc_dir = input("Documents Location (ex: /path/you/want/your/documents): ")
doc_ext = ["docx"]

vid_dir = input("Videos Location (ex: /path/you/want/your/videos): ")
vid_ext = ["mp4", "mkv"]

pic_dir = input("Pictures Location (ex: /path/you/want/your/pictures): ")
pic_ext = ["png", "jpg"]

os.chdir(download_dir)
whole_dir = os.listdir()

files = []

for item in whole_dir:
    if os.path.isfile(item) == True:
        files.append(item)

for file in files:
    period_count = file.count(".")

    file = file.replace(".", "", period_count - 1)
    ending = file.split(".")[1]

    if ending in doc_ext:
        shutil.move(file, doc_dir)
    if ending in vid_ext:
        shutil.move(file, vid_dir)
    if ending in pic_ext:
        shutil.move(file, pic_dir)
