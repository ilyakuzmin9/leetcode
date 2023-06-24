"""
Given an array nums of integers, return the length of the longest arithmetic subsequence in nums.
Note that:
A subsequence is an array that can be derived from another array by deleting some or no elements
without changing the order of the remaining elements.
A sequence seq is arithmetic if seq[i + 1] - seq[i] are all the same value (for 0 <= i < seq.length - 1).

"""
# hash table
from typing import List


class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:

        # from collections import Counter
        #
        # def find_most_popular_quantity(lst):
        #     counter = Counter(lst)
        #     most_common = counter.most_common(1)
        #     most_popular_quantity = most_common[0][1]
        #     return most_popular_quantity
        #
        # res = []
        # x = 0
        # for i in range(x, len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #         diff = nums[i] - nums[j]
        #         res.append(diff)
        #
        #     x += 1

        # res = []
        # x = 0
        # for i in range(x, len(nums)-1):
        #     r = []
        #     for j in range(i+1, len(nums)):
        #         diff = nums[i] - nums[j]
        #         r.append(diff)
        #     res.append(set(r))
        #
        #     x += 1

        ht = {}

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                diff = nums[j] - nums[i]
                ht[j, diff] = ht.get((i, diff), 1) + 1

        return max(ht.values())


if __name__ == '__main__':
    nums = [83,20,17,43,52,78,68,45]
    sol = Solution()
    result = sol.longestArithSeqLength(nums)
    print(result)
    pass

