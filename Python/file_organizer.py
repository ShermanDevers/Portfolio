import os
import shutil

doc_dir = input("Where do you want your documents to be placed (ex: path/you/want/your/documents): ")
vid_dir = input("Where do you want your video files to be placed (full path): ")
pic_dir = input("Where do you want your pictures to be placed (full path): ")


os.chdir("/home/sherman/Downloads")
files = os.listdir()
doc_ext = ["docx"]
vid_ext = ["mp4", "mkv"]
pic_ext = ["png", "jpg"]

for file in files:
    period_count = file.count(".")
    remove_count = period_count - 1

    file = file.replace(".", "", period_count - 1)
    ending = file.split(".")[1]

    if ending in doc_ext:
        shutil.move(file, doc_dir)
    if ending in vid_ext:
        shutil.move(file, vid_dir)
    if ending in pic_ext:
        shutil.move(file, pic_dir)
