"""
Given n orders, each order consist in pickup and delivery services.

Count all valid pickup/delivery possible sequences such that delivery(i) is always after of pickup(i).

Since the answer may be too large, return it modulo 10^9 + 7.
"""

class Solution:
    def countOrders(self, n: int) -> int:
        slots = 2 * n
        output = 1
        while slots > 0:
            valid_choices = slots * (slots - 1) // 2
            output *= valid_choices
            slots -= 2
        return output % (10**9 + 7)


if __name__ == '__main__':
    sol = Solution()
    result = sol.countOrders(n=2)
    print(result)