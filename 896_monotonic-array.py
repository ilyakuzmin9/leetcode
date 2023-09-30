"""
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given array is monotonic, or false otherwise.
"""
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if nums == sorted(nums):
            return True
        elif nums == sorted(nums, reverse=True):
            return True
        else:
            return False