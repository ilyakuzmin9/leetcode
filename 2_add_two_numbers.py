from typing import Optional


class ListNode:
    def __init__(self, val):
        self.value = val
        self.right = None


class LinkedList:
    def __init__(self):
        self.head = None

    def llist_print(self):
        curr_node = self.head
        while curr_node is not None:
            print(curr_node.value, curr_node.right)
            curr_node = curr_node.right

    def llist_append(self, value):
        new_node = ListNode(value)
        if self.head is None:
            self.head = new_node
            return None

        last_node = self.head
        while last_node.right is not None:
            last_node = last_node.right
        last_node.right = new_node


def llists_two_sum(a_llist_1, a_llist_2):
    p1 = a_llist_1.head
    p2 = a_llist_2.head

    llists_sum = LinkedList()

    carry = 0

    while p1 is not None or p2 is not None:
        if not p1:
            i = 0
        else:
            i = p1.value
        if not p2:
            j = 0
        else:
            j = p2.value
        s = i + j + carry

        if s >= 10:
            carry = 1
            reminder = s % 10
            llists_sum.llist_append(reminder)
        else:
            carry = 0
            llists_sum.llist_append(s)
        if p1 is not None:
            p1 = p1.right
        if p2 is not None:
            p2 = p2.right

    return llists_sum





# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         l1 = ListNode(0, 1)
#         return l1


if __name__ == '__main__':
    l1 = [2, 4, 3]
    l2 = [5, 6, 4]
    llist1 = LinkedList()
    llist2 = LinkedList()
    for item in l1:
        llist1.llist_append(item)
    for elem in l2:
        llist2.llist_append(elem)

    llist_sum = llists_two_sum(llist1, llist2)

    llist1.llist_print()
    llist2.llist_print()
    llist_sum.llist_print()
    print('done')

