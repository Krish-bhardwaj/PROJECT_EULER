from math import factorial
def solve(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))
print(solve(20 + 20, 20))

