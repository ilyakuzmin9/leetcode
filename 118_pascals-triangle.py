"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
"""

from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            res = [[1]]
        else:
            res = [[1], [1, 1]]

            for i in range(2, numRows):
                # l = i
                row = [1]
                for j in range(0, i-1):
                    row.append(res[i - 1][j]+res[i-1][j+1])
                row.append(1)

                res.append(row)

        return res

if __name__ == '__main__':
    sol = Solution()
    result = sol.generate(numRows=5)
    print(result)