class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        cache = [0]*len(nums)

        for num in nums:
            if cache[num]:
                return num
            cache[num] = 1

