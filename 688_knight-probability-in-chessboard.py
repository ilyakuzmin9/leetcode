"""
On an n x n chessboard, a knight starts at the cell (row, column) and attempts to make exactly k moves. The rows and columns are 0-indexed, so the top-left cell is (0, 0), and the bottom-right cell is (n - 1, n - 1).

A chess knight has eight possible moves it can make, as illustrated below. Each move is two cells in a cardinal direction, then one cell in an orthogonal direction.


Each time the knight is to move, it chooses one of eight possible moves uniformly at random (even if the piece would go off the chessboard) and moves there.

The knight continues moving until it has made exactly k moves or has moved off the chessboard.

Return the probability that the knight remains on the board after it has stopped moving.
"""

class Solution:
    def knightProbability(self, n: int, moves: int, row: int, column: int) -> float:
        knight_moves = [(1,2),(-1,2),(1,-2),(-1,-2),
                        (2,1),(-2,1),(2,-1),(-2,-1)]
        cache = [[[None] * (moves + 1) for _ in range(n)] for _ in range(n)]
        has_cache = [[[False] * (moves + 1) for _ in range(n)] for _ in range(n)]

        def p(x, y, k):
            if k == 0:
                if x == row and y == column:
                    return 1.0
                else:
                    return 0.0

            if has_cache[x][y][k]:
                return cache[x][y][k]

            total_prob = 0.0
            for dx, dy in knight_moves:
                nx, ny = x + dx, y + dy

                if 0 <= nx < n and 0 <= ny < n:
                    total_prob += p(nx, ny, k - 1)

            has_cache[x][y][k] = True
            cache[x][y][k] = total_prob / 8.
            return cache[x][y][k]

        total_prob = 0.0
        for x in range(n):
            for y in range(n):
                total_prob += p(x, y, moves)
        return total_prob


if __name__ == '__main__':
    n = 3
    k = 2
    row = 0
    column = 0
    sol = Solution()
    result = sol.knightProbability(n, k, row, column)

    print(result)
