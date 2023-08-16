"""
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left, right = ListNode(), ListNode()
        ltail, rtail = left, right

        while head:
            if head.val < x:
                ltail.next = head
                ltail = ltail.next
            else:
                rtail.next = head
                rtail = rtail.next
            head = head.next

        ltail.next = right.next
        rtail.next = None

        return left.next


if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l1.next.next.next = ListNode(2)
    l1.next.next.next.next = ListNode(5)
    l1.next.next.next.next.next = ListNode(2)

    sol = Solution()
    result = sol.partition(l1, 3)
    print('done')



