from math import *


# Function to calculate the number of divisors of integer n
def divisors(n):
    limit = int(sqrt(n))
    divisors_list = []
    for i in range(1, limit + 1, 1):
        if n % i == 0:
            divisors_list.append(i)
            if i != n / i:
                divisors_list.append(n / i)
    return len(divisors_list)


# Function to check for triangle number
def isTriangleNumber(n):
    a = int(sqrt(2 * n))
    return 0.5 * a * (a + 1) == n


# Function to calculate the last term of the series adding up to the triangle number
def lastTerm(n):
    if isTriangleNumber(n):
        return int(sqrt(2 * n))
    else:
        return None