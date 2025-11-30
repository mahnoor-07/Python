# Lecture 7 - Decomposition, Abstraction and Functio

# A function that has one argument and and returns one value
def is_even(i):
    if i%2 == 0:
        return True
    else:
        return False
    
# calling the function 
print(is_even(3))
print(is_even(8))

# Write the code that satisfies the following specs
def div_by(n, d):
        if n % d == 0:
            return True
        else:
            return False
        
print(div_by(10, 3))
print(div_by(195, 13))

# Inserting the fuction in a code
for i in range(1,10):
    if is_even(i):
          print(i, "even")
    else:
         print(i, "odd")

# write a program to add odd integers between (and including) a and b
def sum_odd(a, b):
     sum_of_odd = 0
     for i in range(a, b+1):
          if i % 2 == 1:
            sum_of_odd += i
     return sum_of_odd

print(sum_odd(2,7))