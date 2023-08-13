"""
You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * 109.


"""

# dp dfs

from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # t o(n*m), s o(n*m)
        # m, n = len(obstacleGrid), len(obstacleGrid[0])
        # dp = {(m - 1, n - 1): 1}
        #
        # def dfs(r, c):
        #     if r == m or c == n or obstacleGrid[r][c]:
        #         return 0
        #     if (r, c) in dp:
        #         return dp[(r, c)]
        #     dp[(r, c)] = dfs(r + 1, c) + dfs(r, c + 1)
        #     return dp[(r, c)]
        # return dfs(0, 0)

        # t o(n*m), s o(n)
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * n
        dp[n-1] = 1

        for r in reversed(range(m)):
            for c in reversed(range(n)):
                if obstacleGrid[r][c]:
                    dp[c] = 0
                elif c + 1 < n:
                    dp[c] = dp[c] + dp[c + 1]
                else:
                    dp[c] = dp[c] + 0
        return dp[0]






if __name__ == '__main__':
    obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    sol = Solution()
    result = sol.uniquePathsWithObstacles(obstacleGrid)
    print(result)
