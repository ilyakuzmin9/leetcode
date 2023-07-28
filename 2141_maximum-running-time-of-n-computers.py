"""
You have n computers. You are given the integer n and a 0-indexed integer array batteries where the ith battery can run a computer for batteries[i] minutes. You are interested in running all n computers simultaneously using the given batteries.

Initially, you can insert at most one battery into each computer. After that and at any integer time moment, you can remove a battery from a computer and insert another battery any number of times. The inserted battery can be a totally new battery or a battery from another computer. You may assume that the removing and inserting processes take no time.

Note that the batteries cannot be recharged.

Return the maximum number of minutes you can run all the n computers simultaneously.

"""

from typing import List


class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:

        batteries.sort(reverse=True)

        left = 1
        right = sum(batteries) // n

        def trgt(target):
            contrib = 0
            for b in batteries:
                contrib += min(target, b)

            return contrib >= n * target


        while left < right:
            mid = (left + right + 1) // 2

            if trgt(mid):
                left = mid
            else:
                right = mid - 1

        return  left


if __name__ == '__main__':
    n = 2
    batteries = [3, 3, 3]
    sol = Solution()
    result = sol.maxRunTime(n, batteries)
    print(result)
