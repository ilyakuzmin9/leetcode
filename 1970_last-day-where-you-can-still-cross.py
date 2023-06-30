"""
There is a 1-based binary matrix where 0 represents land and 1 represents water.
You are given integers row and col representing the number of rows and columns in the matrix, respectively.

Initially on day 0, the entire matrix is land. However, each day a new cell becomes flooded with water.
You are given a 1-based 2D array cells, where cells[i] = [ri, ci] represents that on the ith day,
the cell on the rith row and cith column (1-based coordinates) will be covered with water (i.e., changed to 1).

You want to find the last day that it is possible to walk from the top to the bottom by only walking on land cells.
You can start from any cell in the top row and end at any cell in the bottom row.
You can only travel in the four cardinal directions (left, right, up, and down).

Return the last day where it is possible to walk from the top to the bottom by only walking on land cells.
"""

# BS + BFS

from typing import List


class Solution:

    def is_possible(self, mid, n, m, cells):
        grid = [[0]*m for _ in range(n)]

        for i in range(mid):
            row, col = cells[i]
            grid[row-1][col-1] = 1

        visited = set()
        stack = [(0, col) for col in range(m) if grid[0][col] == 0]

        while stack:
            row, col = stack.pop()

            if row == n-1:
                return True

            if (row, col) in visited:
                continue

            visited.add((row, col))

            for dx, dy in [(0,1), (0, -1), (1, 0), (-1,0)]:
                new_row, new_col = row + dx, col + dy

                if 0<=new_row < n and 0 <=new_col<m and grid[new_row][new_col] == 0:
                    stack.append((new_row, new_col))

        return False



    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        left, right = 1, len(cells)
        res = -1

        while left <= right:
            mid = (left+right) // 2
            if self.is_possible(mid, row, col, cells):
                res = mid
                left = mid + 1
            else:
                right = mid - 1

        return res


if __name__ == '__main__':
    r = 2
    c = 2
    cells = [[1, 1], [2, 1], [1, 2], [2, 2]]
    sol = Solution()
    result = sol.latestDayToCross(r, c, cells)
    print(result)
