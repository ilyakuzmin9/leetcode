"""
A frog is crossing a river. The river is divided into some number of units, and at each unit, there may or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.

Given a list of stones' positions (in units) in sorted ascending order, determine if the frog can cross the river by landing on the last stone. Initially, the frog is on the first stone and assumes the first jump must be 1 unit.

If the frog's last jump was k units, its next jump must be either k - 1, k, or k + 1 units. The frog can only jump in the forward direction.
"""
from typing import List

# bfs
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] != 1:
            return False

        stack = [(1,1)]
        seen = set()

        while stack:
            stone_num, k = stack.pop(0)

            if stone_num == stones[-1]:
                return True

            for neib in [k - 1, k, k + 1]:
                next_pos = stone_num + neib
                if next_pos == stone_num:
                    continue

                if next_pos in stones and (next_pos, neib) not in seen:
                    stack.append((next_pos, neib))
                    seen.add((next_pos, neib))

        return False


if __name__ == '__main__':
    stones = [0, 1, 3, 5, 6, 8, 12, 17]
    sol = Solution()
    result = sol.canCross(stones)
    print(result)
