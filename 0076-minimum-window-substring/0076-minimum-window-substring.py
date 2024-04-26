class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""

        count_t = Counter(t)
        window_s = {}
        
        match = 0
        res = ""
        res_min = math.inf
        l = 0
        for r in range(len(s)):
            cur = s[r]
            if cur not in count_t:
                continue
            
            window_s[cur] = window_s.get(cur,0) + 1
            if window_s[cur] == count_t[cur]:
                match += 1

            while match == len(count_t):
                if r-l+1 < res_min:
                    res = s[l:r+1]
                    res_min = r-l+1

                if s[l] in count_t:
                    window_s[s[l]] -= 1
                    if window_s[s[l]] < count_t[s[l]]:
                        match -= 1
                        
                l += 1
            

        return res

        