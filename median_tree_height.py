'''
CSC263 Winter 2023
Problem Set 1 Starter Code
University of Toronto Mississauga
'''


# Do NOT add any "import" statements

def median_tree_height(commands, middle):
  '''
  Pre: commands is a list of commands, middle is the middle or lower middle value of the current collection.
  Post: return list of outputs
  '''
  commands = commands[0].split(' ')

  # initialize the heap



if __name__ == '__main__':
    # some small test cases
    # Case 1

    assert [9, 10.0, 11, 10.0] == median_tree_height(
        ['initialize 11 4 7 18 9',
         'insert 15',
         'insert 19',
         'insert 3',
         ], 9)
