from main import Student

# List to store multiple students
students = []

# Creating multiple student objects
s1 = Student("Ali", 20, 101, "Science", 3.2)
s2 = Student("Sara", 21, 102, "Computer Science", 3.8)
s3 = Student("Ahmed", 19, 103, "Math", 3.5)

# Add students to list
students.append(s1)
students.append(s2)
students.append(s3)

# Print all students
for student in students:
    print(student)
