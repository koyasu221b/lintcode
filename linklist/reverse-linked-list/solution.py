"""
Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The first node of the linked list.
    @return: You should return the head of the reversed linked list.
                  Reverse it in-place.
    """
    def reverse(self, head):
        # write your code here
        if head is None:
            return head

        dummy = None

        while head is not None:
            tmp = head.next
            head.next = dummy
            dummy = head
            head = tmp
        return dummy
