"""
Companies
Given an integer array arr and an integer difference,
return the length of the longest subsequence in arr which is an arithmetic sequence
 such that the difference between adjacent elements in the subsequence equals difference.

A subsequence is a sequence that can be derived from arr by deleting some or no elements without changing the order
of the remaining elements.
"""

# dyn pr

from typing import List
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:

        dp = {}
        max_length = 1

        for num in arr:
            if num - difference in dp:
                dp[num] = dp[num-difference] + 1
            else:
                dp[num] = 1

            max_length = max(max_length, dp[num])


        return max_length


if __name__ == '__main__':
    arr = [1, 2, 3, 4]
    difference = 1
    sol = Solution()
    result = sol.longestSubsequence(arr, difference)
    print(result)
