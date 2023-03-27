# Tricky elevator problem for tutorial 8 CSC263

from collections import deque

def shortest_button_pushes(N, X, Y, U, D):
    # Initialize list to store minimum number of button pushes
    min_pushes = [float('inf')] * (N + 1)
    min_pushes[X] = 0

    # Initialize list to store previous floors
    prev_floors = [None] * (N + 1)

    # Initialize queue and enqueue starting floor
    q = deque()
    q.append(X)

    # BFS loop
    while q:
        f = q.popleft()
        # Check if reached target floor
        if f == Y:
            # Reconstruct button push sequence
            button_pushes = []
            curr_floor = Y
            while curr_floor != X:
                prev_floor = prev_floors[curr_floor]
                if curr_floor > prev_floor:
                    button_pushes.append("Up by {}".format(curr_floor - prev_floor))
                else:
                    button_pushes.append("Down by {}".format(prev_floor - curr_floor))
                curr_floor = prev_floor
            button_pushes.reverse()
            return len(button_pushes), button_pushes

        # Try all possible button pushes
        next_floors = [f + U, f - D]
        for next_floor in next_floors:
            if 1 <= next_floor <= N:
                pushes_required = min_pushes[f] + 1
                if pushes_required < min_pushes[next_floor]:
                    min_pushes[next_floor] = pushes_required
                    prev_floors[next_floor] = f
                    q.append(next_floor)

    # If target floor cannot be reached, return "TAKE THE STAIRS!"
    return "TAKE THE STAIRS!"

def shortest_button_pushes_new(N, X, Y, U, D):
    list = [float("inf")] * (N + 1)
    list[X] = 0

    q = deque()
    q.append(X)

    while q:
        f = q.popleft()

        # now loop over all neighbours that we can go
        if X + U <= N: 
            
        if X - D > 1:


    return "TAKE THE STAIRS!"


print(shortest_button_pushes(10, 1, 10, 2, 1))
print(shortest_button_pushes(10, 2, 3, 2, 2))