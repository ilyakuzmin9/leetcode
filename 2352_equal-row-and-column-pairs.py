"""
Given a 0-indexed n x n integer matrix grid,
return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order
(i.e., an equal array).
"""

from typing import List

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:

        column = []
        res = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid)):
                column.append(grid[j][i])

            res = res + grid.count(column)
            # for row in grid:
            #     if column == row:
            #         res += 1
            column = []

        return res


if __name__ == '__main__':
    grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
    sol = Solution()
    result = sol.equalPairs(grid)
    print(result)
