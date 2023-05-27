from typing import List


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:

        dp = {}

        def solution(turn, idx, M):
            if idx == len(piles):
                return 0
            if (turn, idx, M) in dp:
                return dp[(turn, idx, M)]

            result = 0 if turn else float("inf")
            total_piles = 0
            for x in range(1, 2 * M + 1):
                if idx + x > len(piles):
                    break
                total_piles += piles[idx + x - 1]

                if turn:
                    result = max(result, total_piles + solution(not turn, idx + x, max(M, x)))
                else:
                    result = min(result, solution(not turn, idx + x, max(M, x)))
            dp[(turn, idx, M)] = result
            return result
        return solution(True, 0, 1)


if __name__ == '__main__':

    pil = [2, 7, 9, 4, 4]
    sol = Solution()
    res = sol.stoneGameII(pil)
    print(res)
