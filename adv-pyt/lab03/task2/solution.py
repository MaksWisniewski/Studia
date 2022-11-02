# maksymilian wisniewski

# Imperative approach


def perfect_imper(n):
    solution = []
    for i in range(1, n):
        temp = 0
        for j in range(1, i):
            if i % j == 0:
                temp += j

        if temp == i:
            solution.append(i)

    return solution


# List comprehension


def perfect(n):
    return [x for x in range(1, n) if x == sum([y for y in range(1, x) if x % y == 0])]


# Functional approach, in order to get use of filter(), we need to define predicte


def is_perfect(n):
    return n == sum(list(filter(lambda x: n % x == 0, range(1, n))))


def perfect_fun(n):
    return list(filter(is_perfect, range(1, n)))
