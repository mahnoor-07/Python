# # Lecture 6 - Bisection Search

# # Fast Square Root
# x = 36
# epsilon = 0.01
# num_guess = 0

# # initialize endpoints and guess
# low = 0
# high = x
# guess = (high + low)/2.0

# while abs(guess**2 - x) >= epsilon:
#     # what is repeated each time?
#     if guess**2 < x:
#         low = guess 
#     else:
#         high = guess
#     guess = (high + low)/2.0
#     # Make a new guess using the new endpoints
#     num_guess += 1
# print("num_guesses = ", num_guess)
# print(guess, "is close to square root of", x)

# # Find the cube root of positive cubes with in epsilon
# cube = 27 
# epsilon = 0.01
# low = 0
# high = cube
# guess = (high+low)/2
# while abs(guess**3-cube) > epsilon:
#     if guess**3 > cube:
#         high = guess 
#     else:
#         low = guess
#     guess = (high + low)/2

# print(guess)

# Newton-Raphson Root Finder
epsilon = 0.01
k = 24.0
guess = k/2.0
num_guesses = 0

while abs(guess*guess - k) >= epsilon:
    num_guesses += 1
    guess = guess - (((guess**2) - k)/(2*guess))
print("num_guesses = " + str(num_guesses))
print("Square root of "+ str(k) + "is about " + str(guess))