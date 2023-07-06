"""
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array.
Return 0 if there is no such subarray.
"""
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        num_zero = 1
        l = 0
        for r in range(len(nums)):
            num_zero -= nums[r] == 0
            if num_zero < 0:
                num_zero += nums[l] == 0
                l += 1
        return r - l



if __name__ == '__main__':
    nums = [0,1,1,1,0,1,1,0,1]
    sol = Solution()
    result = sol.longestSubarray(nums)
    print(result)
