'''
CSC263 Winter 2023
Problem Set 1 Starter Code
University of Toronto Mississauga
'''


# Do NOT add any "import" statements

# Bubbles down the node at index i to the correct position in a max heap

def max_heapify_down(heap, i):
    '''
    >>> list = []
    >>> retval = max_heapify_down(list, 25)
    >>> retval
    # fill out unit test here later
    '''

    while i * 2 < len(heap):
        #runs until completion, or until it reaches a node with only a left child
        l_index = 2 * i
        r_index = 2 * i + 1

        if r_index >= len(heap):
            break

        if heap[i] >= heap[l_index] and heap[i] >= heap[r_index]:
            #property is satisfied
            break

        elif heap[r_index] <= heap[l_index]:
            #left is bigger (higher priority)
            heap[i], heap[2 * i] = heap[2 * i], heap[i]
            i = 2 * i

        else:
            #right is bigger
            heap[i], heap[2 * i + 1] = heap[2 * i + 1], heap[i]
            i = 2 * i + 1


    if i * 2 == len(heap) - 1:
        #there remains 1 unchecked node with only a left child
        if heap[i * 2] > heap[i]:
            heap[i], heap[2 * i] = heap[2 * i], heap[i]


# Bubbles up the node at index i to the correct position in a max heap
def max_heapify_up(heap, i):
    while i > 1:
        if heap[int(i/2)] >= heap[i]:
            #parent is larger (property holds)
            break

        else:
            #parent is smaller so swap
            heap[int(i/2)], heap[i] = heap[i], heap[int(i/2)]
            i = int(i/2)



# Bubbles down the node at index i to the correct position in a min heap
def min_heapify_down(heap, i):
    while i * 2 < len(heap):
        # runs until completion, or until it reaches a node with only a left child
        l_index = 2 * i
        r_index = 2 * i + 1
        if r_index >= len(heap):
            break

        elif heap[i] <= heap[l_index] and heap[i] <= heap[r_index]:
            #property is satisfied
            break

        elif heap[r_index] >= heap[l_index]:
            #left is smaller (higher priority)
            heap[i], heap[2 * i] = heap[2 * i], heap[i]
            i = 2 * i

        else:
            #right is smaller
            heap[i], heap[2 * i + 1] = heap[2 * i + 1], heap[i]
            i = 2 * i + 1


    if i * 2 == len(heap) - 1:
        #there remains 1 unchecked node with only a left child
        if heap[i*2] < heap[i]:
            heap[i], heap[2 * i] = heap[2 * i], heap[i]



def min_heapify_up(heap, i):
    while i > 1:
        if heap[int(i/2)] <= heap[i]:
            #parent is smaller (property holds)
            break

        else:
            #parent is smaller so swap
            heap[int(i/2)], heap[i] = heap[i], heap[int(i/2)]
            i = int(i/2)



#MIN HEAP IS THE ONE WITH THE BIGGER ELEMENTS
def initialize(middle, commands_list):
    init_list = commands_list[0].split(' ')
    init_list.pop(0)

    min_heap = ["1 based"]
    max_heap = ["1 based"]
    duplicates = 0

    for string in init_list:
        num = int(string)
        if num > middle:
            min_heap.append(num)
        elif num < middle:
            max_heap.append(num)
        else:
            #num = middle
            duplicates += 1

    while len(max_heap) != len(min_heap) and duplicates != 0:
        if len(max_heap) < len(min_heap):
            max_heap.append(middle)

        else:
            min_heap.append(middle)

    if duplicates != 0:
        max_heap.append(middle)

    for i in range( int(len(max_heap)/2), 0, -1):
        max_heapify_down(max_heap, i)

    for i in range( int(len(min_heap)/2) , 0, -1):
        min_heapify_down(min_heap, i)

    return max_heap, min_heap


def min_insert(heap, num):
    heap.append(num)
    min_heapify_up(heap, len(heap) - 1)

def max_insert(heap, num):
    heap.append(num)
    max_heapify_up(heap, len(heap) - 1)

def insert(num, max_heap, min_heap, middle):

    if num == middle:
        if len(min_heap) < len(max_heap):
            min_insert(min_heap, num)
        else:
            max_insert(max_heap, num)
    elif num > middle:
        min_insert(min_heap, num)
    else:
        max_insert(max_heap, num)


def get_higher_middle(min_heap, max_heap):
    if min_heap[1] > max_heap[1]:
        return min_heap[1]
    return max_heap[1]




