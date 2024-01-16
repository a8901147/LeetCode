# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):  
            if not node:
                return [0,True]
            left_depth, left_isbalanced = dfs(node.left)
            right_depth, right_isbalanced = dfs(node.right)
            height_diff = abs(left_depth-right_depth)
            if not left_isbalanced or not right_isbalanced or height_diff>1:
                return [0,False]
            
            return [max(left_depth,right_depth)+1,True]
        return dfs(root)[1]
            

        