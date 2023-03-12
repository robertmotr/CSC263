#ifndef TREE_H
#define TREE_H

/*
As you might expect, for every node x, x.key is greater than 
every key in left sub-tree of x, and x.key is less than every key
in right sub-tree of x
*/

typedef struct {
    BST *right;
    BST *left;
    BST *p;
    int key;
} BST;

void in_order_traversal(BST *x);
void pre_order_traversal(BST *x);
void post_order_traversal(BST *x);

BST *TreeSearch(BST *root, int value);
BST *TreeMin(BST *x);
BST *TreeMax(BST *x);

BST *successor(BST *x);
BST *predecessor(BST *x);

BST *TreeInsert(BST *root, BST *node);
BST *Transplant(BST *root, BST *u, BST *v);
BST *TreeDelete(BST *x, BST *node);

#endif