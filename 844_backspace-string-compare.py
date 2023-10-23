"""
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.
"""


class Solution:
    def backspaceCompare(self, s: str, t: str):
        new_s, new_t = "", ""
        count = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '#':
                count += 1
                continue
            if count > 0:
                count -= 1
                continue
            new_s += s[i]

        for j in range(len(t) - 1, -1, -1):
            if s[t] == '#':
                count += 1
                continue
            if count > 0:
                count -= 1
                continue
            new_s += t[i]

        if new_s == new_t:

            return True
        else:
            return False


if __name__ == '__main__':
    s = "ab#c"
    t = "ad#c"
    sol = Solution()
    result = sol.backspaceCompare(s, t)
    print(result)