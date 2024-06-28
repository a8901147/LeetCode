/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

void dfs(struct TreeNode* node){
    if (!node){
        return;
    }

    struct TreeNode* temp;
    temp = node->left;
    node->left = node->right;
    node->right = temp;

    dfs(node->left);
    dfs(node->right);
}

struct TreeNode* invertTree(struct TreeNode* root) {
    dfs(root);
    return root;
}