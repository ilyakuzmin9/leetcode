"""
You are given a 0-indexed integer array costs where costs[i] is the cost of hiring the ith worker.

You are also given two integers k and candidates. We want to hire exactly k workers according to the following rules:

You will run k sessions and hire exactly one worker in each session.
In each hiring session, choose the worker with the lowest cost from either the first candidates workers
or the last candidates workers. Break the tie by the smallest index.
For example, if costs = [3,2,7,7,1,2] and candidates = 2, then in the first hiring session,
we will choose the 4th worker because they have the lowest cost [3,2,7,7,1,2].
In the second hiring session, we will choose 1st worker because they have the same lowest cost as 4th worker but
they have the smallest index [3,2,7,7,2]. Please note that the indexing may be changed in the process.
If there are fewer than candidates workers remaining, choose the worker with the lowest cost among them.
Break the tie by the smallest index.
A worker can only be chosen once.
Return the total cost to hire exactly k workers.
"""
import heapq
from typing import List
from functools import lru_cache

# class Solution:
#     def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
#         final_res = 0
#         for i in range(0, k):
#             l_c = len(costs)
#             if l_c > candidates:
#                 first_c = costs[0:candidates]
#                 min_first = min(first_c)
#                 last_c = costs[l_c - 1:l_c - 1 - candidates:-1]
#                 min_last = min(last_c)
#                 if min_first <= min_last:
#                     res = min_first
#                     idx = first_c.index(res)
#                     costs.pop(idx)
#                 else:
#                     res = min_last
#                     idx = last_c.index(res)
#                     costs.pop(-(idx+1))
#             else:
#                 res = min(costs)
#                 costs.remove(res)
#
#             final_res += res
#
#         return final_res

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        q1 = []
        q2 = []
        left = 0
        right = len(costs)-1
        res = 0

        for i in range(k):
            while len(q1) < candidates and left <=right:
                heapq.heappush(q1, costs[left])
                left += 1

            while len(q2) < candidates and left<=right:
                heapq.heappush(q2, costs[right])
                right -= 1

            first = q1[0] if q1 else float('inf')
            last = q2[0] if q2 else float('inf')

            if first <= last:
                res += first
                heapq.heappop(q1)
            else:
                res += last
                heapq.heappop(q2)


        return res



if __name__ == '__main__':
    costs = [50,80,34,9,86,20,67,94,65,82,40,79,74,92,84,37,19,16,85,20,79,25,89,55,67,84,3,79,38,16,44,2,54,58]
    k = 7
    candidates = 12
    # costs = [31, 25, 72, 79, 74, 65, 84, 91, 18, 59, 27, 9, 81, 33, 17, 58]
    # k = 11
    # candidates = 9

    # costs = [17, 12, 10, 2, 7, 20, 11, 20, 8]
    # k = 3
    # candidates = 2
    # costs = [1, 2, 4, 1]
    # k = 3
    # candidates = 3
    # costs = [69, 10, 63, 24, 1, 71, 55, 46, 4, 61, 78, 21, 85, 52, 83, 77, 42, 21, 73, 2, 80, 99, 98, 89, 55, 94, 63, 50, 43,
    #  62, 14]
    # k = 21
    # candidates = 31
    sol = Solution()
    result = sol.totalCost(costs, k, candidates)
    print(result)
