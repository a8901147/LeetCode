class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        length = len(s)
        max_appears = max(count.values())
        
        if length%2==0 and max_appears>length//2:
            return ""
        
        if length%2 and max_appears>length//2+1:
            return ""

        max_heap = [(-freq, char) for char, freq in count.items()]
        heapq.heapify(max_heap)

        res = []

        while len(max_heap)>=2:
            freq1, char1 = heapq.heappop(max_heap)
            freq2, char2 = heapq.heappop(max_heap)

            res.extend([char1,char2])

            if freq1*(-1)-1>0:
                heapq.heappush(max_heap, (freq1 + 1, char1))

            if freq2*(-1)-1>0:
                heapq.heappush(max_heap, (freq2 + 1, char2))

        if max_heap:
            freq, char = heapq.heappop(max_heap)
            res.append(char)
            
        return "".join(res)
        