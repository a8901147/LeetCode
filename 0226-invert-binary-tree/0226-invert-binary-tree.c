/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
void swap(struct TreeNode** a, struct TreeNode** b){
    struct TreeNode* temp = *a;
    *a = *b;
    *b = temp;
}

void dfs(struct TreeNode* node){
    if (!node){
        return;
    }

    swap(&node->left,&node->right);
    // struct TreeNode* temp;
    // temp = node->left;
    // node->left = node->right;
    // node->right = temp;

    dfs(node->left);
    dfs(node->right);
}

struct TreeNode* invertTree(struct TreeNode* root) {
    dfs(root);
    return root;
}