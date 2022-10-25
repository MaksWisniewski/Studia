def floor_of_sqrt(n):
    total, i = 0, 0
    while total <= n:
        i = i + 1
        total += 2*i - 1
    return i - 1


from pprint import pprint

if __name__ == "__main__":
    if len
    A = [floor_of_sqrt(i*i) for i in range (1, 14)]
    pprint(A)
