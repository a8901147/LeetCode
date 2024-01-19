# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(minVal,node,maxVal):
            if not node:
                return True
            
            if minVal < node.val < maxVal:
                return dfs(minVal,node.left,node.val) and dfs(node.val,node.right,maxVal)
            
            return False

        
        return dfs(-math.inf,root,math.inf)