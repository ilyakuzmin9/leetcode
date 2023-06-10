"""
You are given an array of characters letters that is sorted in non-decreasing order, and a character target.
There are at least two different characters in letters.

Return the smallest character in letters that is lexicographically greater than target.
If such a character does not exist, return the first character in letters.
"""
from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for i in range(0,len(letters)):
            if letters[i] > target:
                return letters[i]
                break
            elif i == len(letters)-1:
                return letters[0]


if __name__ == '__main__':
    letters = ["c", "f", "j"]
    target = "c"
    sol = Solution()
    result = sol.nextGreatestLetter(letters, target)
    print(result)
