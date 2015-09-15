"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: A ListNode
    @return: A ListNode
    """
    def deleteDuplicates(self, head):
        # write your code here
        if head is None:
            return head
        import sys
        dummy = ListNode(sys.maxint, next=head)
        head = dummy

        while head is not None and head.next is not None:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next

