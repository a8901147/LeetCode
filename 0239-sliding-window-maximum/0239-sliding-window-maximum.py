class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        window = deque([]) #(index,val)
        for r in range(len(nums)):
            cur = nums[r]
            if window and r-window[0][0]==k:
                window.popleft()
            
            while window and window[-1][1] <= cur:
                window.pop()
            window.append([r,cur])

            if r >= k-1:
                res.append(window[0][1])

        return res