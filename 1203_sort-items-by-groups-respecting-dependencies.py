"""
There are n items each belonging to zero or one of m groups where group[i] is the group that the i-th item belongs to and it's equal to -1 if the i-th item belongs to no group. The items and the groups are zero indexed. A group can have no item belonging to it.

Return a sorted list of the items such that:

The items that belong to the same group are next to each other in the sorted list.
There are some relations between these items where beforeItems[i] is a list containing all the items that should come before the i-th item in the sorted array (to the left of the i-th item).
Return any solution if there is more than one solution and return an empty list if there is no solution.


"""
from typing import List


# Topological sort
class Solution(object):
    def sortItems(self, n, m, group, beforeItems):
        """
        :type n: int
        :type m: int
        :type group: List[int]
        :type beforeItems: List[List[int]]
        :rtype: List[int]
        """
        group_item = [[] for _ in range(m + n)]
        inner_group_edges = [[] for _ in range(n)]
        inter_group_edges = [[] for _ in range(m + n)]
        inner_group_indeg = [0 for _ in range(n)]
        inter_group_indeg = [0 for _ in range(m + n)]

        # assign new group for each item in group -1
        group_ind = m
        for i in range(len(group)):
            if group[i] == -1:
                group[i] = group_ind
                group_ind += 1
            group_item[group[i]].append(i)

        for i in range(n):
            cur_group = group[i]
            for prev_item in beforeItems[i]:
                prev_group = group[prev_item]
                if cur_group == prev_group:
                    inner_group_edges[prev_item].append(i)
                    inner_group_indeg[i] += 1
                else:
                    inter_group_edges[prev_group].append(cur_group)
                    inter_group_indeg[cur_group] += 1

        def topological_sort(edges, indeg, nodes):
            queue = []
            for node in nodes:
                if indeg[node] == 0:
                    queue.append(node)
            ans = []
            while queue:
                cur_node = queue.pop(0)
                ans.append(cur_node)
                for new_node in edges[cur_node]:
                    indeg[new_node] -= 1
                    if indeg[new_node] == 0:
                        queue.append(new_node)
            if len(ans) == len(nodes):
                return ans
            else:
                return []

        group_sort = topological_sort(inter_group_edges, inter_group_indeg, list(range(m + n)))
        if len(group_sort) == 0:
            return []
        ans = []
        for cur_group in group_sort:
            cur_nodes = group_item[cur_group]
            if len(cur_nodes) == 0:
                continue
            cur_group_sort = topological_sort(inner_group_edges, inner_group_indeg, cur_nodes)
            if len(cur_group_sort) == 0:
                return []
            ans.extend(cur_group_sort)
        return ans


if __name__ == '__main__':
    n = 8
    m = 2
    group = [-1, -1, 1, 0, 0, 1, 0, -1]
    beforeItems = [[], [6], [5], [6], [3, 6], [], [], []]
    sol = Solution()
    result = sol.sortItems(n, m, group, beforeItems)
    print(result)
