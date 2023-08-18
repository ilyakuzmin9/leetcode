"""
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.
"""
import sys
# bfs

from typing import List
from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """
        rows = len(mat)
        cols = len(mat[0])
        q = deque()

        directions = [(1,0), (-1, 0), (0, 1), (0, -1)]
        res = [[0] * cols for _ in range(rows)]
        cache = set()

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    q.append((i, j))
                    cache.add((i, j))

        dist = 0

        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                if mat[i][j] == 1:
                    res[i][j] = dist

                for d in directions:
                    ni = i + d[0]
                    nj = j + d[1]

                    if 0 <= ni < rows and 0<= nj < cols and (ni, nj) not in cache:
                        q.append((ni, nj))
                        cache.add((ni, nj))

            dist += 1

        return res
        """
        rows = len(mat)
        cols = len(mat[0])

        res = [[sys.maxsize] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    res[i][j] = 0
                else:
                    left = res[i][j - 1] if j > 0 else sys.maxsize
                    up = res[i-1][j] if i > 0 else sys.maxsize
                    res[i][j] = min(left, up) + 1

        for i in range(rows-1, -1, -1):
            for j in range(cols - 1, -1, -1):
                if mat[i][j] == 0:
                    res[i][j] = 0
                else:
                    right = res[i][j + 1] if j < cols-1 else sys.maxsize
                    down = res[i+1][j] if i < rows-1 else sys.maxsize
                    res[i][j] = min(res[i][j], min(right, down) + 1)


        return res


if __name__ == '__main__':
    mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
    sol = Solution()
    result = sol.updateMatrix(mat)
    print(result)