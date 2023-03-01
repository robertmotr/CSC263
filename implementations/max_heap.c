#include "max_heap.h"
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// implements max heap
// left: 2i
// right: 2i + 1
// where i is one-based
// parent: floor(i/2)

// assumes array is sorted for max heap
MaxHeap *create_heap(int *array, int size) {
    MaxHeap *heap = malloc(sizeof(MaxHeap));
    heap->array = array;
    return heap;
}

int extract_max(MaxHeap *heap) {
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