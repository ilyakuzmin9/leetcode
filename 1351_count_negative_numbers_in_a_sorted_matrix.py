"""
Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise,
return the number of negative numbers in grid.
"""

from typing import List

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        def binary_search(a_list, a_left_pointer, a_right_pointer):
            while a_left_pointer <= a_right_pointer:
                mid = int((a_left_pointer + a_right_pointer) / 2)
                if a_list[mid] < 0:
                    a_right_pointer = mid - 1
                elif a_list[mid] >= 0:
                    a_left_pointer = mid + 1

            return len(a_list) - 1 - a_right_pointer

        negatives = 0
        for i in range(0, len(grid)):
            if grid[i][0] < 0:
                negatives = negatives + len(grid[i])*(len(grid) - i)
                break
            else:
                negatives = negatives + binary_search(grid[i], 0, len(grid[i])-1)


        return negatives


if __name__ == '__main__':
    grid = [[3,2],[-3,-3],[-3,-3],[-3,-3]]
    sol = Solution()
    result = sol.countNegatives(grid)
    print(result)
