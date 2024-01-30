class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        part = []
        res = []
        def backtrack(nums):
            if not nums:
                res.append(part[:])
                return 
            part.append(nums[0])
            backtrack(nums[1:])
            part.pop()
            backtrack(nums[1:])
        backtrack(nums)
        return res


        