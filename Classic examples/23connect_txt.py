import os

content = []
dir_path ="./arange_file/many_files"
for file in os.listdir(dir_path):
    if os.path.isfile(f"{dir_path}/{file}") and file.endswith(".txt"):
        with open(f"{dir_path}/{file}",'r',encoding='utf-8') as file:
            content.append(file.read())
final_content = "\n".join(content)
with open("./arange_file/many_files/final.txt","w",encoding='utf-8') as fout:
    fout.write(final_content)
    

'''
代码优化
import os

data_path = "./arange_file/many_files"
content = [
    open(f"{data_path}/{file}", "r", encoding="utf-8").read().strip()
    for file in os.listdir(data_path)
    if os.path.isfile(f"{data_path}/{file}") and file.endswith(".txt")
]

final_content = "\n".join(content)
with open("./arange_file/many_files/final.txt", "w", encoding="utf-8") as fout:
    fout.write(final_content)
'''