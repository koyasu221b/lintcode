"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
from Queue import Queue


class Solution:
    """
    @param root: The root of binary tree.
    @return: buttom-up level order in a list of lists of integers
    """
    def levelOrderBottom(self, root):
        # write your code here
        result = []
        if root is None:
            return result
        queue = Queue()
        queue.put(root)
        while not queue.empty():
            qsize = queue.qsize()
            level = []
            for i in xrange(qsize):
                head = queue.get()
                level.append(head.val)
                if head.left is not None:
                    queue.put(head.left)
                if head.right is not None:
                    queue.put(head.right)
            result.insert(0, level)
        return result
