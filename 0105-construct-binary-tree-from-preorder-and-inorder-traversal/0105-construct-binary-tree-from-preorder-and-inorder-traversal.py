# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        parent = TreeNode(preorder[0])
        mid_index = inorder.index(preorder[0])
        parent.left = self.buildTree(preorder[1:1+mid_index],inorder[:mid_index])
        parent.right = self.buildTree(preorder[1+mid_index:],inorder[mid_index+1:])
        return parent