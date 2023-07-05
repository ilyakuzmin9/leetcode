
#  binary
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones = 0
        twos = 0

        for num in nums:
            ones = (ones ^ num) & (~twos)
            twos = (twos ^ num) & (~ones)

        return ones










if __name__ == '__main__':
    nums = [30000,500,100,30000,100,30000,100]
    sol = Solution()
    result = sol.singleNumber(nums)
    print(result)
