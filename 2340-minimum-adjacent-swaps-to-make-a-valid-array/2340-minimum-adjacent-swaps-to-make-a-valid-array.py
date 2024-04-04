class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        maxIndex = 0
        minIndex = 0

        for curIndex in range(1,len(nums)):
            if nums[curIndex] >= nums[maxIndex]:
                maxIndex = curIndex

            if nums[curIndex] < nums[minIndex]:
                minIndex = curIndex
        
        
        if minIndex == maxIndex:
            return 0
        
        res = minIndex + len(nums)-1-maxIndex

        return res-1 if minIndex > maxIndex else res