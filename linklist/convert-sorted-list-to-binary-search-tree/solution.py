"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param head: The first node of linked list.
    @return: a tree node
    """
    def sortedListToBST(self, head):
        # write your code here
        length = self.length(head)
        self.current = head
        return self.helper(length)

    def helper(self, length):
        if length <= 0:
            return None
        left = self.helper(length/2)
        root = TreeNode(self.current.val)
        self.current = self.current.next
        right = self.helper(length - 1 - length/2)
        root.left = left
        root.right = right
        return root

    def length(self, head):
        length = 0
        while head is not None:
            head = head.next
            length+=1
        return length

