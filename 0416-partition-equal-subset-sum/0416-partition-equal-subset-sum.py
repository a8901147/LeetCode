class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total%2:
            return False
        
        target = sum(nums)/2
        
        dp = set([0])
        for num in nums:
            temp = set()
            for prev in dp:
                cur = num + prev
                if cur == target:
                    return True
                temp.add(cur)
                temp.add(prev)
            dp = temp
        return False
        
        