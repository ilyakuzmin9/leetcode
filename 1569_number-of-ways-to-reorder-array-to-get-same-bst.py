"""
Given an array nums that represents a permutation of integers from 1 to n.
 We are going to construct a binary search tree (BST)
 by inserting the elements of nums in order into an initially empty BST.
 Find the number of different ways to reorder nums so that the constructed BST
 is identical to that formed from the original array nums.

For example, given nums = [2,1,3], we will have 2 as the root, 1 as a left child, and 3 as a right child.
The array [2,3,1] also yields the same BST but [3,2,1] yields a different BST.
Return the number of ways to reorder nums such that the BST formed is identical to the original BST formed from nums.

Since the answer may be very large, return it modulo 109 + 7.
"""


from typing import List

class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        mod = 10**9 + 7

        def combination(nl, nr):
            return factorial[nl + nr] // factorial[nl] // factorial[nr]
        def ways(arr):
            if len(arr) <= 2:
                return 1

            root = arr[0]

            left = [num for num in arr if num < root]
            right = [num for num in arr if num > root]

            return ways(left) * ways(right) * combination(len(left), len(right))

        n = len(nums)
        factorial = [1] * n
        for i in range(1, n):
            factorial[i] = factorial[i-1] * i

        return (ways(nums) - 1) % mod


if __name__ == '__main__':
    nums = [3,4,5,1,2]
    sol = Solution()
    result = sol.numOfWays(nums)
    print(result)
