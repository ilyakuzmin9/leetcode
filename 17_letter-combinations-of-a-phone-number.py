"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

"""

from typing import List
from itertools import combinations, product

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        map = {'0': '', '1': '', '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        full_list = []
        for i in range(0, len(digits)):
            full_list.append(list(map[digits[i]]))


        # comb = combinations(full_str, len(digits))
        # for j in comb:
        #     res.append(j)

        res = list(product(*full_list))
        res_fin = [''.join(j) for j in res]


        return res_fin


if __name__ == '__main__':
    digits = "23"
    sol = Solution()
    result = sol.letterCombinations(digits)
    print(result)
