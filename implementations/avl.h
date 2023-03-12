typedef struct {
    int key;
    int bf;
    AVL *left;
    AVL *right;
    AVL *p;
} AVL;

AVL *AVLSearch(AVL *root, int key);
AVL *AVLInsert(AVL *root, int key);
AVL *AVLDelete(AVL *root, int key);