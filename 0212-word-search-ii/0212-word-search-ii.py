class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.add_word(w)
        
        res = set()
        for r in range(len(board)):
            for c in range(len(board[0])):
                visit = set()
                self.dfs_searchTree(r,c,board,root,visit,res,root,"")

        return list(res)
    
    def dfs_searchTree(self,r,c,board,node,visit,res,root,word):
        if (
            r not in range(len(board)) 
            or c not in range(len(board[0]))
            or board[r][c] not in node.children26
            or (r, c) in visit
        ):
            return
        
        
        node = node.children26[board[r][c]]
        word += board[r][c]
        if node.isword:
            node.isword = False
            res.add(word)
            root.remove_word(word)

        visit.add((r,c))
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        for x,y in dirs:
            self.dfs_searchTree(r+x,c+y,board,node,visit,res,root,word)
        visit.remove((r,c))
        
class TrieNode:
    def __init__(self):
        self.children26 = {}
        self.isword = False
        self.nums = 0
    
    def add_word(self, word:str):
        cur = self
        cur.nums += 1
        for c in word:
            if c not in cur.children26:
                cur.children26[c] = TrieNode()
            cur = cur.children26[c]
            cur.nums += 1
        cur.isword = True

    def remove_word(self, word:str):
        cur = self
        cur.nums -= 1
        for c in word:
            if c in cur.children26:
                if cur.nums == 0:
                    del cur.children26[c]
                    return 
                cur = cur.children26[c]
                cur.nums -= 1
    