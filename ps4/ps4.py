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
    array = [[None for j in range(n)] for i in range(m)]

    array[t_row][t_col] = 0

    possible_moves = [(2, 1), (1, 2), (-1, 2), (2, -1), (-2, 1), (1, -2), (-2, -1), (-1, -2)]
    q = [(t_row, t_col)]
    while q:
        u = q.pop(0)
        for move in possible_moves:
            if isInside(m, n, u[1], u[0], move[1], move[0]) and array[u[0] + move[0]][u[1] + move[1]] is None:
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

    if(nrows == 3 == ncols): #funny edge case where knight might not be able to visit entire board.
        if tingting_row == 1 == tingting_col:
            return "Bahar wins in " + str(1 - bahar_row) + " moves"
        else: array[1][1] = 10

    bahar_pos = (bahar_col, bahar_row)
    moves = 0

    while bahar_pos[1] != nrows - 1:
        bahar_pos = move_bahar(bahar_pos[0], bahar_pos[1], ncols)
        moves += 1

        if(bahar_pos[1] == nrows - 1):
            break

        if array[bahar_pos[1]][bahar_pos[0]] == moves:
            return "Tingting wins in " + str(moves) + " moves"
        elif array[bahar_pos[1]][bahar_pos[0]] < moves:
            # check if tingting CAN catch up
            min_moves = array[bahar_pos[1]][bahar_pos[0]]
            if (moves - min_moves) % 2 == 0:
                return "Tingting wins in " + str(moves) + " moves"
    return "Bahar wins in " + str(moves-1) + " moves"

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

    s = catch_me_if_you_can(24, 56, 6, 12, 17, 31)
    print(s)
    assert s == "Tingting wins in 8 moves"
    s = catch_me_if_you_can(9, 82, 1, 50, 2, 81)
    assert s == "Bahar wins in 6 moves"
    s = catch_me_if_you_can(55, 31, 52, 24, 29, 7)
    assert s == "Bahar wins in 1 moves"
    s = catch_me_if_you_can(25, 22, 23, 10, 2, 0)
    assert s == "Bahar wins in 0 moves"
    s = catch_me_if_you_can(65, 90, 22, 27, 5, 29)
    assert s == "Tingting wins in 17 moves"
    s = catch_me_if_you_can(36, 14, 1, 13, 0, 11)
    assert s == "Bahar wins in 33 moves"
    s = catch_me_if_you_can(44, 58, 12, 57, 29, 25)
    assert s == "Bahar wins in 30 moves"
    s = catch_me_if_you_can(99, 83, 2, 65, 83, 52)
    assert s == "Bahar wins in 95 moves"
    s = catch_me_if_you_can(60, 44, 25, 32, 25, 43)
    assert s == "Tingting wins in 5 moves"
    s = catch_me_if_you_can(72, 37, 26, 23, 53, 33)
    assert s == "Tingting wins in 9 moves"
    s = catch_me_if_you_can(31, 5, 3, 2, 10, 3)
    assert s == "Tingting wins in 3 moves"
    s = catch_me_if_you_can(38, 98, 13, 84, 37, 8)
    assert s == "Bahar wins in 23 moves"
    s = catch_me_if_you_can(14, 93, 2, 83, 13, 24)
    assert s == "Bahar wins in 10 moves"
    s = catch_me_if_you_can(63, 83, 24, 13, 28, 70)
    assert s == "Tingting wins in 19 moves"
    s = catch_me_if_you_can(41, 57, 12, 41, 33, 26)
    assert s == "Bahar wins in 27 moves"
    s = catch_me_if_you_can(94, 88, 22, 28, 46, 60)
    assert s == "Tingting wins in 12 moves"
    s = catch_me_if_you_can(21, 90, 0, 31, 6, 6)
    assert s == "Bahar wins in 19 moves"
    s = catch_me_if_you_can(49, 81, 0, 9, 33, 22)
    assert s == "Tingting wins in 12 moves"

    s = catch_me_if_you_can(62, 8, 46, 0, 31, 0)
    print(s)
    assert s == "Bahar wins in 14 moves"
    s = catch_me_if_you_can(11, 47, 5, 27, 4, 24)
    assert s == "Tingting wins in 4 moves"
    s = catch_me_if_you_can(51, 61, 16, 35, 25, 22)
    assert s == "Tingting wins in 14 moves"
    s = catch_me_if_you_can(4, 30, 0, 21, 0, 12)
    assert s == "Bahar wins in 2 moves"
    s = catch_me_if_you_can(86, 74, 37, 28, 3, 14)
    assert s == "Bahar wins in 47 moves"
    s = catch_me_if_you_can(76, 66, 39, 33, 44, 58)
    assert s == "Tingting wins in 10 moves"
    s = catch_me_if_you_can(88, 19, 31, 3, 67, 1)
    assert s == "Tingting wins in 14 moves"
    s = catch_me_if_you_can(5, 51, 3, 46, 0, 13)
    assert s == "Bahar wins in 0 moves"
    s = catch_me_if_you_can(60, 93, 57, 84, 31, 14)
    assert s == "Bahar wins in 1 moves"
    s = catch_me_if_you_can(41, 76, 2, 62, 31, 50)
    assert s == "Tingting wins in 14 moves"
    s = catch_me_if_you_can(89, 80, 45, 74, 88, 26)
    assert s == "Tingting wins in 27 moves"
    s = catch_me_if_you_can(9, 50, 2, 35, 8, 25)
    assert s == "Bahar wins in 5 moves"
    s = catch_me_if_you_can(75, 84, 12, 0, 68, 9)
    assert s == "Tingting wins in 19 moves"
    s = catch_me_if_you_can(94, 100, 2, 12, 72, 51)
    assert s == "Tingting wins in 25 moves"
    s = catch_me_if_you_can(93, 21, 36, 3, 46, 11)
    assert s == "Tingting wins in 4 moves"
    s = catch_me_if_you_can(92, 60, 6, 49, 26, 53)
    assert s == "Tingting wins in 8 moves"
    s = catch_me_if_you_can(83, 14, 76, 0, 22, 12)
    assert s == "Bahar wins in 5 moves"
    s = catch_me_if_you_can(84, 20, 4, 11, 32, 13)
    assert s == "Tingting wins in 10 moves"
    s = catch_me_if_you_can(57, 11, 34, 6, 29, 5)
    assert s == "Tingting wins in 5 moves"
    s = catch_me_if_you_can(95, 29, 68, 8, 86, 12)
    assert s == "Tingting wins in 6 moves"
    s = catch_me_if_you_can(50, 35, 39, 16, 6, 31)
    assert s == "Bahar wins in 9 moves"
    s = catch_me_if_you_can(68, 67, 42, 1, 27, 65)
    assert s == "Bahar wins in 24 moves"
    s = catch_me_if_you_can(74, 10, 11, 2, 69, 4)
    assert s == "Bahar wins in 61 moves"
    s = catch_me_if_you_can(99, 27, 16, 8, 68, 19)
    assert s == "Bahar wins in 81 moves"
    s = catch_me_if_you_can(60, 90, 45, 40, 3, 1)
    assert s == "Bahar wins in 13 moves"
    s = catch_me_if_you_can(79, 99, 68, 68, 34, 9)
    assert s == "Bahar wins in 9 moves"
    s = catch_me_if_you_can(47, 85, 2, 69, 18, 82)
    assert s == "Tingting wins in 7 moves"
    s = catch_me_if_you_can(24, 59, 7, 13, 18, 18)
    assert s == "Tingting wins in 4 moves"
    s = catch_me_if_you_can(46, 99, 24, 86, 9, 92)
    assert s == "Bahar wins in 20 moves"
    #s = catch_me_if_you_can(27, 1, 2, 0, 18, 0)
   # assert s == "Bahar wins in 23 moves"
    s = catch_me_if_you_can(9, 24, 4, 7, 8, 19)
    assert s == "Bahar wins in 3 moves"
    s = catch_me_if_you_can(8, 72, 2, 0, 6, 3)
    assert s == "Tingting wins in 3 moves"
    s = catch_me_if_you_can(61, 20, 14, 12, 31, 7)
    assert s == "Bahar wins in 45 moves"
    #s = catch_me_if_you_can(99, 2, 46, 0, 87, 1)
    #assert s == "Bahar wins in 51 moves"
    s = catch_me_if_you_can(29, 34, 11, 24, 9, 2)
    assert s == "Bahar wins in 16 moves"
    s = catch_me_if_you_can(37, 86, 11, 14, 14, 4)
    assert s == "Tingting wins in 11 moves"
    s = catch_me_if_you_can(48, 61, 11, 26, 29, 55)
    assert s == "Tingting wins in 11 moves"
    s = catch_me_if_you_can(8, 62, 4, 39, 6, 42)
    assert s == "Tingting wins in 1 moves"
    s = catch_me_if_you_can(96, 18, 92, 17, 59, 2)
    assert s == "Bahar wins in 2 moves"
    s = catch_me_if_you_can(85, 64, 48, 31, 29, 14)
    assert s == "Tingting wins in 34 moves"
    #s = catch_me_if_you_can(68, 2, 15, 1, 36, 0)
    #assert s == "Tingting wins in 7 moves"
    s = catch_me_if_you_can(20, 25, 13, 4, 13, 21)
    assert s == "Bahar wins in 5 moves"
    s = catch_me_if_you_can(65, 94, 13, 90, 25, 19)
    assert s == "Tingting wins in 37 moves"
    s = catch_me_if_you_can(24, 85, 16, 18, 7, 36)
    assert s == "Bahar wins in 6 moves"
    s = catch_me_if_you_can(72, 57, 58, 4, 50, 14)
    assert s == "Tingting wins in 8 moves"
    s = catch_me_if_you_can(76, 64, 65, 22, 51, 11)
    assert s == "Bahar wins in 9 moves"
    s = catch_me_if_you_can(81, 35, 70, 18, 72, 23)
    assert s == "Tingting wins in 3 moves"
    s = catch_me_if_you_can(7, 48, 1, 24, 1, 41)
    assert s == "Bahar wins in 4 moves"
    s = catch_me_if_you_can(76, 65, 8, 37, 50, 12)
    assert s == "Tingting wins in 25 moves"
    s = catch_me_if_you_can(89, 70, 34, 44, 2, 62)
    assert s == "Bahar wins in 53 moves"
    s = catch_me_if_you_can(17, 69, 12, 53, 11, 22)
    assert s == "Bahar wins in 3 moves"
    s = catch_me_if_you_can(39, 72, 23, 26, 15, 50)
    assert s == "Tingting wins in 12 moves"
    s = catch_me_if_you_can(46, 44, 27, 35, 43, 38)
    assert s == "Tingting wins in 7 moves"
    s = catch_me_if_you_can(78, 30, 46, 8, 41, 29)
    assert s == "Tingting wins in 10 moves"
    s = catch_me_if_you_can(18, 21, 12, 4, 7, 6)
    assert s == "Bahar wins in 4 moves"
    s = catch_me_if_you_can(70, 82, 10, 27, 68, 68)
    assert s == "Tingting wins in 21 moves"
    s = catch_me_if_you_can(96, 73, 18, 62, 12, 41)
    assert s == "Bahar wins in 76 moves"
    s = catch_me_if_you_can(80, 30, 19, 7, 39, 14)
    assert s == "Tingting wins in 7 moves"
    s = catch_me_if_you_can(100, 28, 7, 21, 26, 18)
    assert s == "Tingting wins in 7 moves"
    s = catch_me_if_you_can(57, 56, 8, 8, 56, 1)
    assert s == "Tingting wins in 19 moves"
    s = catch_me_if_you_can(17, 90, 5, 86, 10, 56)
    assert s == "Bahar wins in 10 moves"
    s = catch_me_if_you_can(76, 69, 61, 7, 64, 51)
    assert s == "Bahar wins in 13 moves"
    s = catch_me_if_you_can(90, 95, 41, 0, 74, 49)
    assert s == "Tingting wins in 18 moves"
    s = catch_me_if_you_can(9, 17, 5, 5, 2, 9)
    assert s == "Bahar wins in 2 moves"
    s = catch_me_if_you_can(25, 95, 3, 41, 20, 70)
    assert s == "Tingting wins in 10 moves"
    s = catch_me_if_you_can(92, 10, 36, 8, 12, 9)
    assert s == "Tingting wins in 24 moves"
    s = catch_me_if_you_can(91, 18, 1, 8, 1, 13)
    assert s == "Tingting wins in 3 moves"
    s = catch_me_if_you_can(72, 24, 61, 15, 69, 23)
    assert s == "Tingting wins in 4 moves"
    s = catch_me_if_you_can(38, 23, 29, 9, 33, 22)
    assert s == "Tingting wins in 5 moves"
    s = catch_me_if_you_can(65, 42, 41, 5, 20, 29)
    assert s == "Tingting wins in 21 moves"
    s = catch_me_if_you_can(96, 3, 65, 0, 18, 1)
    assert s == "Bahar wins in 29 moves"
    s = catch_me_if_you_can(15, 4, 12, 1, 5, 3)
    assert s == "Bahar wins in 1 moves"
    s = catch_me_if_you_can(69, 66, 46, 6, 47, 32)
    assert s == "Tingting wins in 9 moves"
    #s = catch_me_if_you_can(28, 2, 20, 1, 13, 0)
    #assert s == "Bahar wins in 6 moves"
    s = catch_me_if_you_can(99, 93, 12, 67, 89, 9)
    assert s == "Tingting wins in 42 moves"
    s = catch_me_if_you_can(42, 65, 36, 21, 2, 57)
    assert s == "Bahar wins in 4 moves"
    s = catch_me_if_you_can(90, 10, 80, 2, 5, 1)
    assert s == "Bahar wins in 8 moves"
    s = catch_me_if_you_can(70, 91, 56, 34, 22, 67)
    assert s == "Bahar wins in 12 moves"
    s = catch_me_if_you_can(71, 75, 35, 58, 19, 7)
    assert s == "Bahar wins in 34 moves"
    s = catch_me_if_you_can(45, 73, 7, 58, 41, 7)
    assert s == "Bahar wins in 36 moves"
    s = catch_me_if_you_can(29, 89, 2, 55, 28, 0)
    assert s == "Bahar wins in 25 moves"
    s = catch_me_if_you_can(46, 67, 31, 66, 29, 2)
    assert s == "Bahar wins in 13 moves"
    s = catch_me_if_you_can(84, 20, 14, 12, 11, 7)
    assert s == "Bahar wins in 68 moves"
    s = catch_me_if_you_can(20, 27, 17, 4, 0, 14)
    assert s == "Bahar wins in 1 moves"
    s = catch_me_if_you_can(47, 71, 23, 7, 17, 6)
    assert s == "Tingting wins in 7 moves"
    s = catch_me_if_you_can(79, 15, 42, 1, 70, 14)
    assert s == "Tingting wins in 11 moves"
    s = catch_me_if_you_can(35, 52, 3, 14, 20, 17)
    assert s == "Tingting wins in 6 moves"
    s = catch_me_if_you_can(12, 33, 0, 4, 1, 2)
    assert s == "Tingting wins in 3 moves"
    s = catch_me_if_you_can(89, 88, 20, 56, 72, 6)
    assert s == "Bahar wins in 67 moves"
    s = catch_me_if_you_can(70, 64, 67, 27, 58, 60)
    assert s == "Bahar wins in 1 moves"
    s = catch_me_if_you_can(63, 92, 33, 11, 51, 40)
    assert s == "Tingting wins in 11 moves"
    s = catch_me_if_you_can(87, 68, 4, 11, 33, 33)
    assert s == "Tingting wins in 11 moves"
    s = catch_me_if_you_can(64, 61, 57, 57, 55, 23)
    assert s == "Bahar wins in 5 moves"
    s = catch_me_if_you_can(88, 32, 5, 23, 5, 3)
    assert s == "Tingting wins in 14 moves"
    s = catch_me_if_you_can(89, 47, 27, 28, 26, 10)
    assert s == "Bahar wins in 60 moves"
    s = catch_me_if_you_can(17, 45, 7, 12, 13, 21)
    assert s == "Tingting wins in 3 moves"
    s = catch_me_if_you_can(69, 43, 42, 35, 19, 1)
    assert s == "Bahar wins in 25 moves"
    s = catch_me_if_you_can(74, 19, 59, 8, 19, 3)
    assert s == "Bahar wins in 13 moves"
    s = catch_me_if_you_can(26, 54, 1, 23, 1, 7)
    assert s == "Tingting wins in 16 moves"
    s = catch_me_if_you_can(96, 83, 59, 68, 1, 65)
    assert s == "Bahar wins in 35 moves"
    s = catch_me_if_you_can(33, 89, 2, 31, 25, 38)
    assert s == "Tingting wins in 8 moves"
    s = catch_me_if_you_can(93, 23, 45, 0, 46, 4)
    assert s == "Tingting wins in 3 moves"
    s = catch_me_if_you_can(39, 52, 9, 41, 15, 29)
    assert s == "Tingting wins in 11 moves"
    s = catch_me_if_you_can(77, 95, 46, 87, 3, 17)
    assert s == "Bahar wins in 29 moves"
    s = catch_me_if_you_can(33, 58, 21, 21, 14, 31)
    assert s == "Tingting wins in 7 moves"
    s = catch_me_if_you_can(32, 65, 3, 17, 2, 33)
    assert s == "Tingting wins in 7 moves"
    s = catch_me_if_you_can(39, 69, 24, 42, 14, 48)
    assert s == "Tingting wins in 10 moves"
    s = catch_me_if_you_can(4, 41, 0, 0, 0, 21)
    assert s == "Bahar wins in 2 moves"
    s = catch_me_if_you_can(86, 85, 84, 27, 77, 1)
    assert s == "Bahar wins in 0 moves"
    s = catch_me_if_you_can(23, 30, 2, 13, 10, 3)
    assert s == "Tingting wins in 10 moves"
    s = catch_me_if_you_can(13, 38, 3, 7, 10, 4)
    assert s == "Tingting wins in 4 moves"
    s = catch_me_if_you_can(2, 91, 0, 1, 1, 48)
    assert s == "Bahar wins in 0 moves"
    s = catch_me_if_you_can(71, 24, 9, 3, 20, 14)
    assert s == "Tingting wins in 6 moves"
    s = catch_me_if_you_can(89, 25, 87, 5, 74, 1)
    assert s == "Bahar wins in 0 moves"
    s = catch_me_if_you_can(11, 22, 0, 21, 1, 5)
    assert s == "Bahar wins in 9 moves"
    s = catch_me_if_you_can(43, 24, 23, 14, 17, 9)
    assert s == "Tingting wins in 10 moves"
    s = catch_me_if_you_can(56, 14, 15, 8, 2, 2)
    assert s == "Tingting wins in 13 moves"
    s = catch_me_if_you_can(9, 59, 4, 57, 8, 26)
    assert s == "Bahar wins in 3 moves"
    s = catch_me_if_you_can(24, 12, 16, 6, 19, 2)
    assert s == "Tingting wins in 5 moves"
    s = catch_me_if_you_can(25, 69, 20, 66, 11, 28)
    assert s == "Bahar wins in 3 moves"
    s = catch_me_if_you_can(29, 31, 0, 12, 20, 29)
    assert s == "Tingting wins in 9 moves"
    s = catch_me_if_you_can(75, 13, 19, 11, 42, 9)
    assert s == "Tingting wins in 8 moves"
    s = catch_me_if_you_can(98, 35, 95, 12, 36, 29)
    assert s == "Bahar wins in 1 moves"
    s = catch_me_if_you_can(100, 69, 64, 29, 0, 7)
    assert s == "Bahar wins in 34 moves"
    s = catch_me_if_you_can(90, 44, 56, 29, 12, 14)
    assert s == "Bahar wins in 32 moves"
    s = catch_me_if_you_can(70, 72, 47, 70, 45, 1)
    assert s == "Bahar wins in 21 moves"
    s = catch_me_if_you_can(91, 35, 23, 27, 35, 31)
    assert s == "Tingting wins in 4 moves"
    s = catch_me_if_you_can(23, 36, 20, 6, 13, 10)
    assert s == "Bahar wins in 1 moves"
    s = catch_me_if_you_can(19, 78, 8, 1, 14, 64)
    assert s == "Bahar wins in 9 moves"
    s = catch_me_if_you_can(81, 83, 51, 23, 72, 65)
    assert s == "Tingting wins in 15 moves"
    s = catch_me_if_you_can(99, 100, 49, 71, 31, 24)
    assert s == "Bahar wins in 48 moves"
    s = catch_me_if_you_can(17, 36, 2, 11, 6, 22)
    assert s == "Tingting wins in 5 moves"
    s = catch_me_if_you_can(96, 12, 63, 9, 5, 5)
    assert s == "Bahar wins in 31 moves"
    s = catch_me_if_you_can(64, 52, 14, 22, 16, 7)
    assert s == "Tingting wins in 15 moves"
    s = catch_me_if_you_can(77, 3, 47, 2, 53, 1)
    assert s == "Bahar wins in 28 moves"
    s = catch_me_if_you_can(66, 98, 41, 28, 35, 80)
    assert s == "Tingting wins in 20 moves"
    s = catch_me_if_you_can(94, 97, 89, 92, 54, 19)
    assert s == "Bahar wins in 3 moves"
    s = catch_me_if_you_can(75, 91, 0, 53, 20, 71)
    assert s == "Tingting wins in 8 moves"
    s = catch_me_if_you_can(22, 85, 12, 82, 6, 49)
    assert s == "Bahar wins in 8 moves"
    s = catch_me_if_you_can(4, 5, 2, 2, 2, 0)
    assert s == "Bahar wins in 0 moves"
    s = catch_me_if_you_can(54, 17, 17, 9, 35, 9)
    assert s == "Tingting wins in 6 moves"
    s = catch_me_if_you_can(8, 43, 4, 25, 2, 27)
    assert s == "Tingting wins in 2 moves"
    s = catch_me_if_you_can(94, 53, 13, 49, 20, 5)
    assert s == "Tingting wins in 24 moves"
    s = catch_me_if_you_can(87, 71, 2, 41, 73, 43)
    assert s == "Tingting wins in 25 moves"
    s = catch_me_if_you_can(92, 69, 60, 56, 81, 40)
    assert s == "Bahar wins in 30 moves"
    #s = catch_me_if_you_can(21, 2, 9, 0, 1, 0)
    #assert s == "Bahar wins in 10 moves"
    s = catch_me_if_you_can(34, 22, 29, 14, 17, 9)
    assert s == "Bahar wins in 3 moves"
    #s = catch_me_if_you_can(4, 1, 1, 0, 0, 0)
    #assert s == "Bahar wins in 1 moves"
    s = catch_me_if_you_can(27, 92, 17, 13, 8, 6)
    assert s == "Bahar wins in 8 moves"
    s = catch_me_if_you_can(74, 22, 47, 1, 46, 2)
    assert s == "Tingting wins in 2 moves"
    s = catch_me_if_you_can(46, 30, 17, 17, 9, 19)
    assert s == "Tingting wins in 8 moves"
    s = catch_me_if_you_can(53, 54, 51, 6, 27, 44)
    assert s == "Bahar wins in 0 moves"
    s = catch_me_if_you_can(4, 34, 0, 19, 0, 29)
    assert s == "Bahar wins in 2 moves"
    s = catch_me_if_you_can(23, 34, 17, 21, 21, 5)
    assert s == "Bahar wins in 4 moves"
    s = catch_me_if_you_can(42, 54, 8, 25, 39, 21)
    assert s == "Tingting wins in 13 moves"
    s = catch_me_if_you_can(85, 35, 70, 27, 29, 29)
    assert s == "Bahar wins in 13 moves"
    s = catch_me_if_you_can(16, 99, 3, 97, 2, 58)
    assert s == "Bahar wins in 11 moves"
    s = catch_me_if_you_can(24, 56, 12, 28, 19, 12)
    assert s == "Bahar wins in 10 moves"
    s = catch_me_if_you_can(60, 92, 50, 86, 2, 54)
    assert s == "Bahar wins in 8 moves"
    s = catch_me_if_you_can(40, 94, 8, 80, 27, 4)
    assert s == "Bahar wins in 30 moves"
    s = catch_me_if_you_can(72, 63, 8, 46, 0, 42)
    assert s == "Tingting wins in 12 moves"
    s = catch_me_if_you_can(69, 61, 41, 29, 51, 57)
    assert s == "Tingting wins in 10 moves"
    s = catch_me_if_you_can(99, 41, 58, 18, 74, 40)
    assert s == "Tingting wins in 8 moves"
    s = catch_me_if_you_can(47, 6, 39, 0, 0, 2)
    assert s == "Bahar wins in 6 moves"
    s = catch_me_if_you_can(94, 88, 68, 34, 84, 9)
    assert s == "Bahar wins in 24 moves"
    s = catch_me_if_you_can(7, 94, 2, 70, 3, 10)
    assert s == "Bahar wins in 3 moves"
    s = catch_me_if_you_can(39, 64, 28, 32, 1, 48)
    assert s == "Bahar wins in 9 moves"
    s = catch_me_if_you_can(61, 96, 9, 59, 29, 56)
    assert s == "Tingting wins in 9 moves"
    s = catch_me_if_you_can(3, 5, 0, 3, 1, 3)
    assert s == "Bahar wins in 1 moves"
    s = catch_me_if_you_can(96, 92, 44, 42, 52, 33)
    assert s == "Tingting wins in 9 moves"
    s = catch_me_if_you_can(29, 34, 0, 12, 3, 4)
    assert s == "Tingting wins in 9 moves"
    s = catch_me_if_you_can(44, 41, 13, 5, 39, 37)
    assert s == "Tingting wins in 12 moves"
    s = catch_me_if_you_can(61, 82, 52, 10, 56, 30)
    assert s == "Bahar wins in 7 moves"
    s = catch_me_if_you_can(76, 43, 2, 37, 20, 3)
    assert s == "Bahar wins in 72 moves"
    s = catch_me_if_you_can(36, 64, 0, 6, 7, 53)
    assert s == "Tingting wins in 16 moves"
    s = catch_me_if_you_can(21, 93, 7, 21, 12, 24)
    assert s == "Tingting wins in 2 moves"
    s = catch_me_if_you_can(72, 70, 55, 5, 5, 49)
    assert s == "Bahar wins in 15 moves"
    s = catch_me_if_you_can(93, 59, 28, 5, 11, 49)
    assert s == "Tingting wins in 21 moves"
    s = catch_me_if_you_can(80, 3, 23, 2, 11, 0)
    assert s == "Tingting wins in 12 moves"
    s = catch_me_if_you_can(56, 84, 52, 57, 25, 76)
    assert s == "Bahar wins in 2 moves"
    s = catch_me_if_you_can(31, 72, 13, 33, 4, 26)
    assert s == "Tingting wins in 16 moves"
    s = catch_me_if_you_can(3, 3, 1, 1, 1, 1)
    print(s)
    assert s == "Tingting wins in 3 moves"

    s = catch_me_if_you_can(1000, 1000, 800, 800, 700, 700) #should return Bahar wins in 198 moves
    print(s)
    assert s == 'Bahar wins in 198 moves'
    s = catch_me_if_you_can(1100, 1100, 800, 800, 700, 700) #should return Tingting  wins in 200 moves
    print(s)
    assert s == 'Tingting wins in 200 moves'

