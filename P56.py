def sum_of_digits(n):
    sod = 0
    while n != 0:
        sod += n % 10
        n //= 10
    return sod

largest = 0

for a in range(0, 100):
    for b in range(0, 100):
        sod = sum_of_digits(a**b)
        if sod > largest:
            largest = sod

print(largest)
