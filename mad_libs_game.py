# Funny Horror Mad Libs Game

print("Welcom to the Mad Libs Game!")

# Asking the user for fun and spooky inputs
name = input("Enter a name: ")
creature = input("Enter a silly scary creature: ")
place = input("Enter a spooky but funny place: ")
sound = input("Enter a ridiculous scary sound: ")
food = input("Enter a weird food item: ")
action = input("Enter a funny action: ")
adjective = input("Enter a funny scary adjective: ")

print("\n    Your Funny Horror Story    \n")

# ABOUT f-strings:
# f-strings let us write variables inside curly braces { }.
# Example: f"{name} is here" will automatically replace {name} with the user's input.
# This makes the code shorter and easier to read than using string + concatenation.

# Story
print(f"One {adjective} night, {name} wandered into the {place}.")
print(f"Suddenly, a {creature} jumped out and yelled '{sound}!'")
print(f"{name} screamed… not because of fear, but because the {creature} was holding {food}.")
print(f"The creature stared at {name}, then started to {action} in slow motion.")
print(f"{name} couldn't stop laughing, and the {creature} got offended and moonwalked away.")
print(f"In the end, {name} and the {creature} became TikTok stars together.")

print("\n The End \n")