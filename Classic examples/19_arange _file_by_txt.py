import os
import shutil
dir = "./arange_file"
for file in os.listdir(dir):
    ext = os.path.splitext(file)[1]
    ext = ext[1:]
    if not os.path.isdir(f"({dir}/{ext})"):
        os.mkdir(f"{dir}/{ext}")
    souce_file = f"{dir}/{file}"
    target_file = f"{dir}/{ext}/{file}"
    shutil.move(souce_file,target_file)
