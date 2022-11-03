# Maksymilian Wiśniewski
# Task: implement a function that generates a list of all primes less or equal than n.


# Iterative approach using sieve of Eratostenes.

from math import sqrt
from math import floor


def primes_imperative(n):
    if n <= 1:
        return []
        
    is_prime = [True] * (1+n)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, floor(sqrt(n+1)) + 1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    
    # I've used here list comprehension in order to write more tidy 
    # code, but i think that could be also written using more basic for loop.
    return [i for i, x in enumerate(is_prime) if x]

# List comprehension technique.
# Naïve approach, number is prime when it's not divisible by any number except one and itself.

def primes(n):
    return [x for x in range(2, n+1) if x == 2 or x == 3 or all(x % y != 0 for y in range(2, floor(sqrt(x))+1))]

# Functional approach

# In order to get use of filter() funciton we need to create a predicate function i.e funciton that 
# gets natural number as an angurment and returns boolean value.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def filter_primes(n):
    return list(filter(is_prime, range(n+1)))
