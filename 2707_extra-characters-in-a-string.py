"""
You are given a 0-indexed string s and a dictionary of words dictionary. You have to break s into one or more non-overlapping substrings such that each substring is present in dictionary. There may be some extra characters in s which are not present in any of the substrings.

Return the minimum number of extra characters left over if you break up s optimally.
"""

# dp
from typing import List
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        words = set(dictionary)

        dp = {len(s): 0}

        def dfs(i):
            if i in dp:
                return dp[i]

            res = 1 + dfs(i + 1)
            for j in range(i, len(s)):
                if s[i:j+1] in words:
                    res = min(res, dfs(j + 1))

            dp[i] = res

            return res
        return dfs(0)


if __name__ == '__main__':
    s = "leetscode"
    dictionary = ["leet", "code", "leetcode"]
    sol = Solution()
    result = sol.minExtraChar(s, dictionary)
    print(result)
