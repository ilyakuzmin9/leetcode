"""
You are given a sorted unique integer array nums.
A range [a,b] is the set of all integers from a to b (inclusive).
Return the smallest sorted list of ranges that cover all the numbers in the array exactly.
That is, each element of nums is covered by exactly one of the ranges
and there is no integer x such that x is in one of the ranges but not in nums.
Each range [a,b] in the list should be output as:
"a->b" if a != b
"a" if a == b
"""
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if nums:
            res = []
            s = []
            s.append(nums[0])
            for i in range(1, len(nums)):
                try:
                    if nums[i] - nums[i-1] == 1:
                        s.append(nums[i])
                        #i += 1
                    else:
                        if len(s) > 1:

                            res.append(f"{s[0]}->{s[-1]}")
                        else:
                            res.append(str(s[0]))

                        s = [nums[i]]
                except IndexError:
                    # res.append(str(s))
                    break
            if len(s) > 1:

                res.append(f"{s[0]}->{s[-1]}")
            else:
                res.append(str(s[0]))


            return res

        else:
            return ['']


if __name__ == '__main__':
    nums = [0,1,2,4,5,7]
    sol = Solution()
    result = sol.summaryRanges(nums)
    print(result)
