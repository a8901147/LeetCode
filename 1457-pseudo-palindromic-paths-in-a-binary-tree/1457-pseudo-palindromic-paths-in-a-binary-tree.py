# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:

        res = [0]
        tracker = defaultdict(int)
        def dfs(node):
            if not node:
                return 

            tracker[node.val] += 1
            dfs(node.left)
            dfs(node.right)

            if not node.left and not node.right:
                check_palidrome()

            tracker[node.val] -= 1

        def check_palidrome():
            odd_num = 0
            for node in tracker:
                if tracker[node]%2:
                    odd_num += 1
                    if odd_num>1:
                        return False
            res[0] += 1
            return True

        dfs(root)
        return res[0]