class Student:
    def __init__(self, name, age, roll_no, major, gpa):
        self.name = name
        self.age = age
        self.roll_no = roll_no
        self.major = major
        self.gpa = gpa

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Roll No: {self.roll_no}, Major: {self.major}, GPA: {self.gpa}"
