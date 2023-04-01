'''
CSC263 Winter 2023
Problem Set 4 Starter Code
University of Toronto Mississauga
'''

# Do NOT add any "import" statements

def isInside(m, n, curr_col, curr_row, move_col, move_row):
    return 0 <= curr_row + move_row <= m - 1 and 0 <= curr_col + move_col <= n - 1

def generate_min_moves(m, n, t_col, t_row):
    # m = rows
    # n = cols
    array = [[None] * n] * m

    array[t_col][t_row] = 0

    possible_moves = [(2, 1), (1, 2), (-1, 2), (2, -1), (-2, 1), (1, -2), (-2, -1), (-1, -2)]
    q = [(t_col, t_row)]
    while q:
        u = q.pop(0)
        for move in possible_moves:
            if isInside(m, n, u[0], u[1], move[0], move[1]) and array[u[0] + move[0]][u[1] + move[1]] is not None:
                array[u[0] + move[0]][u[1] + move[1]] = array[u[0]][u[1]] + 1
                q.append((u[0] + move[0], u[1] + move[1]))
    return array

def move_bahar(bahar_col, bahar_row, ncols):
    if bahar_col < ncols - 1:
        bahar_col += 1
    bahar_row += 1
    return bahar_col, bahar_row

def catch_me_if_you_can(nrows, ncols, bahar_row, bahar_col, tingting_row, tingting_col):
    '''Return the appropriate string, as described in the handout.

    nrows: number of rows in the board
    ncols: number of columns in the board
    bahar_row/bahar_col: Bahar's starting location
    tingting_row/tingting_col: Tingting's starting location
    '''
    array = generate_min_moves(nrows, ncols, tingting_col, tingting_row)

    bahar_pos = (bahar_col, bahar_row)
    moves = 0

    while bahar_pos[1] != nrows - 1:
        bahar_pos = move_bahar(bahar_pos[0], bahar_pos[1], ncols)
        moves += 1

        if array[bahar_pos[0]][bahar_pos[1]] == moves:
            return "Tingting wins in " + str(moves) + " moves"
        elif array[bahar_pos[0]][bahar_pos[1]] < moves:
            # check if tingting CAN catch up
            min_moves = array[bahar_pos[0]][bahar_pos[1]]
            if (moves - min_moves) % 2 == 0:
                return "Tingting wins in " + str(moves) + " moves"
    return "Bahar wins in " + str(moves) + " moves"

if __name__ == '__main__':

    # some small test cases
    # Case 1, Tingting wins in 2 moves
    s = catch_me_if_you_can(50, 50, 10, 10, 10, 12)
    print(s)
    assert s == 'Tingting wins in 2 moves'
    # Case 2, Bahar wins in 1 moves
    s = catch_me_if_you_can(6, 8, 3, 3, 0, 0)
    print(s)
    assert s == 'Bahar wins in 1 moves'

    s = catch_me_if_you_can(1000, 1000, 800, 800, 700, 700) #should return Bahar wins in 198 moves
    print(s)
    assert s == 'Bahar wins in 198 moves'
    s = catch_me_if_you_can(1100, 1100, 800, 800, 700, 700) #should return Tingting  wins in 200 moves
    print(s)
    assert s == 'Tingting wins in 200 moves'

