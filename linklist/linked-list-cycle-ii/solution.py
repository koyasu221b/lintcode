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
    @return: The node where the cycle begins.
                if there is no cycle, return null
    """
    def detectCycle(self, head):
        # write your code here
        if head is None or head.next is None:
            return

        slow = head
        fast = head
        while slow is not None and fast is not None:
            slow = slow.next
            fast = fast.next
            if fast is None:
                return None
            fast = fast.next
            if slow == fast:
                break

        if fast is None:
            return None
        slow = head
        while slow != fast:
            fast = fast.next
            slow = slow.next

        return slow
