"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.
"""
# dp
from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        l = len(s)
        has_cache = [False] * (l + 1)
        cache = [None] * (l + 1)

        def can_break(index):
            if index == l:
                return True

            if has_cache[index]:
                return cache[index]

            has_cache[index] = True
            for word in wordDict:
                if s[index:].startswith(word) and can_break(index + len(word)):
                    cache[index] = True
                    return True
            cache[index] = False
            return False

        return can_break(0)


if __name__ == '__main__':
    # s = "leetcode"
    # wordDict = ["leet", "code"]
    s = "applepenapple"
    wordDict = ["apple", "pen"]
    sol = Solution()
    result = sol.wordBreak(s, wordDict)
    print(result)

