"""
You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.

A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

Return the minimum effort required to travel from the top-left cell to the bottom-right cell.
"""
import heapq
# bfs priorityAQueue -> Djikstra's
from typing import List
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])

        min_heap = [[0, 0, 0]] # [diff, r, c]
        visit = set()
        directions = [[0, 1], [1, 0], [0, -1], [-1,0]]
        while min_heap:
            diff, r, c = heapq.heappop(min_heap)
            if (r, c) in visit:
                continue
            visit.add((r, c))
            if (r, c) == (rows - 1, cols - 1):
                return diff

            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                if (new_r < 0 or new_c < 0 or new_r == rows or new_c == cols or(new_r, new_c) in visit):
                    continue

                new_diff = max(diff, abs(heights[r][c] - heights[new_r][new_c]))
                heapq.heappush(min_heap, [new_diff, new_r, new_c])




if __name__ == '__main__':
    heights = [[1, 2, 2], [3, 8, 2], [5, 3, 5]]
    sol = Solution()
    result = sol.minimumEffortPath(heights)
    print(result)

