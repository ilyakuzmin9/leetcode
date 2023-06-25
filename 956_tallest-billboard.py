"""
You are installing a billboard and want it to have the largest height.
The billboard will have two steel supports, one on each side. Each steel support must be an equal height.

You are given a collection of rods that can be welded together.
For example, if you have rods of lengths 1, 2, and 3, you  can weld them together to make a support of length 6.

Return the largest possible height of your billboard installation. If you cannot support the billboard, return 0.
"""


from typing import List


class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:

        # Dictionary to store maximum heights for each length
        max_heights = {0: 0}

        # Iterate through all rods
        for rod in rods:
            # Create a copy of max_heights to avoid modifying the dictionary during iteration
            for length, height in list(max_heights.items()):
                # Update the maximum heights with the current rod
                max_heights[length + rod] = max(max_heights.get(length + rod, 0), height)
                max_heights[abs(length - rod)] = max(max_heights.get(abs(length - rod), 0),
                                                     height + min(length, rod))

        return max_heights[0]  # Return the maximum height achievable for a length of 0



        # r = 0
        # if len(rods) < 2:
        #     return r
        #
        #
        # from itertools import combinations
        # def sub_sum(arr):
        #     # return list of all subsets of length r
        #     # to deal with duplicate subsets use
        #     # set(list(combinations(arr, r)))
        #     res = []
        #     for i in range(1, len(arr)):
        #         s = [sum(list(x)) for x in combinations(arr, i)]
        #         # s = combinations(arr, i)
        #         for j in s:
        #             res.append((j, sum(arr)-j))
        #
        #     return res
        #
        # for y in sub_sum(rods):
        #     if y[0] == y[1]:
        #         r = y[0]
        #         break
        #
        # return r


if __name__ == '__main__':
    rods = [1,2,3,4,5,6]
    sol = Solution()
    result = sol.tallestBillboard(rods)
    print(result)
