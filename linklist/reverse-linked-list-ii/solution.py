"""
Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The head of linked list
    @param m: start position
    @param n: end position
    """
    def reverseBetween(self, head, m, n):
        # write your code here
        if head is None or m > n:
            return None

        dummy = ListNode(0, next=head)
        head = dummy

        for i in range(m-1):
            if head is None:
                return None
            head = head.next

        prem_node = head
        m_node = prem_node.next
        n_node = m_node
        postn_node = n_node.next

        for i in range(n-m):
            if postn_node is None:
                return None
            tmp = postn_node.next
            postn_node.next = n_node
            n_node = postn_node
            postn_node = tmp

        prem_node.next = n_node
        m_node.next = postn_node

        return dummy.next

