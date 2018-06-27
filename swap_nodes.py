"""
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummp_tmp = dummy = ListNode(0)
        dummp_tmp.next = head
        begin = head
        while begin and begin.next:
            tmp = begin.next.next
            dummp_tmp.next = begin.next
            begin.next.next = begin
            begin.next = tmp
            dummp_tmp = begin
            begin = tmp
        return dummy.next

head = tmp = ListNode(1)
for i in range(2, 3):
    tmp.next = ListNode(i)
    tmp = tmp.next

new_head = Solution().swapPairs(head)
while new_head:
    print new_head.val
    new_head = new_head.next
