"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
"""

from typing import List
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Create a Counter to store the count of each element
        element_count = Counter(nums)

        majority_elements = []
        threshold = len(nums) // 3

        # Iterate through the element count to identify majority elements
        for element, count in element_count.items():
            # Check if the element count is greater than the threshold
            if count > threshold:
                majority_elements.append(element)

        return majority_elements


if __name__ == '__main__':
    nums = [3, 2, 3]
    sol = Solution()
    result = sol.majorityElement(nums)
    print(result)