from solution import *
from timeit import timeit


it = 5
start = 1000
end = 10001
step = 1250 * 2

# test
if __name__ == "__main__":

    print(
        " " * (len(str(end)) - 1) + "N ",
        "Imperative ",
        "List comprehension ",
        "Functional",
    )

    for n in range(start, end, step):
        ti = timeit(lambda: primes_imperative(n), number=it)
        tl = timeit(lambda: primes(n), number=it)
        tf = timeit(lambda: filter_primes(n), number=it)
        print(
            " " * (len(str(end)) - len(str(n)))
            + f"{n}: {ti:10.4f} {tl:19.4f} {tf:11.4f}"
        )
