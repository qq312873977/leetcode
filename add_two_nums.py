# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def toint(self, node):
        return node.val + 10 * self.toint(node.next) if node else 0

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = num2 = ''
        head1 = l1
        head2 = l2
        while head1:
            num1 += str(head1.val)
            head1 = head1.next
        while head2:
            num2 += str(head2.val)
            head2 = head2.next
        sum = int(num1[::-1]) + int(num2[::-1])
        sum = str(sum)[::-1]
        res = ListNode(sum[0])
        head = res
        for i in range(1, len(sum)):
            head.next = ListNode(sum[i])
            head = head.next
        return res

l1 = ListNode(1)
l1.next = ListNode(2)
l2 = ListNode(4)
l2.next = ListNode(5)
print Solution().toint(l1)

# res = Solution().addTwoNumbers(l1, l2)
# head = res
# while head:
#     print head.val
#     head = head.next