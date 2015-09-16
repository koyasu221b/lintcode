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
    @param x: an integer
    @return: a ListNode
    """
    def partition(self, head, x):
        # write your code here
        if head is None:
            return None

        left_dummy = ListNode(0)
        right_dummy = ListNode(0)
        left = left_dummy
        right = right_dummy

        while head is not None:
            if head.val < x:
                left.next = head
                left = head
            else:
                right.next = head
                right = head

            head = head.next

        left.next = right_dummy.next
        right.next = None

        return left_dummy.next