def median_tree_height(commands, middle):
  '''
  Pre: commands is a list of commands, middle is the middle or lower middle value of the current collection.
  Post: return list of outputs
  '''

  #both heaps[0] will be some useless element to make it 1 based, so the real root is heap[1]

  output = []
  max_heap, min_heap = initialize(middle, commands)
  if (len(max_heap) + len(min_heap)) % 2 == 0:
      output.append((max_heap[1] + min_heap[1]) / 2)
  else:
      if len(max_heap) > len(min_heap):
          output.append(max_heap[1])
      else:
          output.append(min_heap[1])
  commands.pop(0)
  for command in commands:
      num = int(command.split()[1])
      insert(num, max_heap, min_heap, middle)
      if (len(max_heap) + len(min_heap)) % 2 == 0:
          output.append( (max_heap[1] + min_heap[1]) / 2)
      else:
          if len(max_heap) > len(min_heap):
              output.append(max_heap[1])
          else:
              output.append(min_heap[1])

  return output







  # initialize the heap

if __name__ == '__main__':
    # some small test cases
    # Case 1
    print(median_tree_height(
        ['initialize 28 14 13 17 50 32 35 16 26 23 41 40 49 27 40 34 15 30 32 12', 'insert 10', 'insert 47',
         'insert 10', 'insert 9', 'insert 29', 'insert 14', 'insert 17', 'insert 2', 'insert 32', 'insert 13',
         'insert 23', 'insert 31', 'insert 27', 'insert 4'], 28))
    print(median_tree_height(
        ['initialize 13 22 15 26 24 33 14 24 16 29 27 36 48', 'insert 23', 'insert 3', 'insert 41', 'insert 12',
         'insert 5', 'insert 15', 'insert 15', 'insert 16', 'insert 11', 'insert 46', 'insert 6', 'insert 34',
         'insert 9', 'insert 39', 'insert 38', 'insert 6', 'insert 48', 'insert 19'], 24))
    print(median_tree_height(
        ['initialize 18 38 36 40 17 12 41', 'insert 39', 'insert 40', 'insert 21', 'insert 12', 'insert 17', 'insert 1',
         'insert 14', 'insert 49', 'insert 9', 'insert 43', 'insert 46', 'insert 46', 'insert 47', 'insert 33',
         'insert 10'], 36))
    print(median_tree_height(
        ['initialize 29 21 38 24 37 19 30 42 34 33 32', 'insert 7', 'insert 48', 'insert 27', 'insert 23', 'insert 49',
         'insert 27', 'insert 50', 'insert 34', 'insert 2', 'insert 33', 'insert 5', 'insert 44', 'insert 10',
         'insert 44', 'insert 28', 'insert 30', 'insert 20', 'insert 21', 'insert 11'], 32))
    print(median_tree_height(
        ['initialize 33 50 44 15 27 35 19 44 23 40 19 23 12 50 16 43 20 28 12', 'insert 23', 'insert 24', 'insert 48',
         'insert 21', 'insert 11', 'insert 35', 'insert 31', 'insert 45', 'insert 5', 'insert 19', 'insert 41',
         'insert 18', 'insert 26', 'insert 34', 'insert 6', 'insert 35', 'insert 19', 'insert 3', 'insert 34'], 27))
    print(median_tree_height(
        ['initialize 20 34 35 19 16', 'insert 38', 'insert 6', 'insert 22', 'insert 47', 'insert 14', 'insert 25'], 20))
    print(median_tree_height(
        ['initialize 48 36 44 27 29 21 31 48 27 46 29 35 15', 'insert 2', 'insert 41', 'insert 18', 'insert 5',
         'insert 30', 'insert 3', 'insert 7'], 31))
    print(median_tree_height(
        ['initialize 33 27 19 14 42 41 26 31 24 16 25 28 18', 'insert 20', 'insert 12', 'insert 2', 'insert 20',
         'insert 4', 'insert 8', 'insert 38', 'insert 2', 'insert 16', 'insert 23', 'insert 18', 'insert 33',
         'insert 24', 'insert 24'], 26))
    print(median_tree_height(
        ['initialize 24 49 26 45 29 41 31 35 30 41', 'insert 9', 'insert 28', 'insert 19', 'insert 42', 'insert 2',
         'insert 41', 'insert 12', 'insert 35', 'insert 33', 'insert 17', 'insert 5'], 31))
    print(median_tree_height(
        ['initialize 22 49 29 37 46', 'insert 31', 'insert 36', 'insert 46', 'insert 31', 'insert 27', 'insert 23',
         'insert 37', 'insert 8', 'insert 11', 'insert 9', 'insert 11', 'insert 12', 'insert 47', 'insert 9',
         'insert 24', 'insert 18'], 37))
    print(median_tree_height(
        ['initialize 43 41 49 48 28 50 13 33 13 49 33', 'insert 3', 'insert 15', 'insert 17', 'insert 45', 'insert 28',
         'insert 17', 'insert 18', 'insert 44', 'insert 27', 'insert 18', 'insert 2', 'insert 50', 'insert 29',
         'insert 34', 'insert 12', 'insert 43', 'insert 10'], 41))
    print(median_tree_height(
        ['initialize 27 27 28 46 37 39 35 18 23 46', 'insert 6', 'insert 20', 'insert 3', 'insert 28', 'insert 38',
         'insert 12', 'insert 20', 'insert 42', 'insert 21', 'insert 32', 'insert 15', 'insert 40', 'insert 25',
         'insert 24', 'insert 28', 'insert 39', 'insert 19', 'insert 1'], 28))
    print(median_tree_height(
        ['initialize 43 50 16 35 50 29 32 24', 'insert 49', 'insert 40', 'insert 6', 'insert 40', 'insert 32',
         'insert 33'], 32))
    print(median_tree_height(
        ['initialize 21 29 47 42 30 38 38 36 17 24 44', 'insert 47', 'insert 47', 'insert 3', 'insert 44', 'insert 13',
         'insert 43', 'insert 33', 'insert 6', 'insert 28', 'insert 18', 'insert 25', 'insert 50', 'insert 7',
         'insert 29', 'insert 25', 'insert 1'], 36))
    print(median_tree_height(
        ['initialize 38 21 32 30 33 26 19 27 44 29 21 43 15 26', 'insert 19', 'insert 30', 'insert 7', 'insert 11',
         'insert 36', 'insert 37', 'insert 43', 'insert 34', 'insert 45'], 27))
    print(median_tree_height(
        ['initialize 28 13 37 26 36 44 24', 'insert 3', 'insert 42', 'insert 50', 'insert 3', 'insert 15', 'insert 15',
         'insert 29', 'insert 23', 'insert 5', 'insert 25', 'insert 33', 'insert 6', 'insert 8', 'insert 25',
         'insert 30'], 28))
    print(median_tree_height(
        ['initialize 46 21 49 29 17', 'insert 14', 'insert 33', 'insert 29', 'insert 6', 'insert 47', 'insert 11',
         'insert 22', 'insert 50'], 29))
    print(median_tree_height(
        ['initialize 19 45 30 35 29 43 30 43 27 26 25 23 13 17 20 15', 'insert 26', 'insert 22', 'insert 45',
         'insert 43', 'insert 28', 'insert 6', 'insert 10', 'insert 32'], 26))
    print(median_tree_height(
        ['initialize 45 49 33 48 28', 'insert 40', 'insert 35', 'insert 29', 'insert 16', 'insert 8', 'insert 41',
         'insert 48'], 45))
    print(median_tree_height(
        ['initialize 29 22 21 31 21 35 35 41 26 35 37 48 32 23 27 49 41 38', 'insert 2', 'insert 10', 'insert 1',
         'insert 13', 'insert 28', 'insert 7', 'insert 33', 'insert 49', 'insert 40', 'insert 4', 'insert 25',
         'insert 10', 'insert 1', 'insert 16', 'insert 17', 'insert 38', 'insert 37', 'insert 3', 'insert 30'], 32))
    print(median_tree_height(
        ['initialize 38 13 20 48 29 22', 'insert 21', 'insert 24', 'insert 10', 'insert 17', 'insert 32', 'insert 18',
         'insert 26', 'insert 6', 'insert 13', 'insert 4', 'insert 40', 'insert 50', 'insert 23', 'insert 22',
         'insert 37', 'insert 31'], 22))
    print(median_tree_height(
        ['initialize 43 30 17 18 33 17 18 45 50 32 15 29 47 25 13 21 27', 'insert 7', 'insert 34', 'insert 13',
         'insert 16', 'insert 50', 'insert 12', 'insert 44', 'insert 13', 'insert 3', 'insert 32', 'insert 18',
         'insert 7', 'insert 33', 'insert 6'], 27))
    print(median_tree_height(
        ['initialize 37 35 32 24 30 43 31 47 41 17 14 49 26 19 24 29 47', 'insert 3', 'insert 10', 'insert 25',
         'insert 8', 'insert 29'], 31))
    print(median_tree_height(
        ['initialize 20 27 40 42 43 33 32 19 50 22 14 49 41 33 25 44', 'insert 29', 'insert 32', 'insert 46',
         'insert 9', 'insert 20', 'insert 8', 'insert 35', 'insert 15'], 33))
    print(median_tree_height(
        ['initialize 33 30 15 40 42 14 24 31 41 16 46 36 44 28 33 37 50 24 30 42', 'insert 50', 'insert 13',
         'insert 34', 'insert 12', 'insert 9', 'insert 50', 'insert 31', 'insert 1', 'insert 13', 'insert 48',
         'insert 17', 'insert 21', 'insert 45', 'insert 8', 'insert 16', 'insert 50', 'insert 17', 'insert 41',
         'insert 2'], 33))
    print(median_tree_height(
        ['initialize 43 43 21 37 18 21 12 19 22 40 43 21 38 33 19', 'insert 14', 'insert 40', 'insert 21', 'insert 11',
         'insert 4', 'insert 38', 'insert 13'], 22))
    print(median_tree_height(
        ['initialize 23 42 26 36 13 32 32 23 30 34 39 27', 'insert 31', 'insert 42', 'insert 34', 'insert 21',
         'insert 38', 'insert 27', 'insert 30'], 30))
    print(median_tree_height(
        ['initialize 31 24 47 24 16 39 31 26 39 37 26 45 32 23 33 33', 'insert 11', 'insert 46', 'insert 7', 'insert 6',
         'insert 38', 'insert 35', 'insert 5', 'insert 3', 'insert 12', 'insert 45', 'insert 17', 'insert 25',
         'insert 48', 'insert 9', 'insert 23', 'insert 8', 'insert 45', 'insert 18'], 31))
    print(median_tree_height(
        ['initialize 19 50 33 25 35 47 46 25 37 26 39 17', 'insert 39', 'insert 50', 'insert 39', 'insert 34',
         'insert 37', 'insert 44', 'insert 23', 'insert 25', 'insert 45', 'insert 26', 'insert 3', 'insert 40',
         'insert 33', 'insert 3', 'insert 19', 'insert 39', 'insert 17', 'insert 23', 'insert 2', 'insert 21'], 33))
    print(median_tree_height(
        ['initialize 15 29 17 28 47 22 46 46 26 38 26 33 47', 'insert 29', 'insert 47', 'insert 39', 'insert 28',
         'insert 3', 'insert 32', 'insert 39', 'insert 40', 'insert 49', 'insert 5', 'insert 17', 'insert 49',
         'insert 12', 'insert 14', 'insert 36', 'insert 12', 'insert 47'], 29))
    print(median_tree_height(
        ['initialize 17 38 39 20 33 39 43 13 42', 'insert 16', 'insert 25', 'insert 36', 'insert 44', 'insert 39',
         'insert 26', 'insert 12', 'insert 4', 'insert 22', 'insert 7', 'insert 50', 'insert 35', 'insert 17',
         'insert 30', 'insert 17', 'insert 2', 'insert 22', 'insert 2', 'insert 42', 'insert 23'], 38))
    print(median_tree_height(
        ['initialize 21 49 19 33 13 38 21 43 47 26 36 18 50 17 24', 'insert 33', 'insert 26', 'insert 16', 'insert 25',
         'insert 17', 'insert 22', 'insert 38', 'insert 33', 'insert 14', 'insert 38', 'insert 35'], 26))
    print(median_tree_height(
        ['initialize 27 42 27 17 29 21 13 38 12', 'insert 46', 'insert 17', 'insert 28', 'insert 46', 'insert 42',
         'insert 13', 'insert 5', 'insert 1', 'insert 43', 'insert 14', 'insert 40', 'insert 3', 'insert 5',
         'insert 44', 'insert 31', 'insert 37', 'insert 12', 'insert 39', 'insert 43', 'insert 46'], 27))
    print(median_tree_height(
        ['initialize 34 48 46 13 36 37 41 24 12 38 45 13 28 37 41 46 30 48 45 37', 'insert 38', 'insert 19',
         'insert 32', 'insert 9', 'insert 19', 'insert 2', 'insert 2', 'insert 15', 'insert 41', 'insert 40',
         'insert 12', 'insert 50', 'insert 33', 'insert 29'], 37))
    print(median_tree_height(
        ['initialize 18 32 50 50 19 31 38 20 12 38 25 48 40 48 15 49 21 46 28', 'insert 23', 'insert 22', 'insert 34',
         'insert 19', 'insert 20', 'insert 8', 'insert 13', 'insert 28', 'insert 32', 'insert 15', 'insert 1',
         'insert 48', 'insert 11'], 32))
    print(median_tree_height(
        ['initialize 40 27 35 22 21 29 39 28 32 37 24 35', 'insert 42', 'insert 26', 'insert 18', 'insert 8',
         'insert 5', 'insert 35'], 29))
    print(median_tree_height(
        ['initialize 14 48 32 18 25 16 50 36 18 33 26', 'insert 24', 'insert 50', 'insert 50', 'insert 43', 'insert 20',
         'insert 12'], 26))
    print(median_tree_height(
        ['initialize 47 42 35 16 49 24 40 35 14 22 46 23 13 24 12 36 46 24 26', 'insert 43', 'insert 31', 'insert 24',
         'insert 14', 'insert 12', 'insert 23', 'insert 28', 'insert 45', 'insert 37', 'insert 46', 'insert 27',
         'insert 5', 'insert 11', 'insert 29', 'insert 33', 'insert 21'], 26))

    #assert [9, 10.0, 11, 10.0] == median_tree_height(
        #['initialize 11 4 7 18 9',
         #'insert 15',
        # 'insert 19',
        # 'insert 3',
       #  ], 9)
