"""
Given the root of a binary tree, the value of a target node target, and an integer k,
return an array of the values of all nodes that have a distance k from the target node.

You can return the answer in any order.
"""

# BFS

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
from typing import List
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not k:
            return [target.val]

        graph = collections.defaultdict(list)
        queue = collections.deque([root])

        while queue:
            node = queue.popleft()
            if node.left:
                graph[node].append(node.left)
                graph[node.left].append(node)
                queue.append(node.left)
            if node.right:
                graph[node].append(node.right)
                graph[node.right].append(node)

                queue.append(node.right)

        res = []
        visited = set([target])

        queue = collections.deque([(target, 0)])
        while queue:
            node, distance = queue.popleft()

            if distance == k:
                res.append(node.val)
            else:
                for edge in graph[node]:
                    if edge not in visited:
                        visited.add(edge)
                        queue.append((edge, distance + 1))

        return res

