from solution import *
from timeit import timeit


it = 10
start = 1000
end = start * 3 // 2
step = (end - start) // it

# test
if __name__ == "__main__":

    print(
        " " * (len(str(end)) - 1) + "N ",
        "Imperative ",
        "List comprehension ",
        "Functional",
    )

    for n in range(start, end, step):
        ti = timeit(lambda: perfect_imper(n), number=it)
        tl = timeit(lambda: perfect(n), number=it)
        tf = timeit(lambda: perfect_fun(n), number=it)
        print(
            " " * (len(str(end)) - len(str(n)))
            + f"{n}: {ti:10.4f} {tl:19.4f} {tf:11.4f}"
        )
