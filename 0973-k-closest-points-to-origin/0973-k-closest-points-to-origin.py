class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist_collect = []
        for x, y in points:
            dist = (abs(x) ** 2) + (abs(y) ** 2)
            dist_collect.append([dist,x,y])
        
        heapq.heapify(dist_collect)
        res = []
        for i in range(k):
            dist,x,y = heapq.heappop(dist_collect)
            res.append([x,y])
        
        return res