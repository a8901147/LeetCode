class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # minheap
        heapq.heapify(nums)
        n = len(nums)-k+1
        res = nums[0]
        for __ in range(n):
            res = heapq.heappop(nums)
        return res
        