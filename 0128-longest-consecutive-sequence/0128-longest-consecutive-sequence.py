class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        nums = list(numset)
        nums.sort()

        res = 0
        counter = 1
        for i in range(len(nums)):
            cur = nums[i]          

            if i-1>=0 and cur == nums[i-1]+1:
                counter += 1
            else:
                counter = 1

            res = max(res,counter)
        
        return res