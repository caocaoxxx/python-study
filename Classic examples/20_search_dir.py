import os
dir_search = "F:\Python Study"
result_files = []
for root,dirs,files in os.walk(dir_search):
    print(root)
    for file in files:
        if file.endswith(".py"):
            file_path = f"{root}/{file}"
            print(file_path)
            result_files.append((file_path,os.path.getsize(file_path)/1000))
print(sorted(  result_files,key=lambda x:x[1],reverse=True)[:10])


