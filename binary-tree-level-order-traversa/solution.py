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
    @return: Level order in a list of lists of integers
    """
    def levelOrder(self, root):
        # write your code here
        result = []
        if root is None:
            return result
        queue = Queue()
        queue.put(root)
        while(not queue.empty()):
            queue_size = queue.qsize()
            level = []
            for i in xrange(queue_size):
                head = queue.get()
                level.append(head.val)
                if head.left is not None:
                    queue.put(head.left)
                if head.right is not None:
                    queue.put(head.right)
            result.append(level)
        return result
