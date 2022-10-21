attendance = ["Martin", "Marcin", "Łukasz", "Paweł "]

first = True
for name in attendance:
    if not first:
        print(", ", end='')
    first = False
    print(name, end='')
