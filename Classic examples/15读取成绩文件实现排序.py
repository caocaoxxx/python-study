def read_file():
    result = []
    with open("./15学生成绩.txt",encoding='utf-8') as file:
        for line in file:
            line = line[:-1]  #文件隐藏有换行符，从第一个元素到最后一个元素，但不包含最后一个元素
            result.append(line.split(","))     
    return result
def sort_grades(datas):
    return sorted(datas,
    key=lambda x : int(x[2]),
    reverse=True)
def write_file(datas):
    with open("./15输出学生成绩.txt",'w',encoding='utf-8') as file:
        for data in datas:
            file.write(",".join(data)+"\n")
            

#读取文件
datas = read_file()
#排序数据
datas = sort_grades(datas)
print('sort_grade datas:',datas)
#写出文件


write_file(datas)