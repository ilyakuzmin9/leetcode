"""
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.

"""
from typing import List
from itertools import combinations

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        l = [*range(1, n+1)]
        comb = combinations(l, k)
        for i in list(comb):
            res.append(list(i))
        return res


if __name__ == '__main__':
    n = 4
    k = 2
    sol = Solution()
    result = sol.combine(n, k)
    print(result)
