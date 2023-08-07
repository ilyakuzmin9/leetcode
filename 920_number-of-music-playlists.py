"""
Your music player contains n different songs. You want to listen to goal songs (not necessarily different) during your trip. To avoid boredom, you will create a playlist so that:

Every song is played at least once.
A song can only be played again only if k other songs have been played.
Given n, goal, and k, return the number of possible playlists that you can create. Since the answer can be very large, return it modulo 109 + 7.
"""


class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        mod = 10**9 + 7
        dp = {}
        def count(cur_goal, old_songs):
            if cur_goal == 0 and old_songs == n:
                return 1
            if cur_goal == 0 or old_songs > n:
                return 0

            if (cur_goal, old_songs) in dp:
                return dp[(cur_goal, old_songs)]

            # Choose new song
            res = (n - old_songs) * count(cur_goal - 1, old_songs + 1)

            # Choose old song
            if old_songs > k:
                res += (old_songs - k) * count(cur_goal - 1, old_songs)

            dp[(cur_goal, old_songs)] = res % mod
            return  dp[(cur_goal, old_songs)]


        return count(goal, 0)



if __name__ == '__main__':
    n = 3
    goal = 3
    k = 1
    sol = Solution()
    result = sol.numMusicPlaylists(n, goal, k)
    print(result)
