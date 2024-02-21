class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False]*(len(s)+1)
        dp[-1]=True

        for i in range(len(dp)-2,-1,-1):
            for word in wordDict:
                if i+len(word)<=len(s) and word == s[i:i+len(word)] and dp[i+len(word)]:
                    dp[i]=True
        return dp[0]