# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        pre_head = ListNode(2)
        pre_head.next = head
        fast = pre_slow = slow = pre_head
        idx = 0
        while fast:
            fast = fast.next
            idx += 1
            if idx >= n + 1:
                pre_slow = slow
                slow = slow.next
        pre_slow.next = slow.next if slow else None
        return pre_head.next


head = begin = ListNode(1)
for i in range(2, 6):
    begin.next = ListNode(i)
    begin = begin.next

head = Solution().removeNthFromEnd(head, 5)
while head:
    print head.val
    head = head.next