from typing import List


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        if len(arr) <= 2:
            return True

        else:

            s_arr = sorted(arr)
            def_diff = s_arr[1] - s_arr[0]
            for i in range(2, len(s_arr)):
                checked_diff = s_arr[i] - s_arr[i - 1]
                if checked_diff != def_diff:
                    return False
                # else:
                #     def_diff = checked_diff

        return True


if __name__ == '__main__':
    arr = [3,5,1]
    # arr = [1, 2, 4]
    sol = Solution()
    result = sol.canMakeArithmeticProgression(arr)
    print(result)
