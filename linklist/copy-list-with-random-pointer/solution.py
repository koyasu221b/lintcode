# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        # write your code here
        current = head
        dummy = RandomListNode(0)
        tail = dummy
        hash = {}
        while current is not None:
            tail.next = RandomListNode(current.label)
            hash[current] = tail.next
            current = current.next
            tail = tail.next

        current = head
        while current is not None:
            if current.random is not None:
                hash[current].random = hash[current.random]
            current = current.next
        return dummy.next
