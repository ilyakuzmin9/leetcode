"""
Given a wooden stick of length n units. The stick is labelled from 0 to n.
For example, a stick of length 6 is labelled as follows:
Given an integer array cuts where cuts[i] denotes a position you should perform a cut at.
You should perform the cuts in order, you can change the order of the cuts as you wish.
The cost of one cut is the length of the stick to be cut, the total cost is the sum of costs of all cuts.
When you cut a stick, it will be split into two smaller sticks
(i.e. the sum of their lengths is the length of the stick before the cut).
Please refer to the first example for a better explanation.
Return the minimum total cost of the cuts.
"""
from typing import List


class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:

        return 1


if __name__ == '__main__':
    length = 7
    cuts_list = [1, 3, 4, 5]
    sol = Solution()
    res = sol.minCost(length, cuts_list)
    print(res)
