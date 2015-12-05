#Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: The first node of the linked list.
    @return: nothing
    """
    def reorderList(self, head):
        # write your code here
        if head is None or head.next is None:
            return

        middle = self.find_middle(head)
        print middle.val
        tail = self.reverse(middle.next)
        print tail.val
        middle.next = None
        self.merge(head, tail)


    def find_middle(self, head):
        slow = head
        fast = head.next
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse(self, head):
        tmp = None
        while head is not None:
            next_node = head.next
            head.next = tmp
            tmp = head
            head = next_node
        return tmp

    def merge(self, head1, head2):
        dummy = ListNode(0)
        index = 0
        while head1 is not None and head2 is not None:
            if index % 2 == 0:
                dummy.next = head1
                head1 = head1.next
            else:
                dummy.next = head2
                head2 = head2.next

            dummy = dummy.next
            index += 1

        if head1 is None:
            dummy.next = head2
        else:
            dummy.next = head1

# values = [2, -1, 0]
# dummy = ListNode(0)
# head = dummy
# for i in values:
#     dummy.next = ListNode(i)
#     dummy = dummy.next
# head = head.next
#
# s = Solution()
# s.reorderList(head)
