class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        nums_a = 0
        nums_b = 0

        res = 0
        for c in text:
            
            if c == pattern[1]:
                res += nums_a
                nums_b += 1
                
            if c == pattern[0]:
                nums_a += 1
            
        return res + max(nums_a,nums_b)