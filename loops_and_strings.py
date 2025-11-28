# Lecture 4 – Break, Loops, Strings, Guess & Check

""" break Statement: Loop stops immediately when 'break' is executed."""

mysum = 0
for i in range (5,11,2):
    mysum += i
    if mysum == 5:
        break
    mysum += 1
print(mysum)

"""Write code that loops a for loop over some range and print how many even numbers are in that 
range"""

even_num = 0
for i in range(5):
    if i%2 == 0:
        even_num += 1
print(even_num)

"""Strings and Loops
Two ways:
   (1) Loop using index
   (2) Loop directly through characters"""

# uses range to iterate through index of s
s = "demo loops - fruit loops"
for index in range(len(s)):
    if s[index] == "i" or s[index] == "u" :
        print("There is i and u.")

# iterate through character s directly
for char in s:
    if char == "i" or char == "u":
        print("There is i and u.")

# using 'in' 
for char in s:
    if char in "iu":
        print("There is i and u.")

# Robot cheerleaders Program

an_letter = "aefhimorsxAJKSDFHS"
word = input("I will cheer for you! Enter a word: ")
times = int(input("Enthusisam Level (1 -10): "))
for w in word:
    if w in an_letter:
        print("Give me an "+ w +": "+w)
    else:
        print("Give me a "+ w +": "+w)
print("What does it spell?")
for i in range(times):
    print(word, "!!!")

# Guess and Check SQUARE ROOT with while loop

guess = 0
neg_flag = False
x = int(input("Enter an integer: "))
if x < 0:
    neg_flag = True
while guess**2 < x:
    guess += 1
if guess**2 == x:
    print("Square root of ", x, "is", guess)
else:
    print(x, "is not a perfect square.")
    if neg_flag:
        print(f'Just checking ... did you mean {-x}')