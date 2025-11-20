# 1. Print Statements

print("Hello World!")
print("This is my first Python practice file.\n")

# 2. Variables

name = "Mahnoor"
age = 21
is_student = True

print("Name:", name)
print("Age:", age)
print("Student:", is_student, "\n")

# 3. Data Types

x = 10           # integer
y = 3.5          # float
z = "Hello"      # string
w = False        # boolean

print("Integer:", x)
print("Float:", y)
print("String:", z)
print("Boolean:", w, "\n")

# printing the type of the variable
print(type(x))
print(type(y))

# 4. Taking Input

user_name = input("Enter your name: ")
print("Welcome,", user_name)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)

# =======================================================================
# Practice Question
# =======================================================================

# 1. sum of two numbers
n1 = int(input("Enter value of n1: "))
n2 = int(input("Enter value of n2: "))
sum = n1 + n2
print("Sum = ", sum)

# 2. area of square
a = int(input("Enter vlue of side: "))
print("Area = ", a*a)

# 3. print average of float values
n1 = float(input("Enter value of n1: "))
n2 = float(input("Enter value of n2: "))
print("Average = ", (n1+n2)/2)
