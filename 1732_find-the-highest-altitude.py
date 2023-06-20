"""
There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes.
The biker starts his trip on point 0 with altitude equal 0.

You are given an integer array gain of length n where gain[i] is the net gain in altitude
between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.
"""
from typing import List


class Solution:
    # def largestAltitude(self, gain: List[int]) -> int:
    #     res = [0]
    #     for i in range(0, len(gain)):
    #         alt = res[i]+gain[i]
    #         res.append(alt)
    #     return max(res)

    def largestAltitude(self, gain: List[int]) -> int:
        res = 0
        a = 0
        for i in gain:
            a += i
            res = max(res, a)

        return res


if __name__ == '__main__':
    gain = [-5,1,5,0,-7]
    sol = Solution()
    result = sol.largestAltitude(gain)
    print(result)
