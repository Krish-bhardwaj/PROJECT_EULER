def is_prime(n):
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

i = 0

gap = 1

ratio = 1

primes = []

all_numbers = [1]

while ratio > 0.1:
    for j in range(4):
        i += gap
        present_number = 2*i + 1
        all_numbers.append(present_number)
        if is_prime(present_number):
            primes.append(2*i + 1)
    ratio = float(len(primes))/len(all_numbers)
    gap += 1

print ((2*i+1)**0.5)