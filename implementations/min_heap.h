# ifndef MINHEAP_H
# define MINHEAP_H

typedef struct {
    int *array;
} MinHeap;

// max heap functions
MinHeap *create_heap(int *array, int size);

int *max(MinHeap *MinHeap);
void increase_priority(MinHeap *MinHeap, int index, int value);
void insert(MinHeap *MinHeap, int value);
void max_heapify_down(MinHeap *MinHeap, int index);

int extract_max(MinHeap *MinHeap);

int *heap_sort(int *array, int size);

MinHeap *build_max_heap(int *array, int size);

#endif

