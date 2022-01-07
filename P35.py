
def compute():
    isprime = list_primality(999999)

    def is_circular_prime(n):
        s = str(n)
        return all(isprime[int(s[i:] + s[: i])] for i in range(len(s)))

    ans = sum(1
              for i in range(len(isprime))
              if is_circular_prime(i))
    return str(ans)


def list_primality(n):
	result = [True] * (n + 1)
	result[0] = result[1] = False
	for i in range(sqrt(n) + 1):
		if result[i]:
			for j in range(i * i, len(result), i):
				result[j] = False
	return result


def sqrt(x):
	assert x >= 0
	i = 1
	while i * i <= x:
		i *= 2
	y = 0
	while i > 0:
		if (y + i)**2 <= x:
			y += i
		i //= 2
	return y


if __name__ == "__main__":
    print(compute())
