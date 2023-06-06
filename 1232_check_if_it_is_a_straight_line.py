"""
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point.
Check if these points make a straight line in the XY plane.
"""

from typing import List


class Solution:
    # def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
    #     if len(coordinates) <= 2:
    #         return True
    #     else:
    #         default_vector = [coordinates[1][0] - coordinates[0][0], coordinates[1][1] - coordinates[0][1]]
    #         for i in range(1, len(coordinates)):
    #             try:
    #                 next_vector = [coordinates[i+1][0] - coordinates[i][0], coordinates[i+1][1] - coordinates[i][1]]
    #
    #                 if 0 in default_vector:
    #                     idx = default_vector.index(0)
    #                     if next_vector[idx] != 0:
    #                         return False
    #
    #                 elif 0 in next_vector:
    #                     idx = next_vector.index(0)
    #                     if default_vector[idx] != 0:
    #                         return False
    #
    #                 else:
    #                     ratio0 = default_vector[0] / next_vector[0]
    #                     ratio1 = default_vector[1] / next_vector[1]
    #
    #                     if ratio0 == ratio1:
    #                         default_vector = next_vector
    #                     else:
    #                         return False
    #
    #             except IndexError:
    #                 break
    #
    #     return True

    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:

        # (y[3] - y[1]) * (x[2] - x[1]) == (y[2]-y[1]) * (x[3] - x[1])

        dx = coordinates[1][0] - coordinates[0][0]
        dy = coordinates[1][1] - coordinates[0][1]

        for i in range(2, len(coordinates)):
            if (coordinates[i][1] - coordinates[0][1]) * dx != dy * (coordinates[i][0] - coordinates[0][0]):
                return False

        return True




if __name__ == '__main__':
    # coordinates = [[0, 1], [1, 3], [-4, -7], [5, 11]]
    coordinates = [[1, 2], [2, 3], [3, 5]]
    # coordinates = [[0, 0], [0, 5], [5, 5], [5, 0]]
    # coordinates = [[1, 1], [2, 2], [2, 0]]
    # coordinates = [[0,0],[0,1],[0,-1]]
    # coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
    sol = Solution()
    result = sol.checkStraightLine(coordinates)
    print(result)
