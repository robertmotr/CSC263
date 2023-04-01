'''
CSC263 Winter 2023
Problem Set 4 Starter Code
University of Toronto Mississauga
'''

# Do NOT add any "import" statements

def catch_me_if_you_can(nrows, ncols, bahar_row, bahar_col, tingting_row, tingting_col):
  '''Return the appropriate string, as described in the handout.
  
  nrows: number of rows in the board
  ncols: number of columns in the board
  bahar_row/bahar_col: Bahar's starting location
  tingting_row/tingting_col: Tingting's starting location
  '''  
  pass
  

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
