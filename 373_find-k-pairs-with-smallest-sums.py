"""
You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.
Define a pair (u, v) which consists of one element from the first array and one element from the second array.
Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.
"""


from typing import List
from collections import defaultdict
import heapq



class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # res = defaultdict(list)
        # for i in range(0, len(nums1)):
        #     for j in range(0, len(nums2)):
        #         res[nums1[i]+nums2[j]].append([nums1[i], nums2[j]])
        # final_res = []
        #
        # s = min(res.keys())
        # final_res.append(res[s])
        # res.pop(s)
        #
        #
        # return final_res

        # res = []
        # for i in range(0, k):
        #     for j in range(0, k):
        #         try:
        #             heapq.heappush(res, (nums1[i]+nums2[j], [nums1[i], nums2[j]]))
        #         except IndexError:
        #             break
        #
        # final_res = []
        # # first = res[0] if res else float('inf')
        # for _ in range(0, k):
        #     try:
        #         final_res.append(res[0][1])
        #         heapq.heappop(res)
        #     except IndexError:
        #         break
        #
        # return final_res

        res = []
        if not nums1 or not nums2 or not k:
            return res

        heap = []
        visited = set()
        heapq.heappush(heap, (nums1[0]+nums2[0], 0, 0))
        visited.add((0, 0))

        while k and heap:
            _, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])

            if i + 1 < len(nums1) and (i + 1, j) not in visited:
                heapq.heappush(heap, (nums1[i + 1]+nums2[j], i+1, j))
                visited.add((i+1, j))
            if j + 1 < len(nums2) and (i, j + 1) not in visited:
                heapq.heappush(heap, (nums1[i]+nums2[j+1], i, j+1))
                visited.add((i, j+1))

            k -= 1

        return res


if __name__ == '__main__':
    nums1 = [1, 1, 2]
    nums2 = [1, 2, 3]
    k = 2
    # nums1 = [1,7,11]
    # nums2 = [2,4,6]
    # k = 3
    # nums1 = [1, 2]
    # nums2 = [3]
    # k = 3
    sol = Solution()
    result = sol.kSmallestPairs(nums1, nums2, k)
    print(result)
