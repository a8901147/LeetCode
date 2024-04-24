class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        post = 1
        post_prod = [1]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            post_prod[i] = post
            post *= nums[i]

        res = []
        prev = 1
        for i in range(len(nums)):
            res.append(post_prod[i]*prev)
            prev *= nums[i]
        
        return res
       
        
