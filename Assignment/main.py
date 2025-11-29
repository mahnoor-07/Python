from student_classes import Student, Student_list, random_name
import random

students = []

for i in range(100):
    name = random_name()
    roll_no = random.randint(1, 999)
    marks = random.randint(40, 100)
    # Add new Student object to list
    students.append(Student(name, roll_no, marks))

student_list = Student_list(students)

print("Student Names:")
for name in student_list:
    print(name)

"""Sort the original list by roll numbers
key=lambda x: x.roll_no mean sort by roll_no attribute"""
students.sort(key=lambda x: x.roll_no)

print("\nSorted by Roll Numbers:")
for s in students:
    print(s.roll_no, "  :  ", s.name)
