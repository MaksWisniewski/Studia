"""
Maksyilian Wiśniewski, task3: multiplication table

Unfortunately, I had no clue how to create tests for this task.
I gave it just a stare to look if it is pretty printed.

"""

# The more pythonic way of declaring two dimensional multilpication table.
# Those two functions below, create 'multiplication tables' as the assigment told so.

def mult_table_1(a, b, c, d):
    return [[i*j for i in range(a, b+1)] for j in range(c,d+1)]

def mult_table_2(a, b, c, d):
    return list(list(range(a*i, (b+1)*i, i)) for i in range(c, d+1))

# Function print_table takes an optional argument i.e a function that generates a multplication table
def print_table(a, b, c, d, function=mult_table_1):
    table = function(a, b, c, d)
    # Size is the lenght of the biggest number in that table
    size = len(str(table[-1][-1])) + 1

    for row in table:
        # rjust method prepends the string with whitespaces
        # row is string made by concatenation of all numbers from that row, previously prepared.
        row = [str(j).rjust(size) for j in row]
        print(''.join(row))


if __name__ == "__main__":
    print('-' * 90)
    print_table(1, 10, 1, 10)
    print('-' * 90)
    print_table(10, 13, 1, 4, mult_table_2)
    print('-' * 90)
    print_table(1, 2, 2, 2)
    print('-' * 90)
    print_table(1, 2, 1, 2)
    print('-' * 90)
    print_table(1, 1, 1, 1)