class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        memo = {}
        def dfs(start,end,getmax):
            if start>end:
                return 0
            if (start,end,getmax) in memo:
                return memo[(start,end,getmax)]
                
            if getmax:
                memo[(start,end,getmax)] = max(nums[start]+dfs(start+1,end,False),nums[end]+dfs(start,end-1,False))
                return memo[(start,end,getmax)]
            else:
                memo[(start,end,getmax)] = min(dfs(start+1,end,True),dfs(start,end-1,True))
                return memo[(start,end,getmax)]

        player1 = dfs(0,len(nums)-1,True)
        return player1>=sum(nums)-player1