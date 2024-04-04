class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        chronological_records = []
        for time, user, web in zip(timestamp,username,website):
            chronological_records.append([time,user,web])
        chronological_records.sort()
        
        user_pattern = defaultdict(list)
        for time, user, web in chronological_records:
            user_pattern[user].append(web)
        

        count_cal = defaultdict(int)
        for user in user_pattern:
            webs = user_pattern[user]
            if len(webs)<3:
                continue
            
            webRoutes = set()
            for first in range(len(webs)-2):
                for second in range(first+1,len(webs)-1):
                    for third in range(second+1,len(webs)):
                        web1 = webs[first]
                        web2 = webs[second]
                        web3 = webs[third]
                        webRoutes.add((web1,web2,web3))
            
            for webRoute in webRoutes:
                count_cal[webRoute] += 1
        
        res = []
        for pattern in count_cal:
            num = count_cal[pattern]
            res.append([num,pattern])
        
        res.sort()
        pattern = res[-1][1]
        num = res[-1][0]
        i = len(res)-2
        while i>=0 and num == res[i][0]:
            pattern = res[i][1]
            i -= 1

        return pattern