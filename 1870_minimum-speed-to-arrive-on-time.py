"""
You are given a floating-point number hour, representing the amount of time you have to reach the office.
To commute to the office, you must take n trains in sequential order.
You are also given an integer array dist of length n, where dist[i] describes the distance (in kilometers) of the ith train ride.

Each train can only depart at an integer hour, so you may need to wait in between each train ride.

For example, if the 1st train ride takes 1.5 hours, you must wait for an additional 0.5 hours before you can depart on the 2nd train ride at the 2 hour mark.
Return the minimum positive integer speed (in kilometers per hour) that all the trains must travel at for you to reach the office on time, or -1 if it is impossible to be on time.

Tests are generated such that the answer will not exceed 107 and hour will have at most two digits after the decimal point.
"""
from typing import List

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        INF = 10**8
        left = 1
        right = INF

        def in_time(speed):
            current = 0

            for d in dist[:-1]:
                current += (d + speed - 1) // speed

            return current + (float(dist[-1])) / float(speed) <= hour

        while left < right:
            mid = (left + right) // 2

            if in_time(mid):
                right = mid
            else:
                left = mid + 1

        if left >= INF:
            return -1

        return left