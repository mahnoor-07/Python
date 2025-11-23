while True:
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        
        result = numerator / denominator
        print("Result:", result)
        break  # Exit the loop if input is valid and division succeeds

    except ZeroDivisionError:
        print("Error: You cannot divide by zero. Please try again.")

    except ValueError:
        print("Error: Please enter a valid number. Try again.")

    finally:
        print("Attempt finished.\n")
