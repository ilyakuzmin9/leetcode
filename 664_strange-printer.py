"""
There is a strange printer with the following two special properties:

The printer can only print a sequence of the same character each time.
At each turn, the printer can print new characters starting from and ending at any place and will cover the original existing characters.
Given a string s, return the minimum number of turns the printer needed to print it.
"""

# dp

class Solution:
    def strangePrinter(self, s: str) -> int:

        l = len(s)
        has_cache = [[False] * l for _ in range(l)]
        cache = [[None] * l for _ in range(l)]

        def get_min(left, right):
            if left == right:
                return 1
            if left > right:
                return 0

            if has_cache[left][right]:
                return cache[left][right]

            best = get_min(left, left) + get_min(left + 1, right)

            for x in range(left + 1, right + 1):
                if s[left] == s[x]:
                    best = min(best, get_min(left, x- 1) + get_min(x + 1, right))

            has_cache[left][right] = True
            cache[left][right] = best

            return best

        return get_min(0, l - 1)


if __name__ == '__main__':
    s = "aaabbb"
    sol = Solution()
    result = sol.strangePrinter(s)
    print(result)
