class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = []
        part = []

        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(i):
            if i == len(digits):
                res.append("".join(part[:]))
                return 
            for c in digitToChar[digits[i]]:
                part.append(c)
                backtrack(i+1)
                part.pop()

        backtrack(0)
        return res
        