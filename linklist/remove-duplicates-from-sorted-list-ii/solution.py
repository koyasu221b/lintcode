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
        dummy = ListNode(0, next=head)
        head = dummy
        while head.next is not None and head.next.next is not None:
                if head.next.val == head.next.next.val:
                    val = head.next.val
                    while head.next is not None and val == head.next.val:
                        head.next = head.next.next
                else:
                    head = head.next
        return dummy.next
