class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        l, r = 0, 0
        res = 0
        is_positive = True
        while l<len(nums):
            while r<len(nums) and nums[r]!=0:
                if nums[r]<0:
                    is_positive = not is_positive
                if is_positive:
                    res = max(res,r-l+1)
                r += 1 

            if r<len(nums) and nums[r] == 0 and is_positive:
                r, l = r+1, r+1
                continue

            if nums[l]<0:
                is_positive = not is_positive  
            l += 1
            if is_positive:
                    res = max(res,r-l)
        return res
            

        