"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
import sys
class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):
        # write your code here
        return self.valid(root, -sys.maxint, sys.maxint)

    def valid(self, root, min_val, max_val):
        if root is None:
            return True

        if root.val <= min_val or root.val >= max_val:
            return False

        left_valid = self.valid(root.left, min_val, root.val)
        right_valid = self.valid(root.right, root.val, max_val)
        return left_valid and right_valid
