"""
Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

"""


class Solution:
    def repeatedSubstringPattern(self, input_str: str) -> bool:
        length = len(input_str)

        for i in range(1, length):
            if length % i == 0:
                substring = input_str[:i]
                if substring * (length // i) == input_str:
                    return True

        return False


if __name__ == '__main__':
    s = "abab"
    sol = Solution()
    result = sol.repeatedSubstringPattern(s)
    print(result)
