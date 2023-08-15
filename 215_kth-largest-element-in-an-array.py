from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # stack = []
        # stack.append(nums[0])
        # for i in range(1, len(nums)):
        #     el = nums[i]
        #     if el >= stack[-1]:
        #         stack.append(nums[i])
        #     elif el <= stack[0]:
        #         stack.insert(0, nums[i])
        #     else:
        #         j = 0
        #         while el >= stack[j]:
        #             j += 1
        #         stack.insert(j, el)
        #
        # return stack[-k]

        # quick sort
        k = len(nums) - k
        def quick_select(l, r):
            pivot, p = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p+=1
            nums[p], nums[r] = pivot, nums[p]

            if p > k:
                return quick_select(l, p - 1)
            elif p < k:
                return quick_select(p + 1, r)
            else:
                return nums[p]

        return quick_select(0, len(nums) - 1)



if __name__ == '__main__':
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    sol = Solution()
    result = sol.findKthLargest(nums, k)
    print(result)