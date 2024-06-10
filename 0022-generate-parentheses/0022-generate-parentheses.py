class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        l = 0
        r = 0

        res = []
        
        def dfs(l,r,part):
            if l == n and r == n:
                res.append(part[:])
                return

            if r+1<=n and l > r:
                dfs(l,r+1,part+")")

            if l+1<=n:
                dfs(l+1,r,part+"(")
        
        dfs(0,0,"")
        return res
            