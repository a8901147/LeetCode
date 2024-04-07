class Solution:
    def knightDialer(self, n: int) -> int:
        adj = {
            0:[4,6],
            1:[6,8],
            2:[7,9],
            3:[4,8],
            4:[0,3,9],
            5:[],
            6:[0,1,7],
            7:[2,6],
            8:[1,3],
            9:[2,4],
        }

        MOD = 10 ** 9 + 7
        def dfs(node,times):
            if times-1 == 0:
                return 1
            if (node,times) in memo:
                return memo[(node,times)]

            total = 0
            for nxt in adj[node]:
                total += dfs(nxt,times-1)
                
            total = total % MOD
            memo[(node,times)] = total
            return total

        res = 0
        memo = {}
        for node in range(10):
            
            res = (res + dfs(node, n)) % MOD  # Apply the MOD here as well

        return res
        