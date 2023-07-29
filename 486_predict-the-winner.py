"""
You are given an integer array nums. Two players are playing a game with this array: player 1 and player 2.

Player 1 and player 2 take turns, with player 1 starting first. Both players start the game with a score of 0. At each turn, the player takes one of the numbers from either end of the array (i.e., nums[0] or nums[nums.length - 1]) which reduces the size of the array by 1. The player adds the chosen number to their score. The game ends when there are no more elements in the array.

Return true if Player 1 can win the game. If the scores of both players are equal, then player 1 is still the winner, and you should also return true. You may assume that both players are playing optimally.
"""
from typing import List


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        l = len(nums)

        has_cache = [[False] * l for _ in range(l)]
        cache = [[None] * l for _ in range(l)]
        def get_best_score(left, right):
            if left == right:
                return nums[left]

            if has_cache[left][right]:
                return cache[left][right]

            pick_left = nums[left] - get_best_score(left+1, right)
            pick_right = nums[right] - get_best_score(left, right - 1)

            has_cache[left][right] = True
            cache[left][right] = max(pick_left, pick_right)
            return cache[left][right]

        if get_best_score(0, l-1) >=0:
            return True

        return False


if __name__ == '__main__':
    nums = [1, 5, 2, 4, 10]
    sol = Solution()
    result = sol.PredictTheWinner(nums)
    print(result)
