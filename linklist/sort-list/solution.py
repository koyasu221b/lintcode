
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: The first node of the linked list.
    @return: You should return the head of the sorted linked list,
                  using constant space complexity.
    """
    def sortList(self, head):
        # write your code here
        if head is None or head.next is None:
            return head

        mid = self.findMiddle(head)

        right = self.sortList(mid.next)
        mid.next = None
        left = self.sortList(head)
        return self.merge(left, right)

    def merge(self, left, right):
        dummy = ListNode(0, next = None)
        tail = dummy
        while left is not None and right is not None:
            if left.val < right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next

            tail = tail.next

        if left is not None:
            tail.next = left
        else:
            tail.next = right

        return dummy.next


    def findMiddle(self, head):
        slow = head
        fast = head.next
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow
