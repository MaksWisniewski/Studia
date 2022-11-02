# Maksymilian Wiśniewski
# Task: implement a function that generates a list of all primes less or equal than n.

# Iterative approach using sieve of Eratostenes.

from math import sqrt
from math import floor

# I assume imput for those funcitons below are only natural numbers.


def primes_imperative(n):
    if n <= 1:
        return []

    primes = [True for i in range(n + 1)]
    primes[0] = primes[1] = False

    p = 2
    while p <= floor(sqrt(n)) + 1:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False

        p += 1

    return [i for i, x in enumerate(primes) if x]


# List comprehension technique.
# Naïve approach, number is prime when it's not divisible by any number except one and itself.


def primes(n):
    n += 1
    return [
        x
        for x in range(2, n)
        if x == 2 or x == 3 or all(x % y != 0 for y in range(2, floor(sqrt(n)) + 1))
    ]


# Functional approach

# In order to get use of filter() funciton we need to create a predicate function i.e funciton that
# gets natural number as an angurment and returns boolean value.


def is_prime(n):
    if n == 2:
        return True
    elif n == 0 or n == 1:
        return False

    for i in range(2, floor(sqrt(n)) + 1):
        if (n % i) == 0:
            return False
    return True


# function filter takes predicate as it's first arguemts and iterable? as second argument


def filter_primes(n):
    return list(filter(is_prime, range(1, n + 1)))


if __name__ == "__main__":
    print(filter_primes(14))
