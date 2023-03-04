#include "tree.h"
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

/*
Traverses through the BST using an in-order pattern.
Calls the parameter func on each node. If func is NULL, then simply prints
each node. Takes O(h) time where h is height of the BST.
*/
void in_order_traversal(BST *x) {
    if(x != NULL) {
        in_order_traversal(x->left);
        printf("%d ", x->key);
        in_order_traversal(x->right);
    }
}

void pre_order_traversal(BST *x) {
    if(x != NULL) {
        printf("%d ", x->key);
        pre_order_traversal(x->left);
        pre_order_traversal(x->right);
    }
}

void post_order_traversal(BST *x) {
    if(x != NULL) {
        post_order_traversal(x->left);
        post_order_traversal(x->right);
        printf("%d ", x->key);
    }
}

int BSTSearch(BST *x, int value) {
    if(x != NULL) {
        if(value > x->key) {
            return BSTSearch(x->right, value);
        }
        if(value < x->key) {
            return BSTSearch(x->left, value);
        }
        // found
        return 1;
    }
    return 0;
}

BST *BSTMin(BST *x) {
    if(x != NULL) {
        while(x->left != NULL) {
            x = x->left;
        }
        return x;
    }
    return NULL;
}

BST *BSTMax(BST *x) {
    if(x != NULL) {
        while(x->right != NULL) {
            x = x->right;
        }
        return x;
    }
    return NULL;
}

int BSTInsert(BST *x, int value) {
    if(x == NULL) {
        BST *tmp = x;
        x = malloc(sizeof(BST));
        x->left = NULL; x->right = NULL; x->p = tmp;
        x->key = value;
        return 1;
    }
    else if(x->key > value) {
        x->left = BSTInsert(x->left, value);
    }
    else if(x->key < value) {
        x->right = BSTInsert(x->right, value);
    }
    else {
        // do nothing since node already exists
    }
}
