"""
There is an infrastructure of n cities with some number of roads connecting these cities. Each roads[i] = [ai, bi] indicates that there is a bidirectional road between cities ai and bi.

The network rank of two different cities is defined as the total number of directly connected roads to either city. If a road is directly connected to both cities, it is only counted once.

The maximal network rank of the infrastructure is the maximum network rank of all pairs of different cities.

Given the integer n and the array roads, return the maximal network rank of the entire infrastructure.

"""
from typing import List

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for a, b in roads:
            graph[a].append(b)
            graph[b].append(a)

        max_rank = 0

        for i in range(n):
            for j in range(i + 1, n):
                rank = len(graph[i]) + len(graph[j])
                if j in graph[i] or i in graph[j]:
                    rank -= 1

                max_rank = max(max_rank, rank)


        return max_rank


if __name__ == '__main__':
    n = 4
    roads = [[0, 1], [0, 3], [1, 2], [1, 3]]
    sol = Solution()
    result = sol.maximalNetworkRank(n, roads)
    print(result)
