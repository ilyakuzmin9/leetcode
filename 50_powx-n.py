"""
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
"""

# class Solution:
#     def myPow(self, x: float, n: int) -> float:
#         res = x**n
#         return res

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def bs(x, n):
            if x == 0: return 0
            if n == 0: return 1

            res = bs(x, n//2)
            res = res * res

            if n % 2:
                return res * x
            else:
                return res

        res = bs(x, abs(n))

        if n >= 0:
            return res
        else:
            return 1/res


if __name__ == '__main__':
    x = 2.00000
    n = 10
    sol = Solution()
    result = sol.myPow(x, n)
    print(result)
