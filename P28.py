
if __name__ == "__main__":
	print(sum(4 * i * i - 6 * (i - 1) for i in range(3, 1001 + 1, 2))+1)