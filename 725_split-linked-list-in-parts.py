"""
Given the head of a singly linked list and an integer k, split the linked list into k consecutive linked list parts.

The length of each part should be as equal as possible: no two parts should have a size differing by more than one. This may lead to some parts being null.

The parts should be in the order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal to parts occurring later.

Return an array of the k parts.
"""
from typing import Optional, List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length, curr = 0, head
        while curr:
            curr = curr.next
            length += 1

        base_len, rem = length // k, length % k
        curr = head
        res =[]
        for i in range(k):
            res.append(curr)
            for j in range(base_len - 1 + (1 if rem else 0)):
                if not curr:
                    break
                curr = curr.next
            rem -= (1 if rem else 0)
            if curr:
                curr.next, curr = None, curr.next

        return res



