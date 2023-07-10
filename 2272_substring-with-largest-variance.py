"""
The variance of a string is defined as the largest difference between the number
of occurrences of any 2 characters present in the string. Note the two characters may or may not be the same.

Given a string s consisting of lowercase English letters only,
return the largest variance possible among all substrings of s.

A substring is a contiguous sequence of characters within a string.
"""


class Solution:
    def largestVariance(self, s: str) -> int:

        f1 = 0
        f2 = 0
        max_var = 0
        pairs = [(l1, l2) for l1 in set(s) for l2 in set(s) if l1 != l2]

        for _ in range(2):
            for pair in pairs:
                f1 = f2 = 0
                for letter in s:
                    if letter not in pair: continue

                    if letter == pair[0]: f1 += 1

                    if letter == pair[1]: f2 += 1

                    if f1 < f2: f1 = f2= 0

                    elif f1 > 0 and f2 > 0:
                        max_var = max(max_var, f1-f2)


            s = s[::-1]

        return max_var


if __name__ == '__main__':
    s = "aababbb"
    sol = Solution()
    result = sol.largestVariance(s)
    print(result)
