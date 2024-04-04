class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        maxIndex = 0
        minIndex = 0

        for curIndex in range(1,len(nums)):
            if nums[curIndex] >= nums[maxIndex]:
                maxIndex = curIndex

            if nums[curIndex] < nums[minIndex]:
                minIndex = curIndex
        
        res = 0
        if minIndex == maxIndex:
            return 0
            
        elif minIndex < maxIndex:
            res += minIndex
            res += len(nums)-1-maxIndex
        else:
            res += minIndex
            res += len(nums)-1-maxIndex
            res -= 1
        return res