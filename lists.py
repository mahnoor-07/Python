# Palindrome Check

list1 = [1, 2, 1]   # Palindrome means same forward & backward
copy_list1 = list1.copy()
copy_list1.reverse()

if copy_list1 == list1:
    print("Palindrome")
else:
    print("Not Palindrome")

print("----------------------------------")

# Count Grade "A"

grade = ["C", "D", "A", "A", "B", "B", "A"]
print("Count of A:", grade.count("A"))

print("----------------------------------")

# Sort the List

grade.sort()
print("Sorted grades:", grade)
