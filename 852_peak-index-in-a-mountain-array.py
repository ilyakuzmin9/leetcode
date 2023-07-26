"""
An array arr a mountain if the following properties hold:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given a mountain array arr, return the index i such that arr[0] < arr[1] < ... < arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

You must solve it in O(log(arr.length)) time complexity.
"""

from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:

        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = int((left + right) / 2)
            if mid != 0:
                if arr[mid-1] < arr[mid] > arr[mid+1]:
                    return arr[mid]
                elif arr[mid-1] < arr[mid] < arr[mid+1]:
                    left = mid + 1
                elif arr[mid-1] > arr[mid] > arr[mid+1]:
                    right = mid - 1
            else:
                if arr[mid] > arr[mid+1]:
                    return arr[mid]
                elif arr[mid] < arr[mid+1]:
                    left = mid + 1


        # return -1




if __name__ == '__main__':
    arr = [0, 1, 0]
    sol = Solution()
    result = sol.peakIndexInMountainArray(arr)
    print(result)
