"""
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size,
and the sign represents its direction (positive meaning right,
negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode.
If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.
"""
from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        state = []
        if len(asteroids) <= 1:
            state = asteroids
        for a in asteroids:
            while state and a<0<state[-1]:
                if abs(a) > state[-1]:
                    state.pop()
                elif abs(a) == state[-1]:
                    state.pop()
                    break

                else:
                    break
            else:
                state.append(a)

        return state


if __name__ == '__main__':
    asteroids = [10,2,-5]
    sol = Solution()
    result = sol.asteroidCollision(asteroids)
    print(result)
