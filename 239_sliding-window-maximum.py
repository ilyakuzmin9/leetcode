from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        # left, right = 0, k
        #
        # res = []
        # for i in range(0, len(nums) + 1 - k):
        #     arr = nums[i + left : i + right]
        #     res.append(max(arr))
        #
        # return res

        res = []
        q = deque() # index
        left = right = 0

        while right < len(nums):
            while q and nums[q[-1]] < nums[right]:
                q.pop()
            q.append(right)

            if left > q[0]:
                q.popleft()

            if (right + 1) >= k:
                res.append(nums[q[0]])
                left += 1
            right += 1

        return res


if __name__ == '__main__':
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    sol = Solution()
    result = sol.maxSlidingWindow(nums, k)
    print(result)
