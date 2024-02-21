class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = set()
        def dfs(i):
            if i == len(s):
                return True
            if i in memo:
                return False

            for word in wordDict:
                if s[i:i+len(word)]==word and dfs(i+len(word)):
                    return True
            
            memo.add(i)
            return False
                    
        return dfs(0)