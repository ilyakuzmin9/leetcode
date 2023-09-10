"""
Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.

The test cases are generated so that the answer can fit in a 32-bit integer.
"""
# dp
from typing import List
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = {0 : 1}

        for total in range(1, target + 1):
            dp[total] = 0
            for n in nums:
                dp[total] += dp.get(total - n, 0)
        return dp[target]


if __name__ == '__main__':
    n = [1, 2, 3]
    t = 4
    sol = Solution()
    result = sol.combinationSum4(n, t)
    print(result)
