import itertools

def compute():
    ans = sum(itertools.islice(filter(is_truncatable_prime, itertools.count(10)), 11))
    return str(ans)


def is_truncatable_prime(n):
    # Test if left-truncatable
    i = 10
    while i <= n:
        if not is_prime(n % i):
            return False
        i *= 10

    # Test if right-truncatable
    while n > 0:
        if not is_prime(n):
            return False
        n //= 10
    return True

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

# Tests whether the given integer is a prime number.
def is_prime(x):
	if x <= 1:
		return False
	elif x <= 3:
		return True
	elif x % 2 == 0:
		return False
	else:
		for i in range(3, sqrt(x) + 1, 2):
			if x % i == 0:
				return False
		return True

if __name__ == "__main__":
    print(compute())
