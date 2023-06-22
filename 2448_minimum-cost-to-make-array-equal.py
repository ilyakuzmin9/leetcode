"""
You are given two 0-indexed arrays nums and cost consisting each of n positive integers.

You can do the following operation any number of times:

Increase or decrease any element of the array nums by 1.
The cost of doing one operation on the ith element is cost[i].

Return the minimum total cost such that all the elements of the array nums become equal.
"""

# use Binary Search
from typing import List
class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:

        def cal_cost(l):
            total_cost = 0
            for i, x in enumerate(nums):
                total_cost += abs(l - x) * cost[i]

            return total_cost

        left = min(nums)
        right = max(nums)
        mid = (left + right) // 2

        while left < right:
            if cal_cost(mid) < cal_cost(mid + 1):
                right = mid
            else:
                left = mid + 1

            mid = (left + right) // 2

        return cal_cost(left)

if __name__ == '__main__':
    nums = [1, 3, 5, 2]
    cost = [2, 3, 1, 14]
    sol = Solution()
    result = sol.minCost(nums, cost)
    print(result)

