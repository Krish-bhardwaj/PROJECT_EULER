def compute():

	ans = sum(i for i in range(1, 10000) if has_pandigital_product(i))
	return str(ans)


def has_pandigital_product(n):
	for i in range(1, sqrt(n) + 1):
		if n % i == 0:
			temp = str(n) + str(i) + str(n // i)
			if "".join(sorted(temp)) == "123456789":
				return True
	return False

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