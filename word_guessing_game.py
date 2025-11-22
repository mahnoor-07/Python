# Word Guessing Game

secret_word = "apple"
hint = "It is red fruit."
attempts = 4

print("Welcome to the Word Guessing Game!")
print("Hint:", hint)
print("You have", attempts, "attempts.\n")

guess = ""                # Stores full-word guesses
letters_guessed = ""      # Stores correct letters guessed

while guess != secret_word and attempts > 0:
    # show the progress
    print("\nCurrent word: ",end="")
    display = ""

    for letter in secret_word:
        if letter in letters_guessed:
            display += letter
        else:
            display += "_"
    
    print(display)

    # Ask the user for input (letter or full word)
    guess = input("Enter a letter or the full word: ").lower()

    # OPTION 1: User enters ONE LETTER
    if len(guess) == 1:

        # Check if the letter is in the word
        if guess in secret_word:
            print("Correct letter!")
            letters_guessed += guess
        else:
            print("Wrong letter!")
            attempts -= 1
            print("Attempts left:", attempts)

    # OPTION 2: User enters FULL WORD
    else:
        if guess == secret_word:
            print("Correct! You guessed the word.")
            break
        else:
            print("Incorrect word guess!")
            attempts -= 1
            print("Attempts left:", attempts)

    # If no "_" left → user guessed all letters
    if "_" not in display:
        print("\nYou guessed the word:", secret_word)
        break

# GAME OVER RESULTS
if attempts == 0:
    print("\nYou lost!")
    print("The correct word was:", secret_word)

    