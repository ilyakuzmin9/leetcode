from typing import List


class Solution:
    # def average(self, salary: List[int]) -> float:
    #     sorted_list = sorted(salary)
    #     sorted_list.pop(0)
    #     sorted_list.pop(-1)
    #     result = sum(sorted_list) / len(sorted_list)
    #     return result
    def average(self, salary: List[int]) -> float:
        diff = max(salary) + min(salary)
        # rs = sum(salary)
        # d = rs - diff
        result = (sum(salary) - diff) / (len(salary) - 2)
        return result


if __name__ == '__main__':
    sal_list = [4000,3000,1000,2000]
    sol = Solution()
    res = sol.average(sal_list)
