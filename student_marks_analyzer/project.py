FILE_NAME = "students_data.txt"

def add_student():
    """Add a new student's record into the text file."""
    name = input("Enter student name: ").strip()
    roll = input("Enter roll number: ").strip()
    marks = input("Enter marks (0-100): ").strip()

    with open(FILE_NAME, "a") as file:
        file.write(f"{name},{roll},{marks}\n")

    print("Student added successfully!\n")


def search_student():
    """Search for a student by their name."""
    name_to_search = input("Enter name to search: ").strip().lower()
    found = False

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                name, roll, marks = line.strip().split(",")
                if name.lower() == name_to_search:
                    print("\nStudent Found")
                    print(f"Name: {name}")
                    print(f"Roll: {roll}")
                    print(f"Marks: {marks}\n")
                    found = True
                    break
    except FileNotFoundError:
        print("No data file found. Add a student first.\n")
        return

    if not found:
        print("Student not found.\n")


def count_results():
    """Count how many students passed and failed.
    
    Passing criteria: marks >= 50
    """
    passed = 0
    failed = 0

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                _, _, marks = line.strip().split(",")
                marks = int(marks)

                if marks >= 50:
                    passed += 1
                else:
                    failed += 1

    except FileNotFoundError:
        print("Data file missing! Add some students first.\n")
        return

    print("\nResult Count")
    print(f"Passed students: {passed}")
    print(f"Failed students: {failed}\n")


def main_menu():
    """Display the menu and handle user choices."""
    while True:
        print("Student Management System")
        print("1. Add Student")
        print("2. Search Student by Name")
        print("3. Count Passed / Failed Students")
        print("4. Exit")

        choice = input("Enter choice (1-4): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            search_student()
        elif choice == "3":
            count_results()
        elif choice == "4":
            print("Exiting program... Goodbye!")
            break
        else:
            print("Invalid input! Please enter a number between 1-4.\n")


# Start the program
main_menu()
