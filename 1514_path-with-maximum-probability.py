"""
You are given an undirected weighted graph of n nodes (0-indexed), represented by an edge list where edges[i] = [a, b]
is an undirected edge connecting the nodes a and b with a probability of success of traversing that edge succProb[i].

Given two nodes start and end, find the path with the maximum probability of success to go from start to end and
return its success probability.

If there is no path from start to end, return 0.
Your answer will be accepted if it differs from the correct answer by at most 1e-5.
"""
import collections
import heapq

"""
Heap
Use Dijkstra's algorithm to find the minimum path between the two nodes after negating all costs.
"""

from typing import List


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        adj = collections.defaultdict(list)
        for i in range(len(edges)):
            src, dst = edges[i]
            adj[src].append([dst, succProb[i]])
            adj[dst].append([src, succProb[i]])

        pq = [(-1, start)]
        visit = set()

        while pq:
            prob, cur = heapq.heappop(pq)
            visit.add(cur)

            if cur == end:
                return prob * -1

            for nei, edgeProb in adj[cur]:
                if nei not in visit:
                    heapq.heappush(pq, (prob * edgeProb, nei))

        return 0


if __name__ == '__main__':
    n = 3
    edges = [[0, 1], [1, 2], [0, 2]]
    succProb = [0.5, 0.5, 0.2]
    start = 0
    end = 2
    sol = Solution()
    result = sol.maxProbability(n, edges, succProb, start, end)
    print((result))
