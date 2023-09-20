"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.
"""
from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        stack = set()
        # l = len(nums)
        for n in nums:
            if n in stack:
                return n

            stack.add(n)
            # if nums[i] in nums[i+1:l]:
            #     return nums[i]

if __name__ == '__main__':
    nums = [1,3,4,2,0,5,7,2]
    sol = Solution()
    result = sol.findDuplicate(nums)
    print(result)