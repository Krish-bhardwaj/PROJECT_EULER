if __name__ == "__main__":
    D_S = [0] * 10000
    for i in range(1, len(D_S)):
        for j in range(i * 2, len(D_S), i):
            D_S[j] += i
    ans = 0
    for i in range(1, len(D_S)):
        j = D_S[i]
        if j != i and j < len(D_S) and D_S[j] == i:
            ans += i
    print(str(ans))
