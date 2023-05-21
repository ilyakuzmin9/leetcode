
# class ListNode:
#     def __init__(self, val):
#         self.value = val
#         self.right = None
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def llist_print(self):
#         curr_node = self.head
#         while curr_node is not None:
#             print(curr_node.value, curr_node.right)
#             curr_node = curr_node.right
#
#     def llist_append(self, value):
#         new_node = ListNode(value)
#         if self.head is None:
#             self.head = new_node
#             return None
#
#         last_node = self.head
#         while last_node.right is not None:
#             last_node = last_node.right
#         last_node.right = new_node
#
#
# def llists_two_sum(a_llist_1, a_llist_2):
#     p1 = a_llist_1.head
#     p2 = a_llist_2.head
#
#     llists_sum = LinkedList()
#
#     carry = 0
#
#     while p1 is not None or p2 is not None:
#         if not p1:
#             i = 0
#         else:
#             i = p1.value
#         if not p2:
#             j = 0
#         else:
#             j = p2.value
#         s = i + j + carry
#
#         if s >= 10:
#             carry = 1
#             reminder = s % 10
#             llists_sum.llist_append(reminder)
#         else:
#             carry = 0
#             llists_sum.llist_append(s)
#         if p1 is not None:
#             p1 = p1.right
#         if p2 is not None:
#             p2 = p2.right
#
#     return llists_sum
#
#
# if __name__ == '__main__':
#     l1 = [2, 4, 3]
#     l2 = [5, 6, 4]
#     llist1 = LinkedList()
#     llist2 = LinkedList()
#     for item in l1:
#         llist1.llist_append(item)
#     for elem in l2:
#         llist2.llist_append(elem)
#
#     llist_sum = llists_two_sum(llist1, llist2)
#
#     llist1.llist_print()
#     llist2.llist_print()
#     llist_sum.llist_print()
#     print('done')

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = l1
        p2 = l2

        node = ListNode()
        llists_sum = node

        carry = 0

        while p1 is not None or p2 is not None or carry != 0:
            if p1 is None:
                i = 0
            else:
                i = p1.val
            if p2 is None:
                j = 0
            else:
                j = p2.val

            s = i + j + carry

            if s >= 10:
                carry = 1
                reminder = s % 10
                node.val = reminder

            else:
                carry = 0
                node.val = s

            if p1 is not None:
                p1 = p1.next
            if p2 is not None:
                p2 = p2.next
            if p1 is None and p2 is None and carry == 0:
                break

            node.next = ListNode()
            node = node.next

        return llists_sum

if __name__ == '__main__':
    l1 = ListNode(9)
    l1.next = ListNode(9)
    n = l1.next
    n.next = ListNode(9)


    l2 = ListNode(9)
    l2.next = ListNode(9)
    # m = l2.next
    # m.next = ListNode(4)

    sol = Solution()
    ll_sum = sol.addTwoNumbers(l1, l2)

    print('done')
