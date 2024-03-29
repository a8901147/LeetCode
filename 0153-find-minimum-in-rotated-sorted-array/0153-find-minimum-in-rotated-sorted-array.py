class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l < r:
            mid = (l+r)//2
            if nums[mid] < nums[len(nums)-1]:
                r = mid
            else:
                l = mid + 1
        return nums[l]