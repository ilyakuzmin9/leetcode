"""
Given an integer n, return all the structurally unique BST's (binary search trees),
which has exactly n nodes of unique values from 1 to n. Return the answer in any order.
"""

from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # catalan's sequence
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        # return all trees with thr num,bers between low and upper inclusively
        def construct(lower, upper):
            if lower > upper:
                return [None]
            if lower == upper:
                return [TreeNode(val=lower)]

            res = []

            for x in range(lower, upper + 1):
                # x is the current node
                left = construct(lower, x - 1)
                right = construct(x + 1, upper)

                for l in left:
                    for r in right:
                        res.append(TreeNode(val=x, left=l, right=r))

            return res

        return construct (1, n)