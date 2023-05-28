from typing import List


class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:

        dp = {}
        def solution(i):
            if i == len(stoneValue):
                return 0
            if i in dp:
                return dp[i]

            result = float('-inf')
            for j in range(i, min(i + 3, len(stoneValue))):
                result = max(result, sum(stoneValue[i:j+1]) - solution(j + 1))
            dp[i] = result

            return result
        return 'Alice' if solution(0) > 0 else ('Bob' if solution(0) < 0 else 'Tie')


if __name__ == '__main__':
    pil = [1, 2, 3, 7]
    sol = Solution()
    res = sol.stoneGameIII(pil)
    print(res)
