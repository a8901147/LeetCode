/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int maxDepth(struct TreeNode* root) {
    if (!root){
        return 0;
    }
    int leftmax = maxDepth(root->left);
    int rightmax = maxDepth(root->right);
    return fmax(leftmax,rightmax)+1;
}