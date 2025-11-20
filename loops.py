# 1. For Loop

print("Counting from 1 to 5:")
for i in range(1, 6):
    print(i)

print("\n")

# 2. For Loop with List

fruits = ["apple", "banana", "mango", "orange"]

print("Fruits list:")
for fruit in fruits:
    print(fruit)

print("\n")

# 3. While Loop (Simple Counter)

count = 1
print("While loop from 1 to 5:")
while count <= 5:
    print(count)
    count += 1

print("\n")

# 4. Break Statement

print("Break example:")
for i in range(1, 10):
    if i == 5:
        print("Loop stopped at:", i)
        break
    print(i)

print("\n")

# 5. Continue Statement

print("Continue example:")
for i in range(1, 10):
    if i % 2 == 0:
        continue    # skip even numbers
    print("Odd number:", i)

print("\n")

# 6. Nested Loops

print("Nested loop (rows and columns):")
for row in range(1, 4):
    for col in range(1, 4):
        print(f"({row}, {col})")
    print()

# 7. Sum of numbers using loop

n = int(input("Enter a number to find the sum from 1 to n: "))
total = 0

for i in range(1, n + 1):
    total += i

print("Total sum is:", total)
