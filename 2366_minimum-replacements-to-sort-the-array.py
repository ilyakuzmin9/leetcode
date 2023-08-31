"""
You are given a 0-indexed integer array nums. In one operation you can replace any element of the array with any two elements that sum to it.

For example, consider nums = [5,6,7]. In one operation, we can replace nums[1] with 2 and 4 and convert nums to [5,2,4,7].
Return the minimum number of operations to make an array that is sorted in non-decreasing order.
"""
from typing import List
from math import ceil

class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        splits = 0
        right = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            left = nums[i]
            if left > right:
                parts = ceil(left / right)
                splits += parts - 1
                right = left // parts
            else:
                right = left

        return splits



if __name__ == '__main__':
    nums = [3, 9, 3]
    sol = Solution()
    result = sol.minimumReplacement(nums)
    print(result)
