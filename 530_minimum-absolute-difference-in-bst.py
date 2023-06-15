"""
Given the root of a Binary Search Tree (BST),
return the minimum absolute difference between the values of any two different nodes in the tree.
"""


# Definition for a binary tree node.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        prev, res = None, float("inf")

        def dfs(node):
            if not node:
                return None

            dfs(node.left)
            nonlocal prev, res
            if prev:
                res = min(res, node.val - prev.val)
            prev = node
            dfs(node.right)

        dfs(root)

        return res


if __name__ == '__main__':
    root = [4, 2, 6, 1, 3]

    t1 = TreeNode(4)
    t1.left = TreeNode(2)
    t1.right = TreeNode(6)
    t1.left.left = TreeNode(1)
    t1.left.right = TreeNode(3)




    sol = Solution()
    result = sol.getMinimumDifference(t1)
    print(result)
    pass
