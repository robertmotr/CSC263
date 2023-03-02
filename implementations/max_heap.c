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

int extract_max(MaxHeap *heap) {
    // Swap last element in the array with root
    // Then bubble down the root
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

void max_heapify_down(MaxHeap *heap, int index) {
    
}