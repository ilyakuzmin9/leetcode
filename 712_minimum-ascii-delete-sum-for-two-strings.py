"""
Given two strings s1 and s2, return the lowest ASCII sum of deleted characters to make two strings equal.
"""


class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n1 = len(s1)
        n2 = len(s2)

        inf = 10**20
        has_cache = [[False] * (n2+1) for _ in range(n1 + 1)]
        cache = [[None] * (n2+1) for _ in range(n1 + 1)]
        def get_min(index1, index2):
            if index1 == n1 and index2 == n2:
                return 0

            if has_cache[index1][index2]:
                return cache[index1][index2]

            has_cache[index1][index2] = True
            if index1 == n1:
                cache[index1][index2] = get_min(index1, index2 + 1) + ord(s2[index2])
                return cache[index1][index2]
            if index2 == n2:
                cache[index1][index2] = get_min(index1 + 1, index2) + ord(s1[index1])
                return cache[index1][index2]

            best = inf
            if s1[index1] == s2[index2]:
                best = min(best, get_min(index1 + 1, index2 + 1))

            best = min(best, get_min(index1, index2 + 1) + ord(s2[index2]))
            best = min(best, get_min(index1 + 1, index2) + ord(s1[index1]))

            cache[index1][index2] = best
            return best

        return get_min(0, 0)

if __name__ == '__main__':
    s1 = "sea"
    s2 = "eat"
    sol = Solution()
    result = sol.minimumDeleteSum(s1, s2)
    print(result)
