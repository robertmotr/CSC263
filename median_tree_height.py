'''
CSC263 Winter 2023
Problem Set 1 Starter Code
University of Toronto Mississauga
'''


# Do NOT add any "import" statements

# sets node to correct position in heap for a max heap
def max_heapify_down(heap, node):
	'''
	>>> list = []
	>>> retval = max_heapify_down(list, 25)
	>>> retval
	# fill out unit test here later
	'''

	while i * 2 < len(heap):
		l_index = 2 * i
		r_index = 2 * i + 1

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


	if i * 2 == len(heap):
		#left child exists but right doesnt
		if heap[i*2] > heap[i]:
			heap[i], heap[2 * i] = heap[2 * i], heap[i]


# sets node to correct position in heap for a min heap
# INDEX IS 1 BASED !!!!!
def min_heapify_down(heap, i):
	while i * 2 < len(heap):
		l_index = 2 * i
		r_index = 2 * i + 1

		if heap[i] <= heap[l_index] and heap[i] <= heap[r_index]:
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


	if i * 2 == len(heap):
		#left child exists but right doesnt
		if heap[i*2] < heap[i]:
			heap[i], heap[2 * i] = heap[2 * i], heap[i]

#MIN HEAP IS THE ONE WITH THE BIGGER ELEMENTS
def initialize(middle, init_string):
	init_list = init_string.split(' ')
	init_list.pop(0);

	min_heap = []
	max_heap = []
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
	for i in range(duplicates):














def median_tree_height(commands, middle):
  '''
  Pre: commands is a list of commands, middle is the middle or lower middle value of the current collection.
  Post: return list of outputs
  '''
  # question to consider: do we have two median roots?????
  tree_height_heap = []
  min_heap = []
  max_heap = []
  commands = commands.split(' ')
  initialize = commands[0].split(' ')

  # sort input into min_heap and max_heap lists
  for i in range(1, len(initialize)):
  	curr = str(i)
  	if curr < middle:
  		min_heap.append(curr)

  	elif curr > middle:
  		max_heap.append(curr)
  for i in range(floor(n/2), 1):
  	


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
