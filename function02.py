# Lecture 08 - Function as Objects

# Function supports Modularity
def bisection_root(x):
    epsilon = 0.01
    low = 0
    high = x
    ans = (high + low) / 2.0

    # Repeated steps inside loop
    while abs(ans**2 - x) >= epsilon:
        if ans**2 < x:
            low = ans
        else:
            high = ans

        ans = (high + low) / 2.0   

    return ans

# print(bisection_root(4))

# ================================================================

def count_num_with_sqrt_close_to(n, epsilon):
    count = 0
    for i in range(n**3):
        sqrt = bisection_root(i)
        if abs(n-sqrt) < epsilon:
            print(i, sqrt)
            count += 1
    return count

# print(count_num_with_sqrt_close_to(10, 0.1))

# ===============================================================

def apply(criteria, n):
    count = 0
    for i in range(n+1):
        if criteria(i):
            count += 1
    return count

def is_even(x):
    return x % 2 == 0

howmany = apply(is_even, 10)
print(howmany)