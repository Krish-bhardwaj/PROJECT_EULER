
if __name__ == "__main__":
    LIMIT = 28124
    divisorsum = [0] * LIMIT
    for i in range(1, LIMIT):
        for j in range(i * 2, LIMIT, i):
            divisorsum[j] += i
    op = [i for (i, x) in enumerate(divisorsum) if x > i]
    expressible = [False] * LIMIT
    for i in op:
        for j in op:
            if i + j < LIMIT:
                expressible[i + j] = True
            else:
                break
    print(sum(i for (i, x) in enumerate(expressible) if not x))