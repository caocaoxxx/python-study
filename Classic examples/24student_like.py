student = {}
with open("./arange_file/many_files/student_like.txt", 'r', encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        sname, likes = line.split(" ")
        likes = likes.split(",")
        for like in likes:
            if like not in student:
                student[like] = 0
            student[like] += 1

print(student)
