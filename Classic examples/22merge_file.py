course_teacher = {}
with open("./course_teacher.txt",'r',encoding='utf-8') as file:
    for line in file:
        line = line.strip()
        course,teacher = line.split(',')
        course_teacher[course] = teacher

with open("./course_students.txt",'r',encoding='utf-8') as file, open("./course_students_teacher.txt",'w',encoding='utf-8') as outfile:
    for line in file:
        line = line.strip()
        course,sno,student,sgrade = line.split(',')
        teacher = course_teacher.get(course)
        outfile.write(f"{course},{teacher},{sno},{student},{sgrade}\n")
