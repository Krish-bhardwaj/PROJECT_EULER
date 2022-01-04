def func(n):
    count = 0
    for i in range(n):
        if(i%15 == 0):
            count+=i
            continue
        if(i%3 == 0):
            count+=i
            continue
        if(i%5 == 0):
            count+=i
            continue
    return count

print(func(1000))