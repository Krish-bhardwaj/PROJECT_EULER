import eulerlib, sys

def CCL(x): # Collatz chain length
    if x == 1:
        return 1
    if x % 2 == 0:
        y = x // 2
    else:
        y = x * 3 + 1
    return CCL(y) + 1
def solve():
    sys.setrecursionlimit(3000)
    ans = max(range(1, 1000000), key=CCL)
    return str(ans)

if __name__ == "__main__":
    print(solve())
