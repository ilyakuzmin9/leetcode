"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

"""
from typing import List
from itertools import permutations


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        l = len(nums)
        perm = permutations(nums, l)
        for i in list(perm):
            res.append(list(i))
        return res


if __name__ == '__main__':
    nums = [1,2,3]
    sol = Solution()
    result = sol.permute(nums)
    print(result)
