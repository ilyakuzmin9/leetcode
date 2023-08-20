"""
Given a weighted undirected connected graph with n vertices numbered from 0 to n - 1, and an array edges where edges[i] = [ai, bi, weighti] represents a bidirectional and weighted edge between nodes ai and bi. A minimum spanning tree (MST) is a subset of the graph's edges that connects all vertices without cycles and with the minimum possible total edge weight.

Find all the critical and pseudo-critical edges in the given graph's minimum spanning tree (MST). An MST edge whose deletion from the graph would cause the MST weight to increase is called a critical edge. On the other hand, a pseudo-critical edge is that which can appear in some MSTs but not all.

Note that you can return the indices of the edges in any order.
"""

from typing import List

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, v1):
        while v1 != self.parent[v1]:
            self.parent[v1] = self.parent[self.parent[v1]]
            v1 = self.parent[v1]
        return v1

    def union(self, v1, v2):
        root_parent1, root_parent2 = self.find(v1), self.find(v2)
        if root_parent1 == root_parent2:
            return False
        if self.rank[root_parent1] > self.rank[root_parent2]:
            self.parent[root_parent2] = root_parent1
            self.rank[root_parent1] += self.rank[root_parent2]
        else:
            self.parent[root_parent1] = root_parent2
            self.rank[root_parent2] += self.rank[root_parent1]

        return True




class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        for i, e in enumerate(edges):
            e.append(i)

        edges.sort(key=lambda e: e[2])

        mst_weight = 0
        uf = UnionFind(n)
        for v1, v2, w, i in edges:
            if uf.union(v1, v2):
                mst_weight += w

        critical, pseudo = [], []
        for n1, n2, e_weight, i in edges:
            weight = 0
            uf = UnionFind(n)
            for v1, v2, w, j in edges:
                if i != j and uf.union(v1, v2):
                    weight += w

            if max(uf.rank) != n or weight > mst_weight:
                critical.append(i)
                continue

            uf = UnionFind(n)
            uf.union(n1, n2)
            weight = e_weight
            for v1, v2, w, j in edges:
                if uf.union(v1, v2):
                    weight += w
            if weight == mst_weight:
                pseudo.append(i)

        return [critical, pseudo]





        return 1



if __name__ == '__main__':
    n = 5
    edges = [[0, 1, 1], [1, 2, 1], [2, 3, 2], [0, 3, 2], [0, 4, 3], [3, 4, 3], [1, 4, 6]]
    sol = Solution()
    result = sol.findCriticalAndPseudoCriticalEdges(n, edges)
    print(result)
