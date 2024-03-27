class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        def find_par(node):
            cur = node
            while cur != par[cur]:
                cur = find_par(par[cur])
            return cur

        par = [i for i in range(n)]
        rank = [1]*n
        # create the undirected map
        for n1, n2 in edges:
            p1 = find_par(n1)
            p2 = find_par(n2)

            if p1 == p2:
                continue

            if rank[p1]>=rank[p2]:
                rank[p1] += rank[p2]
                par[p2] = p1
            else:
                rank[p2] += rank[p1]
                par[p1] = p2
            
        group_num = {}
        unreachable = 0
        for node in range(n):
            p1 = find_par(node)
            unreachable += n - rank[p1]
        

        return unreachable//2
        


        
        