class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        total = 0
        max_speed = 0
        for pile in piles:
            total += pile
            max_speed = max(max_speed,pile)
        
        # 1. with max_speed koko has to take at least len(piles) hrs to finish
        # 2. to finish in h hrs in minimum speed, best scenario is every pile size is in same size -> min_speed = total/h
        # 3. range = (min_speed, max_speed)
        res = max_speed
        low, top = math.ceil(total/h), max_speed
        while low <= top:
            mid = (low+top)//2
            time = 0
            for pile in piles:
                time += math.ceil(pile/mid)

            if time > h:
                low = mid + 1
            else:
                top = mid - 1
                res = min(res,mid)
        return res