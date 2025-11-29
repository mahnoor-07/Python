import random
import string

# Student Class: stores individual student information
class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
    
# Iterable Class: allows looping through student names
class Student_list:
    def __init__(self, students):
        self.students = students
    def __iter__(self):
        """
        This makes Student_list iterable.
        Instead of returning full Student objects during iteration,
        we only 'yield' the student names.
        """
        for s in self.students:
            yield s.name      # returns name one-by-one in loops

""" Function to generate random names
    random.randint(3, 10): random number between 3 and 10
    random.choices(list, k=n): pick n random characters
    ''.join(list): combine characters to form a string """
def random_name():
    length = random.randint(3, 10) 
    return ''.join(random.choices(string.ascii_letters, k=length))