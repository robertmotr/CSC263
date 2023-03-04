#ifndef TREE_H
#define TREE_H

typedef struct {
    BST *right;
    BST *left;
    BST *parent;
    int value;
} BST;

/* Returns 1 if value is found in x. 0 otherwise.
Takes O(h) time where h is the height of the tree.
*/
int TreeSearch(BST *x, int value);

/*
Inserts value into x. Takes O(h) time where h is the height of the tree.
Returns 1 on success, 0 otherwise.
*/
int TreeInsert(BST *x, int value);

#endif