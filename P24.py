import itertools
print("".join(str(x) for x in next(itertools.islice(itertools.permutations(list(range(10))), 999999, None))))