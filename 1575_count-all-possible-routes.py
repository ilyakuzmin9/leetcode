"""
You are given an array of distinct positive integers locations where locations[i] represents the position of city i.
You are also given integers start, finish and fuel representing the starting city,
ending city, and the initial amount of fuel you have, respectively.

At each step, if you are at city i, you can pick any city j such that j != i and 0 <= j < locations.length
and move to city j. Moving from city i to city j reduces the amount of fuel you have by |locations[i] - locations[j]|.
Please notice that |x| denotes the absolute value of x.

Notice that fuel cannot become negative at any point in time,
and that you are allowed to visit any city more than once (including start and finish).

Return the count of all possible routes from start to finish.
Since the answer may be too large, return it modulo 109 + 7.
"""

# DFS (current city, remining fuel)

from typing import List
from functools import lru_cache
class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:

        @lru_cache(None)
        def dfs(curr, rem):
            if rem < 0:
                return 0
            elif curr == finish:
                res = 1
            else:
                res = 0

            for next_loc in range(len(locations)):
                if curr != next_loc:
                    cost = abs(locations[curr] - locations[next_loc])
                    res += dfs(next_loc, rem - cost)

            return res % (10**9 + 7)

        return dfs(start, fuel)


if __name__ == '__main__':
    locations = [2, 3, 6, 8, 4]
    start = 1
    finish = 3
    fuel = 5
    sol = Solution()
    result = sol.countRoutes(locations, start, finish, fuel)
    print(result)

