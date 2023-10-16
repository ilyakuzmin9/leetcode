"""
You have a pointer at index 0 in an array of size arrLen. At each step, you can move 1 position to the left, 1 position to the right in the array, or stay in the same place (The pointer should not be placed outside the array at any time).

Given two integers steps and arrLen, return the number of ways such that your pointer is still at index 0 after exactly steps steps. Since the answer may be too large, return it modulo 109 + 7.
"""


class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        max_position = min(steps // 2 + 1, arrLen)
        cur_ways = [0] * (max_position + 2)
        next_ways = [0] * (max_position + 2)
        cur_ways[1] = 1
        mod = 10 ** 9 + 7

        while steps > 0:
            for pos in range(1, max_position + 1):
                next_ways[pos] = (cur_ways[pos] + cur_ways[pos - 1] + cur_ways[pos + 1]) % mod

            cur_ways, next_ways = next_ways, cur_ways
            steps -= 1

        return cur_ways[1]  


if __name__ == '__main__':
    steps = 3
    arrLen = 2
    sol = Solution()
    result = sol.numWays(steps, arrLen)
    print(result)