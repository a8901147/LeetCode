# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        # get the height
        q = [root]
        height = -1 
        while q:
            height += 1
            next_level = []
            while q:
                node = q.pop()
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            q = next_level
    
        # start to update the square val (res) once know the height
        rows = height+1
        cols = 2 ** rows -1 
        middle = cols//2

        res = [["" for __ in range(cols)] for __ in range(rows)]
        
        q = [[root,0,cols-1]]
        row = 0
        while q:
            next_level = []
            while q:
                node, l, r = q.pop()
                middle = (l+r)//2
                res[row][middle] = str(node.val)
                if node.left:
                    next_level.append([node.left,l,middle-1])
                if node.right:
                    next_level.append([node.right,middle+1,r])
            q = next_level
            row += 1

        return res
        