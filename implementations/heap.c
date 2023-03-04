#include "heap.h"
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

// File implements all maxheap and minheap functions
// All functions in this file assume ONE-BASED indexing as
// per CSC263 course notes.

// self-explanatory....
int max(MaxHeap *heap) {
    return heap->array[0];
}


/*
Returns a pointer to the maximum element in the heap.
Swaps the last element in the heap with the root, then bubbles
down the swapped element at the roop, taking Theta(log n) time. Returns
the original maximum of the heap.

If the heap is empty, returns NULL.
*/
int extract_max(MaxHeap *heap) {
    int m = max(heap);

    // Swap first and last element
    int tmp = heap->array[heap->size - 1];
    heap->array[heap->size - 1] = heap->array[0];
    heap->array[0] = tmp;

    // Bubble down the swapped element
    bubble_down(heap, 1);
    heap->size--;

    return m;
}

/*
Helper for bubble down. Returns an index to the
largest child from the node it is currently at (position) 
given a one-based integer index. Returns a zero-based index
for easy use. Returns -1 if there are no
children.
*/
int bubble_down_helper(int *position, int index, int size) {
    if(2 * index - 1 >= size) {
        // no children at all
        return -1;
    }
    else if(2 * index >= size) {
        // only left child so return left
        return 2 * index - 1;
    }
    else {
        // both children exist
        // so compare left to right
        if(position[2 * index - 1] > position[2 * index]) {
            return 2 * index - 1;
        }
        else {
            return 2 * index;
        }
    }
}

/*
Bubble down AKA max_heapify_down. Takes O(log n) time in the worst case.
Index is one-based.

issues: are we guaranteed that if we hit a child that is not greater than parent we can stop recursing?
*/
void bubble_down(MaxHeap *heap, int index) {
    int eldest = bubble_down_helper(heap->array, index, heap->size);
    while(eldest != -1 && heap->array[eldest] > heap->array[index - 1]) {
        // check if they need to be swapped
        if(eldest > heap->array[index - 1]) {
            // they need to be swapped
            int tmp = heap->array[index - 1];
            heap->array[index - 1] = heap->array[eldest];
            heap->array[eldest] = tmp;
            index = eldest;
        }
        eldest = bubble_down_helper(heap->array, index, heap->size);
    }
}


/*
Increases the value of element at index index to value, and then bubbles up that element.
Takes O(log n) time in worst case. Index passed in as param is one based.
*/
void increase_priority(MaxHeap *heap, int index, int value) {
    int *arr = heap->array;
    arr[index] = value;

    int i = index;
    int j = (int) (i - 1) / 2;
    // now bubble up
    while(i > 1 && arr[j] < arr[i - 1]) {
        // swap parent with child
        int tmp = arr[j];
        arr[j] = arr[i - 1];
        arr[i - 1] = tmp;

        // bubble up, set new index
        i = (int) (i - 1) / 2;
        j = (i - 1) / 2;
    }
}
/*
Inserts value at the end of the array to keep it nearly complete
Then bubbles up by swapping. Takes O(log n) time.
*/
void insert(MaxHeap *heap, int value) {
    if(heap->allocated == heap->size) {
        // we need to make more room so we realloc
        // we allocate size + 4 more ints than necessary
        // because calling realloc often makes our program slow
        // so we make more room than we need so we call it less often
        heap->allocated = heap->size + 4;
        int *tmp = realloc(heap->array, heap->allocated * sizeof(int));
        heap->size++;

        // now we add the value at the end of the heap
        tmp[heap->size - 1] = value;
        // now bubble up
        increase_priority(heap, heap->size, value);
    }
    else {
        // we don't need to make more room in terms of memory
        // simply add to the end and bubble up
        heap->size++;
        heap->array[heap->size - 1] = value;
        increase_priority(heap, heap->size, value);
    }   
}

/*
Preconditions: i is a node in a nearly complete binary tree.
Left(i) and Right(i) are max-heaps.

Postconditions:
Binary tree rooted at i is a max heap.

Bubbles down index to a proper position by swapping with children.
i is one based.
*/
void max_heapify_down(MaxHeap *heap, int index) {
    bubble_down(heap, index);
}

/*
Given an unsorted array a, and the size of the array size, then
we return a pointer to a MaxHeap created with the array. Operation takes
O(n logn) time. We do this by iterating over each element in the array
taking n steps, and then calling insert taking log n worst case steps.
*/
MaxHeap *build_max_heap_naive(int *array, int size) {
    MaxHeap *heap = malloc(sizeof(MaxHeap));
    heap->allocated = 0;
    heap->size = 0;

    for(int i = 0; i < size; i++) {
        insert(heap, array[i]);
    }
    return heap;
}

/*
Smarter way of building a max-heap from an unsorted array. Takes O(n) time
because we do not use insert method. Returns a pointer to the new 
max heap object created.
*/
MaxHeap *build_max_heap(int *array, int size) {
    for(int i = (int) (size - 1 / 2); i > 0; i--) {
        max_heapify_down(array, i);
    }
}


/*
Given an arbitrary unsorted array of size n, converts the array
into a max-heap using build_max_heap_naive, then sorts into ascending 
order.
*/
int *heap_sort_naive(int *a, int size) {
    MaxHeap *heap = build_max_heap(a, size); // n logn time
    int *b = heap->array;
    for(int i = size; i > 2; i--) { // n time
        int tmp = b[size - 1];
        b[size - 1] = b[0];
        b[0] = tmp;
    }
    free(heap);
    heap = NULL;
    return b;
}

int *heap_sort(int *a, int size) {
    MaxHeap *heap = build_max_heap(a, size); // n time
    int *b = heap->array;

    for(int i = size; i > 2; i--)  {// n time
        int tmp = b[size - 1];
        b[size - 1] = b[0];
        b[0] = tmp;
    }
    free(heap);
    heap = NULL;
    return b;
}

