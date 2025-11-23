# Basic Dictionary Translator

# dictionary of words
dictionary = {
    "hello": "salam",
    "cat": "billi",
    "dog": "kutta",
    "how are you": "kese ho",
    "good morning": "subah bakhair",
    "food": "khana",
    "water": "pani"
}

print("Simple Translator (English to Urdu)\n")

print("Available words:", ", ".join(dictionary.keys()))

while True:
    print("\nOptions:")
    print("1. Translate a word")
    print("2. Add a new word")
    print("3. Exit")

    choice = input("Enter choice (1/2/3): ")

    # translate
    if choice == "1":
        text = input("Enter English word: ").lower()
        if text in dictionary:
            print("Translation:", dictionary[text])
        else:
            print("Sorry, translation not found.")

    # add new word
    elif choice == "2":
        eng = input("Enter English word: ").lower()
        ur = input("Enter Urdu meaning: ").lower()
        dictionary[eng] = ur
        print("Word added successfully!")

    # exit
    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
