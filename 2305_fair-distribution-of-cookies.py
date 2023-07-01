"""
You are given an integer array cookies, where cookies[i] denotes the number of cookies in the ith bag.
You are also given an integer k that denotes the number of children to distribute all the bags of cookies to.
All the cookies in the same bag must go to the same child and cannot be split up.

The unfairness of a distribution is defined as the maximum total cookies obtained by a single child in the distribution.

Return the minimum unfairness of all distributions.
"""
from typing import List

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:

        min_unf = float('inf')
        dist = [0] * k
        def backtrack(i):
            nonlocal min_unf, dist

            if i == len(cookies):
                min_unf = min(min_unf, max(dist))
                return

            if min_unf <= max(dist):
                return

            for j in range(k):
                dist[j] += cookies[i]
                backtrack(i+1)
                dist[j] -= cookies[i]

        backtrack(0)
        return min_unf


if __name__ == '__main__':
    cookies = [8, 15, 10, 20, 8]
    k = 2
    sol = Solution()
    result = sol.distributeCookies(cookies, k)
    print(result)
    pass