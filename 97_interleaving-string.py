"""
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where s and t are divided into n and m
substrings
 respectively, such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.
"""

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        cache = {}
        if len(s1) + len(s2) != len(s3):
            return False

        def dfs(i, j):
            if i == len(s1) and j == len(s2):
                return True
            if (i, j) in cache:
                return cache[(i, j)]

            if i < len(s1) and s1[i] == s3[i + j] and dfs(i + 1, j):
                return True
            if j < len(s2) and s2[j] == s3[i + j] and dfs(i, j + 1):
                return True
            cache[(i, j)] = False
            return False
        return dfs(0,0)



if __name__ == '__main__':
    s1 = ""
    s2 = ""
    s3 = "a"
    sol = Solution()
    result = sol.isInterleave(s1, s2, s3)
    print(result)