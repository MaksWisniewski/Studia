# Maksymilian Wiśniewski

# function solve get's as input any list of list of lenght defined in the
# description of a task i.e 9 x 9


def solve(bo):
    # find is either empty or pair of not assigned value in the board
    find = find_empty(bo)
    if not find:
        # this means that board is full, -> add result to the generator
        yield bo
    else:
        row, col = find

        for i in range(1, 10):
            if valid(bo, i, (row, col)):
                bo[row][col] = i

                for X in solve(bo):
                    # if X is not empty and is propertly defined,
                    # such that it aggres with description of a task
                    if X and is_proper(X) is True:
                        yield X

                bo[row][col] = 0

        yield None


# returns true if board after insertion of a num meets with the inital conditions
def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True


# is_proper [board] check if the result is proper according to the rules.
# that means each number from 1 to 9 is in 3x3 box, in each horizontal line
# and each vertical column


def is_proper(bo):
    for i in range(4):
        for j in range(4):
            temp = set()

            square_x, square_y = (i // 3) * 3, (j // 3) * 3
            for a in range(square_x, square_x + 3):
                for b in range(square_y, square_y + 3):
                    temp.add(bo[a][b])

            if len(temp) != 9:
                return False

    for i in range(9):
        temp = set()
        for j in range(9):
            temp.add(bo[i][j])

        if len(temp) != 9:
            return False

    for i in range(9):
        temp = set()
        for j in range(9):
            temp.add(bo[j][i])

        if len(temp) != 9:
            return False

    return True


def print_board(bo):
    if bo is None:
        return

    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

    print("\n")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None
