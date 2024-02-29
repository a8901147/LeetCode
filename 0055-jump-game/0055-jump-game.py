class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curMax = nums[0]
        for i in range(1,len(nums)):
            if curMax<=0:
                return False
            curMax = max(curMax-1,nums[i])
        return True

        