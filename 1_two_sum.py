"""
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""

from typing import List
import time
import random


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_t = {}

        for i in range(len(nums)):
            item = target - nums[i]
            if item in hash_t and i != hash_t[item]:
                return [hash_t[item], i]
            else:
                hash_t[nums[i]] = i

        return []

# def twoSum(nums: List[int], target: int) -> List[int]:
#     list_len = range(len(nums))
#     for i in range(len(nums)):
#         sub_list_len = range(i+1, len(nums))
#         for j in range(i+1, len(nums)):
#             try:
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
#             except IndexError:
#                 break
#     return[]


# def twoSum(nums: List[int], target: int) -> List[int]:
#     hash_table = {}
#     # for i in range(len(nums)):
#     #     hash_table[nums[i]] = i
#     for i, val in enumerate(nums):
#         hash_table[val] = i
#
#     for j in range(len(nums)):
#         item = target - nums[j]
#         if item in hash_table and j != hash_table[item]:
#             return [j, hash_table[item]]
#     return []


# def twoSum(nums: List[int], target: int) -> List[int]:
#     hash_map = {}
#     for i in range(len(nums)):
#         if nums[i] in hash_map:
#             return [i, hash_map[nums[i]]]
#         else:
#             hash_map[target - nums[i]] = i


if __name__ == '__main__':
    # Generate 5 random numbers between 10 and 30
    # r_list = random.sample(range(1, 100), 99)
    r_list = [3,3]
    target = 6
    sol = Solution()
    start = time.time()
    res = sol.twoSum(r_list, target)

    print(res)
    end = time.time()
    print(end - start)
