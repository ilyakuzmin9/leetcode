"""
You are given two 0-indexed integer arrays, cost and time, of size n representing the costs and the time taken to paint n different walls respectively. There are two painters available:

A paid painter that paints the ith wall in time[i] units of time and takes cost[i] units of money.
A free painter that paints any wall in 1 unit of time at a cost of 0. But the free painter can only be used if the paid painter is already occupied.
Return the minimum amount of money required to paint the n walls.
"""
from typing import List


class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        dp = {}

        def dfs(i, remain):
            if remain <= 0:
                return 0
            if i == len(cost):
                return float('inf')
            if (i, remain) in dp:
                return dp[(i, remain)]

            paint = cost[i] + dfs(i + 1, remain - 1 - time[i])
            skip = dfs(i + 1, remain)
            dp[(i, remain)] = min(paint, skip)
            return dp[(i, remain)]

        return dfs(0, len(cost))


if __name__ == '__main__':
    cost = [1, 2, 3, 2]
    time = [1, 2, 3, 2]
    sol = Solution()
    result = sol.paintWalls(cost, time)
    print(result)
