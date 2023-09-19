from typing import List
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> dict:
        sum_dict = dict()
        for i in range(len(mat)):
            weight = sum(mat[i])
            sum_dict.update({i: weight})
        sort_dict = sorted(sum_dict.items(), key=lambda item: item[1])

        return list(zip(*sort_dict[:k]))[0]

if __name__ == '__main__':
    mat =[[1, 1, 0, 0, 0],
 [1, 1, 1, 1, 0],
 [1, 0, 0, 0, 0],
 [1, 1, 0, 0, 0],
 [1, 1, 1, 1, 1]]
    k = 3
    sol = Solution()
    result = sol.kWeakestRows(mat, k)
    print(result)
