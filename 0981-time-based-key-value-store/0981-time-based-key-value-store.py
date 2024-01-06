class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([timestamp,value])

    def get(self, key: str, timestamp: int) -> str:
        time = self.store[key]
        if not time or time[0][0] > timestamp:
            return ""
        
        l, r = 0, len(time) - 1
        prev_time = 0
        res = ""
        while l<=r:
            mid = (l+r)//2
            if time[mid][0] > timestamp:
                r = mid - 1
            else:
                if prev_time < time[mid][0]:
                    prev_time = max(prev_time,time[mid][0])
                    res = time[mid][1]
                l = mid + 1

        return res



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)