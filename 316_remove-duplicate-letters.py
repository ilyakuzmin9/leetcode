"""
Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is
the smallest in lexicographical order
 among all possible results.
"""
from collections import Counter
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count = Counter(s)
        stack = []
        seen = set()
        for c in s:
            count[c] -= 1
            if c in seen:
                continue
            while stack and c < stack[-1] and count[stack[-1]] > 0:
                removed = stack.pop()
                seen.remove(removed)
            stack.append(c)
            seen.add(c)

        return ''.join(stack)


if __name__ == '__main__':
    s = "cbacdcbc"
    sol = Solution()
    result = sol.removeDuplicateLetters(s)
    print(result)
