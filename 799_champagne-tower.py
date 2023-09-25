"""
We stack glasses in a pyramid, where the first row has 1 glass, the second row has 2 glasses, and so on until the 100th row.  Each glass holds one cup of champagne.

Then, some champagne is poured into the first glass at the top.  When the topmost glass is full, any excess liquid poured will fall equally to the glass immediately to the left and right of it.  When those glasses become full, any excess champagne will fall equally to the left and right of those glasses, and so on.  (A glass at the bottom row has its excess champagne fall on the floor.)

For example, after one cup of champagne is poured, the top most glass is full.  After two cups of champagne are poured, the two glasses on the second row are half full.  After three cups of champagne are poured, those two cups become full - there are 3 full glasses total now.  After four cups of champagne are poured, the third row has the middle glass half full, and the two outside glasses are a quarter full, as pictured below.


"""

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:

        prev_row = [poured]

        for row in range(1, query_row +1):
            cur_row = [0] * (row + 1)
            for i in range(row):
                extra = prev_row[i] - 1
                if extra > 0:
                    cur_row[i] += 0.5 * extra
                    cur_row[i+1] += 0.5 * extra
            prev_row = cur_row

        return min(1, prev_row[query_glass])


if __name__ == '__main__':
    poured = 100000009
    query_row = 33
    query_glass = 17
    sol = Solution()
    result = sol.champagneTower(poured, query_row, query_glass)
    print(result)
