"""
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
"""
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:

        # res_l = []
        #
        # for i in range(n+1):
        #     res = ''
        #     res_count = 0
        #     while i != 0:
        #         if i % 2 == 1:
        #             res_count += 1
        #         res = str(i % 2) + res
        #         i = i // 2
        #     res_l.append(res_count)
        #
        #
        # return res_l

        res_l = []

        for i in range(n + 1):
            "{0:b}".format(i)

            res_l.append("{0:b}".format(i).count("1"))

        return res_l




if __name__ == '__main__':
    n = 5
    sol = Solution()
    result = sol.countBits(n)
    print(result)
