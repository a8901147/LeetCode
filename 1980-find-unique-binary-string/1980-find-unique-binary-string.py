class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        index = 0
        res = []
        for num in nums:
            if num[index] == "0":
                res.append("1")
            else:
                res.append("0")
            index += 1
        return "".join(res)

        