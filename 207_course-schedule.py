"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
 You are given an array prerequisites where prerequisites[i] = [ai, bi]
  indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.
"""
from typing import List
from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for pair in prerequisites:
            course, pre = pair
            graph[course].append(pre)

        visit = [0] * numCourses

        def hasCycle(course):
            if visit[course] == 1: return True
            if visit[course] == 2: return False

            visit[course] = 1
            for pre in graph[course]:
                if hasCycle(pre):
                    return True

            visit[course] = 2
            return False

        for course in range(numCourses):
            if hasCycle(course):
                return False

        return True



if __name__ == '__main__':
    numCourses = 2
    prerequisites = [[1, 0]]
    sol = Solution()
    result = sol.canFinish(numCourses, prerequisites)
    print(result)
