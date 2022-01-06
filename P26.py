import itertools

def reciprocal_cycle_len(n):
    seen = {}
    x = 1
    for i in itertools.count():
        if x in seen:
            return i - seen[x]
        else:
            seen[x] = i
            x = x * 10 % n

if __name__ == "__main__":
    print(str(max(range(1, 1000), key=reciprocal_cycle_len)))
