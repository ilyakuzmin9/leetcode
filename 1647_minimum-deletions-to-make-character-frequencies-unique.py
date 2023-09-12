"""
A string s is called good if there are no two different characters in s that have the same frequency.

Given a string s, return the minimum number of characters you need to delete to make s good.

The frequency of a character in a string is the number of times it appears in the string. For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.
"""

from collections import Counter

class Solution:
    def minDeletions(self, s: str) -> int:
        cnt = Counter(s)
        deletions = 0
        used_frequencies = set()

        for char, freq in cnt.items():
            while freq > 0 and freq in used_frequencies:
                freq -= 1
                deletions += 1
            used_frequencies.add(freq)

        return deletions