from math import factorial as f

counter = 0

for n in range(23, 101):
    for r in range(4, n-3):
        if (f(n)/(f(r)*f(n-r))) > 1000000:
            counter += 1

print (counter)