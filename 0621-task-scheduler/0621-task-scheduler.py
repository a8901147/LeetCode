class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dic = Counter(tasks)
        arr = dic.values()
        maxval = max(arr)
        
        maxtimes = Counter(arr)[maxval]
        needs = (maxval-1)*(n+1)+1+maxtimes-1

        return needs if len(tasks)<needs else len(tasks)

        