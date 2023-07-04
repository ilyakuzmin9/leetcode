"""
Given two strings s and goal, return true if you can swap two letters in s so the result is equal to goal,
otherwise, return false.

Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j
and swapping the characters at s[i] and s[j].

For example, swapping at indices 0 and 2 in "abcd" results in "cbad".
"""
from collections import Counter


class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:

        c1, c2 = Counter(A), Counter(B)
        if c1 != c2:
            return False

        diff = sum([1 for i in range(len(A)) if A[i] != B[i]])

        if diff == 2:
            return True
        elif diff == 0:
            return any([cnt > 1 for char, cnt in c1.items()])
        else:
            return False


if __name__ == '__main__':
    s = "ab"
    goal = "ba"
    sol = Solution()
    result = sol.buddyStrings(s, goal)
    print(result)
