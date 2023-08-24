"""
Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.
"""
import heapq
from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        maxHeap = [[-cnt, char] for char, cnt in count.items()]
        heapq.heapify(maxHeap)

        prev = None
        res = ''
        while maxHeap or prev:
            if prev and not maxHeap:
                return ''
            cnt, char = heapq.heappop(maxHeap)
            res = res + char
            cnt = cnt + 1
            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            if cnt != 0:
                prev = [cnt, char]

        return res


if __name__ == '__main__':
    s = "aab"
    sol = Solution()
    result = sol.reorganizeString(s)
    print(result)