class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        hashT = {}
        for index in range(len(s)):
            char = s[index]
            hashT[char] = index
        
        part = 0
        end = 0
        for index in range(len(s)):
            char = s[index]
            end = max(end,hashT[char])
            part += 1
            if index == end:
                res.append(part)
                part = 0
        
        return res

