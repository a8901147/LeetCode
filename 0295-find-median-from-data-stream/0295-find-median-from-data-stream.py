class MedianFinder:

    def __init__(self):
        self.rightHeap = []
        self.leftHeap = []
        
    def addNum(self, num: int) -> None:
        if self.rightHeap and num > self.rightHeap[0]:
            heapq.heappush(self.rightHeap, num)
        else:
            heapq.heappush(self.leftHeap, -1 * num)

        if len(self.leftHeap)-len(self.rightHeap)>1:
            extra = heapq.heappop(self.leftHeap)*-1
            heapq.heappush(self.rightHeap,extra)
        
        if len(self.rightHeap)-len(self.leftHeap)>1:
            extra = heapq.heappop(self.rightHeap)*-1
            heapq.heappush(self.leftHeap,extra)

    def findMedian(self) -> float:
        if len(self.leftHeap) == len(self.rightHeap):
            return (self.leftHeap[0]*-1+self.rightHeap[0])/2
        elif len(self.leftHeap) > len(self.rightHeap):
            return self.leftHeap[0]*-1
        else:
            return self.rightHeap[0]



# Your MedianFinder object will be                                 instantiated and called as such:
# obj = MedianFinder()     
# obj.addNum(num)
# param_2 = obj.findMedian()