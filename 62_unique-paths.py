"""
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # t o(n*m), s o(n*m)
        # m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = {(m - 1, n - 1): 1}

        def dfs(r, c):
            if r == m or c == n:
                return 0
            if (r, c) in dp:
                return dp[(r, c)]
            dp[(r, c)] = dfs(r + 1, c) + dfs(r, c + 1)
            return dp[(r, c)]

        return dfs(0, 0)


if __name__ == '__main__':
    m = 3
    n = 7
    sol = Solution()
    result = sol.uniquePaths(m, n)
    print(result)
