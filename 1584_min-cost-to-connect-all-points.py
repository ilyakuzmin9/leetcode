"""
You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.
"""

# Prim's algo, bfs
from typing import List
import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        n = len(points)
        adj = {i: [] for i in range(n)}
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        res = 0
        visit = set()
        min_heap = [[0, 0]]
        while len(visit) < n:
            cost, i = heapq.heappop(min_heap)
            if i in visit:
                continue
            res += cost
            visit.add(i)
            for nei_cost, nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(min_heap, [nei_cost, nei])
        return res


if __name__ == '__main__':
    points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
    sol = Solution()
    result = sol.minCostConnectPoints(points)
    print(result)

