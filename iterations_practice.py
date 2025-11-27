# Lecture 3 – Iterations (MIT OCW Practice)

"""WHILE LOOPS
while <condition>:
<block of code>
The loop keeps running as long as the condition is TRUE.
Make sure the condition eventually becomes FALSE,
otherwise you create an INFINITE LOOP."""

where = input("You're in the Lost Forest. Go left or right? ").lower()

while where == "right":
    where = input("You're still in the Lost Forest. Go left or right? ").lower()

print("You got out of the Lost Forest!")

n = int(input("Enter a non-negative integer: "))
while n>0:
    print("x")
    n = n-1

"""Expand this code to show a sad face when the user entered the while loop more than 2 times
Hint: use a variable as counter """

a = 0
where = input("You're in the Lost Forest. Go left or right? ").lower()

while where == "right":
    a = a + 1
    if a > 2:
        print(":(")
    where = input("You're still in the Lost Forest. Go left or right? ").lower()

print("You got out of the Lost Forest!")

"""Find 4!
i is our loop variable
factorial keeps the track of the product """

x = 4
i = 1
factorial = 1
while i <= x:
    factorial *= i
    i += 1
print(f'{x} factorial is {factorial}')

"""FOR LOOPS
for <variable> in <sequence>:
<block of code>
For loops are great for:
- looping over a range of numbers
- looping through characters in a string"""

"""mysum is the variable to store the running sum
range(10) makes i be 0 then 1, 2 ..... ,9 """

mysum = 0 
for i in range (10):
    mysum += i
print(mysum)

"""Fix the code to use variable start and end in the range, to get the total sum between and including those values. 
Example: start = 3, end = 5 and sum should be 12 """

mysum = 0
start = 3
end = 5
for i in range(start, end+1):
    mysum += i
print(mysum)

"""Find 4!
i is our loop variable
factorial keeps the track of the product """

x = 4
factorial = 1
for i in range(1, x+1, 1):
    factorial *= i
print(f'{x} factorial is {factorial}')