import itertools


def compute():
    DIGITS = 1000
    prev = 1
    cur = 0
    for i in itertools.count():
        if len(str(cur)) > DIGITS:
            raise RuntimeError("Not found")
        elif len(str(cur)) == DIGITS:
            return str(i)
        prev, cur = cur, prev + cur


if __name__ == "__main__":
    print(compute())