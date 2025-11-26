# Lecture 2 – Strings Basics (MIT OCW Practice)

""" 1. Concatenation
Joining two or more strings using + """

print("1. Concatenation:")
a = "me"
b = "myself"

c = a + b       # "memyself"
print(c)        

d = a + " " + b # "me myself"
print(d)        

""" 2. Repetition
Multiplying a string with an integer repeats it """

print("\n2. Repetition:")
silly = a * 3    # "mememe"
print(silly)     

"""3. Slicing
s[start:stop:step]"""

print("\n3. Slicing:")
s = "abcdefgh"
print(s[3:6])     # def
print(s[3:6:2])   # df
print(s[:])       # abcdefgh
print(s[::-1])    # hgfedcba

""" 4. Immutability
Strings cannot be changed directly"""

print("\n4. Immutability:")
s = "car"
# s[0] = "b"   # Error: strings are immutable

s = "b" + s[1:]  # Reassigning creates new string
print(s)         # bar

"""5. INPUT / OUTPUT BASICS
input() → Always returns a STRING.
print() → Displays output."""

print("\n5. Input / Output Basics")

text = input("Type anything: ")
print(5 * text)         # Repeats the string 5 times


num1 = input("Type a number: ")
print(5 * num1)         # Still repeats string (because num1 is a string)


num2 = int(input("Type a number: "))
print(5 * num2)         # Numeric multiplication (because cast to int)

"""6. f-STRINGS
 Cleaner formatting using f"...{variable}..."   """

print("\n6. f-String Example")

num = 3000
fraction = 1/3

print(f'{num * fraction} is {fraction * 100}% of {num}')

""" 7. BRANCHING (IF / ELIF / ELSE)
 Python checks conditions in order and executes ONE block."""

print("\n7. Branching Example")

pset_time = 15
sleep_time = 8
total_time = pset_time + sleep_time

if total_time > 24:
    print("Impossible! Not enough hours in a day.")
elif total_time == 24:
    print("Full schedule!")
else:
    leftover = 24 - total_time
    print(leftover, "hours of free time!")

print("End of day")