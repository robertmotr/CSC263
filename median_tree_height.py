"""
CSC263 Winter 2023
Problem Set 1 Starter Code
University of Toronto Mississauga
"""


# Do NOT add any "import" statements


# Bubbles down the node at index i to the correct position in a max heap
def max_heapify_down(heap, i):
    """
    >>> list = []
    >>> max_heapify_down(list, 25)
    # fill out unit test here later
    """

    while i * 2 < len(heap):
        # runs until completion, or until it reaches a node with only a left child
        l_index = 2 * i
        r_index = 2 * i + 1

        if r_index >= len(heap):
            break

        if heap[i] >= heap[l_index] and heap[i] >= heap[r_index]:
            # property is satisfied
            break

        elif heap[r_index] <= heap[l_index]:
            # left is bigger (higher priority)
            heap[i], heap[2 * i] = heap[2 * i], heap[i]
            i = 2 * i

        else:
            # right is bigger
            heap[i], heap[2 * i + 1] = heap[2 * i + 1], heap[i]
            i = 2 * i + 1

    if i * 2 == len(heap) - 1:
        # there remains 1 unchecked node with only a left child
        if heap[i * 2] > heap[i]:
            heap[i], heap[2 * i] = heap[2 * i], heap[i]


# Bubbles up the node at index i to the correct position in a max heap
def max_heapify_up(heap, i):
    while i > 1:
        if heap[int(i / 2)] >= heap[i]:
            # parent is larger (property holds)
            break

        else:
            # parent is smaller so swap
            heap[int(i / 2)], heap[i] = heap[i], heap[int(i / 2)]
            i = int(i / 2)


# Bubbles down the node at index i to the correct position in a min heap
def min_heapify_down(heap, i):
    while i * 2 < len(heap):
        # runs until completion, or until it reaches a node with only a left child
        l_index = 2 * i
        r_index = 2 * i + 1
        if r_index >= len(heap):
            break

        elif heap[i] <= heap[l_index] and heap[i] <= heap[r_index]:
            # property is satisfied
            break

        elif heap[r_index] >= heap[l_index]:
            # left is smaller (higher priority)
            heap[i], heap[2 * i] = heap[2 * i], heap[i]
            i = 2 * i

        else:
            # right is smaller
            heap[i], heap[2 * i + 1] = heap[2 * i + 1], heap[i]
            i = 2 * i + 1

    if i * 2 == len(heap) - 1:
        # there remains 1 unchecked node with only a left child
        if heap[i * 2] < heap[i]:
            heap[i], heap[2 * i] = heap[2 * i], heap[i]


def min_heapify_up(heap, i):
    while i > 1:
        if heap[int(i / 2)] <= heap[i]:
            # parent is smaller (property holds)
            break

        else:
            # parent is smaller so swap
            heap[int(i / 2)], heap[i] = heap[i], heap[int(i / 2)]
            i = int(i / 2)


def initialize(middle, commands_list):
    init_list = commands_list[0].split(' ')
    init_list.pop(0)

    min_heap = ["1 based"]
    max_heap = ["1 based"]
    # both heaps have an unused element at index 0 to make the heap 1 based.

    duplicates = 0

    for string in init_list:
        num = int(string)
        if num > middle:
            min_heap.append(num)
        elif num < middle:
            max_heap.append(num)
        else:
            # num = middle
            duplicates += 1

    # since elements equal to the median could be put in either heap, they are added at the end
    # ensuring they are added to the smallest of the heaps, keeping their sizes balanced
    while len(max_heap) != len(min_heap) and duplicates != 0:
        if len(max_heap) < len(min_heap):
            max_heap.append(middle)

        else:
            min_heap.append(middle)
        duplicates -= 1

    if duplicates != 0:
        max_heap.append(middle)

    for i in range(int(len(max_heap) / 2), 0, -1):
        max_heapify_down(max_heap, i)

    for i in range(int(len(min_heap) / 2), 0, -1):
        min_heapify_down(min_heap, i)

    return max_heap, min_heap


def min_insert(heap, num):
    heap.append(num)
    min_heapify_up(heap, len(heap) - 1)


def max_insert(heap, num):
    heap.append(num)
    max_heapify_up(heap, len(heap) - 1)


def extract_max(heap):
    heap[1], heap[-1] = heap[-1], heap[1]
    out = heap.pop(-1)
    max_heapify_down(heap, 1)
    return out


def extract_min(heap):
    heap[1], heap[-1] = heap[-1], heap[1]
    out = heap.pop(-1)
    min_heapify_down(heap, 1)
    return out


def insert(num, max_heap, min_heap, middle):
    if num == middle:
        if len(min_heap) < len(max_heap):
            min_insert(min_heap, num)
        else:
            max_insert(max_heap, num)
    elif num > middle:
        # moves the smallest element from min to max if min is larger and about to gain a new element
        if len(min_heap) > len(max_heap):
            max_insert(max_heap, extract_min(min_heap))

        min_insert(min_heap, num)
    else:
        # moves the largest element from max to min if min is larger and about to gain a new element
        if len(min_heap) < len(max_heap):
            min_insert(min_heap, extract_max(max_heap))

        max_insert(max_heap, num)


def get_higher_middle(min_heap, max_heap):
    if min_heap[1] > max_heap[1]:
        return min_heap[1]
    return max_heap[1]


def median_tree_height(commands, middle):
    """
  Pre: commands is a list of commands, middle is the middle or lower middle value of the current collection.
  Post: return list of outputs
  """

    # both heaps[0] will be some useless element to make it 1 based, so the real root is heap[1]

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
            output.append((max_heap[1] + min_heap[1]) / 2)
        else:
            if len(max_heap) > len(min_heap):
                output.append(max_heap[1])
            else:
                output.append(min_heap[1])

    return output

    # initialize the heap


if __name__ == '__main__':
    assert [9, 10.0, 11, 10.0] == median_tree_height(
        ['initialize 11 4 7 18 9',
         'insert 15',
         'insert 19',
         'insert 3',
         ], 9)
