"""
You are given an integer n, which indicates that there are n courses labeled from 1 to n. You are also given a 2D integer array relations where relations[j] = [prevCoursej, nextCoursej] denotes that course prevCoursej has to be completed before course nextCoursej (prerequisite relationship). Furthermore, you are given a 0-indexed integer array time where time[i] denotes how many months it takes to complete the (i+1)th course.

You must find the minimum number of months needed to complete all the courses following these rules:

You may start taking a course at any time if the prerequisites are met.
Any number of courses can be taken at the same time.
Return the minimum number of months needed to complete all the courses.

Note: The test cases are generated such that it is possible to complete every course (i.e., the graph is a directed acyclic graph).
"""
from typing import  List

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = [[] for _ in range(n)]

        for prev, next in relations:
            graph[prev - 1].append(next - 1)

        memo = [-1] * n

        def calculateTime(course):
            if memo[course] != -1:
                return memo[course]

            if not graph[course]:
                memo[course] = time[course]
                return memo[course]

            max_prerequisite_time = 0
            for prereq in graph[course]:
                max_prerequisite_time = max(max_prerequisite_time, calculateTime(prereq))

            memo[course] = max_prerequisite_time + time[course]
            return memo[course]

        overall_min_time = 0
        for course in range(n):
            overall_min_time = max(overall_min_time, calculateTime(course))

        return overall_min_time


if __name__ == '__main__':
    n = 3
    relations = [[1,3],[2,3]]
    time = [3,2,5]

    sol = Solution()
    result = sol.minimumTime(n, relations, time)
    print(result)
