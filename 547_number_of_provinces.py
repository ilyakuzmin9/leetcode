"""
There are n cities. Some of them are connected, while some are not.
If city a is connected directly with city b, and city b is connected directly with city c,
then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1
if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

"""

from typing import List
from collections import deque

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        q = deque()
        seen = set()
        num_prov = 0

        for i in range(0, len(isConnected)):
            if i not in seen:

                q.append(i)
                while q:
                    s = q.popleft()
                    seen.add(s)

                    for j in range(0, len(isConnected)):
                        if (isConnected[s][j] == 1 and j not in seen):
                            q.append(j)

                num_prov += 1

        return num_prov


if __name__ == '__main__':
    isConnected = [[1,0,0],[0,1,0],[0,0,1]]
    sol = Solution()
    result = sol.findCircleNum(isConnected)
    print(result)
