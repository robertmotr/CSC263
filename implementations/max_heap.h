# ifndef MAXHEAP_H
# define MAXHEAP_H

typedef struct {
    int *array;
    int size;
} MaxHeap;

MaxHeap *create_heap(int *array, int size); // done
int max(MaxHeap *heap); // done
int extract_max(MaxHeap *MaxHeap); // done
void increase_priority(MaxHeap *MaxHeap, int index, int value); // done
void insert(MaxHeap *MaxHeap, int value); // done
void max_heapify_down(MaxHeap *MaxHeap, int index); // done

MaxHeap *build_max_heap_naive(int *array, int size); // done
MaxHeap *build_max_heap(int *array, int size); // done

int *get_elder_violation(MaxHeap *heap, int index); // done
void bubble_down(MaxHeap *heap, int index); // done

int *naive_heap_sort(MaxHeap *heap); // done
int *heap_sort(MaxHeap *heap);

#endif

