"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class ListNodeWrapper(object):
    def __init__(self, node):
        self.node = node

    def __cmp__(self, other):
        return cmp(self.node.val, other.node.val)

class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        # write your code here
        if lists is None or len(lists) == 0:
            return None
        from Queue import PriorityQueue
        queue = PriorityQueue()
        for each_list in lists:
            head = each_list
            while head is not None:
                queue.put(ListNodeWrapper(head))
                head = head.next
        dummy = ListNode(0)
        tail = dummy
        while not queue.empty():
            wrapper_node = queue.get()
            tail.next = wrapper_node.node
            tail = tail.next
        return dummy.next
