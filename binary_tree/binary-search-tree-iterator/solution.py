"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

Example of iterate a tree:
iterator = Solution(root)
while iterator.hasNext():
    node = iterator.next()
    do something for node
"""
class BSTIterator:
    #@param root: The root of binary tree.
    def __init__(self, root):
        # write your code here
        self.stack = []
        self.current = root

    #@return: True if there has next node, or false
    def hasNext(self):
        # write your code here
        return len(self.stack) > 0 or self.current is not None


    #@return: return next node
    def next(self):
        #write your code here
        while self.current is not None:
            self.stack.append(self.current)
            self.current = self.current.left

        next_node = self.stack.pop()
        self.current = next_node.right
        return next_node
