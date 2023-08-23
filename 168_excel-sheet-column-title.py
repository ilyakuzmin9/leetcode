"""
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.
"""
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:

        # def rec(i):
        #     i = i // 26
        #     r = i % 26
        #     if i > 26:
        #         r = r + rec(i)
        #
        #         return r
        i = columnNumber
        rs = ''
        while i > 26:
            r = i % 26
            if r == 0:
                r = 26
                i = i // 26 - 1
            else:
                i = i // 26
            rs = chr(r + 96) + rs

        res = (chr(i + 96) + rs).upper()


        # res = rs
        # rem = columnNumber % 26
        # res = chr(rec(columnNumber) + 96) + chr(rem + 96)

        return res


if __name__ == '__main__':
    columnNumber = 5
    sol = Solution()
    result = sol.convertToTitle(columnNumber)
    print(result)
