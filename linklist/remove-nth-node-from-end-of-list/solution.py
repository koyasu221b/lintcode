"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer.
    @return: The head of linked list.
    """
    def removeNthFromEnd(self, head, n):
        # write your code here
        if n == 0:
            return head
        dummy = ListNode(-1, next=head)
        for i in range(n):
            if head is None:
                return None
            head = head.next

        preDelete = dummy
        while head is not None:
            head = head.next
            preDelete = preDelete.next
        preDelete.next = preDelete.next.next
        return dummy.next
