from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sort_arr = sorted(nums1 + nums2)
        len_arr = len(sort_arr)
        if len_arr % 2 == 0:
            mid = len_arr // 2
            return (sort_arr[mid-1] + sort_arr[mid]) / 2
        else:
            mid = len_arr // 2
            return sort_arr[mid]



if __name__ == '__main__':
    nums1 = [2]
    nums2 = [1,2,3,4,5,6]
    sol = Solution()
    arr = sol.findMedianSortedArrays(nums1, nums2)
    print(arr)