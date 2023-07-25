"""
Given an integer n, return a list of all possible full binary trees with n nodes.
Each node of each tree in the answer must have Node.val == 0.

Each element of the answer is the root node of one possible tree.
You may return the final list of trees in any order.

A full binary tree is a binary tree where each node has exactly 0 or 2 children.
"""

# Definition for a binary tree node.

# dfs
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List, Optional
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:

        dp = {0: [], 1: [TreeNode()]}

        def dfs(n):
            if n in dp:
                return dp[n]

            res = []
            for  l in range(n):
                r = n - l -1
                leftTrees, rightTrees = dfs(l), dfs(r)

                for t1 in leftTrees:
                    for t2 in rightTrees:
                        res.append(TreeNode(0, t1, t2))
            dp[n] = res
            return res

        return dfs(n)



