# ifndef HEAP_H
# define HEAP_H

// Max heap function definitions

typedef struct {
    int *array;
    int size;
    int allocated;
} MaxHeap;

int max(MaxHeap *heap); // done
int extract_max(MaxHeap *MaxHeap); // done
void increase_priority(MaxHeap *MaxHeap, int index, int value); 
void insert(MaxHeap *MaxHeap, int value); // done

void bubble_down(MaxHeap *heap, int index); // aka max_heapify_down
MaxHeap *build_max_heap_naive(int *array, int size); // done
MaxHeap *build_max_heap(int *array, int size); // done

int *heap_sort_naive(int *a, int size); // done
int *heap_sort(int *a, int size); // done

// Min heap function definitions
// TODO: define and implement min heap functions

typedef struct {
    int *array;
    int size;
} MinHeap;

#endif

