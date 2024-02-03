class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map = {i: [] for i in range(numCourses)}
        for curr, pre in prerequisites:
            pre_map[pre].append(curr)
        
        def dfs(crs):
            if crs in seen:
                return False
            
            seen.add(crs)
            for nxt in pre_map[crs]:
                if not dfs(nxt):
                    return False
            seen.remove(crs)
            pre_map[crs] = []
            return True


        for crs in pre_map:
            seen = set()
            if not dfs(crs):
                return False
        return True