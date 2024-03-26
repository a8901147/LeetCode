class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
      
        reversible_pairs = [["0","0"],["1","1"],["6","9"],["8","8"],["9","6"],]
        def dfs(n,last_digit):
            if n == 0:
                return [""]

            if n == 1:
                return ["0","1","8"]
            
            
            inners = dfs(n-2,n)
            res = []
            for l ,r in reversible_pairs:
                for inner in inners:
                    if l != '0' or n != last_digit:
                        composition = l + inner + r
                        res.append(composition)

            return res

        return dfs(n,n)
