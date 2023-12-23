# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(node1, node2):
            if node2.left:
                if node1.left:
                    node1.left.val += node2.left.val
                    dfs(node1.left,node2.left)
                else:
                    node1.left = node2.left

            if node2.right:
                if node1.right:
                    node1.right.val += node2.right.val
                    dfs(node1.right,node2.right)
                else:
                    node1.right = node2.right

        if root1 and root2:
            root1.val += root2.val
            head = root1
            dfs(root1,root2)
            return head
        else:
            return root1 if root1 else root2