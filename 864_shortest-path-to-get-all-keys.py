"""
You are given an m x n grid grid where:
'.' is an empty cell.
'#' is a wall.
'@' is the starting point.
Lowercase letters represent keys.
Uppercase letters represent locks.
You start at the starting point and one move consists of walking one space in one of the four cardinal directions.
You cannot walk outside the grid, or walk into a wall.

If you walk over a key, you can pick it up and you cannot walk over a lock unless you have its corresponding key.

For some 1 <= k <= 6, there is exactly one lowercase and one uppercase letter of the first k letters of the English
alphabet in the grid.
This means that there is exactly one key for each lock, and one lock for each key;
and also that the letters used to represent the keys and locks were chosen in the same order as the English alphabet.

Return the lowest number of moves to acquire all keys. If it is impossible, return -1.
"""

# BFS
import collections
from typing import List


class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        cnt = 0
        sr = 0
        sc = 0
        n, m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] in ('abcdef'):
                    cnt += 1
                if grid[i][j] == '@':
                    sr, sc = i, j

        queue = collections.deque([(sr, sc, "")])
        moves = 0
        isVisited = set()
        while queue:
            size = len(queue)
            for _ in range(size):
                cr, cc, keys = queue.popleft()

                if len(keys) == cnt:
                    return moves

                if (cr, cc, keys) in isVisited:
                    continue
                isVisited.add((cr, cc, keys))

                for x, y in [[0,1], [1,0], [0,-1], [-1,0]]:
                    nr, nc = cr + x, cc + y
                    if nr < 0 or nc < 0 or nr >= n or nc >= m or grid[nr][nc] == '#':
                        continue

                    char = grid[nr][nc]
                    if char in 'ABCDEF' and char.lower() in keys:
                        queue.append((nr, nc, keys))

                    elif char in '.@':
                        queue.append((nr, nc, keys))

                    elif char in 'abcdef':
                        if char in keys:
                            queue.append((nr, nc, keys))

                        else:
                            queue.append((nr, nc, keys+char))

            moves += 1

        return -1


if __name__ == '__main__':
    grid = ["@.a..","###.#","b.A.B"]
    sol = Solution()
    result = sol.shortestPathAllKeys(grid)
    print(result)
