# Lecture 09 - Lambda Functions, Tuples and Lists

# Anonymous Function
"""Lambda function is the one-time use function. it can't be reused because it as no name"""

print("Number is even or not: ",(lambda x: x%2 == 0)(8))

# Tuples
"""Indexable ordered sequence of objects.
Cannot change elements values, immutable"""

seq = (2, 'a', 4, (1,2))

print(len(seq))       # 4
print(seq[3])         # (1,2)
print(seq[-1])        # (1,2)
print(seq[3] [0])     # 1
# print(seq[4])         # error

# Iterating over sequences
for e in seq:
    print(e)

# It can be used to return more than one value from the function
def quotient_and_reminder(x, y):
    q = x // y
    r = x % y
    return(q, r)

both = quotient_and_reminder(10, 3)
print("both: ", both)
(quot, rem) = quotient_and_reminder(5, 2)
print("quotient is: ", quot)
print("reminder is: ", rem)

# Lists
"""Indexeble ordered sequences of objects
Mutable mean you can change the value of specific elements of the list"""

l = [2, 'a', 4, [1,2]]

# iterating over the list
def list_sum(L):
    total = 0
    for e in L:
        total += e
    return(total)
list_sum([1,3,5])