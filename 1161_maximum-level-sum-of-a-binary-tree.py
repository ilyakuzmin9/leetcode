"""
Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.
Return the smallest level x such that the sum of all the values of nodes at level x is maximal.
"""


from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        q = [root]
        max_level = 1
        level = 1
        max_sum = float("-inf")

        while q != []:
            level_sum = 0
            next_level = []

            for node in q:
                level_sum += node.val


                if node.left is not None:
                    next_level.append(node.left)
                if node.right is not None:
                    next_level.append(node.right)

            if level_sum > max_sum:
                max_sum = level_sum
                max_level = level




            q = next_level
            level += 1

        return max_level



if __name__ == '__main__':
    # root = [1,7,0,7,-8, null, null]

    t1 = TreeNode(1)
    t1.left = TreeNode(7)
    t1.right = TreeNode(0)
    t1.left.left = TreeNode(7)
    t1.left.right = TreeNode(-8)
    sol = Solution()
    result = sol.maxLevelSum(t1)
    print(result)
