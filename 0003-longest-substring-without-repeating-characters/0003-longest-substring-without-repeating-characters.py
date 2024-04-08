class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
       
        res = 0
        l = 0
        for r in range(len(s)):
            cur = s[r]
            while cur in char_index:
                char_index[s[l]] -= 1
                if char_index[s[l]] == 0:
                    del char_index[s[l]]
                l += 1
            
            char_index[cur] = char_index.get(cur,0) + 1
            res = max(res,r-l+1)

        return res
                
            