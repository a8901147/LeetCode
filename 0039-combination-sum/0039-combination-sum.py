class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        part = []
        def backtrack(nums, target):
            if target == 0:
                res.append(part[:])
                return 
            
            for i in range(len(nums)):
                if nums[i]<=target:
                    part.append(nums[i])
                    backtrack(nums[i:],target-nums[i])
                    part.pop()

        backtrack(candidates,target)
        return res
