# 1. if statement

num = int(input("Enter a number: "))

if num > 0:
    print("The number is positive.")

# 2. if-else statement

age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult.")
else:
    print("You are not an adult.")

# 3. if-elif-else statement

marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: Fail")

# 4. Multiple conditions

temperature = int(input("Enter temperature: "))

if temperature > 30 and temperature <= 45:
    print("Weather: Hot")
elif temperature > 15 and temperature <= 30:
    print("Weather: Normal")
elif temperature >= 0 and temperature <= 15:
    print("Weather: Cold")
else:
    print("Temperature out of range")

# 5. Even or Odd Program

num2 = int(input("Enter a number: "))

if num2 % 2 == 0:
    print("Even number")
else:
    print("Odd number")
