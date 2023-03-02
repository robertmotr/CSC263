# ifndef MAXHEAP_H
# define MAXHEAP_H

typedef struct {
    int *array;
    int size;
} MaxHeap;

MaxHeap *create_heap(int *array, int size);
int max(MaxHeap *heap);
int extract_max(MaxHeap *MaxHeap);
void increase_priority(MaxHeap *MaxHeap, int index, int value);
void insert(MaxHeap *MaxHeap, int value);
void max_heapify_down(MaxHeap *MaxHeap, int index);
int *heap_sort(int *array, int size);
MaxHeap *build_max_heap(int *array, int size);

int *get_elder_violation(MaxHeap *heap, int index);
void bubble_down(MaxHeap *heap, int index);

#endif

