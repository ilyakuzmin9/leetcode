"""
You have k bags. You are given a 0-indexed integer array weights where weights[i] is the weight of the ith marble.
You are also given the integer k.

Divide the marbles into the k bags according to the following rules:

No bag is empty.
If the ith marble and jth marble are in a bag,
then all marbles with an index between the ith and jth indices should also be in that same bag.
If a bag consists of all the marbles with an index from i to j inclusively,
then the cost of the bag is weights[i] + weights[j].
The score after distributing the marbles is the sum of the costs of all the k bags.

Return the difference between the maximum and minimum scores among marble distributions.
"""
from typing import List
import itertools
import heapq


class Solution:
  def putMarbles(self, weights: List[int], k: int) -> int:
    # To distribute marbles into k bags, there will be k - 1 cuts. If there's a
    # cut after weights[i], then weights[i] and weights[i + 1] will be added to
    # the cost. Also, no matter how we cut, weights[0] and weights[n - 1] will
    # be counted. So, the goal is to find the max//min k - 1 weights[i] +
    # weights[i + 1].

    # weights[i] + weights[i + 1]
    A = [a + b for a, b in itertools.pairwise(weights)]
    return sum(heapq.nlargest(k - 1, A)) - sum(heapq.nsmallest(k - 1, A))


if __name__ == '__main__':
    weights = [1, 3, 5, 1]
    k = 2
    sol = Solution()
    result = sol.putMarbles(weights, k)
    print(result)

