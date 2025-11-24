# Word Count Program

while True:   # Keep running until a valid file is entered
    try:
        file_name = input("Enter the .txt file name (or type 'exit' to quit): ")
        
        # Exit option
        if file_name.lower() == "exit":
            print("Exiting program...")
            break

        # Check file extension
        if not file_name.endswith(".txt"):
            print("Error: Only .txt files are allowed.\n")
            continue

        total_words = 0

        # Try opening the file
        with open(file_name, "r") as file:
            for line in file:
                words = line.split()
                total_words += len(words)

        # If everything is successful, break the loop
        print("Total words in the file:", total_words)
        break

    except FileNotFoundError:
        print("Error: File not found. Please try again.\n")

    except Exception as e:
        print("An unexpected error occurred:", e)