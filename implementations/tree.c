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

BST *TreeSearch(BST *root, int value) {
    if(root == NULL || value == root->key) {
        return root;
    }
    if(value < root->key) {
        return TreeSearch(root->left, value);
    }
    else {
        return TreeSearch(root->right, value);
    }
}

BST *TreeMin(BST *x) {
    while(x->left != NULL) {
        x = x->left;
    }
    return x;
}

BST *TreeMax(BST *x) {
    while(x->right != NULL) {
        x = x->right;
    }
    return x;
}


// TreeMin of right child
// or go up through parent until we're no longer in a right subtree
// case 1: worst case n time
// case 2: worst case n time
BST *successor(BST *x) {
    // two cases:
    // x has a right child
    if(x->right != NULL) {
        return TreeMin(x->right);
    }
    // x doesn't have a right child
    BST *y = x->p;
    while(y != NULL && x == y->right) {
        x = y;
        y = y->p;

    }
    return y;
}

// TreeMax of left child
// or go up through parent until we're no longer in a right subtree
// case 1: n time worst
// case 2: n time worst
BST *predecessor(BST *x) {
    // two cases
    // x has a left child
    if(x->left != NULL) {
        return TreeMax(x->left);
    }
    // x doesnt have a left child
    BST *y = x->p;
    while(y != NULL && y->right == x) {
        x = y;
        y = y->p;
    }
    return y;
}


BST *TreeInsert(BST *root, BST *node) {
    if(root == NULL) {
        root = node;
    }
    else if(node->key < root->key) {
        root->left = TreeInsert(root->left, node);
    }
    else if(node->key > root->key) {
        root->right = TreeInsert(root->right, node);
    }
    else { // x.key == root.key
        // replace root with node
    }
}

BST *Transplant(BST *root, BST *u, BST *v) {

}

BST *TreeDelete(BST *x, BST *node) {
    if(x->left == NULL) {
        Transplant(x, node, x->right);
    }
    else if(x->right == NULL) {
        Transplant(x, node, x->left);
    }
    else {
        BST *y = TreeMin(x->right);
        Transplant(x, y, y->right);
        Transplant(x, node, y);
    }
    return x;
}