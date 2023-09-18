"""
You have an undirected, connected graph of n nodes labeled from 0 to n - 1. You are given an array graph where graph[i] is a list of all the nodes connected with node i by an edge.

Return the length of the shortest path that visits every node. You may start and stop at any node, you may revisit nodes multiple times, and you may reuse edges.

"""
from typing import List
from collections import deque

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        queue = deque([(1 << i, i, 0) for i in range(n)])
        visited = set((1 << i, i) for i in range(n))

        while queue:
            mask, node, dist = queue.popleft()
            if mask == (1 << n) - 1:
                return dist
            for neighbor in graph[node]:
                new_mask = mask | (1 << neighbor)
                if (new_mask, neighbor) not in visited:
                    visited.add((new_mask, neighbor))
                    queue.append((new_mask, neighbor, dist + 1))


if __name__ == '__main__':
    print((1 << 4) - 1)
    graph = [[1, 2, 3], [0], [0], [0]]
    sol = Solution()
    result = sol.shortestPathLength(graph)
    print(result)
