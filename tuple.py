
student = ("Soban", 17, "Computer Science", 4.0)

name, age, major, gpa = student
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Major: {major}")
print(f"GPA: {gpa}")
print(f"Number of info fields: {len(student)}")
students = (
    ("Ali", 20, "Computer Science", 3.8),
    ("Sara", 22, "Mathematics", 3.5),
    ("John", 19, "Physics", 3.9),
    ("Mona", 21, "Biology", 3.2),
    ("Zain", 23, "Economics", 3.6),
)

print("Student GPA List: ")
for s_name, s_age, s_major, s_gpa in students:
    print(f"{s_name} - GPA: {s_gpa}")
try:
    student[3] = 4.0
except TypeError:
    print("Error! tuples are non-modifyable")