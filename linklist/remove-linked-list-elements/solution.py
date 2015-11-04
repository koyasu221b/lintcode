# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param val, an integer
    # @return a ListNode
    def removeElements(self, head, val):
        # Write your code here
        if head is None:
            return head
        import sys
        dummy = ListNode(sys.maxint)
        dummy.next = head
        head = dummy

        while head.next is not None:
            if head.next.val == val:
                head.next = head.next.next
            else:
                head = head.next

        return dummy.next
