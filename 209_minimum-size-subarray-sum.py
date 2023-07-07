"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a
subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
 """


from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        left, total = 0, 0
        res = float('inf')

        if sum(nums) < target:
            return 0


        for r in range(len(nums)):
            if nums[r] >= target:
                return 1
            total += nums[r]
            while total >= target:
                res = min(res, r - left + 1)
                total -= nums[left]
                left += 1



        return 0 if res == float('inf') else res


if __name__ == '__main__':
    target = 11
    nums = [1,2,3,4,5]
    sol = Solution()
    result = sol.minSubArrayLen(target, nums)
    print(result)
