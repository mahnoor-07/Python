""" Multi-Tool Python Program
Contains: Greeting, Calculator, Even/Odd Checker, Largest Number Finder"""

# Function 1: Greet the user

def greet():
    """Ask the user for their name and print a greeting."""
    name = input("Enter your name: ")
    print(f"\nHello, {name}! Welcome to the Multi-Tool Program.\n")

# Calculator functions (+, -, *, /)

def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def subtract(a, b):
    """Return the difference of two numbers."""
    return a - b


def multiply(a, b):
    """Return the product of two numbers."""
    return a * b


def divide(a, b):
    """Return the quotient of two numbers. Handle division by zero."""
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b


def calculator():
    """Take two numbers and an operation symbol, then call the correct math function."""
    print("\n--- Calculator ---")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    print("Choose operation: +  -  *  /")
    operator = input("Enter operation: ")

    if operator == "+":
        result = add(a, b)
    elif operator == "-":
        result = subtract(a, b)
    elif operator == "*":
        result = multiply(a, b)
    elif operator == "/":
        result = divide(a, b)
    else:
        result = "Invalid operation."

    print("Result:", result)

# Function 3: Even or Odd Checker

def is_even(num):
    """Return True if number is even, otherwise False."""
    return num % 2 == 0


def even_odd_checker():
    """Ask for a number and check if it is even or odd using is_even()."""
    print("\n--- Even/Odd Checker ---")
    n = int(input("Enter a number: "))

    if is_even(n):
        print("The number is EVEN.")
    else:
        print("The number is ODD.")

# Function 4: Largest of 3 Numbers

def largest(a, b, c):
    """Return the largest of three numbers."""
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    return c


def largest_checker():
    """Ask user for three numbers, then print the largest using largest()."""
    print("\n--- Largest of Three Numbers ---")
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    z = float(input("Enter third number: "))

    print("The largest number is:", largest(x, y, z))

# Menu + Main Program Loop
def menu():
    """Display menu options and call the corresponding function."""
    while True:
        print("\n===== Multi-Tool Menu =====")
        print("1. Greet User")
        print("2. Calculator")
        print("3. Even/Odd Checker")
        print("4. Largest of Three Numbers")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            greet()
        elif choice == "2":
            calculator()
        elif choice == "3":
            even_odd_checker()
        elif choice == "4":
            largest_checker()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
            continue

        # Ask user if they want to continue
        again = input("\nDo you want to continue using the program? (yes/no): ").lower()
        if again != "yes":
            print("Okay, exiting the program. Goodbye!")
            break


# Run the program
menu()
