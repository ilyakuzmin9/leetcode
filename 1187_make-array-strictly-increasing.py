"""
Given two integer arrays arr1 and arr2,
return the minimum number of operations (possibly zero) needed to make arr1 strictly increasing.

In one operation,
you can choose two indices 0 <= i < arr1.length and 0 <= j < arr2.length and do the assignment arr1[i] = arr2[j].

If there is no way to make arr1 strictly increasing, return -1.
"""
import bisect
from typing import List


class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:

        arr2.sort()
        def find(value):
            res = float('inf')
            left, right = 0, len(arr2) - 1
            while left <= right:
                pivot = (left + right) // 2
                if arr2[pivot] > value:
                    res = min(res, arr2[pivot])
                    right = pivot - 1
                else:
                    left = pivot + 1

            return res if res != float('inf') else -1

        visited = {}

        def dp(index, prev):
            if index == len(arr1):
                return 0
            if (index, prev) in visited:
                return visited[(index, prev)]

            res = float('inf')

            if arr1[index] > prev:
                res = min(res, dp(index + 1, arr1[index]))

            greater_than = find(prev)
            if greater_than != -1:
                res = min(res, 1 + dp(index + 1, greater_than))

            visited[(index, prev)] = res

            return res

        res = dp(0, -1)
        return res if res != float('inf') else -1



if __name__ == '__main__':
    arr1 = [1, 5, 3, 6, 7]
    arr2 = [1, 3, 2, 4]
    sol = Solution()
    result = sol.makeArrayIncreasing(arr1, arr2)
    print(result)
