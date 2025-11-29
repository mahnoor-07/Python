
# Lecture 5 – Floats and Approximation

# Converting a decimal fraction (base-10) into binary (base-2)
x = 0.625       # Decimal number to convert

"""Find the smallest power of 2 that turns x into an integer
We keep multiplying by 2 until the fractional part becomes 0"""

p = 0
while ((2**p) * x) % 1 != 0:
    remainder = (2**p) * x - int((2**p) * x)
    print("Remainder =", remainder)    # Shows approximation issues
    p += 1

# Convert the scaled number into an integer
num = int(x * (2**p))

# Convert the integer into binary manually
result = ''
if num == 0:
    result = '0'

while num > 0:
    result = str(num % 2) + result    # Extract last bit
    num //= 2                         # Shift right (integer division)

# Pad leading zeros if needed
while len(result) < p:
    result = '0' + result

# Insert decimal point p places from the right
binary_result = result[:-p] + "." + result[-p:]
print("The binary representation of", x, "is", binary_result)

# ================================================================================

"""Approximation Method for Finding Square Root
Using incremental guessing (exhaustive enumeration)"""
x = 36                 
epsilon = 0.01         
guess = 0.0            
num_guess = 0          
increment = 0.0001     

"""Keep increasing the guess until the square of the guess is
within epsilon (acceptable error) of the target number x.
This loop may take many iterations depending on increment."""
while abs(guess**2 - x) >= epsilon:
    guess += increment     
    num_guess += 1         

print(f"num_guesses = {num_guess}")   
print(f"{guess} is close to the square root of {x}")  
