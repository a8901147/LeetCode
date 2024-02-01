class Solution:
    def partition(self, s: str) -> List[List[str]]:
        part = []
        res = []
        def backtrack(i):
            if i == len(s):
                res.append(part[:])
                return 
            for index in range(i ,len(s)):
                string = s[i:index+1]
                if is_palindrome(string):
                    part.append(string)
                    backtrack(index+1)
                    part.pop()

        def is_palindrome(s):
            l, r = 0, len(s)-1
            while l<=r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True
        
        backtrack(0)
        return res
