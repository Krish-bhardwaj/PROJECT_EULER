import eulerlib, itertools

print(next(itertools.islice(filter(eulerlib.is_prime, itertools.count(2)), 10000, None)))
