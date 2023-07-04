"""
We have n buildings numbered from 0 to n - 1.
Each building has a number of employees.
It's transfer season, and some employees want to change the building they reside in.

You are given an array requests where requests[i] = [fromi, toi] represents an employee's request to transfer
from building fromi to building toi.

All buildings are full, so a list of requests is achievable only if for each building,
the net change in employee transfers is zero.
This means the number of employees leaving is equal to the number of employees moving in.
For example if n = 3 and two employees are leaving building 0, one is leaving building 1, and one is leaving building 2,
there should be two employees moving to building 0, one employee moving to building 1,
and one employee moving to building 2.

Return the maximum number of achievable requests.
"""
import itertools
from typing import List

class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        # move_in = []
        # move_out = []
        # res = 0
        # stack = []
        # for i in range(0, len(requests)):
        #
        #     if requests[i][0] == requests[i][1]:
        #         if requests[i] in stack:
        #             stack.remove(requests[i])
        #         stack.append(requests[i])
        #         continue
        #     else:
        #         stack.append(requests[i])
        #
        # for j in range(0, len(stack)):
        #     move_out.append(stack[j][0])
        #     move_in.append(stack[j][1])
        #
        # for x in range(0, len(move_out)):
        #     if move_out[x] in move_in:
        #         move_in.remove(move_out[x])
        #         res += 1
        # return res

        for k in range(len(requests), 0, -1):

            for c in itertools.combinations(range(len(requests)), k):
                degree = [0] * n
                for i in c:
                    degree[requests[i][0]] -= 1
                    degree[requests[i][1]] += 1
                if not any(degree):
                    return k

        return 0

if __name__ == '__main__':
    n = 3
    requests = [[0,0],[1,1],[0,0],[2,0],[2,2],[1,1],[2,1],[0,1],[0,1]]
    sol = Solution()
    result = sol.maximumRequests(n, requests)
    print(result)
