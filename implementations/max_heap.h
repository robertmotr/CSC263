# ifndef MAXHEAP_H
# define MAXHEAP_H

typedef struct {
    int *array;
} MaxHeap;

// max heap functions
MaxHeap *create_heap(int *array, int size);

int *max(MaxHeap *MaxHeap);
void increase_priority(MaxHeap *MaxHeap, int index, int value);
void insert(MaxHeap *MaxHeap, int value);
void max_heapify_down(MaxHeap *MaxHeap, int index);

int extract_max(MaxHeap *MaxHeap);

int *heap_sort(int *array, int size);

MaxHeap *build_max_heap(int *array, int size);

#endif

