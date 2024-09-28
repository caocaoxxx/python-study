students = [
    {"sno":101,"sname":"小张","sgrade":88},
    {"sno":102,"sname":"小王","sgrade":99},
    {"sno":103,"sname":"小名","sgrade":77},
    {"sno":104,"sname":"小并","sgrade":66},
]
students_sort = sorted(students,key=lambda x:x["sgrade"])
for row in students_sort:
    for item in row:
        print(item,end='\t')
print(f'source {students}, sort result{students_sort}')