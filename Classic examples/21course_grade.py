with open("./course_students.txt", encoding="utf-8") as file:
    students_grade = {}
    for line in file:
        line = line.strip()
        parts = line.split(",")
        course = parts[0]
        grade = int(parts[3])
        if course not in students_grade:    
            students_grade[course] = [] # 如果课程不在字典中，创建一个空列表
        students_grade[course].append(int(grade))  # 将成绩添加到列表中

for course,grades in students_grade.items():
    print(f"course:{course},max:{max(grades)},min:{min(grades)},avg:{sum(grades)/len(grades):.2f}")

