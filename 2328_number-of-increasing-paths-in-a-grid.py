"""
You are given an m x n integer matrix grid, where you can move from a cell to any adjacent cell in all 4 directions.
Return the number of strictly increasing paths in the grid such that you can start from any cell and end at any cell.
Since the answer may be very large, return it modulo 109 + 7.
Two paths are considered different if they do not have exactly the same sequence of visited cells.
"""


# DFS

from typing import List
from functools import lru_cache


class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        mod = 10**9 + 7

        @lru_cache(None)
        def dfs(row, col):
            res = 1
            for dx, dy in [[row, col+1], [row+1, col], [row-1, col], [row, col-1]]:
                if 0 <= dx < rows and 0 <= dy < cols and grid[dx][dy] > grid[row][col]:
                    res += dfs(dx, dy)

            return res

        count_val = []
        for i in range(rows):
            for j in range(cols):
                count_val.append(dfs(i, j))

        return sum(count_val) % mod


if __name__ == '__main__':
    grid = [[1, 1], [3, 4]]
    sol = Solution()
    result = sol.countPaths(grid)
    print(result)
