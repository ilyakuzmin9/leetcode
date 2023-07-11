"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.min_depth = float('inf')
        self.dfs(root, 0)
        return self.min_depth

    def dfs(self, node, cur_depth):
        if not node:
            return
        if not node.left and not node.right:
            self.min_depth = min(self.min_depth, cur_depth + 1)

        self.dfs(node.left, cur_depth + 1)
        self.dfs(node.right, cur_depth + 1)



if __name__ == '__main__':
    root = [3, 9, 20, null, null, 15, 7]
    sol = Solution()
    result = sol.minDepth(root)
