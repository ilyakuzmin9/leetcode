class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        start = 0
        for char in s:
            if char in t[start:len(t)]:
                for i in range(start, len(t)):
                    if char == t[i]:
                        start = i + 1
                        break
                    elif char != t[i]:
                        continue
                    else:
                        return False
            else:
                return False
        return True


if __name__ == '__main__':
    s = "abc"
    t = "ahbgdc"
    sol = Solution()
    result = sol.isSubsequence(s, t)
    print(result)