"""
You are given the customer visit log of a shop represented by a 0-indexed string customers consisting only of characters 'N' and 'Y':

if the ith character is 'Y', it means that customers come at the ith hour
whereas 'N' indicates that no customers come at the ith hour.
If the shop closes at the jth hour (0 <= j <= n), the penalty is calculated as follows:

For every hour when the shop is open and no customers come, the penalty increases by 1.
For every hour when the shop is closed and customers come, the penalty increases by 1.
Return the earliest hour at which the shop must be closed to incur a minimum penalty.

Note that if a shop closes at the jth hour, it means the shop is closed at the hour j.
"""


class Solution:
    # def bestClosingTime(self, customers: str) -> int:
    #     stack = set()
    #     l = len(customers)
    #     res = (0, customers[::-1].count('Y'))
    #     for i in range(0, l):
    #         pen = customers[-1:i:-1].count('Y') + customers[0:i:1].count('N')
    #         if pen < res[1]:
    #             res = (i+1, pen)
    #
    #     return res[0]


    def bestClosingTime(self, customers: str) -> int:
        max_score = score = 0
        best_hour = -1

        for i, c in enumerate(customers):
            score += 1 if c == 'Y' else -1
            if score > max_score:
                max_score, best_hour = score, i

        return best_hour + 1


if __name__ == '__main__':
    customers = "YYNY"
    sol = Solution()
    result = sol.bestClosingTime(customers)
    print(result)