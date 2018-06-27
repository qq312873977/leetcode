"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""
# Definition for singly-linked list.


import random

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 or not l2:
            return l1 or l2

        dummy = head = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next
        head.next = l1 or l2
        return dummy.next

    def mergeTwoLists_2(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        res = head = l1
        while l1 and l2:
            l1 = l1.next
            head.next = l2 if l2 else l1
            l2 = l2.next
            head = head.next
            head.next = l1 if l1 else l2
            head = head.next
        return res

l1 = tmp1 = ListNode(0)
l2 = tmp2 = ListNode(1)
for i in range(1, 9):
    if i < 6:
        tmp1.next = ListNode(2*i)
        tmp1 = tmp1.next
    tmp2.next = ListNode(2*i+1)
    tmp2 = tmp2.next

t = l1
while t:
    print t.val
    t = t.next

print '#############'

t = l2
while t:
    print t.val
    t = t.next

print '#############'

head = Solution().mergeTwoLists(l1, l2)

while head:
    print head.val
    head = head.next