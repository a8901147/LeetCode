class Solution:
    def minFlips(self, target: str) -> int:
        prev = "0"
        res = 0
        for c in target:
            if prev != c:
                res += 1

            prev = c
        return res