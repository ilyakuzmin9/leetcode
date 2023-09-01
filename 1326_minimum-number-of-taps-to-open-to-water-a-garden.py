"""
There is a one-dimensional garden on the x-axis. The garden starts at the point 0 and ends at the point n. (i.e The length of the garden is n).

There are n + 1 taps located at points [0, 1, ..., n] in the garden.

Given an integer n and an integer array ranges of length n + 1 where ranges[i] (0-indexed) means the i-th tap can water the area [i - ranges[i], i + ranges[i]] if it was open.

Return the minimum number of taps that should be open to water the whole garden, If the garden cannot be watered return -1.
"""
import sys
from typing import List


class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        dp = [sys.maxsize] * (n+1)
        dp[0] = 0

        for i, tap_range in enumerate(ranges):
            left = max(0, i - tap_range)
            right = min(n, i + tap_range)

            for j in range(left, right + 1):
                dp[j] = min(dp[j], dp[left] + 1)

        return dp[n] if dp[n] < sys.maxsize else -1


if __name__ == '__main__':
    n = 5
    ranges = [3, 4, 1, 1, 0, 0]
    sol = Solution()
    result = sol.minTaps(n, ranges)
    print(result)
