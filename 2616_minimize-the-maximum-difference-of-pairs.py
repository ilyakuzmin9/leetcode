"""
You are given a 0-indexed integer array nums and an integer p. Find p pairs of indices of nums such that the maximum difference amongst all the pairs is minimized. Also, ensure no index appears more than once amongst the p pairs.

Note that for a pair of elements at the index i and j, the difference of this pair is |nums[i] - nums[j]|, where |x| represents the absolute value of x.

Return the minimum maximum difference among all p pairs. We define the maximum of an empty set to be zero.
"""

from typing import List
class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:

        def is_valid(threshold):
            i, cnt = 0, 0
            while i < len(nums) - 1:
                if abs(nums[i] - nums[i+1]) <= threshold:
                    cnt += 1
                    i += 2
                else:
                    i += 1
                if cnt == p:
                    return True
            return False

        if p == 0:
            return 0

        nums.sort()
        left, right = 0, 10**9
        res = 10**9
        while left <= right:
            mid = left + (right - left) // 2
            if is_valid(mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1

        return res

if __name__ == '__main__':
    nums = [10, 1, 2, 7, 1, 3]
    p = 2
    sol = Solution()
    result = sol.minimizeMax(nums, p)
    print(result)