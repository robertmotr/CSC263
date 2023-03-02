#include "max_heap.h"
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// implements max heap
// left: 2i
// right: 2i + 1
// where i is one-based
// parent: floor(i/2)

/* 
Given a pointer array to a max heap implementation, intended
for use in bubbling down. The max heap is known to have a violation.
Returns a pointer to the eldest child of the parent from *(array + 0). 
Note that get_elder takes an index as a one-based number.
Returns NULL if there is no eldest child that is bigger than the parent.
*/
int *get_elder_violation(MaxHeap *heap, int index) {
    // parent has no children
    if(2 * index > heap->size) {
        return NULL;
    } 
    
    // no right child but there is a left, so has to be left
    if(2 * index + 1 > heap->size) {
        if(heap->array[2 * index - 1] > heap->array[index - 1]) {
            return (heap->array + 2 * index - 1);
        }
    }
    else {
        // parent has two children so we compare 
        if(heap->array[2 * index - 1] > heap->array[index - 1]) {
            return (heap->array + 2 * index - 1);
        }
        else if (heap->array[2 * index] > heap->array[index  - 1]) {
            // must be right child
            return (heap->array + 2 * index);
        }
    }
    // Parent has children but has no
    // children that are bigger than parent
    return NULL;

}

// assumes array is sorted for max heap
MaxHeap *create_heap(int *array, int size) {
    MaxHeap *heap = malloc(sizeof(MaxHeap));
    heap->array = array;
    return heap;
}

/*
Returns a pointer to the maximum element in the heap.
Swaps the last element in the heap with the root, then bubbles
down the swapped element at the roop, taking Theta(log n) time. Returns
the original maximum of the heap.

If the heap is empty, returns NULL.
*/
int extract_max(MaxHeap *heap) {
    // Swap last element in the array with root
    // Then bubble down the root
    if(heap->size <= 0) {
        return __INT_MAX__;
    } 

    int root = heap->array[0];
    int tmp = heap->array[heap->size - 1];
    heap->array[heap->size - 1] = heap->array[0];
    heap->array[0] = tmp;
    heap->size--;
    // Now we bubble down
    bubble_down(heap, 1);
    return root;
}

/*
Bubbles down a node at i into its correct position.
*/
void bubble_down(MaxHeap *heap, int index) {
    int *eldest_child = get_elder_violation(heap, index);
    while(eldest_child != NULL) {
        int tmp = heap->array[index - 1];
        heap->array[index - 1] = *eldest_child;
        *eldest_child = tmp;

        eldest_child = get_elder_violation(heap, index);
    }
}

int max(MaxHeap *heap) {
    return heap->array[0];
}

/*
Increases the value of element i to value, and then bubbles up
accordingly.
Theta(logn) = Theta(height) time
*/
void increase_priority(MaxHeap *heap, int index, int value) {
    int *arr = heap->array;
    arr[index - 1] = value;

    int i = index;

    // now bubble up
    while(arr[(int) (i / 2) - 1] < arr[i - 1] && i > 1) {
        // swap positions and bubble up
        int temp = arr[(int) (i / 2) - 1];
        arr[(int) (i / 2) - 1] = arr[i - 1];
        arr[i - 1] = temp;

        i = (int) (i / 2);   
    }
}
/*
Inserts value at the end of the array to keep it nearly complete
Then bubbles up by swapping
*/
void insert(MaxHeap *heap, int value) {
    MaxHeap *tmp = heap;

    tmp = realloc(heap->array, (heap->size + 1) * sizeof(int));

    if(tmp == NULL) {
        perror("realloc");
        exit(1);
    }
    else {
        heap->array = tmp;
        heap->size++;
        heap->array[heap->size - 1] = value; 
    }

    int *arr = heap->array; 
    int i = heap->size;

    // now bubble up
    increase_priority(heap, heap->size, value);
}

/*
Preconditions: i is a node in a nearly complete binary tree.
Left(i) and Right(i) are max-heaps.

Postconditions:
Binary trees rooted at i is a max heap.

Bubbles down index to a proper position by swapping with children.
i is one based.
*/
void max_heapify_down(MaxHeap *heap, int index) {
    bubble_down(heap, index);
}

/*
Given an unsorted array A, return a max-heap that includes all elements in A.
We call maxheapinsert for each element in A, taking Theta(n logn) time.
*/
MaxHeap *build_max_heap_naive(int *array, int size) {
    MaxHeap *h = malloc(sizeof(MaxHeap));
    h->size = size;
    h->array = malloc(sizeof(int) * size);

    for(int i = 0; i < size; i++) {
        insert(h, array[i]);
    }
    return h;
}

/*
Starting from bottom of tree,
call max heapify down on all non-leaf nodes.
That is, for i = floor(n/2) to 1:
            MaxHeapifyDown
(for i as a one based index)
*/
MaxHeap *build_max_heap(int *array, int size) {
    MaxHeap *h = malloc(sizeof(MaxHeap));
    h->size = size;
    h->array = malloc(sizeof(int) * size);

    for(int i = (int) (i / 2) - 1; i > 1; i--) {
        max_heapify_down(h, i + 1);
    }
    return h;
}

/*
Implements a naive heap sort that takes Theta(n logn) time.
Given a max-heap H, we can create a sorted array by extracting max
element n times. Array will be sorted in non-ascending order. 
*/
int *naive_heap_sort(MaxHeap *heap) {
    int *sorted_array = malloc(sizeof(int) * heap->size);

    int max = extract_max(heap);
    int i = 0;
    while(max != __INT_MAX__) {
        sorted_array[i] = max;
        max = extract_max(heap);
        i++;
    }
    return sorted_array;
}

/*
Implements a smarter heap sort that takes Theta(log n) time.
Given a max-heap H, we can create a sorted array by:
    - converting A to max heap
    - point count to end of A
    - 
*/
int *heap_sort(MaxHeap *heap) {

}